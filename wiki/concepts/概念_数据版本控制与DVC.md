---
type: "concept"
tags:
  - MLOps
  - Data-Version-Control
  - DVC
  - Reproducibility
sources:
  - "wiki/sources/2026-08-01_Data-Version-Control_19fbed_part4.md"
updated: "2026-08-04"
---

# 数据版本控制与 DVC

## 1. 核心定位与 MLOps 复现性价值
在机器学习（ML）与 MLOps 实践中，项目的完整性由**代码**与**数据**共同决定。**DVC（Data Version Control）** 是一款专为机器学习设计的开源数据版本控制工具。其核心定位是提供轻量级的数据追踪与版本控制解决方案，确保机器学习项目具备 100% 的**可复现性（Reproducibility）**与实验可追踪性。

## 2. 传统 Git 在追踪大文件时的局限与瓶颈
传统的版本控制系统（如 Git/GitHub）是为轻量级代码文件设计的。当面临数 GB 级别的大型数据集、模型权重或中间特征文件时，Git 显现出明显的局限性：
* **尺寸限制与性能瓶颈**：GitHub 等远程仓库对单次推送文件大小及仓库总容量有硬性限制（例如单文件 100MB 警告，2GB 限制），这使得直接将大文件 push 到 Git 变得几乎不可能。
* **克隆速度慢**：如果将二进制大文件硬推入 Git 历史，会导致 `.git` 目录体积呈指数增长，使得拉取和克隆仓库的性能严重下降。

## 3. DVC 两阶段联动机制
DVC 通过与 Git 协同的**两阶段联动机制**巧妙地解决了大文件版本控制问题，使 Git 专注于追踪轻量级的文本，而 DVC 专注于管理繁重的物理数据。

### 阶段一：元数据描述（Git 追踪指针）
1. 当用户向 DVC 注册一个数据集（例如使用命令 `dvc add dataset.csv`）时，DVC 会计算该文件的 MD5 哈希值。
2. DVC 在本地的 `.dvcignore` 等配置文件中屏蔽该原始物理文件，同时生成一个极小的、与原文件同名但以 `.dvc` 结尾的元数据指针文件（例如 `dataset.csv.dvc`）。
3. 该 `.dvc` 文件中记录了原始文件的 MD5 哈希值、文件大小和物理路径。
4. 用户将该轻量级的 `.dvc` 指针文件提交至 Git 仓库进行版本管理。

### 阶段二：物理存储分流（外部仓库物理版控）
1. 真正的海量物理数据文件不会进入 Git。
2. DVC 通过配置远程数据仓库（Remote Storage，如 AWS S3、Google Cloud Storage (GCS)、Microsoft Azure Blob Storage、SFTP 或本地 NAS 等），在执行 `dvc push` 时，将大物理文件以其 MD5 哈希值重命名并推送到外部远程仓库进行存储和版控。
3. 外部存储分流确保了大型物理数据集在云端的高效、安全隔离。

## 4. 可复现工作流
在多人协作或模型复现场景中，DVC 和 Git 协同工作的标准流程如下：
1. **拉取代码与指针**：
   ```bash
   git clone <git-repo-url>
   git checkout <target-commit-or-branch>
   ```
   此时，工作区内只有代码和 `.dvc` 指针文件，而没有真正的数据文件。
2. **同步拉取物理数据**：
   ```bash
   dvc pull
   ```
   DVC 会自动读取当前 Git commit 对应的 `.dvc` 指针文件，解析出所需的 MD5 值，并前往配置的外部远程仓库将精确匹配版本的数据集下载到本地的工作空间。

这种 `git checkout` ➕ `dvc pull` 的工作流，保证了**特定版本的代码**与**特定版本的数据**在时间戳上强一致对齐，构成了可复现 MLOps 流程的基石。

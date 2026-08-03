---
type: "source"
tags:
  - MLOps
  - Data-Version-Control
  - DVC
summary: "介绍如何使用数据版本控制（DVC）与 Git 协同工作，解决 Git 无法处理大文件的问题，从而实现机器学习项目的完全可复现性。"
sources:
  - "raw/articles/2026-08-01_Data-Version-Control_19fbed_part4.md"
updated: "2026-08-04"
---

# 来源信息
- **邮件主题**：Build a Stock Market Research Agentic Workflow
- **发送人**：Daily Dose of DS <avi@dailydoseofds.com>
- **发布日期**：2026-08-01
- **原始 ID**：19fbed5d2cd155dd

# 核心要点
- 由于 GitHub 等代码托管平台对推送的大文件大小有上限限制，通过 Git 直接对数 GB 大小的数据集进行版本控制是不切实际的。
- 机器学习（ML）项目的驱动不仅依赖于代码，还涉及大规模、且随实验快速变化的数据文件。为了保证实验的可复现性与可追踪性，对数据集进行版本控制必不可少。
- 数据版本控制（DVC）通过将另一个专门用于大文件的版本控制系统与 Git 集成，解决了该问题。其基本流程是在 Git 中追踪轻量级的元数据指针，而在外部存储中存放真实的大文件数据。

# 关键引文
- "Versioning GBs of datasets is practically impossible with GitHub because it imposes an upper limit on the file size we can push to its remote repositories."
- "To ensure proper reproducibility and experiment traceability, it is also necessary to version datasets."
- "The core idea is to integrate another version controlling system with Git, specifically used for large files."

# 联动概念与实体
- [[wiki/concepts/概念_数据版本控制与DVC|概念_数据版本控制与DVC]]

---
> 📎 **物理文献**：[[raw/articles/2026-08-01_Data-Version-Control_19fbed_part4.md]]

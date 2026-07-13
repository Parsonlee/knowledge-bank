# AGENTS.md — 个人知识库系统总纲与 Agent 操作指南

This file provides guidance to Claude Code/Codex/Antigravity and other AI Agents when working with code and markdown notes in this repository.

## 0. 项目定位与核心目标
- **项目定位**：基于 Obsidian 的个人知识库（vault），通过 Git 同步到 GitHub（`Parsonlee/knowledge-bank`，私有仓库）。这不是传统意义上的软件工程项目——它是 Markdown 笔记、剪藏与配置的集合。本仓库本质上是专门为 AI Agent 进行知识管理、结构化治理与自动化运维设计的工作空间。
- **核心目标**：维护 `wiki/` 目录，通过结构化提炼与图谱联动，将其打造为**可复利的知识层**。
- **跨平台与同步说明**：
  - 桌面端（Mac/Linux/Windows）与移动端（iOS/iPadOS）通过 Obsidian + Obsidian Git 插件定时自动 commit & push/pull。
  - `.obsidian/` 目录下的配置、插件和主题随仓库跨端同步；`workspace.json` 等设备绑定缓存已在 `.gitignore` 中排除。

## 1. 目录结构与分层架构
系统知识管理分为严格的三层架构，请 AI Agent 严格遵循边界执行操作。

> [!CAUTION] 🚨 分层推导与唯一上游溯源纪律（Derivation Chain Rules）
> 为了彻底杜绝“空中楼阁/虚假幻觉生成”与“断链越级”，全库严格遵循单向数据推导管线：**`raw/`（零级底座） 👉 `wiki/sources/`（一级产物） 👉 `wiki/entities/` 与 `wiki/concepts/` 等（末端产物）**。各层边界与上游纪律如下：
> 1. **零级底座 (`raw/` & `Clippings/`) —— 绝对只读**：作为唯一事实来源，绝对只读不改。
> 2. **一级产物 (`wiki/sources/`) —— 唯一上游只能是 `raw/`**：每个摘要页是物理文献的直接结构化产物，Frontmatter 中的 `sources:` 必须且只能有唯一上游 `raw/xxx.md`，做到 1对1 精准映射。
> 3. **末端产物 (`wiki/entities/`、`wiki/concepts/`、`wiki/comparisons/`、`wiki/overview/`) —— 唯一上游只能是 `wiki/sources/`，严禁越级链接 `raw/`**：
>    - 所有末端产物的合规事实来源，**只能并且必须来自 `wiki/sources/xxx.md`**。
>    - **严禁越级（No Bypassing）**：末端产物绝对不能绕过 `sources/` 摘要层直接链接到 `raw/` 物理文件！
>    - **严禁无源虚假生成（No Phantom Generation）**：任何 Frontmatter `sources:` 为空且在全库 `sources/` 中毫无支撑的末端产物，均被定性为“无源虚假生成”，在 Lint 审计与精简中一律直接物理清除。

### 1.1 原始资料层 (Raw Sources) —— 唯一事实来源，**只读不改**
作为知识库的底座，所有外部输入均首先归档于此，严格保持只读。

| 目录           | 用途                                                             | 权限边界     |
| ------------ | -------------------------------------------------------------- | -------- |
| `raw/`       | 主文章库——原 Cubox 导入笔记与由 Clippings 剪藏归档的文献全文 100% 收纳于此             | **只读不改** |
| `Clippings/` | 网页剪藏缓冲区（Staging）——由官方剪藏插件自动保存，**完成 Ingest 入库后必须移动至 `raw/` 归档** | **只读不改** |

### 1.2 知识图谱维护层 (Wiki Layer) —— **由 LLM / Agent 核心生成与维护**
整个 `wiki/` 目录是 LLM 结构化输出的核心图谱仓库，通过严密的网状双链建立起可复利的知识网络。

| 目录 / 文件 | 命名规范与用途 |
|------|------|
| `wiki/sources/` | 单个来源的结构化摘要页（`xxx.md`，`sources:` 字段精确指向唯一上游 `raw/xxx.md`） |
| `wiki/entities/` | 实体页（`实体_xxx.md`，人物、机构、书籍、开源项目等，`sources:` 只能指向 `wiki/sources/`） |
| `wiki/concepts/` | 概念页（`概念_xxx.md`，理论、算法、方法论、模型架构等，`sources:` 只能指向 `wiki/sources/`） |
| `wiki/comparisons/` | 对比分析页（`xxx_vs_yyy.md`，横向对比与技术选型，`sources:` 只能指向 `wiki/sources/`） |
| `wiki/overview/` | 综述 / 总览页（`综述_xxx.md`，体系化的专题总结，`sources:` 只能指向 `wiki/sources/`） |
| `wiki/index.md` | Wiki 知识库分类内容总索引 |
| `wiki/log.md` | 操作流水日志（追溯知识库演化历史） |

### 1.3 独立工作文档与静态资源层 (Assets & Docs Layer)
针对日常职场业务交付、用户个人手写思考以及多媒体附件，设定专有的独立管理空间，与 `wiki/` 知识层解耦：

| 目录 | 功能作用与设计意图 | 权限边界 |
|------|------|------|
| `assets/` | **离线多媒体资源库**：仅存放用户手写原创笔记、离线导入或业务文档依赖的本地图片（如 `.png`, `.jpg`）和 `.pdf` 文档。**注意**：为控制 Git 仓库体积，网页剪藏或抓取的网络文章图一律保留公网 Markdown 外链 URL，严禁下载到本目录。 | 静态资源管理 |
| `workdocs/` | **业务与专题工作文档库**：存放个人的工作交付物、专题调研报告、Word 原始文档（如 `.docx`）及其转化的 Markdown 产物（如 `workdoc-md/`），作为独立于 `wiki/` 图谱的业务资产。 | **Agent 不主动修改原文**，仅可按指令做读取、提炼或归纳沉淀 |
| `notes/` | **个人随想与手写笔记库**：用户手写的原创独立思考、技术总结与日常心得。 | **Agent 绝对不主动修改** |

### 1.4 自动化工程、脚本与运维支撑层 (Engineering & Maintenance Layer)
当前项目本质上是一个面向 AI 协同的 **LLM Wiki Repository 工程体系**。为保障 Agent 能够进行持续集成、健康度审查与自动化运维，设立了专有的工程工具与缓冲空间：

| 目录 / 文件 | 功能作用与设计意图 | Agent 操作规范 |
|------|------|------|
| `scripts/` | **图谱运维与自动化治理库**：为 LLM Wiki 定制的 Python 工具集。包括全库健康诊断与级联清理核心工具 `vault_lint.py`、概念与来源链接校验审查 `concept_source_lint.py`、原始资料重组归档工具 `restructure_raw.py` 等。 | Agent 在执行 `lint`、`prune` 等复杂整顿与级联清理操作时，**强烈推荐直接调用此目录下预置的 Python 工具**，绝不臆造写删逻辑 |
| `tmp/` | **临时缓冲与调试空间**：已被 `.gitignore` 排除的临时文件交换区。存放 Agent 的中间计算产物、临时测试脚本或转码临时缓存。 | 允许 Agent 自由读写与清理，**禁止在此目录中存放任何需要持久化的正文或 Wiki 页面** |

### 1.5 系统元数据与 Agent 生态层 (Config & Ecosystem Layer)
| 目录 / 文件 | 功能作用与设计意图 | 说明 |
|------|------|------|
| `AGENTS.md` / `TODO.md` | `AGENTS.md` 为系统架构设计与 Agent 行为核心宪法（本文件）；`TODO.md` 为本系统演化路线与待办需求清单。 | 核心指导与协作指南 |
| `.agents/` | **Agent 技能扩展库（Skills）**：存放预置或扩展的特定任务能力定义（如 `.agents/skills/docx/SKILL.md`，用于指导 Agent 读写处理 Word 文档）。 | Agent 能力插件层 |
| `.obsidian/` | **Obsidian 本地环境与 MCP 服务配置库**：维护图谱样式、工作区配置与 `Local REST API` 插件运行参数，随 Git 跨终端自动同步。 | 系统元数据区，不随便删改 |
| `.claude/` / `CLAUDE.md` | **工具生态兼容配置**：针对相关 AI Coding Agent 工具的引导指针与工作区配置。 | 兼容适配区 |

## 2. 页面类型与 Frontmatter 规范
所有 wiki 页面使用 Markdown，顶部 YAML frontmatter 格式严格遵守规范示例如下：

```yaml
---
type: "source|entity|concept|comparison|overview"
tags: ["LLM/arch", "AI-Agent/coding"] # 需选用标准 Tag 体系
summary: "一句话说明这页的核心内容/贡献"
sources: ["raw/xxx.md"] # 100% 精准锚定物理文件路径
updated: "YYYY-MM-DD"
---
```

### 2.1 Source Summary（来源摘要页）
- **路径**：`wiki/sources/xxx.md`
- **内容要求**：
  - 来源信息（标题、作者、时间、链接）
  - 核心要点（3–7 条 bullet）与关键引文（可选）
  - 关联实体 / 概念链接（`[[entities/实体_xxx]]` / `[[concepts/概念_yyy]]`）
- **正文末尾物理文献插链**：为打通 Obsidian 关系图谱可视化连接（避免底层全文呈现为外围孤散点），必须在 Source 摘要页正文最末尾追加双向链接：
  `> 📎 **物理文献**：[[raw/xxx.md]]`

### 2.2 Entity Page（实体页）
- **路径**：`wiki/entities/实体_xxx.md`
- **内容要求**：基本信息、行为 / 特征 / 状态、相关事件 / 计划 / 实验链接、来自哪些来源（列出 `sources`）。

### 2.3 Concept Page（概念页）
- **路径**：`wiki/concepts/概念_xxx.md`
- **内容要求**：定义、使用场景 / 步骤、在本知识库中的应用示例、关联实体 / 其它概念。

### 2.4 Comparison Page（对比分析页）
- **路径**：`wiki/comparisons/xxx_vs_yyy.md`
- **内容要求**：比较对象简介、相同点、不同点（目标、成本、适用场景等）、结论 / 选择建议。

### 2.5 Overview / Synthesis（综述 / 总览页）
- **路径**：`wiki/overview/综述_xxx.md`
- **内容要求**：一句话结论（Summary）、当前理解 / 总体框架、支撑它的主要来源和页面链接、未决问题 / 待验证假设。

## 3. MCP 集成与工具选择
Vault 内运行了 **Local REST API with MCP** 插件。当桌面端 Obsidian 打开时，AI Agent 可通过 MCP 工具（`mcp__obsidian__*`）直接读写与搜索 vault。连接配置在根目录 `.mcp.json`（project 范围，已 gitignore）。
- **端点**：`http://127.0.0.1:27123/mcp/`（HTTP，仅本机回环）
- **认证**：Bearer token 在 `.mcp.json` 中
- **前提**：桌面端 Obsidian 运行中，Local REST API 插件已启用

> [!tip] 优先使用 MCP 工具
> 对 vault 的实时操作优先使用 MCP 工具（如 `vault_read`、`vault_write`、`vault_patch`、`search_query`、`search_simple`、`tag_list`），因为它们能直接访问 Obsidian 的实时元数据和图谱链接结构。批量处理或脚本自动化场景可直接操作本地 `.md` 物理文件。
> - `vault_patch`：精准修改 frontmatter（如替换 `tags`：`contentType: application/json`, `operation: replace`）或指定标题下的内容。

## 4. 核心工作流（Operations）
AI Agent 在处理日常任务时，必须遵守以下三大核心操作闭环：

### 4.1 Ingest（新资料入库操作）
当用户要求把新收藏、新文章或文档进行「入库 / Ingest」时，**必须完整执行以下闭环动作**：
1. **深度阅读与原始净化**：阅读原始资料（如 `raw/xxx.md` 或 `Clippings/xxx.md`），若正文不足则抓取 URL 全文。提炼 3-7 条核心要点与关键引文。同时顺带执行**语法净化**（转义正文行内 `#xxx` 防止全局 Tag 污染，转义矩阵/张量等非链接的 `[[` 防止幽灵出链）。
2. **生成 Source 摘要页**：在 `wiki/sources/` 目录下创建对应的 `.md` 摘要页（严格遵守 Frontmatter 格式并在文末追加物理文献链接 `> 📎 **物理文献**：[[raw/xxx.md]]`）。
3. **构建双向维基网络**：在 Source 摘要页正文中，凡提及重要技术概念、人物、机构或项目，一律使用 Obsidian 链接格式 `[[entities/实体_xxx]]` 或 `[[concepts/概念_yyy]]` 与知识库产生关联。
4. **联动 Entities & Concepts**：检查被引用的 `wiki/entities/` 或 `wiki/concepts/` 页面是否存在：
   - 若存在：打开该实体 / 概念页，将新要点或进展更新进去，并在正文或来源中补充关联。
   - 若不存在但概念核心且高频：在对应目录下创建新页面。
5. **剪藏文章归档移动（Clippings -> raw）**：
   - 如果本次 Ingest 的原始文章来源于 `Clippings/` 剪藏缓冲库，**在完成摘要提炼与维基图谱构建后，必须将原始 Markdown 文件从 `Clippings/xxx.md` 移动到 `raw/xxx.md`（作为唯一归档永久保存）**。
   - 同步确保对应的 `wiki/sources/xxx.md` 摘要页中，Frontmatter 的 `sources:` 字段及文末物理文献插链统一精准指向 `raw/xxx.md`。
6. **全量同步索引与日志**：
   - 打开 `wiki/index.md`，在对应分类下同步挂载**所有本次新建的 Source、Concept 与 Entity 页面**（严禁只登摘要漏登新建概念 / 实体）。
   - 打开 `wiki/log.md` 追加一笔日志记录：
     `## [YYYY-MM-DD] ingest | raw/xxx -> wiki/sources/xxx.md (+ affected pages)`

### 4.2 Query（知识查询与沉淀）
当用户提问或检索专题知识时：
1. **精准定位**：优先通过 MCP 搜索或读取 `wiki/index.md` 快速定位候选页面。
2. **综合解答**：基于页面内容回答，并给出具体来源引用（如 `如 [[wiki/sources/xxx]] 所述...`）。
3. **沉淀新知（可选）**：如果回答包含有价值的横向对比、选型分析或架构综述，主动提议将其写入 `wiki/comparisons/` 或 `wiki/overview/`；新建页面务必**在正文插链接入图谱并同步挂载至 `wiki/index.md`**，最后在 `wiki/log.md` 登记 `query | 新建 ...`。

### 4.3 Lint & Prune（健康检查、精简与图谱垃圾回收）
当用户要求对知识库进行「Lint / 健康检查 / 精简 / 冲突审查 / 删除收藏」时，**强烈推荐使用项目中预置的自动化脚本工具 `python3 scripts/vault_lint.py`**：

1. **常规扫描诊断 (`python3 scripts/vault_lint.py lint`)**：
   - **图谱与链审计**：检测知识库中的观点矛盾、过时表述、孤立无入链页面、低频提及实体（如仅出现 1 次的人 / 组织）、以及缺失的双向链接与死链。
   - **漏登审计**：扫描 `wiki/sources/`、`wiki/concepts/`、`wiki/entities/` 检查是否存在漏登 `wiki/index.md` 的孤立文档。
   - **语法污染扫描 (`python3 scripts/vault_lint.py sanitize-raw`)**：检测并自动转义物理源文件中未转义的行内伪 Tag 或矩阵 / 张量伪出链 `[[...]]`。
2. **精简与级联清理机制（`python3 scripts/vault_lint.py prune <raw_path>` / Cascading Pruning SOP）**：
   当用户主动要求删除或清理最上游原始层资料（如 `raw/xxx.md` 或 `Clippings/xxx.md`）时，**必须执行严密的图谱级联清理链条（自上而下四步法）**：
   - **第一步（精准清理摘要页）**：删除目标物理源文件时，读取所有 `wiki/sources/*.md` 的 Frontmatter，只要 `sources:` 列表中命中被删源路径，将对应的 Source 摘要页连带删除。
   - **第二步（同步更新总索引）**：打开 `wiki/index.md`，将对应分类下指向已删 Source 摘要页的索引条目自动精准剔除。
   - **第三步（入度审计与垃圾回收 GC）**：解析被删 Source 页中引用过的所有实体 `[[entities/...]]` 和概念 `[[concepts/...]]`，对它们在全库执行引用度（In-degree）检查：
     - **情况 A（剩余被引次数 $\ge 1$）**：说明属于通用核心知识，**保留页面**，仅在其正文末尾 `## 来源` 中摘除指向已删文章的链接。
     - **情况 B（剩余被引次数 $= 0$）**：说明其为随着该被删文产生的冷门孤立产物（Orphan Pages），**触发垃圾回收连带清理**。
   - **第四步（登记操作流水）**：在 `wiki/log.md` 登记 `lint/prune | prune raw/xxx.md (+ Cascading cleanup sources, index & gc entities/concepts)`。
3. **先提议，再动刀 (`--dry-run` vs `--apply`)**：
   运行 `python3 scripts/vault_lint.py prune <path>` 默认即为 **Dry-run 模式**，自动向用户输出结构化的「自上而下四步级联影响分析清单」。**严禁未经确认直接大规模动刀**；确认无误后方可运行追加 `--apply` 参数执行正式动刀。

## 5. Tag 体系
Tag 统一存放在 YAML frontmatter 的 `tags:` 数组中。严格沿用主库已有的分层 Tag 体系（使用 `/` 分隔），**不另起一套**。主要分支如下：

- `LLM/` — arch, training, inference, reasoning, hallucination, tokenization
- `AI-Agent/` — coding, tool-calling, context-engineering, deep-research, AI-BI, skill, prompt-engineering, multi-agent, memory, UI
- `RAG/` — embedding, query, chunking, retrieval, eval
- `Skill/` — python, data-analysis, claude-code, linux
- `CV/` — detection, data-augmentation, arch
- `Infra/` — AI, gpu
- 顶层独立 — `DeepLearning`, `AIGC`, `创业`, `面试`, `Life`, `Recommendation`, `TTS`

> [!CAUTION] 🚨 Tag 排他性定界与消歧纪律（Disambiguation Rules）
> 为杜绝 AI Agent 产生分类混淆与池化泛化，所有 Agent 在录入或校验文献及笔记时，务必严格遵守以下排他性边界铁律：
> 
> 1. **`AI-Agent/skill` vs `Skill/*` 绝不混用（理论机制 vs 人类实操）**：
>    - **`AI-Agent/skill`**：仅限 **智能体原生能力扩展的底层工程规范与运行机制**（如 `SKILL.md` 双消息注入规范、动态工具发现机制、Claude Agent Skills 元工具源码剖析等理论/机制文献）。
>    - **`Skill/*`**：仅限 **人类开发者/业务日常使用中的实操 SOP 与技巧心得**（如 `Skill/claude-code` 专指人类使用 Claude Code CLI 的快捷键/配置指南，`Skill/python` 指日常开发笔记）。**严禁将人类工具实操笔记打入 `AI-Agent/skill`**。
> 
> 2. **细分叶子优先纪律（No Top-level Pooling）**：
>    - 在 `RAG/`、`LLM/`、`AI-Agent/` 体系下，**必须优先精准锚定末端细分叶子分类**（如 `RAG/chunking`、`LLM/arch`）；
>    - 严禁出于省事把垂直领域的文章笼统丢入顶层单分类（如 `RAG`、`LLM`），顶层分类仅供覆盖全局框架的宏观综述文使用。

## 6. Git 与通用约定
> [!tip] 操作原则
> 不确定时，先提议再执行，不做大规模自动改动。每次完成 Ingest 后建议建立 Git 提交，便于历史回溯。

- **Git User**：`Hugo Yang <hugoyang1229@gmail.com>`
- **提交信息**：中英文均可，建议带规范类型前缀（如 `docs:`, `chore:`, `feat:` 等）。
- **Obsidian Git 插件自动提交格式**：`vault backup: {{date}}`
- **安全红线**：永远不要提交 `.mcp.json`（内含 API Token，已严格在 `.gitignore` 中排除）。

## 7. 关键文件索引
- `AGENTS.md` — 系统全局架构设计、分层规范与 AI Agent 核心操作总纲（本文件）
- `HANDOFF.md` — 项目当前进度、近期里程碑与下一步任务
- `wiki/index.md` — Wiki 知识层总分类索引
- `wiki/log.md` — 知识库维护操作流水日志

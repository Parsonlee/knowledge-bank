
This file provides guidance to Claude Code/Codex/Antigravity when working with code in this repository.

## 项目说明

基于 Obsidian 的个人知识库（vault），通过 Git 同步到 GitHub（`Parsonlee/knowledge-bank`，私有仓库）。不是软件项目——是 Markdown 笔记、剪藏和配置的集合。

## MCP 集成

Vault 内运行了 **Local REST API with MCP** 插件。当桌面端 Obsidian 打开时，Claude Code 可通过 MCP 工具（`mcp__obsidian__*`）读写搜索 vault。连接配置在 `.mcp.json`（project 范围，已 gitignore）。

- 端点：`http://127.0.0.1:27123/mcp/`（HTTP，仅本机回环）
- 认证：Bearer token 在 `.mcp.json` 中
- 前提：桌面端 Obsidian 运行中，Local REST API 插件已启用

对 vault 的操作优先使用 MCP 工具（读笔记、改 frontmatter、按 tag 搜索、移动文件）。批量/脚本场景可直接操作 `.md` 文件。

## 目录结构与分层架构

系统知识管理分为三层架构，请 AI Agent 严格按照分层边界执行操作：

### 1. 原始资料层 (Raw Sources) —— 唯一事实来源，**只读不改**
| 目录 | 用途 |
|------|------|
| `raw/` | 主文章库——原 Cubox 导入笔记的批注与正文全文 100% 合并收纳于此 |
| `Clippings/` | 网页剪藏库——由 Obsidian 官方剪藏插件自动保存的网页文章 |
| `workdocs/` | 工作项目原始文档（docx 等） |

### 2. 知识维护层 (Wiki Layer) —— **由 LLM/Agent 核心生成与维护**
| 目录 / 文件 | 用途 |
|------|------|
| `wiki/sources/` | 单个来源的结构化摘要页（`sources:` 字段精确指向 `raw/xxx.md` 等物理文件） |
| `wiki/entities/` | 实体页（人物、机构、书籍、开源项目等） |
| `wiki/concepts/` | 概念页（理论、算法、方法论、模型架构等） |
| `wiki/comparisons/` | 对比分析页（横向对比与技术选型） |
| `wiki/overview/` | 综述/总览页（体系化的专题总结） |
| `wiki/index.md` | Wiki 知识库分类内容总索引 |
| `wiki/log.md` | 操作流水日志（追溯知识库演化历史） |

### 3. 用户手写与静态资源层
| 目录 | 用途 |
|------|------|
| `notes/` | 用户手写的原创笔记、指南、独立思考文章（Agent 不主动修改） |
| `assets/` | 离线资源库——仅存放离线导入/手写原创笔记产生的本地图片或 PDF（网页剪藏图片一律使用公网外链 URL，不下载到本目录） |
| `tmp/` | 已 gitignore 的临时空间（不再存放持久化正文） |

## LLM Wiki 核心工作流（Operations）

未来的 AI Agent 在处理任何任务时，请遵守以下三大日常核心操作规范：

### 1. Ingest（新资料入库操作）
当用户要求把新收藏、新文章或文档进行「入库 / Ingest」时，**必须完整执行以下闭环动作**：
1. **深度阅读与原始净化**：阅读原始资料（如 `raw/xxx.md` 或 `Clippings/xxx.md`），若正文不足则抓取 URL 全文。提炼 3-7 条核心要点与关键引文。同时顺带执行**语法净化**（转义正文行内 `#xxx` 防止全局 Tag 污染，转义矩阵/张量等非链接的 `[[` 防止幽灵出链）。
2. **生成 Source 摘要页**：在 `wiki/sources/` 目录下创建对应的 `.md` 摘要页。
   - YAML Frontmatter 格式严格遵守规范：
     ```yaml
     ---
     type: source
     tags: [LLM/arch, AI-Agent/coding] # 需选用标准 Tag 体系
     summary: "一句话说明这篇文章/资料的核心贡献与主题"
     sources: ["raw/xxx.md"] # 100% 精准锚定物理文件路径
     updated: "YYYY-MM-DD"
     ---
     ```
   - **正文末尾物理文献插链**：为打通 Obsidian 关系图谱可视化连接（避免底层全文呈现为外围孤散点），必须在 Source 摘要页正文最末尾追加双向链接：
     `> 📎 **物理文献**：[[raw/xxx.md]]`
3. **构建双向维基网络**：在 Source 摘要页正文中，凡提及重要技术概念、人物、机构或项目，一律使用 Obsidian 链接格式 `[[entities/xxx]]` 或 `[[concepts/yyy]]` 与知识库产生链接。
4. **联动 Entities & Concepts**：检查被引用的 `wiki/entities/` 或 `wiki/concepts/` 页面是否存在：
   - 若存在：打开该实体/概念页，将新要点或进展更新进去，并在正文或来源中补充关联。
   - 若不存在但概念核心且高频：在 `wiki/entities/` 或 `wiki/concepts/` 中创建新页面。
5. **全量同步索引与日志**：
   - 打开 `wiki/index.md`，在对应分类下同步挂载**所有本次新建的 Source、Concept 与 Entity 页面**（严禁只登摘要漏登新建概念/实体）。
   - 打开 `wiki/log.md` 追加一笔日志记录：
     `## [YYYY-MM-DD] ingest | raw/xxx -> wiki/sources/xxx.md (+ affected pages)`

### 2. Query（知识查询与沉淀）
当用户提问或检索专题知识时：
1. **精准定位**：优先通过 MCP 搜索或读取 `wiki/index.md` 快速定位候选页面。
2. **综合解答**：基于页面内容回答，并给出具体来源引用（如 `如 [[wiki/sources/xxx]] 所述...`）。
3. **沉淀新知（可选）**：如果回答包含有价值的横向对比、选型分析或架构综述，主动提议将其写入 `wiki/comparisons/` 或 `wiki/overview/`；新建页面务必**在正文插链接入图谱并同步挂载至 `wiki/index.md`**，最后在 `wiki/log.md` 登记 `query | 新建 ...`。

### 3. Lint & Prune（健康检查、精简与图谱垃圾回收）
当用户要求对知识库进行「Lint / 健康检查 / 精简 / 冲突审查 / 删除收藏」时：
1. **常规扫描诊断**：
   - **图谱与链审计**：检测知识库中的观点矛盾、过时表述、孤立无入链页面、低频提及实体（如仅出现 1 次的人/组织）、以及缺失的双向链接。
   - **漏登审计**：扫描 `wiki/sources/`、`wiki/concepts/`、`wiki/entities/` 检查是否存在漏登 `wiki/index.md` 的孤立文档。
   - **语法污染扫描**：检测物理源文件中是否有未转义的行内伪 Tag 或矩阵伪出链。
2. **精简与级联清理机制（Cascading Pruning SOP）**：
   当用户主动要求删除或清理最上游原始层资料（如 `raw/xxx.md` 或 `Clippings/xxx.md`）时，**必须执行严密的图谱级联清理链条（自上而下四步法）**：
   - **第一步（精准清理摘要页）**：删除目标物理源文件时，读取所有 `wiki/sources/*.md` 的 Frontmatter，只要 `sources:` 列表中命中被删源路径，将对应的 Source 摘要页连带删除。
   - **第二步（同步更新总索引）**：打开 `wiki/index.md`，将对应分类下指向已删 Source 摘要页的索引条目自动精准剔除。
   - **第三步（入度审计与垃圾回收 GC）**：解析被删 Source 页中引用过的所有实体 `[[entities/xxx]]` 和概念 `[[concepts/yyy]]`，对它们在全库执行引用度（In-degree）检查：
     - **情况 A（剩余被引次数 $\ge 1$）**：说明属于通用核心知识，**保留页面**，仅在其正文末尾 `## 来源` 中摘除指向已删文章的链接。
     - **情况 B（剩余被引次数 $= 0$）**：说明其为随着该被删文产生的冷门孤立产物（Orphan Pages），**触发垃圾回收连带清理**。
   - **第四步（登记操作流水）**：在 `wiki/log.md` 登记 `lint/prune | prune raw/xxx.md (+ Cascading cleanup sources, index & gc entities/concepts)`。
3. **先提议，再动刀 (Dry-run & Apply)**：执行大范围图谱治理或精简清理前，先向用户输出结构化的「级联清理检查报告与影响清单」，**严禁未经确认直接大规模动刀**。确认无误后方可执行。

## Tag 体系

Tag 存放在 YAML frontmatter 的 `tags:` 数组中。使用 `/` 分隔的层级 tag。主要分支：

- `LLM/` — arch, training, inference, reasoning, hallucination, tokenization
- `AI-Agent/` — coding, tools, context-engineering, deep-research, AI-BI, skill, prompt-engineering, multi-agent, memory, UI
- `RAG/` — embedding, query, chunking, retrieval, eval
- `Skill/` — python, data-analysis, claude-code, linux
- `CV/` — detection, data-augmentation, arch
- `Infra/` — AI, gpu
- 顶层独立：`DeepLearning`, `AIGC`, `创业`, `面试`, `Life`, `Recommendation`, `TTS`

修改 tag 时，使用 `vault_patch` 操作 frontmatter 的 `tags` 字段，`contentType: application/json`，`operation: replace`。

## Git 约定

- 用户：`Hugo Yang <hugoyang1229@gmail.com>`
- 提交信息：中英文均可，带类型前缀（`docs:`, `chore:` 等）
- Obsidian Git 插件自动提交信息格式：`vault backup: {{date}}`
- 永远不要提交 `.mcp.json`（含 API token，已在 `.gitignore` 中）

## 关键文件

- `TheSchema.md` — 系统全局架构设计与核心规则总纲
- `HANDOFF.md` — 项目当前进度、近期里程碑与下一步任务
- `wiki/index.md` — Wiki 知识层总分类索引
- `wiki/log.md` — 知识库维护操作流水日志
- `notes/setup-config.md` — Obsidian 配置指南（中文界面对照）
- `.obsidian/app.json` — 附件路径设为 `assets/`，自动更新链接已开启


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
1. **深度阅读与提炼**：阅读原始资料（如 `raw/xxx.md` 或 `Clippings/xxx.md`），若正文不足则抓取 URL 全文。提炼 3-7 条核心要点与关键引文。
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
3. **构建双向维基网络**：在 Source 摘要页正文中，凡提及重要技术概念、人物、机构或项目，一律使用 Obsidian 链接格式 `[[entities/xxx]]` 或 `[[concepts/yyy]]` 与知识库产生链接。
4. **联动 Entities & Concepts**：检查被引用的 `wiki/entities/` 或 `wiki/concepts/` 页面是否存在：
   - 若存在：打开该实体/概念页，将新要点或进展更新进去，并在 `sources:` 中补充关联。
   - 若不存在但概念核心且高频：在 `wiki/entities/` 或 `wiki/concepts/` 中创建新页面。
5. **更新索引与日志**：
   - 打开 `wiki/index.md`，在对应分类下补充新页面的链接与 `summary`。
   - 打开 `wiki/log.md` 追加一笔日志记录：
     `## [YYYY-MM-DD] ingest | raw/xxx -> wiki/sources/xxx.md (+ affected pages)`

### 2. Query（知识查询与沉淀）
当用户提问或检索专题知识时：
1. **精准定位**：优先通过 MCP 搜索或读取 `wiki/index.md` 快速定位候选页面。
2. **综合解答**：基于页面内容回答，并给出具体来源引用（如 `如 [[wiki/sources/xxx]] 所述...`）。
3. **沉淀新知（可选）**：如果回答包含有价值的横向对比、选型分析或架构综述，主动提议将其写入 `wiki/comparisons/` 或 `wiki/overview/`，并在 `wiki/log.md` 登记 `query | 新建 ...`。

### 3. Lint（健康检查与图谱治理）
当用户要求对知识库进行「Lint / 健康检查 / 精简 / 冲突审查」时：
1. **扫描诊断**：检测知识库中的观点矛盾、过时表述、孤立无入链页面、低频提及实体（如仅出现 1 次的人/组织）、以及缺失的双向链接。
2. **先提议，再动刀**：先输出结构化的「治理与建议清单」（包括建议合并、拆分、移除或修补的内容），**严禁未经确认直接大规模删除或重构**。
3. **执行与登记**：用户确认同意后批量执行变更，并在 `wiki/log.md` 登记 `lint | merge/remove ...`。

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

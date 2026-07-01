# HANDOFF — 个人知识库搭建与维护

## Goal

基于 Obsidian 搭建个人知识库，实现跨平台多端访问（Mac/Win/iOS），并接入 Claude Code / Antigravity 通过 MCP 直接操作 vault。当前重心：完成 Cubox 旧笔记与新文档的结构化治理，优化 LLM Wiki 架构与元数据规范。

## Current Progress

| 事项 | 状态 | 备注 |
|------|------|------|
| Vault 初始化 + Git + GitHub 同步 | ✅ | |
| 桌面端 Obsidian + Local REST API 插件配置 | ✅ | 当前 HTTPS 端口 27124 已激活 |
| Claude Code / Antigravity MCP 接入 | ✅ | 配置文件建立于根目录 `.mcp.json` |
| 全量 Cubox 文章 Ingest（Phase 1-6，191 篇） | ✅ | 构建了 191 source + 331 concept + 137 entity |
| **Wiki Sources Frontmatter 全量规范化清洗** | ✅ | **191 篇笔记 Frontmatter 100% 符合规范且无语法错误** |
| **Sources 字段物理文件关联审计与锚定** | ✅ | **191 篇笔记 100% 精准关联到 `Cubox/*.md` 物理文件** |

**当前 wiki 规模**：191 source + 331 concept + 137 entity

## What Worked

- **双重层级验证方案（API + 物理磁盘）**：
  在校验 Markdown 头部语法时，利用 HTTP 头部 `Accept: application/vnd.olrapi.note+json` 访问 Obsidian Local REST API (`https://127.0.0.1:27124/vault/{path}`)，直接让 Obsidian 底层引擎 `CachedMetadata` 进行 YAML 解析验证，确保 100% 兼容；同时配合 Python `os.path.exists` 校验实体路径，成功杜绝死链和假关联。
- **URL + 相似度双通道智能匹配**：
  对于原本只写了文章标题或旧版字典格式的 Frontmatter，自动化脚本提取页面中的有效 URL 与 `Cubox/*.md` 文件内容比对，配合文件名相似度（SequenceMatcher），实现了 100% 的无遗漏物理文件关联。
- **旧版元数据下沉正文**：
  旧版笔记把 `title`、`author`、`source_url` 等写在 Frontmatter 中导致字段冗杂。将其清洗剥离并统一格式化置入正文 `## 来源信息` 区域，既保证了 Frontmatter 简洁规范，又保留了完整追溯信息。

## What Didn't Work

- **非安全 HTTP 端口连接 (`http://127.0.0.1:27123`)**：
  在当前本地插件配置 (`obsidian-local-rest-api/data.json`) 中，`enableInsecureServer` 为 `false`，导致 HTTP 27123 端口拒绝连接。应统一使用安全 HTTPS 端口 `https://127.0.0.1:27124/mcp/` 进行 API 和 MCP 请求。
- **YAML 裸双引号直接注入**：
  部分笔记原标题或文件名带有中文/英文引号或破折号（如 `...硬核"辟谣"指南...` 或 `...NotebookLM --- Context...`），直接放入 YAML 中会导致解析器崩溃（`ParserError`）。必须使用标准的 YAML dump 转义或使用严格正则进行头部匹配划分。

## 关键配置（速查）

- **MCP 端点**：`https://127.0.0.1:27124/mcp/`，API Key 及配置在根目录 `.mcp.json`（已 gitignore）
- **Git User**：`Hugo Yang <hugoyang1229@gmail.com>`
- **Remote Repo**：`https://github.com/Parsonlee/knowledge-bank.git`
- **规则文档**：`TheSchema.md`、`AGENTS.md`、`TODO.md`

## Next Steps

### 1. Tag 体系清洗与梳理（重点优先级）
- 按照 `AGENTS.md` 定义的规范，对 `wiki/entities` 和 `wiki/sources` 下笔记的 `tags:` 列表进行整理，确保统一归入标准层级分支（如 `LLM/`, `AI-Agent/`, `RAG/`, `Skill/`, `Infra/` 等）。

### 2. 精简实体与概念页（精细化治理）
- 针对 `wiki/entities` 中出现频率低、仅提及 1 次的人或组织进行筛选评估，制定清理阈值或深度讨论优化方案。

### 3. 解析与导入工作项目文档
- `workdocs/` 目录下存放了工作期间的 Word 项目文档（`.docx` 格式），需要编写解析处理流程并导入到 Wiki 架构中。

### 4. 移动端同步与日常维护
- **iOS 同步**：通过 GitHub 细粒度 PAT 在 iOS 端 Obsidian Git 插件中完成远程同步配置。
- **自动提交**：建议确保桌面端 Obsidian Git 的 Vault backup interval 设置为 `10` 分钟。

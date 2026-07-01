# HANDOFF — 个人知识库搭建与维护

## Goal

基于 Obsidian 搭建个人知识库，实现跨平台多端访问（Mac/Win/iOS），并接入 Claude Code / Antigravity 通过 MCP 直接操作 vault。当前重心：完成 Cubox 旧笔记与新文档的结构化治理，优化 LLM Wiki 架构与元数据规范，打造可复利的知识层。

## Current Progress

| 事项 | 状态 | 备注 |
|------|------|------|
| Vault 初始化 + Git + GitHub 同步 | ✅ | |
| 桌面端 Obsidian + Local REST API 插件配置 | ✅ | 当前 HTTPS 端口 27124 已激活 |
| Claude Code / Antigravity MCP 接入 | ✅ | 配置文件建立于根目录 `.mcp.json` |
| 全量 Cubox 文章 Ingest（Phase 1-6，191 篇） | ✅ | 构建了 191 source + 331 concept + 137 entity |
| **Wiki Sources Frontmatter 全量规范化清洗** | ✅ | **191 篇笔记 Frontmatter 100% 符合规范且无语法错误** |
| **Sources 字段物理文件关联审计与锚定** | ✅ | **191 篇笔记 100% 精准关联到 `Cubox/*.md` 物理文件** |
| **Sources & Entities Tag 与 Frontmatter 标准化治理** | ✅ | **191 篇 Sources 与 137 篇 Entities 100% 拥有标准 Frontmatter 及合规技术领域 Tag** |

**当前 wiki 规模**：191 source + 331 concept + 137 entity

## What Worked

- **正交解耦架构设计（主题 Tag + 载体属性）**：
  明确了全局共用 `AGENTS.md` 定义的技术领域 Tag 树（`LLM/`, `RAG/`, `AI-Agent/` 等）以保证跨页面网状聚合互通，同时完全依靠 YAML Frontmatter 的 `type:` 属性与物理目录路径实现知识载体类型隔离，避免了 Tag 体系的分裂与污染。
- **批量脚本标准化清洗**：
  在针对 25 篇旧版无 Frontmatter（仅用 Blockquote 记录属性）的实体页进行重构时，利用 Python 自动化脚本精准解析提炼 `summary`、`sources` 和 `confidence`，并在保留正文笔记的同时一键生成合规 YAML 头部，兼顾了效率与准确率。
- **双重层级验证方案（API + 物理磁盘）**：
  在校验 Markdown 头部语法时，利用 HTTP 头部 `Accept: application/vnd.olrapi.note+json` 访问 Obsidian Local REST API (`https://127.0.0.1:27124/vault/{path}`)，直接让 Obsidian 底层引擎 `CachedMetadata` 进行 YAML 解析验证，确保 100% 兼容；同时配合 Python `os.path.exists` 校验实体路径，杜绝死链。
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

### 1. 概念页 (wiki/concepts) Tag 补全与低频精简（优先事项）
- 当前 `wiki/concepts/` 有 117 篇页面缺失 Tag。且 `entities` / `concepts` 中存在部分低频提及（如引用仅 1 次且无实质内容）的人或组织。需要按照「先提议再执行」原则，梳理概念页 Tag 并设置阈值精简合并。

### 2. 解析与导入工作项目文档 (`workdocs/`)
- `workdocs/` 目录下存放了工作期间的项目文档（`.docx` 格式），需要编写解析处理管线提取要点，导入到 Wiki 架构中并在 `wiki/sources` 生成对应项目笔记。

### 3. 五彩 (Wucai) 剪藏库同步入库
- 对接五彩高亮与剪藏数据，参照 Cubox 文章的 Ingest 标准完成清洗与双向链接建库。

### 4. 移动端同步与日常维护
- **iOS 同步**：通过 GitHub 细粒度 PAT 在 iOS 端 Obsidian Git 插件中完成远程同步配置。
- **自动提交**：建议确保桌面端 Obsidian Git 的 Vault backup interval 设置为 `10` 分钟。

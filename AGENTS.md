
This file provides guidance to Claude Code/Codex/Antigravity when working with code in this repository.

## 项目说明

基于 Obsidian 的个人知识库（vault），通过 Git 同步到 GitHub（`Parsonlee/knowledge-bank`，私有仓库）。不是软件项目——是 Markdown 笔记、剪藏和配置的集合。

## MCP 集成

Vault 内运行了 **Local REST API with MCP** 插件。当桌面端 Obsidian 打开时，Claude Code 可通过 MCP 工具（`mcp__obsidian__*`）读写搜索 vault。连接配置在 `.mcp.json`（project 范围，已 gitignore）。

- 端点：`http://127.0.0.1:27123/mcp/`（HTTP，仅本机回环）
- 认证：Bearer token 在 `.mcp.json` 中
- 前提：桌面端 Obsidian 运行中，Local REST API 插件已启用

对 vault 的操作优先使用 MCP 工具（读笔记、改 frontmatter、按 tag 搜索、移动文件）。批量/脚本场景可直接操作 `.md` 文件。

## 目录结构

| 目录 | 用途 |
|------|------|
| `Cubox/` | 主文章库——导入的剪藏，frontmatter 中有分类 tag |
| `notes/` | 原创笔记、指南、独立文章 |
| `Clippings/` | 网页剪藏（少量） |
| `inbox/` | 空的速记收件箱 |
| `assets/` | 附件（图片、PDF） |
| `tmp/` | 已 gitignore 的临时空间 |

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

- `HANDOFF.md` — 项目进度、待办事项、决策记录
- `notes/setup-config.md` — Obsidian 配置指南（中文界面对照）
- `.obsidian/app.json` — 附件路径设为 `assets/`，自动更新链接已开启

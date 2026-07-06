---
type: entity
tags:
- AI-Agent/coding
- Skill/claude-code
summary: Claude Code 是由 Anthropic 推出的一款基于终端命令行（CLI）的深度工程化 AI Coding Agent 工具。它以顶级大模型（Claude
  3.5 Sonnet / Claude 3.7 Sonnet）为引擎，可以直接在开发者的本地代码库或知识库中深度工作。
created: '2026-07-06'
updated: '2026-07-06'
---

# 实体：Claude Code

## 简介

**Claude Code** 是由 Anthropic 推出的一款基于终端命令行（CLI）的深度工程化 AI Coding Agent 工具。它以顶级大模型（Claude 3.5 Sonnet / Claude 3.7 Sonnet）为引擎，可以直接在开发者的本地代码库或知识库中深度工作。

## 核心特性与在知识库中的定位

### 1. 知识库管理员（LLM Wiki 的“大脑”）
在 [[概念_LLM_Wiki范式]] 中，Claude Code 不是单纯的问答助手，而是扮演**知识编译与维护者**的角色。通过读取工程根目录下的 `CLAUDE.md`（作为规章制度与行为准则），它能自动执行：
- 抓取外部文献（并对微信反爬等复杂场景调用 Playwright 浏览器）。
- 提炼核心观点，编写或更新结构化的 Markdown 词条。
- 维护双向链接，解决知识图谱死链与矛盾冲突。
- 自动更新全局索引 `INDEX.md` 与操作流水 `LOG.md`。

### 2. 本地化与多端联动
- **零基建依赖**：直接操作本地文件系统，配合 [[实体_Obsidian]] 实现“可读可编可查”。
- **IM 远程调用**：通过 `Claude-to-IM` 等开源桥接项目，可与飞书、微信、Slack 打通，实现移动端随时发消息即由工作站后台触发入库与编译。

## 来源与参考

- [[Claude Code与Obsidian飞书知识库搭建实践]]
- [[概念_LLM_Wiki范式]]
---
type: entity
tags:
- Skill/knowledge-bank
summary: Obsidian 是一款基于本地文件系统的强大 Markdown 个人知识库与笔记管理软件。它以“离线优先、私有数据绝对掌控、双向链接（Bi-directional
  Links）与图谱可视化”为核心特色。
sources:
- raw/Claude Code + Obsidian + 飞书，我搭了一套会自己长大的知识库.md
- raw/一套提示词帮你实现小红书、公众号封面自由.md
- wiki/sources/Claude Code与Obsidian飞书知识库搭建实践.md
created: '2026-07-06'
updated: '2026-07-06'
---

# 实体：Obsidian

## 简介

**Obsidian** 是一款基于本地文件系统的强大 Markdown 个人知识库与笔记管理软件。它以“离线优先、私有数据绝对掌控、双向链接（Bi-directional Links）与图谱可视化”为核心特色。

## 在 AI 知识管理中的核心作用

在 [[概念_LLM_Wiki范式]]（由 [[实体_Andrej_Karpathy]] 倡导）和现代化个人知识库架构中，Obsidian 被定位为 **"IDE"（集成开发环境）**：
- **纯文本与开放性**：所有笔记均以 `.md` 格式保存在本地 Vault 文件夹中，为 AI 智能体（如 [[实体_Claude_Code]]）直接通过命令行或 MCP（Model Context Protocol）读写提供了天然的“无障碍代码库”。
- **Graph View（知识图谱）**：作为人类观察知识网络的“眼睛”，以可视化节点与连线展示各个层级概念的密集关联度与生长时间线。
- **与 MCP 深度融合**：通过 Local REST API 等插件，支持 AI Agent 在桌面端打开时实现高精准的秒级搜索、标签筛选、Frontmatter 增删与页面联现。

## 来源与参考

- [[Claude Code与Obsidian飞书知识库搭建实践]]
- [[概念_LLM_Wiki范式]]
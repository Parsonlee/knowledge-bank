---
type: source
tags:
  - AI-Agent/MCP
  - AI-Agent/tool-calling
summary: 介绍了 AI 工程师必须掌握的 6 个 Model Context Protocol (MCP) 原语，包括客户端的 Sampling、Roots、Elicitations，以及服务端的 Tools、Resources、Prompts，阐述了其作为双向通信协议超越传统单向工具调用的特性。
sources:
  - raw/articles/2026-03-04_6-must-know-MCP-primitives-for-AI-Engineers_19cba7.md
updated: '2026-08-03'
---

## 来源信息

- **来源**: Daily Dose of DS
- **原标题**: [6 must-know MCP primitives for AI Engineers](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-1/)
- **日期**: 2026-03-04
- **作者**: Avi Chawla

## 核心要点

1. **双向通信架构**：MCP 与传统单向的工具调用（Tool Calling）不同，它在 AI 应用（客户端/Client）与工具服务端（Server）之间建立起对称的双向通信通道，极大地扩展了交互能力。
2. **客户端（Client-side）三大原语**：
   - **Sampling (采样原语)**：服务器可反向要求客户端的本地 LLM 生成文本补全，同时由客户端来控制执行权限、计费与安全性。
   - **Roots (根路径原语)**：允许客户端限定服务器能访问的本地文件目录范围，提供了沙箱隔离的安全保障。
   - **Elicitations (启发/人工介入原语)**：服务器可在任务中途，以结构化的形式向客户端或用户请求必要的输入以确认操作。
3. **服务端（Server-side）三大原语**：
   - **Tools (工具原语)**：由模型主动触发的可执行函数，如写入数据库、发送邮件或触发逻辑。
   - **Resources (资源原语)**：由应用层控制的只读被动数据，如文件内容、数据库 Schema 或外部文档。
   - **Prompts (提示模板)**：预设的结构化 Prompt 模板，帮助用户快速组合工具和资源来完成特定工作流。

## 关键引文

> "But unlike simple tool calling, MCP creates a two-way communication between your AI apps and servers."
> "Elicitations: This allows servers to request user input mid-task, in a structured way."

## 关联概念/实体

- **关联概念**：[[wiki/concepts/概念_MCP六大原语]]

> 📎 **物理文献**：[[raw/articles/2026-03-04_6-must-know-MCP-primitives-for-AI-Engineers_19cba7.md]]

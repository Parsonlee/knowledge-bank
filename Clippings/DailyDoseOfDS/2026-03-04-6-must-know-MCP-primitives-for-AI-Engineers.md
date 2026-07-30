---
title: "6 must-know MCP primitives for AI Engineers."
source: "https://mail.google.com/mail/u/0/#inbox/19cba7e7c4fb570a"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-04
created: 2026-07-30
description: "深度剖析模型上下文协议（Model Context Protocol, MCP）的 6 大核心原语，包含客户端的 Sampling、Roots、Elicitations 与服务端的 Tools、Resources、Prompts。"
tags:
  - clippings
---

# AI 工程师必知的 6 大 MCP 原语（6 must-know MCP primitives for AI Engineers.）

许多开发者认为模型上下文协议（Model Context Protocol, MCP）仅仅是另一种简单的工具调用（Tool Calling）标准，但这仅仅触及了 MCP 的皮毛。

与单向的函数调用不同，MCP 在 AI 应用（客户端）与 MCP 服务端之间建立了**双向交互与安全隔离的完整基础设施**。

本文将拆解赋予 MCP 强大能力的 6 大核心原语（Primitives）。

![MCP 双向通讯架构与 6 大核心原语结构图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff36fe7ed-476e-41ff-9db2-2ccdeae564eb_2060x1368.png)
*图 1：MCP 双向通讯架构与 6 大核心原语结构图解*

---

### 一、 客户端三大原语（Client-side Primitives）

MCP 客户端通常拥有 LLM 的控制主权，它向服务端暴露了 3 个关键能力：

1. **Sampling（采样）**：允许 MCP 服务端向客户端的 LLM 请求补全（Completions）。服务端可以借用客户端的 LLM 模型算力完成子任务，但权限控制仍握在客户端手中。
2. **Roots（根目录）**：定义服务端能够访问的文件系统范围，实现代码与数据的安全沙箱隔离（Sandboxed & Scoped）。
3. **Elicitations（反向问询）**：允许服务端在任务执行中途，以结构化的方式向人类用户请求补充信息或选择。

---

### 二、 服务端三大原语（Server-side Primitives）

MCP 服务端向应用暴露了另外 3 个核心能力：

4. **Tools（工具）**：由模型驱动控制的函数，负责执行写入数据库、触发外部逻辑、发送邮件等主动操作。
5. **Resources（资源）**：由应用程序控制的被动只读数据（如本地文件、日历事件、知识库文档）。
6. **Prompts（提示词模版）**：由用户选择控制的预构建指令模板，引导 LLM 如何组合利用 Tools 和 Resources。

### 总结

掌握 Sampling、Roots、Elicitations、Tools、Resources 和 Prompts 这 6 大原语，是构建企业级安全、可扩展 AI Agent 系统的核心基础。

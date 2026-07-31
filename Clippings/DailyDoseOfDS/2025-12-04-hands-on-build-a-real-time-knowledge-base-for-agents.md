---
title: "[Hands-on] Build a real-time knowledge base for Agents"
source: "https://mail.google.com/mail/u/0/#inbox/19aeb04f6c67ee9d"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-04
created: 2026-07-30
description: "介绍开源框架 Airweave，展示如何为 AI Agent 构建实时双时域知识库，实现跨应用与数据库的即时数据检索。"
tags:
  - clippings
---

# 实战：为 Agent 构建实时知识库！（[Hands-on] Build a real-time knowledge base for Agents）

实时知识库（Real-time knowledge bases）代表了 Agent 工作流的未来方向。

今天，我们将学习如何使用 **Airweave** 构建一个实时知识库。Airweave 是一个开源框架，用于构建即时、双时域（bi-temporal）的知识库，让你的 Agent 始终基于最新的事实数据做出推理决策。

![Airweave 实时知识库架构图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5e9dacd-b48d-4769-a759-9a1fdc6a67d2_1068x1068.png)

---

### 核心功能与特点

* **无缝集成多种数据源**：Airweave 可连接至 Notion、Google Drive 以及 SQL 数据库等工具，将其内容实时转化为可检索的知识体系。
* **本地容器化运行**：整体架构可以在你本地机器的 Docker 容器中轻松部署。
* **灵活接口暴露**：支持通过 API 以及 MCP Server（模型上下文协议服务器）进行暴露供 Agent 轻松调用。

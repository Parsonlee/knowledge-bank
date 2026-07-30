---
title: "MCP 工作流中的 Sampling 入门（含实现）"
source: "https://mail.google.com/mail/u/0/#inbox/197941692c48e0a4"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-21
created: 2026-07-30
description: "MCP 速成课第 5 部分介绍如何将 Sampling 集成进 MCP 工作流，并回顾前四部分的主题与实现内容。"
tags:
  - clippings
---

# MCP 工作流中的 Sampling 入门（含实现）

[MCP 速成课第 5 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-5)现已发布，讲解把 Sampling 集成到 MCP 工作流的过程。该部分涵盖：

- 什么是 Sampling，以及它为何有用；
- FastMCP 中对 Sampling 的支持；
- 服务端如何工作；
- 如何在客户端编写 sampling handler；
- 模型偏好（model preferences）；
- Sampling 的使用场景；
- 错误处理和一些最佳实践。

和此前关于 [RAG](https://www.dailydoseofds.com/a-crash-course-on-building-rag-systems-part-1-with-implementations/) 与 [AI Agent](https://www.dailydoseofds.com/ai-agents-crash-course-part-1-with-implementation/) 的系列一样，这个系列兼顾基础与实现，逐步带领读者完成学习。

## 前四部分回顾

### 第 1 部分

[MCP 速成课第 1 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-1/) 介绍：

- LLM 中上下文管理为什么重要；
- 提示、链式调用和函数调用的局限；
- 工具集成中的 M×N 问题；
- MCP 如何通过结构化的 Host–Client–Server 模型解决这个问题。

### 第 2 部分

[MCP 速成课第 2 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-2/) 进入实践，涵盖：

- MCP 的核心能力：Tools、Resources 与 Prompts；
- JSON-RPC 如何驱动通信；
- 传输机制：Stdio、HTTP + SSE；
- 一个可运行的、与 Claude 和 Cursor 配合的完整 MCP 服务器；
- 函数调用与 MCP 的比较。

### 第 3 部分

[MCP 速成课第 3 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-3/) 从零构建了一个完全自定义的 MCP 客户端：

- 如何构建不依赖 Cursor 或 Claude 等预构建方案的自定义 MCP 客户端；
- 完整 MCP 生命周期实际运行时的样子；
- 通过实际集成揭示 MCP 作为客户端—服务器架构的本质；
- 通过动手实现说明 MCP 与传统 API、函数调用的区别。

### 第 4 部分

[MCP 速成课第 4 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-4/) 使用工具、资源和提示构建完整 MCP 工作流，内容包括：

- MCP 中 resources 和 prompts 的具体含义；
- 在服务端实现 resources 与 prompts；
- tools、resources 和 prompts 之间的区别；
- 在 Claude Desktop 内使用 resources 与 prompts；
- 一个通过 tools、prompts 与 resources 协同驱动的完整真实场景用例。

该协议已经在真实世界的 Agent 系统中发挥作用；本速成课将从第一性原理到生产使用，说明如何实现和扩展它。

---
title: "在四种主流智能体框架中实用地集成 MCP"
source: "https://mail.google.com/mail/u/0/#inbox/1980063d889e559c"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-07-12
created: 2026-07-30
description: "MCP 速成课程第 8 部分介绍如何将 MCP 接入 LangGraph、LlamaIndex、CrewAI 与 PydanticAI，并回顾该系列此前的基础、实现、安全与沙箱主题。"
tags:
  - clippings
---

# 在四种主流智能体框架中实用地集成 MCP

[MCP 速成课程第 8 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-8)现已发布，讲解如何将 MCP 集成进四个被广泛采用的智能体框架：LangGraph、LlamaIndex、CrewAI 和 PydanticAI。

![MCP 课程内容概览](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c09dee5-4d57-40f4-89a7-4cdbed33ba47_1000x302.png)

本部分具体涵盖：

- MCP 的近期进展；
- 对上述四个框架的清晰、简明介绍；
- 将 MCP 连接到每个框架的分步实操流程。

每种集成均配有详细实现，目标是不仅理解思路，也能将集成工作带入自己的技术栈。

## 系列内容回顾

该系列延续此前 RAG 和 AI Agents 系列的风格，兼顾基础知识和实施细节，按步骤展开。

- [第 1 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-1/)：说明 LLM 中上下文管理的重要性、提示词/链式调用/函数调用的局限、工具集成的 $M \times N$ 问题，以及 MCP 如何以 Host–Client–Server 结构解决该问题。
- [第 2 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-2/)：介绍 Tools、Resources、Prompts 三项核心能力，JSON-RPC 通信，Stdio 与 HTTP + SSE 传输方式；并给出可运行的 MCP Server（配合 Claude 和 Cursor）以及函数调用与 MCP 的比较。
- [第 3 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-3/)：从零构建自定义 MCP Client，不依赖 Cursor 或 Claude 等预构建方案；借由实作展示完整生命周期、客户端—服务器架构，以及 MCP 与传统 API、函数调用的差别。
- [第 4 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-4/)：构建同时运用工具、资源和提示词的完整 MCP 工作流；说明资源与提示词的含义、服务端实现、三者的区别、Claude Desktop 中的使用方式，以及真实场景中的协同。
- [第 5 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-5)：讨论 sampling、FastMCP 对 sampling 的支持、服务端机制、客户端 sampling handler、模型偏好、适用场景、错误处理与实践建议。
- [第 6 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-6)与[第 7 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-7)：覆盖 MCP 工作流的测试、安全和沙箱化，包括 MCP Inspector、提示词注入、工具投毒、服务器冒充、能力暴露过度、MCP roots 的边界定义与执行，以及使用 Docker 容器化 FastMCP Server、运行时限制和沙箱客户端连接。

MCP 已在真实的智能体系统中发挥作用；这一系列从第一性原理到生产使用，讲解如何实现和扩展它。

> 延伸阅读：[第 8 部分课程页面](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-8)。

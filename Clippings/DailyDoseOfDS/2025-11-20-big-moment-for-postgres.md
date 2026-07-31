---
title: "Postgres 的重要时刻！（Big moment for Postgres!）"
source: "https://mail.google.com/mail/u/0/#inbox/19aa2d674dcfaef6"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-20
created: 2026-07-30
description: "介绍了 Tiger Data 推出的 Agentic Postgres，这是一个专为 AI Agent 设计的 Postgres 版本，支持分支、内置 MCP 服务器、混合搜索和原生内存。"
tags:
  - clippings
---

# Postgres 的重要时刻！（Big moment for Postgres!）

AI Agent 打破了传统数据库的功能定位。

传统数据库是为人类建立的，而 Agent 打破了这种模式。

* 它们无休止地分支。
* 它们同时运行十个实验。
* 它们需要隔离、上下文、内存、结构化推理和安全的沙盒。

让 Agent 接触生产系统是可怕的，因为 Postgres 的旧模型从来不是为了这种行为而建立的。

Agentic Postgres 是 Tiger Data 推出的一款适用于 Agent 的 Postgres 版本，它解决了这个问题。

我们认为这是今年 Agent 技术栈最大的升级之一。

一些关键特性：

* 它能瞬间创建整个数据库的分支，这对于并行的 Agent 评估、安全的实验、迁移或隔离测试来说非常完美。Fork 只需几秒钟，而且几乎不需要成本。
* 它内置了一个 MCP 服务器，Agent 可以用它来获取模式指导、最佳实践以及安全、结构化地访问 Postgres。这对于在真正理解的基础上运行迁移也很有帮助。
* 它自带真正的混合搜索（向量搜索和 BM25），因此 Agent 可以直接在数据库内部检索数据。
* 数据库原生支持 Memory（内存/记忆）。这为 Agent 的进化提供了一个持久的上下文。

这是我们第一次看到 Postgres 让人感觉已经为 AI 原生时代做好了准备。

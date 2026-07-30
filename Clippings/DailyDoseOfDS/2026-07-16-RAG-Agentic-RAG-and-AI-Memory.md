---
title: "RAG, Agentic RAG, and AI Memory"
source: "https://mail.google.com/mail/u/0/#inbox/19f6ca0f2c928ca3"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-16
created: 2026-07-30
description: "梳理 AI 检索架构从传统 RAG（单次只读检索）到 Agentic RAG（基于工具调用的动态检索），再到 AI Memory（读写结合与持续学习）的演进脉络。"
tags:
  - clippings
---

# RAG、Agentic RAG 与 AI Memory 演进全景（RAG, Agentic RAG, and AI Memory）

RAG 从来都不是终点。

**AI Agent 的记忆（Memory）才是所有技术的演进方向。**

让我们用最简单的方式拆解这一演进过程。

![RAG, Agentic RAG 与 AI Memory 架构对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9f7cfaf-2340-4084-8eb2-147bb9361d06_1478x1371.gif)

* **RAG (2020-2023)**：
  * 单次检索信息，生成回答
  * 无决策能力，仅执行“获取并回答”
  * 痛点：经常检索出无关的上下文

* **Agentic RAG**：
  * Agent 自行决定*是否*需要检索
  * Agent 挑选*哪一个*数据源进行查询
  * Agent 验证检索结果*是否*有用
  * 痛点：依然是纯只读模式，无法从交互中学习

* **AI Memory**：
  * 对外部知识库同时进行**读取与写入**
  * 从过往对话中不断学习
  * 记住用户偏好与历史上下文
  * 实现真正意义上的个性化

思维模型非常直化：
* **RAG**：只读（Read-only），单次交互（One-shot）
* **Agentic RAG**：通过工具调用实现只读（Read-only via tool calls）
* **Agent Memory**：通过工具调用实现读写（Read-write via tool calls）

---

### 赋予 Agent 记忆力的强大之处

Agent 现在可以“记住”事情，例如用户偏好、历史对话以及重要日期。所有这些信息都被存储起来，并可在未来的交互中随时检索。

这解锁了更宏大的能力：**持续学习（Continual Learning）**。

Agent 不再冻结在训练完成的那一刻，而是能够从每一次交互中积累知识。它们不需要重新训练就能随着时间的推移不断进化。

记忆是将静态模型转变为真正自适应 AI 系统的桥梁。

但这也并非一帆风顺。

记忆引入了传统 RAG 从未遇到过的新挑战：**记忆污染/损坏（Memory Corruption）**、**决定该遗忘什么（Deciding what to forget）**，以及**管理多种记忆类型（程序性记忆 Procedural、情境性记忆 Episodic 和语义记忆 Semantic）**。

从头解决这些问题非常困难。如果你想为你的 Agent 赋予类人的记忆能力，可以了解一下 [Graphiti](https://github.com/getzep/graphiti)——一个用于构建实时知识图谱的开源框架。

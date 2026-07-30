---
title: "AI Agent Tech Stack!"
source: "https://mail.google.com/mail/u/0/#inbox/19b522575aa6f7ef"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-24
created: 2026-07-30
description: "梳理构建 AI Agent 系统的完整技术栈，全面解析开发框架、基座模型、向量存储、工具执行、记忆管理与可观测性六大核心层级。"
tags:
  - clippings
---

# AI Agent 技术栈全景拆解！（AI Agent Tech Stack!）

构建 AI Agent 已经不再仅仅是选择一个模型，而是需要在多个关键层级上组装出正确的技术栈。

我们整理了下面这张全景图解，全面梳理了当前 Agent 系统在各个层级上的主流技术路线：

![AI Agent 技术栈全景图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F087bd811-1545-440c-905b-5234350d7f88_1200x846.png)

---

### 六大关键技术层级拆解

1. **Agent 开发框架（Agent Development Frameworks）**：
   * 这是你的 Agent 控制逻辑所在之处。
   * 开源解决方案（如 LangGraph、CrewAI、Google ADK）正与托管云服务（如 AWS Bedrock、Vertex AI）展开强力竞争。

2. **基座模型（Foundation Models）**：
   * 这是整个系统的“大脑”。
   * 分为开源权重模型（Llama、Mistral、DeepSeek、Qwen）与闭源 API 模型（Claude、GPT、Gemini）。你在这一步的选择将塑造下游的一切。

3. **数据存储（Data Storage）**：
   * 向量数据库（Vector DBs）对于绝大多数 LLM 和 Agent 应用来说是不可或缺的基础设施。

4. **工具执行层（Tool Execution）**：
   * 该层级定义了 Agent 如何通过外部工具开展实际行动。
   * Composio 在工具编排领域正获得巨大的关注。

5. **记忆管理（Memory Management）**：
   * Mem0、Zep 和 Cognee 等正在解决“Agent 如何在跨 Session 中长久保留上下文记忆”的挑战。

6. **可观测性（Observability）**：
   * 无法度量就无法改进。使用 DeepEval、Opik 和 LangSmith 等开展链路追踪与系统评估。

---
title: "AI Agent 的 MCP 与 Skills：连接层与知识层的分工"
source: "https://mail.google.com/mail/u/0/#inbox/19faa9c1ec5cf9ba"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-28
created: 2026-07-30
description: "区分 MCP 与 Skill：MCP 负责工具连接，Skill 封装面向具体任务的程序性知识，Agent 则结合上下文和推理编排两者。"
tags:
  - clippings
---

# AI Agent 的 MCP 与 Skills：连接层与知识层的分工（MCP & Skills for AI agents）

![原邮件配图](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/9rGBZYGBphFvZMS29EyxdM/email)

MCP 与 Skills 并不是同一件事！

当人们开始认真构建 AI Agent 时，把两者混为一谈是最常见的错误之一。

邮件中的图解释了它们在底层如何工作。

下面从头拆解这两者。

> [!info] 课程推广
> 邮件推广了其 [MCP 课程](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-1/)，并表示课程包含实现细节。

课程覆盖基础知识、架构、上下文管理、JSON-RPC 通信、构建完整的自定义本地 MCP 客户端、工具、资源和提示词、MCP 中的 Sampling、测试、安全与沙箱，以及与 LangGraph、LlamaIndex、CrewAI、PydanticAI 等常用 Agent 框架的集成等内容。

在 MCP 出现之前，把 AI 模型连接到外部工具意味着每次都要编写自定义集成代码。

例如，10 个模型与 100 个工具会带来 1,000 个需要构建和维护的独特连接器。

MCP 通过一套共享通信标准解决了这个问题。

每个工具都成为暴露自身能力的“服务器”；每个 AI Agent 都成为知道如何请求的“客户端”。它们通过结构化 JSON 消息，在清晰、定义良好的接口上通信。

例如，一个 GitHub MCP server 只需构建一次，便可与 Claude、ChatGPT、Cursor 或任何其他会说 MCP 的 Agent 一起工作。这就是核心价值：**一次编写集成，处处复用。**

但大多数解释恰恰止步于此。

MCP 解决了连接问题，却没有解决使用问题。

也就是说，即使你给 Agent 接入 50 个连接完善的 MCP 工具，如果它不知道何时调用哪个工具、按什么顺序调用、以及应携带什么上下文，它仍然可能表现不佳。

这正是 Skill 试图填补的空白。

Skill 是一个可移植的程序性知识包。可以把它想成一个 `SKILL.md` 文件：它告诉 Agent 的不只是“这里有你的工具”，还包括“针对这项具体任务，应当怎样使用它们”。

写作 Skill 可以封装语气指南和输出模板；代码审查 Skill 可以封装应检查的模式与应遵循的规则。

**MCP 给 Agent 一只手；Skills 给它肌肉记忆。**

它们共同构成生产级 AI Agent 的完整能力栈：

- MCP 负责工具连接（wiring layer，布线层）。
- Skills 负责任务执行（knowledge layer，知识层）。
- Agent 运用自身的上下文与推理来编排两者。

因此，先进的 Agent 配置日益同时交付两类能力：为集成提供 MCP servers，为领域专长提供 `SKILL.md` 文件。

如果你在构建 Agent，邮件提到 [skills.sh](https://skills.sh/) 是一个包含 85,000+ Skills、可供任何 Agent 使用的仓库。

> [!info] 课程推广：MCP 课程分篇
> - [第 1 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-1/)：基础、架构与上下文管理。
> - [第 2 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-2/)：核心能力、JSON-RPC 通信等。
> - [第 3 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-3/)：构建完整的自定义本地 MCP 客户端。
> - [第 4 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-4/)：使用工具、资源和提示词构建完整 MCP 工作流。
> - [第 5 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-5/)：将 Sampling 集成到 MCP 工作流。
> - [第 6 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-6)：MCP 工作流中的测试、安全与沙箱。
> - [第 7 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-7)：测试、安全与沙箱。
> - [第 8 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-8)：与 LangGraph、LlamaIndex、CrewAI 和 PydanticAI 集成。
> - [第 9 部分](https://www.dailydoseofds.com/model-context-protocol-crash-course-part-9)：用 LangGraph MCP 工作流构建综合性的真实案例。

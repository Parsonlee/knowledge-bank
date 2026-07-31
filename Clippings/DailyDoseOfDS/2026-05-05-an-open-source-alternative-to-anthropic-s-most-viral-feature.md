---
title: "An open-source alternative to Anthropic’s most viral feature!"
source: "https://mail.google.com/mail/u/0/#inbox/19dfa25648e2f2cb"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-05
created: 2026-07-30
description: "开源 Generative UI 框架 CopilotKit（Open Generative UI）打破 Anthropic 独占，实现运行时流式生成与沙箱隔离可视化界面。"
tags:
  - clippings
---

# Anthropic 最火爆功能的开源替代方案（An open-source alternative to Anthropic’s most viral feature!）

在此之前，Anthropic 的 **Generative UI（生成式用户界面）** 功能仅存在于其自家产品中。

由 CopilotKit 推出的 **Open Generative UI** 是对该范式的一个开源实现，能够在任何应用中运行。

Agent（智能体）会在运行时实时生成 HTML/SVG，而 CopilotKit 会将其逐 Token（令牌）地以流式传输方式渲染到应用聊天界面内部的一个沙箱化 iframe 中。

因此，用户可以实时观察 UI 自行组装构建的过程，而无需等待完整响应生成完毕。

![Open Generative UI 实时构建图示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdee18025-d723-4e66-9a7c-cb55e92f6e49_2528x1696.jpeg)

该沙箱具备完全隔离性，无法访问父应用、DOM 或用户数据。因此，即使 Agent 幻觉生成了损坏的标记或意料之外的 JavaScript 代码，也不会有任何内容泄漏到 iframe 之外。

在底层机制上，Agent 并不会从预构建的组件库中进行选择。相反，它每次都会从零开始生成任意视觉效果。

默认情况下输出是不受约束的，但你可以通过定义**基于 Prompt 的技能（Skills）**来塑造它，指导 Agent 遵循特定的视觉格式或设计规范。

例如，一个技能提示词（Skill Prompt）可以引导 Agent 生成带有规范轴标签和响应式尺寸的 Chart.js 仪表板，或是带有旋转控制功能的交互式 3D 模型。

![Prompt 技能导向的生成对比图示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fae961770-46b8-4fe5-a303-9ab829f54b51_2528x1696.jpeg)

上图展示了这一点，你所看到的输出质量实际上来源于技能层（Skills Layer）的提炼与约束。

Open Generative UI 运行在 AG-UI 之上，因此它开箱即用支持 LangGraph、CrewAI、Mastra、Google ADK、AWS Strands 等多种 Agent 框架。

它还附带了一个独立运行的 MCP Server（模型上下文协议服务器），可直接插接到 Claude Code、Cursor 或任何兼容 MCP 的客户端中。

整个技术栈建立在 CopilotKit 之上——这是一个专为 Agent 和生成式 UI 打造的开源前端框架，在 GitHub 上拥有 30k+ Stars，并提供了 React、Next.js、Angular 和 Vue 的 SDK。

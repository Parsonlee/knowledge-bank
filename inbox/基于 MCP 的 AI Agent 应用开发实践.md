---
title: "基于 MCP 的 AI Agent 应用开发实践"
source: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247514365&idx=1&sn=dd898cc5dfe8ab4fe7c48442a2d7fc35&subscene=0
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# 基于 MCP 的 AI Agent 应用开发实践

> [!quote]
> 痛点
> 缺少标准化的上下文和工具集导致开发者的三大痛点：
> 开发耦合度高：工具开发者需要深入了解 Agent 的内部实现细节，并在 Agent 层编写工具代码。这导致在工具的开发与调试困难。
> 工具复用性差：因每个工具实现都耦合在 Agent 应用代码内，即使是通过 API 实现适配层在给到 LLM 的出入参上也有区别。从编程语言角度来讲，没办法做到跨编程语言进行复用。
> 生态碎片化：工具提供方能提供的只有 OpenAPI，由于缺乏标准使得不同 Agent 生态中的工具 Tool 互不兼容。

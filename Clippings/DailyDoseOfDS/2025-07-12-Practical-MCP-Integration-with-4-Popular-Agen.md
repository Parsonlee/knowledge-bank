---
title: ​Practical MCP Integration with 4 Popular Agentic Frameworks​
source: https://mail.google.com/mail/u/0/#inbox/1980063d889e559c
author:
  - "[[DailyDoseOfDS]]"
published: 2025-07-12
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 ​Practical MCP Integration with 4 Popular Agentic Frameworks​ 的原理剖析与工程实践。
tags:
  - clippings
---

# ​Practical MCP Integration with 4 Popular Agentic Frameworks​

## 1. 核心要点解析

本期内容重点涵盖：
- **​Practical MCP Integration with 4 Popular Agentic Frameworks​**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/l2hehmhlzq5e2zb6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* ​Practical MCP integration with 4 Popular Agentic frameworks​.
* Where did the GPU memory go?
* [Hands-on] ​Build a 100% local Llama-OCR app​.​

Reading time: 3 minutes.

TODAY'S ISSUE

MCP
---

-----------------------------------------------------------------
​Practical MCP integration with 4 Agentic frameworks (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/m2h7h5h372kv5nsm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC04Lw==
)​
-----------------------------------------------------------------

​Part 8 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/m2h7h5h372kv5nsm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC04Lw==
) of the MCP crash course is now available, where we cover how to
integrate MCPs with some of the most widely used agentic
frameworks: LangGraph, LlamaIndex, CrewAI, and PydanticAI.

​MCP crash course part 8 → (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/dpheh0hemdzv6qam/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC04
)​

-->​MCP crash course part 8 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/dpheh0hemdzv6qam/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC04
)
​MCP crash course part 8 (
https://www.dailydoseofds.com/model-context-protocol-crash-course-part-8
)More specifically, it covers:

​
* Some recent advancements in MCPs.
* A clear and concise primer on each of the four frameworks.
* Step-by-step practical walkthroughs for connecting MCP into
each framework.

Each integration is accompanied by detailed implementations,
ensuring you not only grasp the idea but can also perform
integrations into your own stack.

Just like our past series on RAG (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/e0hph7h72m96v0b8/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
) and AI Agents (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/7qh7h8h9mdvql9hz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYWktYWdlbnRzLWNyYXNoLWNvdXJzZS1wYXJ0LTEtd2l0aC1pbXBsZW1lbnRhdGlvbi8=
), this series is both foundational and implementation-heavy,
walking you through everything step-by-step.

​
​In Part 1 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/owhkhqhw7x3p9ghv/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0xLw==
), we introduce:

-->​MCP crash course Part 1 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/owhkhqhw7x3p9ghv/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0xLw==
)
​MCP crash course Part 1 (
https://www.dailydoseofds.com/model-context-protocol-crash-course-part-1/
)* Why context management matters in LLMs.
* The limitations of prompting, chaining, and function calling.
* The M×N problem in tool integrations..
* And how MCP solves it through a structured Host–Client–Server
model.

​In Part 2 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/z2hghnhe859n6wip/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0yLw==
), we go hands-on and cover:

-->​MCP crash course Part 2 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/z2hghnhe859n6wip/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0yLw==
)
​MCP crash course Part 2 (
https://www.dailydoseofds.com/model-context-protocol-crash-course-part-2/
)* The core capabilities in MCP (Tools, Resources, Prompts).
* How JSON-RPC powers communication.
* Transport mechanisms (Stdio, HTTP + SSE).
* A complete, working MCP server with Claude and Cursor.
* Comparison between function calling and MCPs.

​In Part 3 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/p8heh9h4lrkm68bq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0zLw==
), we built a fully custom MCP client from scratch:

-->​MCP crash course Part 3 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/p8heh9h4lrkm68bq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0zLw==
)
​MCP crash course Part 3 (
https://www.dailydoseofds.com/model-context-protocol-crash-course-part-3/
)* How to build a custom MCP client and not rely on prebuilt
solutions like Cursor or Claude.
* What the full MCP lifecycle looks like in action.
* The true nature of MCP as a client-server architecture, as
revealed through practical integration.
* How MCP differs from traditional API and function calling,
illustrated through hands-on implementations.

​In Part 4 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/dpheh0hemdzv6vcm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC00Lw==
), we built a full-fledged MCP workflow using tools, resources,
and prompts.

-->​MCP crash course Part 4 (
https://click.convertkit-mail2.com/k0u5k5g6nwf6h58dvprflhoqxe577i8hzn655/dpheh0hemdzv6vcm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC00Lw==
)
​MCP crash course Part 4 (
https://www.dailydoseofds.com/model-context-protocol-crash-course-part-4/
)* What exactly are resources and prompts in MCP?
* Implementing resources

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

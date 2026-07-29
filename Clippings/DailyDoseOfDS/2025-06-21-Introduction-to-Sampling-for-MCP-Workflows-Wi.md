---
title: Introduction to Sampling for MCP Workflows (With Implementation)
source: https://mail.google.com/mail/u/0/#inbox/197941692c48e0a4
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-21
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Introduction to Sampling for MCP Workflows (With Implementation) 的原理剖析与工程实践。
tags:
  - clippings
---

# Introduction to Sampling for MCP Workflows (With Implementation)

## 1. 核心要点解析

本期内容重点涵盖：
- **Introduction to Sampling for MCP Workflows (With Implementation)**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/8ghqhohopvxzomak/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* AI Engineering Hub.
* Introduction to Sampling for MCP workflows (with
implementation).
* [In case you missed it] 9 MCP projects for AI engineers.

Reading time: 3 minutes.

TODAY'S ISSUE

​AI Engineering Hub​
--------------------

-----------------------------------------------------------------
​70+ MCP, RAG, and AI Agents Projects (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/vqh3hrho37dlowbg/aHR0cHM6Ly9naXRodWIuY29tL3BhdGNoeTYzMS9haS1lbmdpbmVlcmluZy1odWIvdHJlZS9tYWlu
)​
-----------------------------------------------------------------

~6 months back, we launched the AI Engineering Hub (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/vqh3hrho37dlowbg/aHR0cHM6Ly9naXRodWIuY29tL3BhdGNoeTYzMS9haS1lbmdpbmVlcmluZy1odWIvdHJlZS9tYWlu
) repo, and yesterday, it crossed 10k+ stars on GitHub. It is
also trending on GitHub today:

​
A small ask: If you love what we do, can you star us on GitHub
here: ​AI Engineering Hub (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/vqh3hrho37dlowbg/aHR0cHM6Ly9naXRodWIuY29tL3BhdGNoeTYzMS9haS1lbmdpbmVlcmluZy1odWIvdHJlZS9tYWlu
)?

-->Star the AI Engineering Hub (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/vqh3hrho37dlowbg/aHR0cHM6Ly9naXRodWIuY29tL3BhdGNoeTYzMS9haS1lbmdpbmVlcmluZy1odWIvdHJlZS9tYWlu
)
Star the AI Engineering Hub (
https://github.com/patchy631/ai-engineering-hub/tree/main )Won’t
take more than 2 seconds. Thank you so much for your support.

MCP
---

-----------------------------------------------------------------
​Introduction to Sampling for MCP Workflows (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/l2hehmhlv9zeldh6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC01
)​
-----------------------------------------------------------------

​Part 5 of the MCP crash course (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/l2hehmhlv9zeldh6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC01
) is now available, where we explain the process to integrate
Sampling into MCP workflows.

​MCP crash course part 5 → (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/m2h7h5h30p7v3xtm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC01Lw==
)​

-->​MCP crash course part 5 (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/l2hehmhlv9zeldh6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC01
)
​MCP crash course part 5 (
https://www.dailydoseofds.com/model-context-protocol-crash-course-part-5
)More specifically, it covers:

* What is sampling, and why is it useful?
* Sampling support in FastMCP
* How does it work on the server side?
* How to write a sampling handler on the client side?
* Model preferences
* Use cases for sampling
* Error handling and some best practices

Just like our past series on RAG (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/dpheh0hewgmve3fm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
) and AI Agents (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/e0hph7h7wg26q9b8/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYWktYWdlbnRzLWNyYXNoLWNvdXJzZS1wYXJ0LTEtd2l0aC1pbXBsZW1lbnRhdGlvbi8=
), this series is both foundational and implementation-heavy,
walking you through everything step-by-step.

​
​In Part 1 (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/7qh7h8h9p7mqwkuz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0xLw==
), we introduce:

-->​MCP crash course Part 1 (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/7qh7h8h9p7mqwkuz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0xLw==
)
​MCP crash course Part 1 (
https://www.dailydoseofds.com/model-context-protocol-crash-course-part-1/
)* Why context management matters in LLMs.
* The limitations of prompting, chaining, and function calling.
* The M×N problem in tool integrations..
* And how MCP solves it through a structured Host–Client–Server
model.

​In Part 2 (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/owhkhqhwlv7pg6hv/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0yLw==
), we go hands-on and cover:

-->​MCP crash course Part 2 (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/owhkhqhwlv7pg6hv/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0yLw==
)
​MCP crash course Part 2 (
https://www.dailydoseofds.com/model-context-protocol-crash-course-part-2/
)* The core capabilities in MCP (Tools, Resources, Prompts).
* How JSON-RPC powers communication.
* Transport mechanisms (Stdio, HTTP + SSE).
* A complete, working MCP server with Claude and Cursor.
* Comparison between function calling and MCPs.

​In Part 3 (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/z2hghnherv8np7ap/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0zLw==
), we built a fully custom MCP client from scratch:

-->​MCP crash course Part 3 (
https://click.convertkit-mail2.com/wvuv9vo06zughkoq93ki7hnvgwxxxh8h4wlvv/z2hghnherv8np7ap/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

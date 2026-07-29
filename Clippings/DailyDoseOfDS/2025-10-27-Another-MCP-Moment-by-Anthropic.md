---
title: Another MCP Moment by Anthropic?
source: https://mail.google.com/mail/u/0/#inbox/19a274be34a3e99c
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-27
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Another MCP Moment by Anthropic? 的原理剖析与工程实践。
tags:
  - clippings
---

# Another MCP Moment by Anthropic?

## 1. 核心要点解析

本期内容重点涵盖：
- **Another MCP Moment by Anthropic?**

## 2. 深度拆解与正文翻译

Master full-stack AI Engineering (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/08hwh9h2g0z9wvtl/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)

----------------------
In today's newsletter:
----------------------

* Get RAG-ready data from any unstructured doc.
* Another MCP moment by Anthropic?
* ​ANN search using inverted file index​.

TODAY'S ISSUE

Parsing
-------

-----------------------------------------------------------------
Get RAG-ready data from any unstructured doc (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/8ghqhohoqe92pdfk/aHR0cHM6Ly9naXRodWIuY29tL3RlbnNvcmxha2VhaS90ZW5zb3JsYWtl
)
-----------------------------------------------------------------

Every AI company we have talked to is literally trying to solve
this problem!

How to build a RAG system that’s:

* hallucination-free
* citation-backed
* works on complex real-world docs

Here’s how you can do this in just a few lines of code:

Tensorlake (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/8ghqhohoqe92pdfk/aHR0cHM6Ly9naXRodWIuY29tL3RlbnNvcmxha2VhaS90ZW5zb3JsYWtl
) lets you extract custom-defined structured data from any
unstructured doc in just 3 steps:

-->​Tensorlake GitHub repo​ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/8ghqhohoqe92pdfk/aHR0cHM6Ly9naXRodWIuY29tL3RlbnNvcmxha2VhaS90ZW5zb3JsYWtl
)
​Tensorlake GitHub repo​ (
https://github.com/tensorlakeai/tensorlake )
​
* Define schema
* Enable citations
* Extract

This returns RAG-ready data with precise citations and bounding
boxes, which you can feed to your LLM to generate citation-backed
and auditable responses.

Find the Tensorlake GitHub repo here → (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/8ghqhohoqe92pdfk/aHR0cHM6Ly9naXRodWIuY29tL3RlbnNvcmxha2VhaS90ZW5zb3JsYWtl
) (don’t forget to star it)

-->​Tensorlake GitHub repo​ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/8ghqhohoqe92pdfk/aHR0cHM6Ly9naXRodWIuY29tL3RlbnNvcmxha2VhaS90ZW5zb3JsYWtl
)
​Tensorlake GitHub repo​ (
https://github.com/tensorlakeai/tensorlake )

Hands-on
--------

--------------------------------
Another MCP moment by Anthropic?
--------------------------------

Anthropic just released Claude Skills.

And it might be bigger than MCP:

I’ve been testing skills for the past 3-4 days, and they’re
solving a problem most people don’t talk about: agents just keep
forgetting everything.

In the video below, we have shared everything we have learned so
far.

video preview (
https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/a4xJgHQ8Nbk8g4A8riZomz/player
)-->
video preview-->
(
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/l2hehmhl65rnv9i6/aHR0cHM6Ly9hcGkuZmlsZWtpdGNkbi5jb20vZS9rN1lIUE4yNFNveHlNOG5HS1puRHhhL2E0eEpnSFE4TmJrOGc0QThyaVpvbXovcGxheWVy
)

​
It covers:

* The core idea (skills as SOPs for agents)
* Anatomy of a skill
* Skills vs. MCP vs. Projects vs. Subagents

​
* Building your own skills
* Hands-on example

Skills are the early signs of continual learning that Karpathy
also talked about in his recent podcast.

The video has everything you need to know!

That said, talking of the MCP moment, we covered everything you
need to know about MCPs in the MCP crash course.

* Part 1 covered MCP fundamentals, the architecture, context
management, etc. →​ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/m2h7h5h3mkeq06sm/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0xLw==
)
* Part 2 covered core capabilities, JSON-RPC communication, etc.
→​ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/dpheh0he8z5owlim/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0yLw==
)
* Part 3 built a fully custom and local MCP client →​ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/e0hph7h7q94lwrh8/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC0zLw==
)
* Part 4 built a full-fledged MCP workflow using tools,
resources, and prompts →​ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/7qh7h8h9wvz6pxfz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC00Lw==
)
* ​Part 5 taught how to integrate Sampling into MCP workflows →​
(
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/owhkhqhwg3o6leiv/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC01Lw==
)
* Part 6 covered testing, security, and sandboxing in MCP
Workflows →​ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/z2hghnhep9wkrgsp/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC02
)
* Part 7 covered testing, security, and sandboxing in MCP
Workflows →​ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/p8heh9h4gkx2lkhq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC03
)
* Part 8 integrated MCPs with the most widely used agentic
frameworks: LangGraph, LlamaIndex, CrewAI, and PydanticAI →​ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/6qheh8hlnvo5d5io/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC04
)
* ​P​​art 9 covered using LangGraph MCP workflows to build a
comprehensive real-world use case→ (
https://click.convertkit-mail2.com/qdu393wq7es7h4o5zeoflh89p0rkkb4h8po66/kkhmh6hn6gm53efl/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbW9kZWwtY29udGV4dC1wcm90b2NvbC1jcmFzaC1jb3Vyc2UtcGFydC05Lw==
)

vector dB
---------

-----------------------------------------

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

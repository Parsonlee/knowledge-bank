---
title: ​Context Engineering for Agents​
source: https://mail.google.com/mail/u/0/#inbox/199785061541447a
author:
  - "[[DailyDoseOfDS]]"
published: 2025-09-23
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 ​Context Engineering for Agents​ 的原理剖析与工程实践。
tags:
  - clippings
---

# ​Context Engineering for Agents​

## 1. 核心要点解析

本期内容重点涵盖：
- **​Context Engineering for Agents​**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/92umdmr368anh6d43g4a9hzpl8333hwhzg066/7qh7h8h9o53mngcz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* ​Connect any LLM to any MCP server (open-source)!
* ​Context engineering for Agents​.
* A free ML course that requires zero technical background!

* ​8 RAG architectures, explained visually​.

TODAY'S ISSUE

open-source
-----------

-----------------------------------------------------------------
​Connect any LLM to any MCP server! (
https://click.convertkit-mail2.com/92umdmr368anh6d43g4a9hzpl8333hwhzg066/owhkhqhwrd5703hv/aHR0cHM6Ly9naXRodWIuY29tL21jcC11c2UvbWNwLXVzZQ==
)​
-----------------------------------------------------------------

​
​mcp-use (
https://click.convertkit-mail2.com/92umdmr368anh6d43g4a9hzpl8333hwhzg066/owhkhqhwrd5703hv/aHR0cHM6Ly9naXRodWIuY29tL21jcC11c2UvbWNwLXVzZQ==
) is the open source framework to connect any LLM to any MCP
server and build custom agents that have tool access, without
using closed source or application clients.

It lets you build 100% local MCP clients.

​Find the GitHub repo here → (
https://click.convertkit-mail2.com/92umdmr368anh6d43g4a9hzpl8333hwhzg066/owhkhqhwrd5703hv/aHR0cHM6Ly9naXRodWIuY29tL21jcC11c2UvbWNwLXVzZQ==
) (don’t forget to star)

visual explainer
----------------

-----------------------------------------------------------------
​Context engineering for Agents (
https://click.convertkit-mail2.com/92umdmr368anh6d43g4a9hzpl8333hwhzg066/z2hghnhe3x08m4bp/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
)​
-----------------------------------------------------------------

Context engineering is getting important, but we feel that many
people still struggle a bit to truly understand what it actually
means.

Today, let’s cover everything you need to know about context
engineering in a step-by-step manner!

Let's begin!

Simply put, context engineering is the art and science of
delivering the right information, in the right format, at the
right time, to your LLM.

Here's a quote by Andrej Karpathy on context engineering...

​
To understand context engineering, it's essential to first
understand the meaning of context.

Agents today have evolved into much more than just chatbots.

The graphic below summarizes the 6 types of contexts an agent
needs to function properly, which are:

​
* Instructions
* Examples
* Knowledge
* Memory
* Tools
* Guardrails

This tells you that it's not enough to simply "prompt" the
agents.

You must engineer the input (context).

Think of it this way:

​
* If LLM is a CPU.
* Then the context window is the RAM.

You're essentially programming the "RAM" with the perfect
instructions for your AI.

How do we do it?

Context engineering can be broken down into 4 fundamental stages:

​
* Writing Context
* Selecting Context
* Compressing Context
* Isolating Context

Let's understand each, one-by-one...

1) Writing context:
-------------------

Writing context means saving it outside the context window to
help an agent perform a task.

​
You can do so by writing it to:

* Long-term memory (persists across sessions)
* Short-term memory (persists within a session)
* A state object

2) Read context:
----------------

Reading context means pulling it into the context window to help
an agent perform a task.

​
Now this context can be pulled from:

* A tool
* Memory
* Knowledge base (docs, vector DB)

3) Compressing context
----------------------

Compressing context means keeping only the tokens needed for a
task.

​
The retrieved context may contain duplicate or redundant
information (multi-turn tool calls), leading to extra tokens &
increased cost.

Context summarization helps here.

4) Isolating context
--------------------

Isolating context involves splitting it up to help an agent
perform a task.

​
Some popular ways to do so are:

* Using multiple agents (or sub-agents), each with its own
context
* Using a sandbox environment for code storage and execution
* And using a state object

So essentially, when you are building a context engineering
workflow, you are engineering a “context” pipeline so that the
LLM gets to see the right information, in the right format, at
the right time.

This is exactly how context engineering works!

Just like you engineer features so that your ML model works...

* Features that do not contribute to the output should be removed
* Highly correlated features may not help much in some cases,
etc...

...similarly, you engineer the context of the LLM so that it
responds accurately.

Nothing fancy.

👉 Over to you: What are your thoughts on context engineering?
Have you built something with it yet?

mL101
-----

-----------------------------------------------------------------
​A free ML course that requires zero technical background! (
https://click.convertkit-mail2.com/92umdmr368anh6d43g4a9hzpl8333hwhzg066/p8heh9h4zo8lp2aq/aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj0xdmtiN0JDTVFkMA==
)​
-----------------------------------------------------------------

Making Friends with Machine Learning by Cassie Kozyrkov is one of
the best introductions to ML we’ve ever seen.

​
While we are technical, the best part, in our opinion, is that it
covers everything from an intuitive and conceptual perspective
instead of being technical and programmatic.

So even if you have no technical background, you are still good
to watch this and connect the dots with real-world analogies.
​
The 6.5-hour course has 4 parts:

* Part 1: Introduction to ML
* Part 2: ML in practice
* Part 3: The 12 Steps of AI
* Part 4: Introduction to algorithms

This helps you:

* Build an intuitive understanding of

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

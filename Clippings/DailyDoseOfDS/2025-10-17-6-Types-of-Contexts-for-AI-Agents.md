---
title: 6 Types of Contexts for AI Agents
source: https://mail.google.com/mail/u/0/#inbox/199f3a89f1a116c9
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-17
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 6 Types of Contexts for AI Agents 的原理剖析与工程实践。
tags:
  - clippings
---

# 6 Types of Contexts for AI Agents

## 1. 核心要点解析

本期内容重点涵盖：
- **6 Types of Contexts for AI Agents**

## 2. 深度拆解与正文翻译

​

Master full-stack AI engineering (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/6qheh8hllrzr85bo/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)

----------------------
In today's newsletter:
----------------------

* ​Codegen: Idea to feature in seconds!​
* Keras’ post-training quantization in one line of code!
* 6 Types of contexts for AI Agents.

TODAY'S ISSUE

Together with codegen
---------------------

-----------------------------------------------------------------
Codegen: Idea to feature in seconds! (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/kkhmh6hnnwrw0eal/aHR0cHM6Ly9jb2RlZ2VuLnNoL2pvaW4=
)
-----------------------------------------------------------------

Codegen (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/kkhmh6hnnwrw0eal/aHR0cHM6Ly9jb2RlZ2VuLnNoL2pvaW4=
) lets you describe any code modification and let AI do the work.

We’ve integrated it into Slack, and now we can review PRs, ship
features, and start new projects, all without ever leaving a chat
window.

-->Build with Codegen Agents​ (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/kkhmh6hnnwrw0eal/aHR0cHM6Ly9jb2RlZ2VuLnNoL2pvaW4=
)
Build with Codegen Agents​ ( https://codegen.sh/join )Below, I
asked it to produce a video RAG using the Gemini API:

​
Codegen returned with a PR, which resulted in this:

​
Explore Codegen yourself here → (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/kkhmh6hnnwrw0eal/aHR0cHM6Ly9jb2RlZ2VuLnNoL2pvaW4=
)

-->Build with Codegen Agents​ (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/kkhmh6hnnwrw0eal/aHR0cHM6Ly9jb2RlZ2VuLnNoL2pvaW4=
)
Build with Codegen Agents​ ( https://codegen.sh/join )And yes,
you can use it for free, just connect your GitHub account.

open-source
-----------

------------------------------------------------------
Keras’ Post-training quantization in one line of code!
------------------------------------------------------

Keras now lets you quantize models with just one line of code.

Simply run model.quantize(quantization_mode) as depicted below:

​
You can either quantize your own models or any pre-trained model
obtained from KerasHub.

It supports quantization to int4, int8, float8, and GPTQ modes.

Learn more in the docs here → (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/58hvh7hggxqxdou6/aHR0cHM6Ly9rZXJhcy5pby9ndWlkZXMvcXVhbnRpemF0aW9uX292ZXJ2aWV3Lw==
)

context engineering
-------------------

-----------------------------------------------------------------
6 types of contexts for Agents (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/25h2hoh33969pec3/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYWktYWdlbnRzLWNyYXNoLWNvdXJzZS1wYXJ0LTEtd2l0aC1pbXBsZW1lbnRhdGlvbi8=
)
-----------------------------------------------------------------

A poor LLM can possibly work with an appropriate context, but
even a SOTA LLM can never make up for an incomplete context.

That is why production-grade LLM apps don’t just need
instructions but rather structure, which is the full ecosystem of
context that defines their reasoning, memory, and decision loops.

And all advanced agent architectures now treat context as a
multi-dimensional design layer, not a line in a prompt.

Here’s the mental model to use when you think about the types of
contexts for Agents:

​
* Instructions: This defines the who, why, and how:* Who’s the
agent? (PM, researcher, coding assistant)
* Why is it acting? (goal, motivation, outcome)
* How should it behave? (steps, tone, format, constraints)

* Examples: This shows what good and bad look like:* This
includes behavioral demos, structured examples, or even
anti-patterns.
* Models learn patterns much better than plain rules

* Knowledge: This is where you feed it domain knowledge.* From
business processes and APIs to data models and workflows
* This bridges the gap between text prediction and
decision-making

* Memory: You want your Agent to remember what it did in the
past. This layer gives it continuity across sessions.*
Short-term: current reasoning steps, chat history
* Long-term: facts, company knowledge, user preferences

* Tools: This layer extends the Agent’s power beyond language and
takes real-world action.* Each tool has parameters, inputs, and
examples.
* The design here decides how well your agent uses external APIs.

* Tool Results: This layer feeds the tool’s results back to the
model to enable self-correction, adaptation, and dynamic
decision-making.

These are the exact six layers that help you build fully
context-aware Agents.

Btw, this isn’t theory, it’s exactly how systems like Claude
Code, real-world agents, and effective memory tools are already
working today.

Context engineering is becoming the core skill for anyone
building long-horizon, multi-step agents.

We did a crash course to help you implement reliable Agentic
systems, understand the underlying challenges, and develop
expertise in building Agentic apps on LLMs, which every industry
cares about now.

Here’s everything we did in the crash course (with
implementation):

* ​​In Part 1​​ (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/25h2hoh33969pec3/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYWktYWdlbnRzLWNyYXNoLWNvdXJzZS1wYXJ0LTEtd2l0aC1pbXBsZW1lbnRhdGlvbi8=
), we covered the fundamentals of Agentic systems, understanding
how AI agents act autonomously to perform tasks.
* ​​In Part 2​​ (
https://click.convertkit-mail2.com/d0uwowlp78h0ho8e20lumhznv7q44ilhokgvv/qvh8h7hddwzwm6cl/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYWktYWdlbnRzLWNyYXNoLWNvdXJzZS1wYXJ0LTItd2l0aC1pbXBsZW1lbnRhdGlvbi8=
), we extended Agent capabilities by integrating custom tools,
using structured outputs, and we also

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

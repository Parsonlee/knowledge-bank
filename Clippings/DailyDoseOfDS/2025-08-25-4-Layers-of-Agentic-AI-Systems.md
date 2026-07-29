---
title: 4 Layers of Agentic AI Systems
source: https://mail.google.com/mail/u/0/#inbox/198e2e9234d8b09f
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-25
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 4 Layers of Agentic AI Systems 的原理剖析与工程实践。
tags:
  - clippings
---

# 4 Layers of Agentic AI Systems

## 1. 核心要点解析

本期内容重点涵盖：
- **4 Layers of Agentic AI Systems**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/68ud0dr3k9i8h57054xiohpl020kkh9hnlpoo/7qh7h8h90od97lfz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* ​Deploy AI apps by adding a Python decorator [open-source]​.
* 4 Layers of Agentic AI, explained visually.
* Building pairwise sentence scoring systems​.
* ​PyTorch Dataloader has two terrible default settings​.

TODAY'S ISSUE

Open-source
-----------

-----------------------------------------------------------------
​Deploy AI apps by adding a Python decorator (
https://click.convertkit-mail2.com/68ud0dr3k9i8h57054xiohpl020kkh9hnlpoo/owhkhqhw4rxwvdbv/aHR0cHM6Ly9naXRodWIuY29tL2JlYW0tY2xvdWQvYmV0YTk=
)​
-----------------------------------------------------------------

(
https://click.convertkit-mail2.com/68ud0dr3k9i8h57054xiohpl020kkh9hnlpoo/owhkhqhw4rxwvdbv/aHR0cHM6Ly9naXRodWIuY29tL2JlYW0tY2xvdWQvYmV0YTk=
)​
​Beam (
https://click.convertkit-mail2.com/68ud0dr3k9i8h57054xiohpl020kkh9hnlpoo/owhkhqhw4rxwvdbv/aHR0cHM6Ly9naXRodWIuY29tL2JlYW0tY2xvdWQvYmV0YTk=
) is an open-source alternative to Modal that makes deploying
serverless AI workloads effortless with zero infrastructure
overhead.

Steps:

* uv add beam-client
* Build your AI workflow.
* Wrap the invocation around a method.
* Decorate with the @endpoint decorator and specify server
config.

Key features:

* Lightning-fast container launches
* Distributed volume storage support
* Auto-scales from 0 to 100s of containers
* GPU support (4090s, H100s, or bring your own)
* Deploy inference endpoints with simple decorators
* Spin up isolated sandboxes for LLM-generated code

Completely open-source!

​Beam GitHub repo → (
https://click.convertkit-mail2.com/68ud0dr3k9i8h57054xiohpl020kkh9hnlpoo/owhkhqhw4rxwvdbv/aHR0cHM6Ly9naXRodWIuY29tL2JlYW0tY2xvdWQvYmV0YTk=
) (don’t forget to star)

-->​Beam GitHub repo (
https://click.convertkit-mail2.com/68ud0dr3k9i8h57054xiohpl020kkh9hnlpoo/owhkhqhw4rxwvdbv/aHR0cHM6Ly9naXRodWIuY29tL2JlYW0tY2xvdWQvYmV0YTk=
)
​Beam GitHub repo ( https://github.com/beam-cloud/beta9 )

Agents
------

-----------------------------------------------------------------
​4 Layers of Agentic AI (
https://click.convertkit-mail2.com/68ud0dr3k9i8h57054xiohpl020kkh9hnlpoo/p8heh9h49zr40wsq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYWktYWdlbnRzLWNyYXNoLWNvdXJzZS1wYXJ0LTEtd2l0aC1pbXBsZW1lbnRhdGlvbi8=
)​
-----------------------------------------------------------------

The following graphic depicts a layered overview of Agentic AI
concepts, depicting how the ecosystem is structured from the
ground up (LLMs) to higher-level orchestration (Agentic
Infrastructure).

​
Let’s break it down layer by layer:

1) LLMs (foundation layer)
--------------------------

At the core, you have LLMs like GPT, DeepSeek, etc.

Core concepts here:

* Tokenization & inference parameters: how text is broken into
tokens and processed by the model.
* Prompt engineering: designing inputs to get better outputs.
* LLM APIs: programmatic interfaces to interact with the model.

This is the engine that powers everything else.

2) AI Agents (built on LLMs)
----------------------------

Agents wrap around LLMs to give them the ability to act
autonomously.

Key responsibilities:

* Tool usage & function calling: connecting the LLM to external
APIs/tools.
* Agent reasoning: reasoning methods like ReAct (reasoning + act)
or Chain-of-Thought.
* Task planning & decomposition: breaking a big task into smaller
ones.
* Memory management: keeping track of history, context, and
long-term info.

Agents are the brains that make LLMs useful in real-world
workflows.

3) Agentic systems (multi-agent systems)
----------------------------------------

When you combine multiple agents, you get agentic systems.

Features:

* Inter-Agent communication: agents talking to each other, making
use of protocols like ACP, A2A if needed.
* Routing & scheduling: deciding which agent handles what, and
when.
* State coordination: ensuring consistency when multiple agents
collaborate.
* Multi-Agent RAG: using retrieval-augmented generation across
agents.
* Agent roles & specialization: Agents with unique purposes
* Orchestration frameworks: tools (like CrewAI, etc.) to build
workflows.

This layer is about collaboration and coordination among agents.

4) Agentic Infrastructure
-------------------------

The top layer ensures these systems are robust, scalable, and
safe.

This includes:

* Observability & logging: tracking performance and outputs
(using frameworks like DeepEval).
* Error handling & retries: resilience against failures.
* Security & access control: ensuring agents don’t overstep.
* Rate limiting & cost management: controlling resource usage.
* Workflow automation: integrating agents into broader pipelines.
* Human-in-the-loop controls: allowing human oversight and
intervention.

This layer ensures trust, safety, and scalability for
enterprise/production environments.

Overall, Agentic AI, as a whole, involves a stacked architecture,
where each outer layer adds reliability, coordination, and
governance over the inner layers.

NLP
---

-----------------------------------------------------------------
​Building pairwise sentence scoring systems (
https://click.convertkit-mail2.com/68ud0dr3k9i8h57054xiohpl020kkh9hnlpoo/x0hph6henwke65c5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYmktZW5jb2RlcnMtYW5kLWNyb3NzLWVuY29kZXJzLWZvci1zZW50ZW5jZS1wYWlyLXNpbWlsYXJpdHktc2NvcmluZy1wYXJ0LTEv
)​
-----------------------------------------------------------------

So real-world NLP systems implicitly or explicitly depend on
context similarities:

* A RAG system heavily relies on pairwise sentence scoring (this
could be at varying levels of granularity based on how you chunk
the data) to retrieve relevant co

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

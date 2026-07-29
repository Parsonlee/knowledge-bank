---
title: Agents Need a New Kind of Web Search
source: https://mail.google.com/mail/u/0/#inbox/19f6ca0f2c928ca3
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-16
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Agents Need a New Kind of Web Search 的原理剖析与工程实践。
tags:
  - clippings
---

# Agents Need a New Kind of Web Search

## 1. 核心要点解析

本期内容重点涵盖：
- **Agents Need a New Kind of Web Search**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (  )​

----------------------
In today's newsletter:
----------------------

* A free O’Reilly book on debugging production systems.
* Agents need a new kind of web search.
* RAG, Agentic RAG, and AI Memory.
* ​Knowledge Distillation using Teacher Assistant​.

TODAY'S ISSUE

TOGETHER WITH HONEYCOMB
-----------------------

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
​A free O’Reilly book on debugging production systems (  )​
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Coding agents collapsed the cost of writing code, but validation capacity stayed as is. Tests still encode only the failure modes someone anticipated, and staging still cannot reproduce production traffic.

AI-generated code makes this worse because it fails on unknown-unknowns. Nobody formed a mental model while writing it, so nobody can predict which inputs will break it.

​
The same holds for prompt changes, which can pass every offline eval and still degrade for one user segment because eval sets rarely match production traffic.

That leaves production as the only environment where this code gets validated, and it demands telemetry that answers questions nobody predicted.

Dashboards only answer the questions someone thought to set up in advance. Catching an unknown failure means keeping raw, high-cardinality events and slicing them by user ID, prompt version, or any other attribute after the fact.”

This is also why Observability Engineering, the 2022 O’Reilly book that became the standard reference on the topic, just got a near-complete rewrite.

​
The authors rebuilt it around this exact shift, with 27 net-new chapters on instrumenting LLM apps, feeding production telemetry back into evals, and debugging with agentic AI.

​Honeycomb partnered with us on this issue and has made the early-release chapters free to download → (  )​

-->​Download the book for free!​ (  )
​Download the book for free!​ ( https://fandf.co/4gcwi8P )Grab the free copy today to learn about observability engineering!

AGENTS
------

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
​Agents need a new kind of web search (  )​
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Andrej Karpathy once said LLMs are a bit like a coworker with anterograde amnesia. That’s the condition where you keep your old memories but can’t form new ones.

​
An LLM lives with that condition in two ways. It doesn’t remember you across conversations, and it never learns anything that happened after its training ended.

Memory features exist to patch the first gap. This piece is about the second one, because agents mostly get hired to deal with the present.

Markets move, people change roles, prices update, and news breaks. Web search is how the model sees any of it, and how well it works ends up deciding how useful the whole agent is.

So you bolt a search tool onto your agent and assume it can now read the web. Then you check the first few traces, and the result is disappointing.

Nearly all the tokens you paid for went into raw page text the agent had to dig through. Only a thin slice went into answering your question.

The reason is what a search call actually returns. A typical search API hands back links and thirty-word snippets, nothing more.

So the agent isn’t reading the web, it’s reading a table of contents. Fetching the actual pages becomes its job, which means pulling the HTML, stripping the markup, and digging out the usable text before any real work starts.

On a single query, you barely notice the overhead. In a task that takes several searches, like a research run or a briefing pipeline, you pay it again on every single one.

​
The problem isn’t that agents search badly. It’s that each search call returns pointers to content instead of the content itself, and the agent pays to close that gap on every call.

We ran the same question through three retrieval setups and counted tokens. The most expensive setup costs roughly 4x the cheapest retrieval option.

This piece walks through those numbers and shows what a search response should look like when an agent is the one reading it. It also covers a class of questions that only full documents can answer.

Let’s start with where the cost actually comes from.

Every loop iteration pays a retrieval cost.

That repeated fetch-and-clean work has a name. Call it the retrieval tax, the tokens an agent burns preparing content before it can reason about your problem.

One looping agent is enough to feel it. A research agent searches, reads what came back, decides what to look up next, and searches again, and every pass pays the tax on top of the last one.

​
Here’s what that costs on a single question. We picked “What was Y2K?” on purpose, because the model already knows the answer from training.

We answered it three ways, straight from memory, through a web search loop, and through an owned index (a search service that crawls and cleans pages ahead of time and stores its own processed copy of the web), counting the total tokens billed each time.

Picking a question the model already knows is what keeps the experiment clean. The thinking cost is identical in all three runs, so any tokens above it come purely from the retrieval.

* From memory, the whole thing took about 600 tokens. That’s the baseline, the cost of just answering with zero retrieval.
* An owned index is a search service that has 

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

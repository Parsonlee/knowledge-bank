---
title: Component-level Evals for LLM apps
source: https://mail.google.com/mail/u/0/#inbox/197c270c599ab371
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-30
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Component-level Evals for LLM apps 的原理剖析与工程实践。
tags:
  - clippings
---

# Component-level Evals for LLM apps

## 1. 核心要点解析

本期内容重点涵盖：
- **Component-level Evals for LLM apps**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/p8heh9h4lkv3g3aq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* ​Build any MCP server in two steps​.
* ​Component-level evals for LLM apps​.
* KV caching in LLM, explained visually.
* 4 strategies for Multi-GPU training.

Reading time: 3 minutes.

TODAY'S ISSUE

prompt-to-mcp
-------------

-----------------------------------------------------------------
​Build any MCP server in two steps (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/x0hph6hel8gr9pu5/aHR0cHM6Ly93d3cuZmFjdG9yeS5haS8=
)​
-----------------------------------------------------------------

Here's the easiest way to build any MCP server:

* Download the FastMCP repo with GitIngest.
* Give it to FactoryAI (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/x0hph6hel8gr9pu5/aHR0cHM6Ly93d3cuZmFjdG9yeS5haS8=
) and specify the MCP server to build.

Factory's Droids handle the entire workflow to generate
production-ready code with README, usage,
error-handling—everything!

-->Build with Factory! (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/x0hph6hel8gr9pu5/aHR0cHM6Ly93d3cuZmFjdG9yeS5haS8=
)
Build with Factory! ( https://www.factory.ai/ )Here’s one of our
test runs where we asked the Droids to build a stock analysis MCP
server in Factory:

​
And it did it perfectly with zero errors, while creating a README
and usage guide, and implementing error-handling, without asking:

​
​Build your own MCP server here → (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/x0hph6hel8gr9pu5/aHR0cHM6Ly93d3cuZmFjdG9yeS5haS8=
)​

LLM evaluation
--------------

-----------------------------------------------------------------
​Component-level Evals for LLM apps (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/6qheh8hldvqknwso/aHR0cHM6Ly9naXRodWIuY29tL2NvbmZpZGVudC1haS9kZWVwZXZhbA==
)​
-----------------------------------------------------------------

Most LLM evals treat the app like a black box.

Feed the input → Get the output → Run evals on the overall
end-to-end system.

​
But LLM apps need component-level evals (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/kkhmh6hn3g7d62il/aHR0cHM6Ly9kZWVwZXZhbC5jb20vZG9jcy9ldmFsdWF0aW9uLWNvbXBvbmVudC1sZXZlbC1sbG0tZXZhbHM=
) and tracing since the issue can be anywhere inside the box,
like the retriever, tool call, or the LLM itself.

In DeepEval (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/6qheh8hldvqknwso/aHR0cHM6Ly9naXRodWIuY29tL2NvbmZpZGVudC1haS9kZWVwZXZhbA==
) (open-source), you can do that in just three steps:

* Trace individual LLM components (tools, retrievers, generators)
with the @observe decorator.
* Attach different metrics to each part.
* Get a visual breakdown of what’s working on a test-case-level
and component-level.

See the example below for a RAG app:

​
Here’s a quick explanation:

* Start with some standard import statements:

​
* Define your LLM app in a method decorated with the @observe
decorator:

​
* Next, attach component-level metrics to each component you want
to trace:

​
Done!

Finally, we define some test cases and run component-level evals
on the LLM app:

​
This produces an evaluation report:

​
You can also inspect individual tests to understand why they
failed/passed:

​
There are two good things about this:

* You don't have to refactor any of your existing LLM app’s code.
* DeepEval is 100% open-source with 8500+ stars, and you can
easily self-host it so your data stays where you want.

​Here’s the GitHub repo → (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/6qheh8hldvqknwso/aHR0cHM6Ly9naXRodWIuY29tL2NvbmZpZGVudC1haS9kZWVwZXZhbA==
)​

​You can read about component-level evals in the documentation
here → (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/kkhmh6hn3g7d62il/aHR0cHM6Ly9kZWVwZXZhbC5jb20vZG9jcy9ldmFsdWF0aW9uLWNvbXBvbmVudC1sZXZlbC1sbG0tZXZhbHM=
)​

LLM inference
-------------

-----------------------------------------------------------------
​KV caching in LLMs, explained visually (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/58hvh7hgzpevkzs6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9rdi1jYWNoaW5nLWluLWxsbXMtZXhwbGFpbmVkLXZpc3VhbGx5Lw==
)​
-----------------------------------------------------------------

KV caching is a popular technique to speed up LLM inference.

To get some perspective, look at the inference speed difference
from our demo:

​
* with KV caching → 9 seconds
* without KV caching → 40 seconds (~4.5x slower, and this gap
grows as more tokens are produced).

The visual explains how it works:

​
​We covered this in detail in a recent issue here → (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/58hvh7hgzpevkzs6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vcC9rdi1jYWNoaW5nLWluLWxsbXMtZXhwbGFpbmVkLXZpc3VhbGx5Lw==
)​

​

Visual explainers
-----------------

-----------------------------------------------------------------
​4 strategies for multi-GPU training (
https://click.convertkit-mail2.com/r8ul7ldqe2foh35z37nf2hdwlk666s7hm4o66/25h2hoh3er5v4of3/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1iZWdpbm5lci1mcmllbmRseS1ndWlkZS10by1tdWx0aS1ncHUtbW9kZWwtdHJhaW5pbmcv
)​
-----------------------------------------------------------------

By default, deep learning models only utilize a single GPU for
training, even if multiple GPUs are available.

An ideal way to train models is to distribute the training
workload across multiple GPUs.

The graphic below depicts four common strategies for multi-GPU
training:

​
We covered multi-GPU 

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

---
title: The Anatomy of Diffusion LLMs
source: https://mail.google.com/mail/u/0/#inbox/19d838888f466ecf
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-12
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 The Anatomy of Diffusion LLMs 的原理剖析与工程实践。
tags:
  - clippings
---

# The Anatomy of Diffusion LLMs

## 1. 核心要点解析

本期内容重点涵盖：
- **The Anatomy of Diffusion LLMs**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* The anatomy of diffusion LLMs.
* ​Evaluate MCP-powered LLM apps.
* 20 most common magic methods in Python OOP.

TODAY'S ISSUE

Deep dive
---------

-----------------------------------------------------------------
​The anatomy of diffusion LLMs (

)​
-----------------------------------------------------------------

This week’s deep dive covers one of the most important
architectural shifts happening in language modeling right now:
diffusion LLMs.

​Read the full Part 1 deep dive here → (

)​

-->​Diffusion LLMs Part 1 (

)
​Diffusion LLMs Part 1 (
https://www.dailydoseofds.com/diffusion-models-part-1/ )
​
It builds a complete understanding from first principles:

* how autoregressive generation is structurally memory-bandwidth
bound)
* why Gaussian noise can’t work on discrete tokens
* how masked diffusion solves this with an ELBO-derived training
objective
* the math behind the forward and reverse processes
* unmasking strategies
* block diffusion for KV cache compatibility
* and a detailed engineering comparison between the two
paradigms.

​Read the full Part 1 deep dive here → (

)​

*********
Why care?
*********

Every production LLM today, GPT-4, Claude, Gemini, LLaMA,
generates text the same way: one token at a time, left to right.

​
Each token requires loading the full model weights through GPU
memory, performing a tiny computation, and then loading all the
weights again for the next token. On an A100, this means roughly
1 FLOP per byte of data moved, while the GPU is designed for 100+
FLOPs per byte.

​
​Diffusion LLMs (

) take a completely different approach. They start with a fully
masked sequence and iteratively unmask all tokens in parallel,
using bidirectional attention at every step. This shifts
inference from memory-bandwidth bound to compute-bound, which is
exactly where modern GPUs are efficient.

The results are catching up fast. Block diffusion (BD3-LM) is
within 0.5 perplexity points of autoregressive on LM1B. LLaDA at
8B parameters matches LLaMA 3 on MMLU and exceeds it on
TruthfulQA and HumanEval. And models like Dream 7B are already
being served in production with SGLang.

Understanding how it works at a mathematical level, from the
forward masking process to the ELBO objective to block-level KV
caching, is going to be increasingly valuable as these models
scale.

​You can read the Part 1 here → (

)​

👉 Over to you: Do you think the future of LLM generation is pure
diffusion, pure autoregressive, or some hybrid of the two?

MCP
---

-----------------------------------------------------------------
​Evaluate MCP-powered LLM apps (

)​
-----------------------------------------------------------------

There are primarily 2 factors that determine how well an MCP app
works:

* If the model is selecting the right tool?
* And if it's correctly preparing the tool call?

Today, let's learn how to evaluate any MCP workflow using
DeepEval’s latest MCP evaluations (open-source).

​This issue was written while referring to the DeepEval docs → (

)​

Here's the workflow:

​
* Integrate the MCP server with the LLM app.
* Send queries and log tool calls, tool outputs in DeepEval.
* Once done, run the eval to get insights on the MCP
interactions.

Now let's dive into the code for this!

1️⃣ Setup
---------

First, we install DeepEval to run MCP evals.

​
It's 100% open-source with 11k+ stars and implements everything
you need to define metrics, create test cases, and run evals
like:

* component-level evals
* multi-turn evals
* LLM Arena-as-a-judge, etc.

2️⃣ Create an MCP server
------------------------

Next, we define our own MCP server with two tools that the LLM
app can interact with.

​
Notice that in our implementation, we intentionally avoid
specifying any descriptive docstrings to make things tricky for
the LLM.

3️⃣ Connect to MCP server
-------------------------

Moving on, we set up the client session that connects to the MCP
server and manages tool interactions.

​
This is the layer that sits between the LLM and the MCP server.

4️⃣ Track MCP interactions
--------------------------

Next, we define a method that accepts a user query and passes
that to Claude Opus (along with the MCP tools) to generate a
response.

​
We filter the tool calls from the response to create an object of
MCPToolCall class from DeepEval.

5️⃣ Create a test case
----------------------

At this stage, we know:

* the input query
* all the MCP tools
* all the tools invoked
* and the final LLM response

Thus, after execution, we create an LLMTestCase using this info.

​

6️⃣ Define metric
-----------------

We define an MCPUseMetric from DeepEval, which computes two
things:

​
* How well did the LLM utilize the MCP capabilities given to it?
* How well did the LLM ensure argument correctness for tool call?

The minimum of both scores is the final score.

7️⃣ Run the evaluation
----------------------

Finally, we invoke DeepEval’s evaluate() method to score the test
case against the metric.

​
This outputs a score between 0-1 with a 0.5 threshold default.

We run multiple queries for evaluation.

The DeepEval dashboard displays the full trace, like:

​
* query
* response
* failure/success reason
* tools invoked and params, etc.

As expected, the app failed on most queries, and our MCPUseMetric
spotted that correctly.

This evaluation helped us improve this app by defining better
docstrings, and the app, which initially passed only 1 or 2 out
of 24 test cases, now achieves a 100% success rate:

​
​This issue was written while referring to the DeepEval docs → (

)​

​Find more details in DeepEval’s GitHub repo → (

)​

Python
------

--------------------

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

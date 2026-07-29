---
title: Train Classical ML Models on Large Datasets
source: https://mail.google.com/mail/u/0/#inbox/19dfa25648e2f2cb
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-05
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Train Classical ML Models on Large Datasets 的原理剖析与工程实践。
tags:
  - clippings
---

# Train Classical ML Models on Large Datasets

## 1. 核心要点解析

本期内容重点涵盖：
- **Train Classical ML Models on Large Datasets**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* An open-source alternative to Anthropic’s most viral feature!
* ​Train classical ML models on large datasets​.
* How does BM25 ranking algorithm work?

TODAY'S ISSUE

open-source
-----------

-----------------------------------------------------------------
​An open-source alternative to Anthropic’s most viral feature! (

)​
-----------------------------------------------------------------

Until now, Anthropic’s Generative UI capabilities only existed
inside its own products.

Open Generative UI by CopilotKit is an open-source implementation
of that same pattern that works in any app.

The agent generates HTML/SVG at runtime, and CopilotKit streams
it token-by-token into a sandboxed iframe inside the app’s chat.

So the user can watch the UI assemble itself in real time, not
after the full response is ready.

​
The sandbox is fully isolated with no access to the parent app,
the DOM, or user data. So if the agent hallucinates broken markup
or unexpected JavaScript, nothing leaks outside the iframe.

Under the hood, the agent does not select from pre-built
components. Instead, it generates arbitrary visuals from scratch
every time.

The output is unconstrained by default, but you can shape it by
defining prompt-based skills that teach the agent specific visual
formats or guidelines.

For instance, a skill prompt can guide the agent toward producing
a Chart.js dashboard with proper axis labels and responsive
sizing, or an interactive 3D model with rotation controls.

​
The graphic below depicts this, and the output quality you see
actually comes from the skills layer.

​
Open Generative UI runs on AG-UI, so it works out of the box with
LangGraph, CrewAI, Mastra, Google ADK, AWS Strands, and more.

It also ships with a standalone MCP server that plugs into Claude
Code, Cursor, or any MCP-compatible client.

And the entire stack is built on top of CopilotKit, the
open-source frontend framework for agents and generative UI. 30k+
GitHub stars, with SDKs for React, Next.js, Angular, and Vue.

​Here’s a live demo gallery if you want to test this yourself → (

)​

​CopilotKit GitHub repo (30k+ stars) → (

)​

machine learning
----------------

-----------------------------------------------------------------
​Train classical ML models on large datasets (

)​
-----------------------------------------------------------------

The list of sklearn implementations that support a batch API is
quite small:

​
This is concerning since, in the enterprise space, the data is
primarily tabular.

Classical ML algorithms, such as tree-based ensemble methods, are
frequently used for modeling.

However, typical implementations of these models are not
“big-data-friendly” because they require the entire dataset to be
in memory.

There are two ways to approach this:

* The first way is to use big-data frameworks like Spark MLlib to
train them.​​​​We covered this in detail →​ (

)​
* There’s one more way: Random Patches. Let’s learn below.

Random Patches
--------------

Note: This approach will only work in an ensemble setting. So,
you would have to train multiple models.

The idea is to sample random data patches (rows and columns) and
train a tree model on each patch.

(

)​
Repeat this step multiple times by randomly generating different
data patches to obtain the entire random forest model.

These are the results mentioned in the thesis (check pages 174
and 178) on 13 datasets:

From left to right → Cifar10, mnist3v8, mnist4v9, mnist, isolet,
arcene, breast2, madelon, marti, reged, second, this, and sido.
* In most cases, the random patches approach performs better than
the traditional random forest.
* In other cases, there is a marginal difference in performance.

And this is how we can train a random forest model on large
datasets that do not fit into memory.

Why does it work?
-----------------

The idea is similar to what we discussed when we covered Bagging,
which eventually allowed us to build our own variant of the
Bagging algorithm: ​​​​Why Bagging is so ridiculously effective
at variance reduction?​​​​ (

)​

In a gist, building trees that are as different as possible
guarantees a greater reduction in variance.

In this case, the dataset overlap between two trees will be less
than that in a typical random forest. This aids in the Bagging
objective and leads to a more robust model.

To understand this mathematically, read this: ​​​​Why Bagging is
so ridiculously effective at variance reduction? (

)​

algorithms
----------

-----------------------------------------------------------------
​How does BM25 ranking algorithm work? (

)​
-----------------------------------------------------------------

A 30-year-old algorithm with zero training, zero embeddings, and
zero fine-tuning still powers Elasticsearch, OpenSearch, and most
production search systems today.

It’s called BM25.

Let’s understand what makes it so powerful:

​
Imagine you’re searching for “transformer attention mechanism” in
a library of ML papers.

BM25 asks three simple questions:

“How rare is this word?”

Every paper contains “the” and “is”, which makes it useless. But
“transformer” is specific and informative. BM25 boosts rare words
and ignores the noise.

→ This is IDF(qᵢ) in the formula

“How many times does it appear?”

If “attention” appears 10 times in a paper, that’s a good sign.
But 10 vs 100 occurrences won’t make much difference. BM25
applies diminishing returns.

→ This is f(qᵢ, D) combined with k₁ that controls saturation

“Is this document unusually long?”

A 50-page paper will naturally contain more keywords than a
5-page paper. BM25 levels the playing field so longer documents
don’t cheat their way to the top.

→

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

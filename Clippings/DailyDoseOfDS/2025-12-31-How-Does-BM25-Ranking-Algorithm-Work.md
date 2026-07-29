---
title: How Does BM25 Ranking Algorithm Work?
source: https://mail.google.com/mail/u/0/#inbox/19b71b8454693ea2
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-31
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 How Does BM25 Ranking Algorithm Work? 的原理剖析与工程实践。
tags:
  - clippings
---

# How Does BM25 Ranking Algorithm Work?

## 1. 核心要点解析

本期内容重点涵盖：
- **How Does BM25 Ranking Algorithm Work?**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnwp3mpc6h8k52600bgh32dww/25h2hoh3nd202la3/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* A production-grade browser automation framework for Agents
(open-source)!
* How Does BM25 Ranking Algorithm Work?
* ​6 graph feature engineering techniques​.

TODAY'S ISSUE

Open-source
-----------

-----------------------------------------------------------------
​A production-grade browser automation framework for Agents! (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnwp3mpc6h8k52600bgh32dww/qvh8h7hdqnr2rzil/aHR0cHM6Ly9naXRodWIuY29tL2Jyb3dzZXJiYXNlL3N0YWdlaGFuZA==
)​
-----------------------------------------------------------------

Typical browser automation tools like Selenium, Playwright, or
Puppeteer require you to hard-code your automations.

This makes them brittle since one change in the website can
disrupt the entire automation.

On the other hand, high-level Agents like OpenAI Operator can be
unpredictable in production.

​Stagehand (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnwp3mpc6h8k52600bgh32dww/qvh8h7hdqnr2rzil/aHR0cHM6Ly9naXRodWIuY29tL2Jyb3dzZXJiYXNlL3N0YWdlaGFuZA==
) is an open-source framework that bridges the gap between:

-->​Stagehand GitHub repo (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnwp3mpc6h8k52600bgh32dww/qvh8h7hdqnr2rzil/aHR0cHM6Ly9naXRodWIuY29tL2Jyb3dzZXJiYXNlL3N0YWdlaGFuZA==
)
​Stagehand GitHub repo ( https://github.com/browserbase/stagehand
)
​
* brittle traditional automation like Playwright, Selenium, etc.,
and
* unpredictable full-agent solutions like OpenAI Operator.

Key features:

* Use AI when you want to navigate unfamiliar pages, and use code
(Playwright) when you know exactly what you want to do.
* Preview AI actions before running them, and cache repeatable
actions to save tokens.
* Compatible with SOTA computer use models with just one line of
code.
* Available in both Python and Typescript SDK.

Stagehand also has an open-source MCP server.

​You can find the GitHub repo here → (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnwp3mpc6h8k52600bgh32dww/qvh8h7hdqnr2rzil/aHR0cHM6Ly9naXRodWIuY29tL2Jyb3dzZXJiYXNlL3N0YWdlaGFuZA==
)​

-->​Stagehand GitHub repo (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnwp3mpc6h8k52600bgh32dww/qvh8h7hdqnr2rzil/aHR0cHM6Ly9naXRodWIuY29tL2Jyb3dzZXJiYXNlL3N0YWdlaGFuZA==
)
​Stagehand GitHub repo ( https://github.com/browserbase/stagehand
)

algorithms
----------

-------------------------------------
How Does BM25 Ranking Algorithm Work?
-------------------------------------

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

→ This is |D|/avgdl controlled by parameter b

Overall, BM25 is based around three questions, with no
requirement for neural networks (refer to the image below again):

​
BM25 excels at exact keyword matching, which is something
embeddings often struggle with. It also shines when your corpus
has domain-specific terminology that embedding models probably
weren’t trained on.

If your user searches for “error code 5012,” embeddings might
return semantically similar results. BM25 will find the exact
match.

This is why hybrid search exists.

Top RAG systems today combine BM25 with vector search. You get
the best of both worlds: semantic understanding AND precise
keyword matching.

Also, the entire hybrid search stack you mentioned is actually
implemented in Airweave (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnwp3mpc6h8k52600bgh32dww/g3hnh5hmxp3o39ir/aHR0cHM6Ly9naXRodWIuY29tL2FpcndlYXZlLWFpL2FpcndlYXZl
) that we use as a context layer for Agents:

-->​Airweave GitHub repo (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnwp3mpc6h8k52600bgh32dww/g3hnh5hmxp3o39ir/aHR0cHM6Ly9naXRodWIuY29tL2FpcndlYXZlLWFpL2FpcndlYXZl
)
​Airweave GitHub repo ( https://github.com/airweave-ai/airweave )
​
So before you throw GPUs at every search problem, consider BM25.
It might already solve your problem, or make your semantic search
even better when combined.

👉 Over to you: What topics would you like to learn next?

Thanks for reading!

Graph ML
--------

-----------------------------------------------------------------
​6 graph feature engineering techniques (
https://fff97757.click.convertkit-mail2.com/lmu9m96v3wcmhnwp3mpc6h8k52600bgh32dww/9qhzhnhdn9p3prt9/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tZ3JhcGgtbmV1cmFsLW5ldHdvcmtzLWltcGxlbWVudGF0aW9uLWluY2x1ZGVkLw==
)​
-----------------------------------------------------------------

Like images, text, and tabular datasets have features, so do
graph datasets.

This means when building models on graph datasets, we can
engineer these features to achieve better performance.

Today, let us lea

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

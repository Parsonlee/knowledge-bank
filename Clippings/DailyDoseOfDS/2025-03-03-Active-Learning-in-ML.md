---
title: Active Learning in ML
source: https://mail.google.com/mail/u/0/#inbox/1955d7c8c16ec8c4
author:
  - "[[DailyDoseOfDS]]"
published: 2025-03-03
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Active Learning in ML 的原理剖析与工程实践。
tags:
  - clippings
---

# Active Learning in ML

## 1. 核心要点解析

本期内容重点涵盖：
- **Active Learning in ML**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/qdu393wq7es7h44wno7blh8304kkkc4/7qh7h8h9vwnkmqcz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Make your RAG application 10x smarter with ColiVara.
* Active Learning in ML.

Reading time: 3 minutes.

TODAY'S ISSUE

TOGETHER WITH COLIVARA
----------------------

-----------------------------------------------------------------
​Make your RAG application 10x smarter! (
https://click.convertkit-mail2.com/qdu393wq7es7h44wno7blh8304kkkc4/owhkhqhw3gqk79cv/aHR0cHM6Ly9naXRodWIuY29tL3RqbWxhYnMvQ29saVZhcmE=
)​
-----------------------------------------------------------------

​ColiVara (
https://click.convertkit-mail2.com/qdu393wq7es7h44wno7blh8304kkkc4/owhkhqhw3gqk79cv/aHR0cHM6Ly9naXRodWIuY29tL3RqbWxhYnMvQ29saVZhcmE=
) is a unique document retrieval method that does not need
chunking or text processing.

It still feels like RAG but without OCR, text extraction, broken
tables, or missing images.

-->ColiVara GitHub (
https://click.convertkit-mail2.com/qdu393wq7es7h44wno7blh8304kkkc4/owhkhqhw3gqk79cv/aHR0cHM6Ly9naXRodWIuY29tL3RqbWxhYnMvQ29saVZhcmE=
)
ColiVara GitHub ( https://github.com/tjmlabs/ColiVara )
​
Here’s why it’s powerful:

* Vision-based indexing
* 100+ file format support
* Seamless local or cloud quickstart
* State-of-the-art multimodal retrieval
* APIs & SDKs for both Python/TypeScript
* Late-interaction embeddings for extra accuracy
* No vector DB management (pgVector under the hood)

​

Check out the GitHub repo here: ColiVara GitHub (
https://click.convertkit-mail2.com/qdu393wq7es7h44wno7blh8304kkkc4/owhkhqhw3gqk79cv/aHR0cHM6Ly9naXRodWIuY29tL3RqbWxhYnMvQ29saVZhcmE=
).

Today's daily dose of data science
----------------------------------

---------------------
Active Learning in ML
---------------------

Data annotation is difficult, expensive, and time-consuming.

Active learning is a relatively easy and inexpensive way to build
supervised models when you don’t have annotated data to begin
with.

As the name suggests, the idea is to build the model with active
human feedback on examples it is struggling with.

The visual below summarizes this:

​
We begin by manually labeling a tiny percentage of the dataset:

​
I have used active learning (successfully) while labeling as low
as ~1% of the dataset, so try something in that range.
Next, build a model on this small labeled dataset. This won’t be
a good model, but that’s fine:

​
Next, generate predictions on the dataset we did not label:

​
Since the dataset is unlabeled, we cannot determine if these
predictions are correct.

That’s why we train a model that can implicitly or explicitly
provide a confidence level with its predictions.

​
Probabilistic models are a good fit since one can determine a
proxy for confidence level from probabilistic outputs.

This is shown below:

​
In the above two examples, consider the gap between 1st and 2nd
highest probabilities:

* In example #1, the gap is large. This can indicate that the
model is confident in its prediction.
* In example #2, the gap is small. This can indicate that the
model is NOT confident in its prediction.

After generating the confidence, rank all predictions in order of
confidence:

​
Provide human label to the low-confidence predictions and feed it
back to the model with the seed dataset:

​
There’s no point labeling predictions the model is already
confident with. This diagram should help you understand this
point:

​
Repeat the process a few times (train → generate predictions and
confidence → label low confidence prediction) and stop when you
are satisfied with the performance.

Active learning is a huge time-saver in building supervised
models on unlabeled datasets.

The only thing that you have to be careful about is generating
confidence measures.

If you mess this up, it will affect every subsequent training
step.

Also, while combining the low-confidence data with the seed data,
we can use the high-confidence data. The labels would be the
model’s predictions.

​
This variant of active learning is called cooperative learning.

👉 Over to you: Do you like cooperative learning or active
learning?

THAT'S A WRAP

NO-FLUFF DS/ML RESOURCES TO...
------------------------------

-----------------------------------------------------------------
​Succeed in DS/ML roles (
https://click.convertkit-mail2.com/qdu393wq7es7h44wno7blh8304kkkc4/z2hghnhe9pl48xtp/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcA==
)​
-----------------------------------------------------------------

​
All businesses care about impact. That’s it!

* Can you reduce costs?
* Drive revenue?
* Can you scale ML models?
* Predict trends before they happen?

We have discussed several other topics (with implementations) in
the past that align with such topics.

-->Develop Industry ML skills (
https://click.convertkit-mail2.com/qdu393wq7es7h44wno7blh8304kkkc4/z2hghnhe9pl48xtp/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcA==
)
Develop Industry ML skills (
https://www.dailydoseofds.com/membership )Here are some of them:

* Learn how to build Agentic systems in this ongoing crash course
(
https://click.convertkit-mail2.com/qdu393wq7es7h44wno7blh8304kkkc4/p8heh9h4kgq3l0iq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYWktYWdlbnRzLWNyYXNoLWNvdXJzZS1wYXJ0LTEtd2l0aC1pbXBsZW1lbnRhdGlvbi8=
).
* Learn how to build real-world RAG apps, evaluate, and scale
them in this crash course (
https://click.convertkit-mail2.com/qdu393wq7es7h44wno7blh8304kkkc4/x0hph6he89qrlvs5/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYS1jcmFzaC1jb3Vyc2Utb24tYnVpbGRpbmctcmFnLXN5c3RlbXMtcGFydC0xLXdpdGgtaW1wbGVtZW50YXRpb25zLw==
).
* Learn sophisticated graph architectures and how to train them
on graph data in this crash course (
h

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

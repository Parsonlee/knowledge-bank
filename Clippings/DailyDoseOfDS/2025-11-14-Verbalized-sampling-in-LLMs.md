---
title: Verbalized sampling in LLMs.
source: https://mail.google.com/mail/u/0/#inbox/19a841a055b8cd28
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-14
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Verbalized sampling in LLMs. 的原理剖析与工程实践。
tags:
  - clippings
---

# Verbalized sampling in LLMs.

## 1. 核心要点解析

本期内容重点涵盖：
- **Verbalized sampling in LLMs.**

## 2. 深度拆解与正文翻译

​Master full-stack AI Engineering (
https://click.convertkit-mail2.com/zluvnvdrxlunhkwe86daphwogmg00a6h93200/7qh7h8h9w26odxfz/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Native Video RAG in just 5 lines of code!
* Verbalized sampling in LLMs.
* [Interview question] Transformer vs. Mixture of Experts in LLMs

TODAY'S ISSUE

Multimodal rag
--------------

-----------------------------------------------------------------
​Native RAG over Video in just 5 lines of code! (
https://click.convertkit-mail2.com/zluvnvdrxlunhkwe86daphwogmg00a6h93200/owhkhqhwgm6rxeiv/aHR0cHM6Ly93d3cucmFnaWUuYWkvbXVsdGltb2RhbA==
)​
-----------------------------------------------------------------

Most RAG systems stop at text.

But a lot of valuable context lives in spoken words and visuals
like calls, interviews, demos, lectures, and it’s tough to build
production-grade RAG solutions on them.

Here’s how you can do RAG over videos in just 5 lines of code
with Ragie (
https://click.convertkit-mail2.com/zluvnvdrxlunhkwe86daphwogmg00a6h93200/owhkhqhwgm6rxeiv/aHR0cHM6Ly93d3cucmFnaWUuYWkvbXVsdGltb2RhbA==
):

-->Build RAG over videos (
https://click.convertkit-mail2.com/zluvnvdrxlunhkwe86daphwogmg00a6h93200/owhkhqhwgm6rxeiv/aHR0cHM6Ly93d3cucmFnaWUuYWkvbXVsdGltb2RhbA==
)
Build RAG over videos ( https://www.ragie.ai/multimodal )
​
* Ingest .mp4, .wav, .mkv, or 10+ formats.
* Run a natural language query like “Moments when Messi scored a
goal?”
* Get the exact timestamp + streamable clip that answers it.

Here’s one of our runs where we gave it a goal compilation video,
and it retrieved the correct response:

​
* Top image: ARG vs CRO. It determined there’s a penalty and
retrieved the score before and after the penalty.
* Bottom image: ARG vs MEX: It fetched the score before the goal,
and how the goal was scored accurately.

​Start building RAG over audio and video here → (
https://click.convertkit-mail2.com/zluvnvdrxlunhkwe86daphwogmg00a6h93200/owhkhqhwgm6rxeiv/aHR0cHM6Ly93d3cucmFnaWUuYWkvbXVsdGltb2RhbA==
)​

-->Build RAG over videos (
https://click.convertkit-mail2.com/zluvnvdrxlunhkwe86daphwogmg00a6h93200/owhkhqhwgm6rxeiv/aHR0cHM6Ly93d3cucmFnaWUuYWkvbXVsdGltb2RhbA==
)
Build RAG over videos ( https://www.ragie.ai/multimodal )

LLms
----

-----------------------------------------------------------------
​Verbalized sampling in LLMs (
https://click.convertkit-mail2.com/zluvnvdrxlunhkwe86daphwogmg00a6h93200/z2hghnhep2k35ghp/aHR0cHM6Ly9hcnhpdi5vcmcvYWJzLzI1MTAuMDExNzE=
)​
-----------------------------------------------------------------

Post-training alignment methods, such as RLHF, are designed to
make LLMs helpful and safe.

​
However, these methods unintentionally cause a significant drop
in output diversity (called mode collapse).

When an LLM collapses to a mode, it starts favoring a narrow set
of predictable or stereotypical responses over other outputs.

According to a paper, mode collapse happens because the human
preference data used to train the LLM has a hidden flaw called
typicality bias.

​
Here’s what happens.

* Annotators are asked to rate different responses from an LLM,
and later, the LLM is trained using a reward model that learns to
mimic these human preferences.
* However, it is observed that annotators naturally tend to favor
answers that are more familiar, easy to read, and predictable.
This is the typicality bias. So even if a new, creative answer is
just as good (or correct) as a common one, the human’s preference
often leans toward the common one.
* Due to this, the reward model boosts responses that the
original (pre-aligned) model already considered likely.
* This aggressively sharpens the LLM’s probability distribution,
collapsing the model’s creative output to one or two dominant,
highly predictable responses.

That said, this is not an irreversible effect, and the LLM still
has two personalities after alignment:

* The original model that learned the rich possibilities during
pre-training.
* The safety-focused, post-aligned model [to mention again, due
to typicality bias, it had been unintentionally suppressed to
strongly favor the most predictable response]

Verbalized sampling (VS) solves this.

It is a training-free prompting strategy introduced to circumvent
mode collapse and recover the diverse distribution learned during
pre-training.

​
The core idea of verbalized sampling is that the prompt itself
acts like a mental switch.

When you directly prompt “Tell me a joke”, the aligned
personality immediately takes over and outputs the most
reinforced answer.

But in verbalized sampling, you prompt it with “Generate 5
responses with their corresponding probabilities. Tell me a
joke.”

In this case, the prompt does not request an instance, but a
distribution.

This causes the aligned model to talk about its full knowledge
and is forced to utilize the diverse distribution it learned
during pre-training.

So essentially, by asking the LLM to verbalize the probability
distribution, the model is able to tap into the broader, diverse
set of ideas, which comes from the rich distribution that still
exists inside its core pre-trained weights.

Experiments across various tasks demonstrate significant
benefits:

​
* Verbalized sampling significantly enhances diversity by
1.6–2.1x over direct prompting, while maintaining or improving
quality. Variants like verbalized sampling-based CoT
(Chain-of-Thought) and verbalized sampling-based Multi improve
generation diversity even further.
* Larger, more capable models like GPT-4.1 and Gemini-2.5-Pro
benefit more from Verbalizeb sampling, showing diversity gains up
to 2 times greater than smaller models.
* Verbalized sampling better retains diversity across
post-training stages (SFT, DPO, RLVR), recovering about 66.8% of
th

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

---
title: 72 Techniques to Optimize LLMs in Production
source: https://mail.google.com/mail/u/0/#inbox/19d9d1a7d44f86a9
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-17
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 72 Techniques to Optimize LLMs in Production 的原理剖析与工程实践。
tags:
  - clippings
---

# 72 Techniques to Optimize LLMs in Production

## 1. 核心要点解析

本期内容重点涵盖：
- **72 Techniques to Optimize LLMs in Production**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* Cut retrieval token count by 3X and get better RAG accuracy
too.
* 72 techniques to optimize LLMs in production.

TODAY'S ISSUE

RAG
---

-----------------------------------------------------------------
​Cut retrieval token count by 3X and get better RAG accuracy too
(

)​
-----------------------------------------------------------------

Most RAG cost optimization happens at the model layer, like
smaller models, fewer calls, and batching.

The retrieval payload itself rarely gets measured.

​
A typical setup retrieves 5 chunks per query, each around 300
tokens. That’s 1,500 input tokens before the LLM writes a single
word, and at scale, that compounds.

But the bigger problem is accuracy. Enterprise documents repeat
the same facts across multiple file versions.

When retrieved chunks say slightly different versions of the same
thing, the LLM blends them. The answer sounds confident and is
wrong in ways that are hard to catch.

Blockify (GitHub repo (

)) sits between your raw docs and vector store.

​
Instead of splitting text into raw chunks, it uses a fine-tuned
LLM to generate small, structured knowledge units called
IdeaBlocks, where each one is built around one question and one
validated answer. Average size: 98 tokens.

It runs on Intel Xeon CPUs, so no GPU server is needed to get
started.

On a published benchmark, the IdeaBlock index outperformed raw
chunked indexing by 13.55% on vector accuracy, using the same
source documents and embedding model.

The token count dropped 3.09X as a direct result of the smaller
unit size.

The cost drops because the quality improved, not separately from
it.

​You can find the Blockify GitHub repo here → (

)​

LLms
----

-----------------------------------------------------------------
​72 techniques to optimize LLMs in production (

)​
-----------------------------------------------------------------

On an H100 running Llama 70B, a single inference request hits 92%
GPU compute utilization during prefill, then drops to 28% during
decode on the same hardware a moment later. The workload changed,
not the GPU.

For context:

* Prefill processes the entire prompt in parallel and saturates
tensor cores.
* Decode generates one token at a time and reads the full KV
cache from HBM at every step, which makes it memory-bandwidth
bound.

This asymmetry is why a single optimization never gets you very
far, and why LLM inference prices have still fallen roughly 10x
per year, with GPT-4-level performance going from $20 per million
tokens in late 2022 to around $0.40 today.

Most of that drop came from the serving stack, and we put
together this visual, which lists the techniques that go into
optimizing LLMs in production (

).

​
Every technique in the grid above is a response to one of three
bottlenecks: prefill compute, decode memory bandwidth, or the
cost of everything that wraps the model.

Stacking enough of these techniques closes the 5-8x
cost-efficiency gap between optimized vLLM or TensorRT-LLM
deployments and naive FP16 inference.

Today, let’s walk through the nine layers, what each one actually
solves, and how they stack up in a real production deployment.

We covered a lot more in the LLMOps course (

) with implementations and engineering logic.
​You can start reading it here → (

)​

​1. Model compression (

)​
-----------------------------------------------------------------

​
Model weights live in GPU memory all the time.

A 70B model in FP16 is 140GB before you load a single token of
context. Compression attacks this usage directly.

* INT8 halves the memory vs FP16.
* INT4 cuts it 4x.
* FP8 gives you native tensor core support on Hopper and
Blackwell, which means compression plus speedup.

GPTQ, AWQ, and SmoothQuant are the three main algorithms here.

* GPTQ uses Hessian-based second-order information
* AWQ preserves salient weights based on activation magnitudes,
* SmoothQuant handles both weights and activations at W8A8.

Distillation and pruning attack the parameter count itself rather
than the bits per parameter.

Multi-LoRA serving is the escape hatch for multi-tenant
deployments, where you keep one base model in memory and hot-swap
small adapter weights per request.

We covered this specific pillar in

* ​Part 9 of MLOps course → (

)​
* ​Part 10 of MLOps course → (

)​
* ​Part 12 of LLOps course → (

)​

2. Attention and architecture
-----------------------------

​
Standard attention is O(N²). At 128K context, this will have 16
billion computations, which is why naive attention is infeasible
at long context even on H100-class hardware.

FlashAttention reorders the attention math to be IO-aware,
avoiding materializing the full N×N matrix.

​PagedAttention (

) applies OS-style virtual memory to the KV cache, eliminating
fragmentation.

MQA, GQA, and MLA attack the number of KV heads.

MQA shares one KV head across all queries, GQA groups them, MLA
compresses keys and values into a low-rank latent. DeepSeek-V2
reported a 93.3% KV cache reduction from MLA alone.

Sliding window attention restricts each token to a local window.
MoE activates only a subset of experts per token. These are
architectural choices driven entirely by serving economics.

We covered this specific pillar in:

* ​Part 3 of LLMOps course → (

)​
* ​Part 13 of LLMOps course → (

)​

3. Decoding
-----------

​
Decode is memory-bound because every new token requires a full
pass over the weights and KV cache.

* ​Speculative decoding (

) sidesteps this by generating a draft with a cheap model, then
verifying in parallel with the main model.
* Medusa attaches extra prediction heads to the model itself, so
the same model can draft its own candidate t

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

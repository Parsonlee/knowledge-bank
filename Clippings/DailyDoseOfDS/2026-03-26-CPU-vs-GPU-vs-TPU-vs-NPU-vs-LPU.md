---
title: CPU vs GPU vs TPU vs NPU vs LPU
source: https://mail.google.com/mail/u/0/#inbox/19d2bbc9492d99c6
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-26
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 CPU vs GPU vs TPU vs NPU vs LPU 的原理剖析与工程实践。
tags:
  - clippings
---

# CPU vs GPU vs TPU vs NPU vs LPU

## 1. 核心要点解析

本期内容重点涵盖：
- **CPU vs GPU vs TPU vs NPU vs LPU**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* The missing layer between AI agents and infrastructure.
* ​CPU vs GPU vs TPU vs NPU vs LPU​.
* Breathing KMeans vs KMeans.

TODAY'S ISSUE

open-source
-----------

-----------------------------------------------------------------
​The missing layer between AI agents and infrastructure (

)​
-----------------------------------------------------------------

Most identity models were built for humans and static automation.

AI agents break those assumptions because they act continuously,
make decisions independently, and access infrastructure at
machine speed.

As a result, it becomes nearly impossible to control access,
trace behavior, or know which agent is responsible for what.

​
​Teleport’s Agentic Identity Framework (

) is an open-source, standards-driven architecture for deploying
AI agents securely across infrastructure.

It gives every agent its own cryptographic identity, enforces
access at runtime instead of relying on static privileges,
discovers shadow agents and unmanaged MCP servers automatically,
and maintains full attribution as systems operate autonomously.

The framework also provides controls for LLM usage, including
rate limiting, budgets, and guardrails.

​Get started here to securely deploy Agents in production → (

)​

Thanks to Teleport for partnering today!

AI compute architectures
------------------------

-----------------------------------------------------------------
​CPU vs GPU vs TPU vs NPU vs LPU (

)​
-----------------------------------------------------------------

5 hardware architectures power AI today.

Each one makes a fundamentally different tradeoff between
flexibility, parallelism, and memory access.

The visual below maps the internal architecture of all five side
by side:

​

CPU
---

It is built for general-purpose computing. A few powerful cores
handle complex logic, branching, and system-level tasks.

​
It has deep cache hierarchies and off-chip main memory (DRAM).
It’s great for operating systems, databases, and decision-heavy
code, but not that great for repetitive math like matrix
multiplications.

GPU
---

Instead of a few powerful cores, GPUs spread work across
thousands of smaller cores that all execute the same instruction
on different data.

​
This is why GPUs dominate AI training. The parallelism maps
directly to the kind of math neural networks need.

TPU
---

They go one step further with specialization.

The core compute unit is a grid of multiply-accumulate (MAC)
units where data flows through in a wave pattern.

​
Weights enter from one side, activations from the other, and
partial results propagate without going back to memory each time.

The entire execution is compiler-controlled, not
hardware-scheduled. Google designed TPUs specifically for neural
network workloads.

NPU
---

This is an edge-optimized variant.

The architecture is built around a Neural Compute Engine packed
with MAC arrays and on-chip SRAM, but instead of high-bandwidth
memory (HBM), NPUs use low-power system memory.

​
The design goal is to run inference at single-digit watt power
budgets, like smartphones, wearables, and IoT devices.

Apple Neural Engine and Intel’s NPU follow this pattern.

LPU (Language Processing Unit)
------------------------------

This is the newest entrant, by Groq.

The architecture removes off-chip memory from the critical path
entirely. All weight storage lives in on-chip SRAM.

​
Execution is fully deterministic and compiler-scheduled, which
means zero cache misses and zero runtime scheduling overhead.

The tradeoff is that it provides limited memory per chip, which
means you need hundreds of chips linked together to serve a
single large model. But the latency advantage is real.

AI compute has evolved from general-purpose flexibility (CPU) to
extreme specialization (LPU). Each step trades some level of
generality for efficiency.

The visual below maps the internal architecture of all five side
by side, and it was inspired by ByteByteGo’s post on CPU vs GPU
vs TPU. We expanded it to include two more architectures that are
becoming central to AI inference today.

​
That said, if you want to get hands-on with actual GPU
programming using CUDA, learn about how CUDA operates GPU’s
threads, blocks, grids (with visuals), etc., we covered it here:
​ (

)​Implementing (Massively) Parallelized CUDA Programs From
Scratch Using CUDA Programming (

).

👉 Over to you: Which of these 5 have you actually worked with or
deployed on?

machine learning
----------------

--------------------------
Breathing KMeans vs KMeans
--------------------------

Since KMeans’ performance heavily depends on the centroid
initialization step, it is always advised to run the algorithm
multiple times with different initializations.

​
But this repetition introduces an unnecessary run-time overhead.

The Breathing KMeans algorithm solves this issue while providing
better clustering results than KMeans.

​
There is also an open-source implementation of Breathing KMeans
with a sklearn-like API.

To get started, install the bkmeans library and run the algorithm
as follows:

​
Done!

If you are curious, we have covered how Breathing KMeans works in
the next section.

On a side note, data conformity is another big issue with KMeans,
which makes it highly inapplicable in many data situations.
​
These three detailed guides cover distribution-based and
density-based clustering, which address KMeans’ limitations in
specific data situations:
​

- Gaussian Mixture Models (GMMs) [derived and implemented from
scratch using NumPy] (

).
​

- DBSCAN++: The Faster and Scalable Alternative to DBSCAN
Clustering [with implementation] (

).
​

- HDBSCAN: An Al

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

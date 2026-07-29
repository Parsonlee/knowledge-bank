---
title: 4 Parallel Processing Techniques in Python
source: https://mail.google.com/mail/u/0/#inbox/19c2a80854fc31f8
author:
  - "[[DailyDoseOfDS]]"
published: 2026-02-04
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 4 Parallel Processing Techniques in Python 的原理剖析与工程实践。
tags:
  - clippings
---

# 4 Parallel Processing Techniques in Python

## 1. 核心要点解析

本期内容重点涵盖：
- **4 Parallel Processing Techniques in Python**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (
https://fff97757.click.convertkit-mail2.com/xmuwrw34kxh6hpopmdof5h2ddrdlltnhpl8xx/owhkhqhwx2070wiv/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Training LLM Agents using RL without writing any custom reward
functions.
* 4 parallel processing techniques in Python.
* ​Why do ML models need calibration?​

TODAY'S ISSUE

open-source
-----------

-----------------------------------------------------------------
​Training LLM Agents using RL without writing any custom reward
functions (
https://fff97757.click.convertkit-mail2.com/xmuwrw34kxh6hpopmdof5h2ddrdlltnhpl8xx/z2hghnhe5qm8mpcp/aHR0cHM6Ly9naXRodWIuY29tL29wZW5waXBlL0FSVA==
)​
-----------------------------------------------------------------

Training LLM agents with RL typically requires writing custom
reward functions, which means you need labeled data, expert
feedback, or hours spent hand-crafting reward logic for every new
task.

​
​RULER from OpenPipe (open-source) (
https://fff97757.click.convertkit-mail2.com/xmuwrw34kxh6hpopmdof5h2ddrdlltnhpl8xx/z2hghnhe5qm8mpcp/aHR0cHM6Ly9naXRodWIuY29tL29wZW5waXBlL0FSVA==
) takes a different approach. Instead of scoring each trajectory
in isolation, it asks an LLM judge to rank multiple trajectories
against each other.

This works because relative comparison is fundamentally easier
than absolute scoring, and since GRPO normalizes scores within
each group anyway, only the relative rankings matter.

The implementation is straightforward:

​
You can use any LiteLLM-supported model as the judge, add custom
rubrics for specific evaluation criteria, and it automatically
caches responses to avoid redundant API calls.

It’s a practical way to get started with agent training without
the usual reward engineering overhead.

​You can find the OpenPipe ART GitHub repo here → (
https://fff97757.click.convertkit-mail2.com/xmuwrw34kxh6hpopmdof5h2ddrdlltnhpl8xx/z2hghnhe5qm8mpcp/aHR0cHM6Ly9naXRodWIuY29tL29wZW5waXBlL0FSVA==
)​

Python
------

-----------------------------------------------------------------
​4 parallel processing techniques in Python (
https://fff97757.click.convertkit-mail2.com/xmuwrw34kxh6hpopmdof5h2ddrdlltnhpl8xx/p8heh9h4rnplpxuq/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vb2JqZWN0LW9yaWVudGVkLXByb2dyYW1taW5nLXdpdGgtcHl0aG9uLWZvci1kYXRhLXNjaWVudGlzdHMv
)​
-----------------------------------------------------------------

To unlock true parallelism, Python developers use 4 distinct
techniques: threads, multiprocessing, coroutines, and
subinterpreters. Each solves different problems, and choosing the
wrong one wastes hours of effort.

Let’s understand these 4 approaches today.

Understanding the problem
-------------------------

By default, Python executes code on a single CPU core, even if
your machine has 8 or 16 available.

The reason: the Global Interpreter Lock (GIL).

The GIL ensures only one thread executes Python bytecode at a
time, preventing race conditions but blocking true parallel
execution for CPU-bound tasks.

​
Python offers different approaches to handle this; some bypass
the GIL entirely, some work within its constraints, and some
offer different execution models.

Let’s explore each one.

The 4 Techniques
----------------

We’ll compare these techniques on a simple CPU-bound task.

Here’s our baseline single-threaded code:

​

1) Threads
----------

Threads are lightweight workers sharing the same memory space
within a process. But despite having multiple workers, only one
can execute at any time due to the GIL.

​
Let’s look at the code example for multithreading:

​
We create two threads, assign each the task, start them, and wait
for completion using join().

Result: no speedup.

The GIL ensures only one thread executes at any moment. They take
turns, running sequentially.

The GIL releases during I/O operations, making threads effective
there. But for CPU-bound work, threads don’t help.

2) Multiprocessing
------------------

Each process has its own memory space and its own GIL. This
isolation enables true parallel execution on different CPU cores.

​
Let’s look at the code for multiprocessing:

​
The two processes run simultaneously, giving us nearly 6x
speedup.

​
There are caveats though.

* Startup overhead: Creating processes takes longer than threads.
For tasks taking only milliseconds, the overhead outweighs the
gains.
* No shared memory: Exchanging data requires inter-process
communication (pipes, queues), adding complexity and potential
bottlenecks.

3) Coroutines
-------------

Coroutines enable cooperative multitasking within a single
thread. Instead of the OS deciding when to switch, your code
explicitly yields control at await points.

​
In the code below, we define an async version and use
asyncio.gather() to run both tasks concurrently.

​
In this specific case, it produces no benefit for CPU-intensive
tasks.

This is because Coroutines only switch when you explicitly await.
Our CPU-bound task never yields, so both run sequentially.

Note: Coroutines enable concurrency (handling multiple tasks) but
not parallelism (executing simultaneously). We include them
because developers often confuse the two.
Coroutines shine when waiting on external resources, like APIs,
databases, and file systems. But for pure computation, there’s no
advantage.

4) Subinterpreters
------------------

Multiprocessing offers parallelism but is slow and
resource-heavy. Threads are fast but blocked by the GIL.

Subinterpreters offer a middle ground.

These are isolated execution environments within a single
process. Each has its own memory space and GIL, enabling safe
parallelism with less overhead than multiprocessing.

​
They’re safer than threads because they don’t share global
objects by

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

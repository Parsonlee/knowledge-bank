---
title: What is (was?) GIL in Python?
source: https://mail.google.com/mail/u/0/#inbox/199df440e83cc2f8
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-13
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 What is (was?) GIL in Python? 的原理剖析与工程实践。
tags:
  - clippings
---

# What is (was?) GIL in Python?

## 1. 核心要点解析

本期内容重点涵盖：
- **What is (was?) GIL in Python?**

## 2. 深度拆解与正文翻译

​

​Master full-stack AI engineering (
https://click.convertkit-mail2.com/d0uwowlp78h0ho87kqobmhznv7q44ilhokgvv/6qheh8hlloe3w6ao/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* Scrape the web based on search categories.
* What is (was?) GIL in Python?
* Did Stanford make LLM fine-tuning obsolete?

TODAY'S ISSUE

together with firecrawl
-----------------------

-----------------------------------------------------------------
​Scrape the web based on search categories (
https://click.convertkit-mail2.com/d0uwowlp78h0ho87kqobmhznv7q44ilhokgvv/kkhmh6hnnmvoe3fl/aHR0cHM6Ly93d3cuZmlyZWNyYXdsLmRldi9wbGF5Z3JvdW5k
)​
-----------------------------------------------------------------

With Firecrawl, you can now filter your searches by categories,
like finding research papers, GitHub repos, etc.

Here’s how to do it:

​
This gives much more targeted results by narrowing your search
call to specific content types before you scrape them.

Along with this, here are some recent updates:

* 10x better Semantic Crawling
* New x402 Search Endpoint via CoinbaseDev
* Fire-enrich v2 example
* Improved crawl status + endpoint warnings, and much more.

​Find more info in the docs → (
https://click.convertkit-mail2.com/d0uwowlp78h0ho87kqobmhznv7q44ilhokgvv/58hvh7hgg72409c6/aHR0cHM6Ly9kb2NzLmZpcmVjcmF3bC5kZXYvZmVhdHVyZXMvc2VhcmNoI3NlYXJjaC1jYXRlZ29yaWVz
)​

​You can try it here → (
https://click.convertkit-mail2.com/d0uwowlp78h0ho87kqobmhznv7q44ilhokgvv/kkhmh6hnnmvoe3fl/aHR0cHM6Ly93d3cuZmlyZWNyYXdsLmRldi9wbGF5Z3JvdW5k
)​

python
------

-----------------------------
What is (was?) GIL in Python?
-----------------------------

Python 3.14 was released recently.

Of the many interesting updates (which we shall cover soon), the
update that you can disable GIL (global interpreter lock) is
getting the most attention.

​
Let’s dive in to learn more today!

Some fundamentals
-----------------

* A process is isolated from other processes and operates in its
own memory space. This isolation means that if one process
crashes, it typically does not affect other processes.

​
* Multi-threading occurs when a single process has multiple
threads. These threads share the same resources, like memory.

​

What is GIL?
------------

Simply put, GIL (global interpreter lock) restricts a process
from running more than ONE thread at a time.

​
So essentially, a process can have multiple threads, but ONLY ONE
can run at a given time.

This means the process cannot use multiple CPU cores for
performance optimization, which means multi-threading leads to
similar performance as single-threading.

Let’s understand with a code demo!

* First, we start with some imports and define a long function:

​
* Single threading, wherein we invoke the same function twice,
takes 0.432 seconds.

​
* With multi-threading, we create two threads, one for each
function, and this takes 0.428 seconds:

​
The reason for similar run-time, despite multi-threading, is…

GIL.

On a side note, we do experience a run-time boost with
multi-processing:

​
The above three scenarios (single-threading, multi-threading, and
multi-processing) can be explained visually as follows:

* Single-threading: A single thread executes the same function
twice in order:

​
* Multi-threading: Each thread is assigned the job to execute the
function once. But due to GIL, only one thread can run at a time:

​
* Multi-processing: Each function is executed under a different
process:

​
If this is clear, let’s answer two questions now:

1) Why has Python been using GIL even when it is suboptimal?
------------------------------------------------------------

Thread safety.

When multiple threads run in a process and share the same
resources (such as memory), problems can arise when they try to
access and modify the same data.

For instance, say we want to run two operations with two threads
on a Python list:

​
* If t1 runs before t2, we get the following output:

​
* If t2 runs before t1, we get the following output:

​
We get different outputs!

This can lead to race conditions, where the outcome depends on
the timing of the threads’ execution.

This, and a few more reasons, made it convenient to execute just
one thread at a time.

On a side note, GIL usually affects CPU-bound tasks and not
I/O-bound tasks, where multi-threading can still be useful.

2) If multi-processing works, why not use that as a workaround?
---------------------------------------------------------------

This is easier said than done.

Unlike threads, which share the same memory space, processes are
isolated.

​
As a result, they cannot directly share data as threads do.

While there are inter-process communication (IPC) mechanisms like
pipes, queues, or shared memory to exchange information between
processes, they add a ton of complexity.

Thankfully, Python 3.14 allows us to disable GIL, which means a
process can fully utilize all CPU cores.

This video depicts the run-time difference:

video preview (
https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/mVrjCCRbJCxW3QKTxBTg3S/player
)-->
video preview-->
(
https://click.convertkit-mail2.com/d0uwowlp78h0ho87kqobmhznv7q44ilhokgvv/25h2hoh33dwqg7a3/aHR0cHM6Ly9hcGkuZmlsZWtpdGNkbi5jb20vZS9rN1lIUE4yNFNveHlNOG5HS1puRHhhL21WcmpDQ1JiSkN4VzNRS1R4QlRnM1MvcGxheWVy
)

​
We have been testing Python 3.14 lately, and we’ll share these
updates in a detailed newsletter issue soon.

That said, if you want to get hands-on with actual GPU
programming using CUDA, learn about how CUDA operates GPU’s
threads, blocks, grids (with visuals), etc., we covered it here:
Implementing (Massively) Parallelized CUDA Programs From Scratch
Using CUDA Programming (
https://click.convertkit-mail2.com/d0uwowlp78h0ho87kqobmhznv

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

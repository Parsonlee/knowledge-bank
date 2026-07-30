---
title: "Sync vs. Async in Python"
source: "https://mail.google.com/mail/u/0/#inbox/19c7821062a6ceb4"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-02-19
created: 2026-07-30
description: "详解 Python asyncio 异步编程机制：协程 async/await、事件循环、并发逻辑，以及 I/O 密集型与 CPU 密集型任务的使用误区。"
tags:
  - clippings
---
# Python 中的同步与异步（Sync vs. Async in Python）

设想你正在从 API 获取数据，响应需要几秒钟时间。

在这段时间内，CPU 处于空闲等待状态。理想情况下，如果可行，它完全可以开始执行另一个任务。

Python 的 `asyncio` 框架专为并发执行设计，它允许你暂停正在等待的任务，并立即开始运行其他任务，从而最大化系统资源利用率。

### 核心机制与代码

典型的 Python 实现是同步运行的（一个接一个），即一个任务必须完全结束，下一个任务才能开始。

`sleep` 象征着任务正在等待其他资源。Python `asyncio` 利用 `async` 和 `await` 两个关键字解决了这个问题：

* **`async def`**：将函数定义为协程（Coroutine）。这是一种特殊的函数，可以被暂停和恢复，被调用时不会立即执行。协程是异步代码的基本构建块。
* **`await`**：只能在 `async` 函数内部使用。它告知 Python 解释器：“我即将等待这个结果。请不要阻塞，把控制权交还给事件循环（Event Loop），以便它可以运行其他挂起的任务。”
* **`Event Loop`（事件循环）**：作为调度器管理所有协程，决定下一个运行、暂停或恢复哪个任务。
* **`asyncio.gather()`**：在事件循环上调度并并发运行多个协程。
* **`asyncio.run(main())`**：异步程序的入口点。它建立并管理事件循环，运行主协程，并在完成后关闭循环。

### 常见误区：CPU 密集型 vs. I/O 密集型

**异步操作是在等待时使代码变快，而不是在计算时变快。**

当你的任务是 CPU 密集型（例如进行复杂的矩阵乘法、大规模数据集排序或图像处理）时，`asyncio` 毫无帮助，因为此时没有需要“等待”的东西，CPU 正处于积极工作状态而非空闲。

此外，`asyncio` 运行在由全局解释器锁（GIL）管理的单 CPU 核心上。它实现的是并发（Interleaving Tasks），而非真正的多核并行（Parallel Task Execution）。

因此，`asyncio` 在 **I/O 密集型**场景中大放异彩，程序的大部分时间都在等待外部设备或网络响应：
* **网络请求**：发起多个并发 API 调用（例如使用 `httpx` 或 `aiohttp`）；
* **数据库查询**：并发运行多个独立的数据库查询；
* **消息队列**：在队列上等待新消息。

如果你的任务是 CPU 密集型的，你需要使用 `multiprocessing` 来利用多 CPU 核心（或者在 Python 3.13+ 中禁用 GIL）。总结一句话：每当你的 CPU 因等待外部资源而空闲时，`async` 就能给它分派工作，助你写出充分利用系统潜能的高效代码。

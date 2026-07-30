---
title: "4 parallel processing techniques in Python"
source: "https://mail.google.com/mail/u/0/#inbox/19c2a80854fc31f8"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-02-04
created: 2026-07-30
description: "对比 Python 中的 4 种并行处理技术：多线程、多进程、协程以及子解释器，并解析无 GIL（Free-threaded）Python 3.13+ 的未来趋势。"
tags:
  - clippings
---
# Python 中的 4 种并行处理技术（4 parallel processing techniques in Python）

为了解锁真正的并行计算，Python 开发者通常使用 4 种截然不同的技术：多线程（Threads）、多进程（Multiprocessing）、协程（Coroutines）和子解释器（Subinterpreters）。每种技术解决不同的问题，选错技术可能会浪费大量精力。

### 理解核心问题与 GIL

默认情况下，即便你的机器拥有 8 核或 16 核 CPU，Python 代码也只在单个 CPU 核心上运行。

原因在于：**全局解释器锁（GIL，Global Interpreter Lock）**。

GIL 确保同一时刻只有一个线程执行 Python 字节码，这防止了竞态条件，但同时也阻碍了 CPU 密集型任务的真正并行执行。

![Python 单核与 GIL 限制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82a6bba4-26c3-4210-ba2e-70cf07cb913d_1456x507.png)

基准单线程代码示例如下：

![单线程基准代码示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff12912bf-3ee4-471c-a8fa-8ef17f7eb2ea_1456x1048.png)

## 4 种主流并行技术

### 1. 多线程（Threads）

线程是运行在同一进程内存空间内的轻量级工作者。但在传统 Python 中，由于 GIL 的限制，同一时间只能有一个线程在执行：

![多线程示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9da59be7-af15-4a4c-bac5-884d92c0e368_1456x507.png)

多线程代码示例：

![多线程代码示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49c0a84a-d19a-46e3-a5d5-87d33d737fd5_1456x1010.png)

**结果：完全没有提速。** 线程在 GIL 约束下交替顺序运行。GIL 在 I/O 操作期间会释放，因此多线程对于 I/O 密集型有效，但对 CPU 密集型任务无效。

### 2. 多进程（Multiprocessing）

每个进程都有独立的内存空间和独立的 GIL，这使得它们能够在不同的 CPU 核心上真正并行运行：

![多进程示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6f3954e-a443-4da6-9aa5-7bfa8c7afb59_1024x323.png)

多进程代码示例：

![多进程代码示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c277862-fc67-4bc1-aef3-70f8a5e08185_1456x1053.png)

两个进程同时运行，获得了接近 **6 倍** 的加速效果：

![多进程执行加速效果](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fb36fee-c3bd-462e-b6ea-3c5477e54244_1024x268.png)

**注意事项**：进程创建开销大于线程；由于没有共享内存，交换数据需要进程间通信（IPC，如 Pipe、Queue），增加了复杂度。

### 3. 协程（Coroutines）

协程在单线程内实现协作式多任务。代码在 `await` 点显式交出控制权：

![协程工作示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a255bc2-5763-4d5c-a24e-c30c265c988c_1024x268.png)

协程代码示例：

![协程代码示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01ef2268-7ea1-4ca0-8bbb-893538209731_1456x1329.png)

协程提供的是**并发（Concurrency）**而非**并行（Parallelism）**，对纯 CPU 计算无收益，但在处理高并发网络或数据库 I/O 时表现极为优异。

### 4. 子解释器（Subinterpreters）

子解释器是在单个进程内创建隔离的执行环境。每个环境拥有独立的内存空间和独立的 GIL，比多进程开销小：

![子解释器架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c84d423-4b6e-4e7f-9ff7-41ef1cd000e9_1024x559.png)

子解释器代码示例：

![子解释器代码示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fea7c10-aebd-4621-9fdf-d6004b01f0f0_1456x922.png)

子解释器在 Python 3.12+ 引入，在 3.14+ 结合 `InterpreterPoolExecutor` 可以取得优异的加速。

### 无 GIL Python（Free-threaded Python）与技术选型总结

Python 3.13 引入了可禁用 GIL 的自由线程构建版本。禁用 GIL 后，线程即可直接用于 CPU 密集型并行任务。

技术选型总结决策图：

![Python 并行技术决策指南图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f9496a5-b3d5-4b20-8494-6a496340b078_1456x1087.png)

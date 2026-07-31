---
title: "Python 的 GIL 是什么（又曾经是什么）？"
source: "https://mail.google.com/mail/u/0/#inbox/199df440e83cc2f8"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-13
created: 2026-07-30
description: "邮件说明 GIL 如何使一个进程同一时刻只能运行一个线程、为何它有助于线程安全，以及多进程的代价；并称 Python 3.14 可禁用 GIL。"
tags:
  - clippings
---

# Python 的 GIL 是什么（又曾经是什么）？

邮件以 Python 3.14 为背景，称其中备受关注的一项更新是可禁用全局解释器锁（GIL，Global Interpreter Lock）。

## 进程、线程与 GIL

进程彼此隔离，各自拥有内存空间；因此一个进程崩溃通常不会影响其他进程。多线程则是一个进程中有多个线程，它们共享包括内存在内的资源。

GIL 的简化描述是：它限制一个进程在任一时刻只能运行**一个**线程。所以进程虽可有多个线程，却不能同时用多个 CPU 核心执行 CPU 密集型 Python 工作；邮件的示例中，顺序执行两次函数耗时 0.432 秒，而两线程执行耗时 0.428 秒，几乎没有差别。

相比之下，将两次计算放进不同进程可以带来运行时间提升，因为它们不受同一进程内 GIL 的限制。

## 为什么过去保留 GIL？

邮件给出的主要原因是**线程安全**。同一进程的线程共享资源；若两个线程同时访问或修改同一份数据，例如 Python 列表，最终结果可能取决于调度先后，形成竞态条件（race condition）。让一次只运行一个线程，能避免或简化这类问题。

GIL 通常影响 CPU 密集任务；对 I/O 密集任务，多线程仍可能有价值。

## 为什么不总用多进程？

多进程虽能并行，却不像线程那样共享内存。进程需要通过管道、队列或共享内存等 IPC 机制交换数据，这会增加实现复杂度。

邮件称 Python 3.14 允许禁用 GIL，因此一个进程可充分使用多 CPU 核；同时给出 [运行时间差异的视频演示](https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/mVrjCCRbJCxW3QKTxBTg3S/player)。

---
title: "CPU、GPU、TPU、NPU 与 LPU：五种 AI 计算架构"
source: "https://mail.google.com/mail/u/0/#inbox/19faa9c1ec5cf9ba"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-28
created: 2026-07-30
description: "解释 CPU、GPU、TPU、NPU 和 Groq LPU 在灵活性、并行性及内存访问方面的根本权衡与适用场景。"
tags:
  - clippings
---

# CPU、GPU、TPU、NPU 与 LPU：五种 AI 计算架构（CPU vs GPU vs TPU vs NPU vs LPU）

![原邮件配图](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/be74uXjtJyZrL9S7isHvqc/email)

如今有五种硬件架构为 AI 提供动力。

它们各自在灵活性、并行性和内存访问之间做出了根本不同的权衡。

下图并排展示了这五种架构的内部结构：

## CPU

CPU 专为通用计算构建。少量强大的核心处理复杂逻辑、分支和系统级任务。

它拥有深层缓存层级与片外主存（DRAM）。它非常适合操作系统、数据库和决策密集型代码，但不太适合矩阵乘法这类重复性数学计算。

## GPU

GPU 不使用少数强大的核心，而是将工作分布到数千个较小的核心上；这些核心对不同数据执行同一条指令。

这正是 GPU 主导 AI 训练的原因：这种并行性与神经网络所需的数学计算直接匹配。

## TPU

TPU 在专用化上更进一步。

其核心计算单元是一张由乘加（MAC）单元构成的网格，数据以波的方式在其中流动。

权重从一侧进入，激活值从另一侧进入，部分结果持续传播，而无需每次都返回内存。

整个执行过程由编译器控制，而不是由硬件调度。Google 专门为神经网络工作负载设计了 TPU。

## NPU

NPU 是面向边缘场景优化的变体。

其架构围绕塞满 MAC 阵列的 Neural Compute Engine 构建，并配有片上 SRAM；但与高带宽内存（HBM）不同，NPU 使用低功耗系统内存。

设计目标是在个位数瓦的功耗预算内运行推理，例如智能手机、可穿戴设备和 IoT 设备。Apple Neural Engine 和 Intel 的 NPU 都遵循这种模式。

## LPU（Language Processing Unit）

LPU 是 Groq 推出的最新参与者。

这种架构完全将片外内存移出关键路径。所有权重存储都位于片上 SRAM 中。

执行完全确定，并由编译器调度，因此没有缓存未命中，也没有运行时调度开销。

代价是每块芯片可提供的内存有限；这意味着为了服务一个大型模型，需要将数百块芯片连接在一起。但其延迟优势是真实存在的。

AI 计算已经从通用灵活性（CPU）演进到极致专用化（LPU）。每一步都是以一部分通用性换取更高效率。

![原邮件配图](https://embed.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/dhYRfnLgrF4qACgX56Fc4p/email)

邮件中的第二张图同样并排展示了五种架构的内部结构；其灵感来自 ByteByteGo 关于 CPU、GPU 和 TPU 的帖子，原文将其扩展为另外两种正在成为 AI 推理核心的架构。

另外，如果你想亲自动手进行 CUDA GPU 编程，学习 CUDA 如何运行 GPU 的线程、块和网格（含可视化），邮件推荐：[Implementing (Massively) Parallelized CUDA Programs From Scratch Using CUDA Programming](https://www.dailydoseofds.com/implementing-massively-parallelized-cuda-programs-from-scratch-using-cuda-programming)。

👉 留给你的问题：这五种架构中，你实际使用过或部署过哪些？

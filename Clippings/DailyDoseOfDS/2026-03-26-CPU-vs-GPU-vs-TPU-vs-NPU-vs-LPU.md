---
title: "CPU vs GPU vs TPU vs NPU vs LPU"
source: "https://mail.google.com/mail/u/0/#inbox/19d2bbc9492d99c6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-26
created: 2026-07-30
description: "对比当前驱动 AI 计算的 5 大主流硬件架构（CPU、GPU、TPU、NPU、LPU），从控制单元、算力并行度、内存带宽与应用场景深度剖析。"
tags:
  - clippings
---
# CPU vs GPU vs TPU vs NPU vs LPU硬件架构对比（CPU vs GPU vs TPU vs NPU vs LPU）

![AI 计算硬件架构对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F750b0761-6731-47ab-b321-738c8a7e6446_1166x728.png)

当前共有 **5 种主流硬件架构** 为人工智能提供算力。每一种架构都在**通用性（Flexibility）**、**并行度（Parallelism）** 与 **内存访问（Memory Access）** 之间做出了截然不同的底层设计权衡。

以下是这 5 大算力芯片的架构深度拆解：

---

## 1. CPU（通用中央处理器）

![CPU 架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec451c02-d03e-461f-b5d7-ce7a8cbd0468_985x507.png)

* **设计初衷**：为通用计算而生。
* **架构特点**：拥有少量极强大的核心（Core），配备复杂的控制逻辑、分支预测器（Branch Predictors）与深层 Cache 级联（L1/L2/L3），通过片外主存 DRAM 交互。
* **适用场景**：操作系统运行、数据库检索与复杂的条件分支决策逻辑。对于大批量重复的矩阵乘法运算效能较低。

---

## 2. GPU（图形处理器）

![GPU 架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff08adb38-f33e-49b8-801b-3abacfa2856f_985x509.png)

* **设计初衷**：大规模数据并行吞吐（SIMD/SIMT 模型）。
* **架构特点**：放弃复杂的控制逻辑，转而堆叠数千个小型核心。所有核心以高并行方式在不同数据上同步执行相同的指令。配备高带宽显存（HBM/GDDR）。
* **适用场景**：主流神经网络的深度学习训练（Training）与高吞吐量推理。

---

## 3. TPU（张量处理器）

![TPU 架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F147eacea-d67b-43cf-b8dd-0840f3ee8400_985x503.png)

* **设计初衷**：Google 专为深度学习矩阵运算定制的 ASIC。
* **架构特点**：核心计算单元为**脉动阵列（Systolic Array）**，由乘加单元（MAC）构成的二维网格。数据像波浪一样在网格间流动：权重从一侧进入，激活值从另一侧进入，中间结果直接在网格内部传递，无需每次读写主存。整个过程由专用编译器直接调配，无需硬件级调度开销。
* **适用场景**：大规模 Transformer 模型训练与云端超大集群推理。

---

## 4. NPU（神经网络处理器）

![NPU 架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5c3018ab-4abc-4a11-9f74-8787b86fac08_985x527.png)

* **设计初衷**：边缘设备（Edge Devices）的功耗受限推理。
* **架构特点**：以 Neural Compute Engine 为中心，整合 MAC 矩阵与片上 SRAM。不同于高功耗 HBM，NPU 配合低功耗系统内存使用。
* **适用场景**：智能手机（如 Apple Neural Engine）、可穿戴设备与 IoT 端的单位数瓦特（Single-digit watt）低功耗 AI 推理。

---

## 5. LPU（语言处理单元）

![LPU 架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7136ebe2-9d8f-47aa-a26b-fc33632c8aeb_1456x695.png)

* **设计初衷**：Groq 研发，专为 LLM 顺序 Token 生成（Sequential Token Generation）解除内存瓶颈。
* **架构特点**：彻底摒弃传统外部 DRAM/HBM 显存，直接将高达数百兆字节的 **On-chip SRAM（晶片内超高速静态内存）** 嵌入芯片。拥有极致的内存带宽与确定性指令调度（Deterministic Instruction Execution）。
* **适用场景**：超低延迟、极高 TPS（Tokens Per Second）的 LLM 实时对话与流式推理。

---

## 总结与选择指南

| 硬件架构 | 核心优势 | 内存机制 | 典型代表 / 供应商 |
| :--- | :--- | :--- | :--- |
| **CPU** | 逻辑控制强，通用性最高 | DRAM + 级联 Cache | Intel Core/Xeon, AMD EPYC |
| **GPU** | 海量并行核心，训练生态成熟 | HBM / GDDR | NVIDIA H100/B200, AMD MI300 |
| **TPU** | 脉动阵列，编译优化，矩阵效率极高 | HBM + 脉动流 | Google TPU v4/v5p/v6 |
| **NPU** | 极低功耗比，边缘推理 | 片上 SRAM + 低功耗内存 | Apple A/M系列 ANE, Intel NPU |
| **LPU** | 片上 SRAM 零延时，极速流式生成 | 片上 SRAM 阵列 | Groq LPU |

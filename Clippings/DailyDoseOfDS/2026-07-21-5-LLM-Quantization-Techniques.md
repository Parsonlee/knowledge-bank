---
title: "5 LLM Quantization Techniques"
source: "https://mail.google.com/mail/u/0/#inbox/19f86be0631f8e2c"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-21
created: 2026-07-30
description: "全面剖析 5 种主流大语言模型量化技术（Naive Rounding, GPTQ, AWQ, LLM.int8(), QAT），对比其离群值处理与显存压缩机制。"
tags:
  - clippings
---

# 5 种大语言模型（LLM）量化技术全景对比（5 LLM Quantization Techniques）

一个 700 亿参数（70B）的 FP16 模型，单是保存模型权重就需要 140GB 显存。量化技术（Quantization）通过将高精度浮点数（如 FP16/BF16）映射为低精度数值（如 INT8/INT4），是让大模型运行于边缘设备与高效服务中的核心技术。

![大模型量化技术映射全景图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb306f134-0557-4da8-a23d-ad979dd5306c_4707x1105.png)
*图 1：大模型量化映射机制全景*

---

### 5 种核心量化技术深入拆解

![5 种量化技术机制对比与分类](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7d5a73e-26e0-4bf9-b48c-48b841ff5b65_1200x896.jpeg)
*图 2：5 种量化技术机制对比*

#### 1. Naive Rounding（朴素四舍五入）
最直接的量化方式，将连续的浮点网格均匀划分为 256（INT8）或 16（INT4）个桶，然后将每个权重推入最近的网格点中。由于大模型中往往存在少量数值极大但至关重要的离群值（Outliers），朴素舍入会导致严重的高精度损失。

#### 2. GPTQ（训练后后处理修正）
GPTQ 属于训练后量化（PTQ）。它逐层对权重矩阵进行量化，并在量化某一个元素后，通过二阶海森矩阵（Hessian Matrix）计算误差，实时修正该层中其余尚未量化的权重，补偿整体输出偏差。

#### 3. AWQ（激活感知权重量化）
AWQ 发现并非所有权重都同等重要：只有约 1% 对应大激活值的通道才对输出质量起决定性作用。AWQ 不对这 1% 关键权重使用更高精度，而是在量化前乘以放大缩放因子，使其在量化网格中分布更广、精度损失更小，推理时再通过反向缩放还原计算。AWQ 对校准数据依赖度低，已成为 vLLM 等服务引擎的标准规范。

#### 4. LLM.int8()（混合精度离群值隔离）
LLM.int8() 采取“不硬碰硬”的策略。在加载模型时，动态识别出值大于阈值的异常维度列：
* 异常列以原始 FP16 精度进行矩阵乘法；
* 剩余 99.9% 的正常数值以 INT8 运行；
* 最终将两部分结果累加。
该方法无需提前训练校准，但由于拆分与合并矩阵操作增加了开销，推理速度不如 INT4 优化 Kernel，常用于本地开发与 QLoRA 微调。

#### 5. QAT（量化感知训练）
QAT 在微调训练期间的前向传播中模拟 INT4 舍入损伤，使模型权重在梯度更新中自动适应量化后的输出，从而在最终导出低精度权重时几乎不损失精度。例如 Google 的 Gemma 3 QAT 权重仅通过 5000 步调优就达到了接近全精度的表现。

这 5 种方法的核心差异在于：**究竟是在舍入时、舍入后、舍入前、推理期还是训练期去解决离群值（Outliers）问题。**

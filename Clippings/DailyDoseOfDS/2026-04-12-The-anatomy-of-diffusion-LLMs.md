---
title: "The anatomy of diffusion LLMs"
source: "https://mail.google.com/mail/u/0/#inbox/19d838888f466ecf"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-12
created: 2026-07-30
description: "深入解析离散扩散语言模型（Diffusion LLMs）的架构原理，对比传统自回归模型（Autoregressive Models）在并行生成、非逐字预测与灵活编辑方面的突破性优势。"
tags:
  - clippings
---
# 扩散 LLM（Diffusion LLMs）的架构原理剖析（The anatomy of diffusion LLMs）

语言模型领域目前正在发生一项极其重要的架构演进：**扩散 LLM（Diffusion LLMs）**。

传统大语言模型（如 GPT-4、Llama）几乎清一色采用**自回归（Autoregressive）架构**。而离散扩散模型的兴起为文本生成带来了全新的范式。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febec5815-4a5f-4688-a64e-68b2cd58578d_680x360.png)

### 自回归模型 vs. 扩散 LLM

1. **自回归模型（Autoregressive Models）**：
   - 生成方式：从左至右（Left-to-Right）逐个 Token 顺序预测。
   - 局限性：无法并行生成；前面的 Token 一旦出错就会造成误差累积；极难进行非顺序的任意位置修改与填空（Infilling）。

2. **扩散 LLM（Diffusion LLMs）**：
   - 生成方式：利用**离散去噪（Discrete Denoising）**过程。
   - 初始化时先生成一个全由 `[MASK]` 标记占位的完整序列，然后在多个去噪步（Denoising Steps）中，并行地逐步解除掩码并修正全句标记。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43585fc9-cc1b-44a9-ad2d-52bc5c6e6dd1_680x354.png)

### 扩散 LLM 的三大核心优势

- **并行解码潜力**：打破逐字串行依赖，具备极高的吞吐与生成速度提升空间。
- **全局灵活编辑**：能够在文本的任意中间位置插入、修改或精炼内容。
- **天然契合代码与结构化生成**：在代码重构、填空补全等强结构任务中展现出卓越的相干性。

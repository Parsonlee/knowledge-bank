---
title: "Two techniques to extend the context length of LLMs"
source: "https://mail.google.com/mail/u/0/#inbox/19acc373a89bc8c4"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-28
created: 2026-07-30
description: "解析扩展大语言模型上下文长度的两大关键技术：稀疏注意力（Sparse Attention）与 Flash Attention。"
tags:
  - clippings
---

# 扩展大语言模型上下文长度的两项核心技术（Two techniques to extend the context length of LLMs）

随着大语言模型（LLM）的应用深入，处理数十万乃至数百万 Token 的长上下文需求日益迫切。然而，标准注意力机制（Standard Self-Attention）面临着严峻的性能瓶颈。

![标准注意力二次方复杂度瓶颈图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F469f5487-0d4c-42b3-870f-64036ab5a8f6_2217x798.jpeg)

**核心挑战**：标准 Transformer 中的注意力机制计算复杂度与显存开销均随序列长度 $ 呈二次方增长（(N^2)$）。当序列长度从 4k 增加到 32k 时，注意力矩阵的显存与计算开销将暴增 64 倍！

为了拓展上下文窗口，业界主要采用了以下两种核心技术方向：

### 1. 稀疏注意力（Sparse Attention）

![稀疏注意力机制示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24561a7c-904d-429d-8f36-a781c9bb6134_2134x1080.jpeg)

稀疏注意力是一种**近似注意力（Approximate Attention）**方法。
* **原理**：取消全盘计算所有 Token 之间的点积注意力，转而仅计算部分特定位置 Token 的注意力。
* **模式**：包括局部滑动窗口（Local Window）、固定步长跨度（Strided Pattern）以及随机连接（Random Connections）等。
* **效果**：将计算复杂度从 (N^2)$ 降低至线性或亚二次方级（如 (N \sqrt{N})$），显著减轻长文本训练与推理开销。

### 2. Flash Attention

![Flash Attention 硬件感知分块与 SRAM 优化图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8775aa17-0917-4789-928e-027dcf135fa0_2409x420.jpeg)

与稀疏注意力不同，Flash Attention 是一种**精确定量注意力（Exact Attention）**算法，它不牺牲任何模型精度。
* **原理**：利用 GPU 内存层次结构（Fast SRAM 与 Slow HBM）的硬件感知优化。
* **分块（Tiling）**：将输入矩阵 , K, V$ 分割为适配 GPU 高速片上缓存 SRAM 大小的块，在 SRAM 中增量式完成 Softmax 与点积计算，避免向慢速 HBM 频繁读写巨大的中间注意力矩阵  	imes N$。
* **效果**：将 HBM 内存访问开销从 (N^2)$ 降至 (N)$，不仅大幅提升计算速度（2-4倍），同时节省大幅显存开销。

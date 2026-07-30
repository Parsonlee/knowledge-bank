---
title: "The anatomy of diffusion LLMs"
source: "https://mail.google.com/mail/u/0/#inbox/19fa5754b2a0ee28"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-27
created: 2026-07-30
description: "详解扩散大语言模型（Diffusion LLMs）的技术原理，分析其如何打破传统自回归模型逐 Token 串行生成的内存带宽瓶颈，实现高效并行解掩码推理。"
tags:
  - clippings
---

# 扩散大语言模型（Diffusion LLMs）架构全景解密（The anatomy of diffusion LLMs）

当今主流的生产级大语言模型（如 GPT-4、Claude、Gemini、LLaMA 等）均采用完全相同的生成范式：**自回归（Autoregressive）模式，从左至右一次生成一个 Token。**

![传统自回归串行生成 vs 扩散模型并行解掩码生成](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F137efd9c-5304-4ca6-a332-1a0456e80e7e_679x374.png)
*图 1：传统自回归串行生成 vs 扩散模型并行解掩码生成*

在自回归生成中，每产生一个新的 Token，都必须将完整模型的权重从 GPU 显存重新加载一次，执行极少量的计算，然后再加载完整权重以生成下一个 Token。在 NVIDIA A100 上，这意味着每传输 1 Byte 数据仅能进行约 1 FLOP 计算，而 GPU 硬件设计的峰值效率通常需要每 Byte 匹配 100+ FLOPs。因此，**自回归推理本质上受限于内存带宽（Memory-Bandwidth Bound）。**

---

### 一、 扩散 LLM 的全新解题思路

扩散 LLM 采取了截然不同的技术路线：它们从一个被完全掩码（Masked）的序列开始，利用双向注意力机制（Bidirectional Attention），在多个迭代步骤中并行地解除 Token 掩码。

这种设计将推理模式从**内存带宽限制**彻底转变为了**计算密集型（Compute-Bound）**，而这正好契合了现代 GPU 算力集群的最强优势。

![扩散模型从全掩码状态迭代去噪还原文本的过程](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F963892de-133d-4774-a859-4d3c77a1a2eb_679x410.png)
*图 2：扩散模型从全掩码状态迭代去噪还原文本的过程*

实验结果正在快速赶超自回归模型：
* **Block Diffusion (BD3-LM)** 在 LM1B 上的困惑度（Perplexity）与自回归模型的差距缩小至 0.5 点以内。
* 80 亿参数的 **LLaDA** 在 MMLU Benchmark 上追平了 LLaMA 3 8B，并在 TruthfulQA 和 HumanEval 上实现超越。
* **Dream 7B** 等模型已通过 SGLang 实现在生产环境中的高性能部署。

---

### 二、 扩散 LLM 的核心技术组件

理解扩散 LLM 的数学与工程细节需要掌握以下三个核心板块：

![离散扩散的前向破坏过程与变分下界（ELBO）训练目标](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe6cd162-18c4-4c3e-bbe5-e8e2656938e9_679x481.png)
*图 3：离散扩散的前向破坏过程与变分下界（ELBO）训练目标*

![基于 Block-level 的 KV Cache 优化](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42aac678-f4e2-459f-a8c2-223f8a2db6a2_680x428.png)
*图 4：基于 Block-level 的 KV Cache 优化*

1. **前向离散破坏过程（Forward Masking Process）**：通过在时间步 $t$ 上引入离散掩码转换矩阵，逐步将干净的文本序列转换为完全掩码的状态。
2. **变分下界优化（ELBO Objective）**：使用逆向预测网络重构原始 Token 概率分布，最大化证据下界。
3. **块级 KV Cache（Block-level KV Caching）**：在并行去噪迭代中，将已确定取消掩码的文本块其键值状态进行缓存，从而避免重复计算。

从前向掩码过程到 ELBO 目标，再到块级 KV Cache 优化，深入掌握扩散 LLM 的底层数学原理与架构设计，将在未来大模型算力演进中展现出巨大的工程价值。

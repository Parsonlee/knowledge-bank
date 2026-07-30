---
title: "LLM Fine-tuning: Techniques to adapt language models."
source: "https://mail.google.com/mail/u/0/#inbox/19cf33bc860b2d6b"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-15
created: 2026-07-30
description: "全面解析大语言模型微调（LLM Fine-tuning）的核心技术路线，包括 Full Fine-tuning、PEFT (LoRA, QLoRA)、Instruction Tuning 以及 Direct Preference Optimization (DPO)。"
tags:
  - clippings
---

# LLM 微调技术全景指南：大语言模型适配方法论（LLM Fine-tuning: Techniques to adapt language models.）

在大语言模型（LLM）的生命周期中，预训练（Pre-training）赋予了模型通用的世界知识与语言能力，而**微调（Fine-tuning）**则是将通用基座模型适配到特定领域任务、遵循复杂指令以及与人类偏好对齐的必经之路。

本文深度拆解主流 LLM 微调技术的分类、原理与最佳实践。

![大语言模型微调技术全景分布图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ee0ecbb-bbf7-466d-965d-007823f66cce_2264x1204.png)
*图 1：大语言模型微调技术全景分布图解*

---

### 一、 微调范式演进：全参数微调 vs PEFT

1. **Full Fine-tuning（全参数微调）**：更新模型的所有参数。尽管效果上限高，但算力与显存开销极其高昂（例如 70B 模型需要 TB 级的显存集群）。
2. **Parameter-Efficient Fine-Tuning (PEFT, 参数高效微调)**：只更新极少数新增或特定的参数，保持预训练权重冻结。

![LoRA 低秩分解矩阵权重更新原理](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb9c4a8f-f7d9-4b20-beec-df5f1ef1dfc6_2240x1208.png)
*图 2：LoRA 低秩分解矩阵权重更新原理*

其中最关键的代表技术为 **LoRA (Low-Rank Adaptation)**：
通过将参数更新量 $\Delta W$ 分解为两个低秩矩阵的乘积：

$$W_{new} = W_{0} + \Delta W = W_{0} + B 	imes A$$

其中 $W_0 \in \mathbb{R}^{d 	imes k}, B \in \mathbb{R}^{d 	imes r}, A \in \mathbb{R}^{r 	imes k}$，且秩 $r \ll \min(d, k)$。这一设计可减少 99% 以上的待训练参数量。

---

### 二、 QLoRA 与量化微调

**QLoRA (Quantized LoRA)** 在 LoRA 的基础上进一步引入了三项关键工程创新：
- **4-bit NormalFloat (NF4)** 数据类型：针对正态分布权重优化的信息论最佳量化格式。
- **Double Quantization（双重量化）**：对量化比例因子再次进行量化，大幅节省显存。
- **Paged Optimizers**：利用 CPU 与 GPU 之间的内存分页传输，解决梯度峰值显存溢出（OOM）问题。

![QLoRA 4-bit 量化与 Paged Optimizer 显存压缩架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bbf8cb2-20f7-4dc7-beee-07a8df8090a9_2328x1208.png)
*图 3：QLoRA 4-bit 量化与 Paged Optimizer 显存压缩架构*

---

### 三、 指令微调与偏好对齐（SFT -> DPO / RLHF）

在得到基础能力的微调模型后，需要进行指令微调（SFT）和偏好对齐：
- **Supervised Fine-Tuning (SFT)**：使用 `<Prompt, Response>` 高质量指令对训练模型遵循指令。
- **Direct Preference Optimization (DPO)**：相比复杂的 RLHF（需要单独训练 Reward Model 和 PPO），DPO 直接利用二元偏好数据拟合交叉熵损失，极大地简化了对齐训练流程。

![从 SFT 到 DPO / RLHF 的 LLM 训练阶段示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0da02ffe-bac1-467e-bdc1-7ad2cf7030c8_895x487.png)
*图 4：从 SFT 到 DPO / RLHF 的 LLM 训练阶段示意图*

熟练掌握从全参数微调、PEFT/LoRA 到 DPO 对齐的完整技术链路，是现代 LLM 算法工程师的核心基本功。

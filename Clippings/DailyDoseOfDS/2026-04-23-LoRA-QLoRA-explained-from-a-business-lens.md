---
title: "LoRA/QLoRA explained from a business lens"
source: "https://mail.google.com/mail/u/0/#inbox/19dbca56ab454b95"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-23
created: 2026-07-30
description: "从商业成本与资源效率的角度深入剖析 LoRA 和 QLoRA 技术，阐明其如何通过冻结原模型权重并训练低秩矩阵，大幅削减大语言模型微调与多租户部署的显存及存储开销。"
tags:
  - clippings
---
# 商业视角下的 LoRA/QLoRA 解读（LoRA/QLoRA explained from a business lens）

商业的核心关切永远在于**业务影响（Impact）**：你是否能够降低成本？能否驱动营收？能否扩展 ML 模型？能否在趋势发生前做出预测？

本文将从商业与工程资源效率的角度，重新审视大语言模型（LLM）微调技术中的 LoRA 和 QLoRA。

### 大模型微调的商业成本困境

对比 BERT-large 与 GPT-3 的参数量差异：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff9afd2f9-892b-4640-8a57-4da5d4ca6bcd_807x400.png)

在传统微调模式下，我们可以轻松在单张 GPU 上对 BERT-large（约 3.4 亿参数）进行多次全参数微调。然而，面对拥有 1750 亿参数的 GPT-3，全参数微调在商业上变得极度昂贵甚至不可行——单是在 float16 精度下加载模型权重就需要 **350 GB** 的显存。

这意味着，如果像 OpenAI 这样的平台在提供微调 API 时采用传统全参数微调，就必须为每个用户单独保存一份完整的模型副本：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3585f1a2-20c1-4b93-b76f-860e253af000_1069x427.png)

- 如果有 10 个用户微调 GPT-3 $ightarrow$ 需储存 **3,500 GB** 模型权重。
- 如果有 1,000 个用户微调 GPT-3 $ightarrow$ 需储存 **350,000 GB** 模型权重。
- 如果有 100,000 个用户微调 GPT-3 $ightarrow$ 需储存 **3,500 万 GB** 模型权重！

此外，还面临两大严峻的资源管理挑战：
1. **长尾闲置开销**：OpenAI 仅按实际调用量计费。若用户仅出于学习或测试目的微调了模型却很少调用，平台依然要为其储存海量权重。
2. **常驻显存浪费**：由于用户请求随时可能到达，平台是否需要将每个微调模型时刻加载在显存中？这无疑会造成极大的算力资源浪费。

### LoRA 的破解之道

**LoRA（Low-Rank Adaptation，低秩适应）** 及 QLoRA 等衍生技术优雅地解决了这一关键商业难题。

其核心思想在于：**在微调过程中仅训练极少量的附加参数，而保持原始基础模型的权重冻结**。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F573e5773-bd17-426f-886d-1761660447bf_1042x986.gif)

具体实现上：
- 假设原始模型某个权重矩阵为 $W$（形状为 $d 	imes d$）。
- LoRA 定义两个对应的低秩分解矩阵 $A$（形状为 $d 	imes r$）与 $B$（形状为 $r 	imes d$），其中秩 $r$ 通常为很小的单位数（如 $r=4$ 或 $8$）。
- 在微调期间，完全冻结权重矩阵 $W$，仅更新低秩矩阵 $A$ 和 $B$ 的权重。

在推理阶段，低秩矩阵相乘 $B \cdot A$ 会相乘产生一个与原矩阵 $W$ 同等形状（$d 	imes d$）的增量矩阵，因此最终输出为：

$$h = W x + \Delta W x = W x + B A x$$

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2cee578-7726-47f6-b280-faaf85b76560_1200x428.png)

### 商业优势总结

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F106a35c8-b8bd-40ad-a8f2-889b281a2137_1200x1244.png)

1. **极其微小的存储开销**：每个用户的 LoRA 附加矩阵通常不超过 **20-25 MB**。相比传统全参数微调的数百 GB，存储需求降低了几个数量级。
2. **高效的多租户共享**：OpenAI/云厂商仅需在 GPU 内存中常驻一份共享的基础模型权重 $W$，并在推理请求到达时动态加载轻量的 LoRA 矩阵。
3. **彻底消解闲置与冷启动成本**：即使大部分微调模型使用率较低，极小的存储占用也不会造成明显的资金压力。

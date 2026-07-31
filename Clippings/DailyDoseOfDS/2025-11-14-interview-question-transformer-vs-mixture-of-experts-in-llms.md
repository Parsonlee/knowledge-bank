---
title: "[Interview question] Transformer vs. Mixture of Experts in LLMs"
source: "https://mail.google.com/mail/u/0/#inbox/19a841a055b8cd28"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-14
created: 2026-07-30
description: "面试精选：深入对比大模型中的 Standard Transformer 与 Mixture of Experts (MoE) 架构差异与路由原理。"
tags:
  - clippings
---

# 【面试精选】大模型中的 Transformer vs. 混合专家架构（MoE）（[Interview question] Transformer vs. Mixture of Experts in LLMs）

在 LLM 系统架构面试中，密集型（Dense）Transformer 与混合专家（Mixture of Experts, MoE）架构的对比是高频考点。

![标准 Dense Transformer 前馈层全员激活示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff74ae548-d64b-46f0-9b10-414a2a045e5c_1292x816.gif)

![MoE 混合专家架构路由器门控机制示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89aa177b-ab94-48f1-873f-787dd42d5f69_1080x846.gif)

### 架构核心差异

1. **标准 Dense Transformer**：每个输入 Token 都必须经过同一个巨大的前馈神经网络（FFN Layer）中所有的参数进行计算。
2. **MoE 架构**：将原本单一的大型 FFN 拆分为多个独立的“专家网络（Experts）”，并引入一个**路由器（Router / Gating Network）**。对于输入的每个 Token，路由器动态选择并仅激活其中 Top-K 个最匹配的专家来进行处理。

![MoE 训练中的专家失衡与路由贪婪陷阱图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Facd5eba8-75b4-45e7-8a47-ca90ef7666fe_1094x662.gif)

![引入噪声与 -infinity 截断解决路由贪婪](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23d13981-a8d2-435f-b1f4-9cf691ad8d6d_1874x774.gif)

![设置 Expert Capacity 负载均衡图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb64800ec-666c-443e-8994-1aead584f9db_1568x702.gif)

### MoE 训练的四大挑战与应对策略

* **挑战 1：路由贪婪导致部分专家未充分训练（Under-trained experts）**
  * *原因*：训练初期表现稍好的某个专家会频繁被路由器选中，从而获得更多更新机会变得更强，导致“赢者通吃”，其余大部分专家无法获得充分训练。
  * *解法*：在路由器的 Logits 中加入适量**噪声（Noise Injection）**，并将非 Top-K 的 Logits 置为 569X\infty$（Softmax 后归零），强行给其他潜在专家被选中的锻炼机会。

* **挑战 2：Token 分配不均衡（Load Imbalance）**
  * *原因*：某些热门专家处理的 Token 远远超过其承载上限。
  * *解法*：设置**专家容量限制（Expert Capacity Limit）**。一旦某个专家处理的 Token 数达到预设阈值，多余的 Token 将被强制推给次优的候选专家。

### 总结与代表性模型

虽然 MoE 模型拥有一大批专家参数（如 Mixtral 8x7B、Llama 4 MoE 等），但在推理计算时仅激活其中一小部分参数，因此能在保持巨大模型容量的同时大幅加快推理吞吐。

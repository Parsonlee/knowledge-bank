---
title: "How to beat GRPO without touching model weights."
source: "https://mail.google.com/mail/u/0/#inbox/19de58fc0d126e4b"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-01
created: 2026-07-30
description: "深入解析 GEPA（基于自然语言反思的 Prompt 演化算法）如何打破 GRPO 的标量奖励瓶颈，以 10-50 倍较低算力提升复合 AI 系统性能。"
tags:
  - clippings
---

# 如何在不修改模型权重的前提下击败 GRPO（How to beat GRPO without touching model weights.）

GRPO 需要数万次 Rollout（轨迹采样）才能收敛。每一次 Rollout 会产生长达 5,000 个 Token 的推理轨迹（包含思考步骤、工具调用与自我修正），然而 GRPO 最终却将这一切压缩为一个单一的标量奖励（Scalar Reward）。

这导致我们反向传播时仅利用了每条轨迹中 1 个 Bit 的信号，却抛弃了数千个 Bit 的结构化诊断信息。

![GRPO 将丰富轨迹压缩为标量奖励导致信号丢失图示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e9d67c2-d11b-4838-bc9c-d8f979ec9591_851x520.png)

**GEPA（Generative Evolutionary Prompt Augmentation）** 采取了一种截然不同的路径：它直接将完整的 Rollout 轨迹交给一个反思 LLM（Reflection LLM），提问：“哪里出错了，Prompt 应该如何修改？”

![GEPA 通过反思模型生成新 Prompt 演化示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F565d9d1f-4514-47be-8a56-bcff6ddbd556_1274x642.png)

在复合 AI 系统（Multi-module Pipelines）上，GEPA 仅需比 GRPO **低 10-50 倍的计算资源** 即可达到甚至超越 GRPO 的性能，且完全不需要训练基础设施。

---

### 1. 信号压缩困境（The Signal Compression Problem）
强化学习在语言模型上的核心痛点在于信号稀疏化。每条轨迹都包含了丰富的错误日志与推理步骤，GRPO 将其转化为单个标量后，不得不依赖海量的采样来弥补信息的丧失。

![自然语言反思替换梯度反向传播图示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4cf73c7b-cc25-4a19-b783-6e8c6ada48bc_851x455.png)

---

### 2. 反馈函数与 6 步演化算法
GEPA 用自然语言反馈函数 $\mu_f$ 替代单纯的标量分值。

演化算法 6 步循环：
1. **Pareto 采样**：从种群中挑选候选 Prompt 集合。
2. **选择模块**：按轮询机制选择待突变模块。
3. **采样测试**：选取 3 个训练样本执行 Rollout。
4. **轨迹收集**：获取完整轨迹与反馈 $\mu_f$。
5. **反思突变**：反思 LLM 分析失败模式并写出新的 Prompt。
6. **接受/拒绝判定**：重新验证，若表现提升则更新种群，否则丢弃。

---

### 3. 核心设计：Pareto 选择（Pareto Selection）
为防止种群迅速陷入局部最优，GEPA 引入质量-多样性优化中的 **Pareto 选择**。

![贪婪选择 vs Pareto 演化选择对比图示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F816d7953-f8d3-480a-84d5-e38f3f299e42_680x378.png)

只要某个 Prompt 候选在**至少一个任务**上表现最佳，Pareto 选择就会保留它，而不是盲目追求整体平均分最高。这保留了独特的解题策略，为后续交叉组合奠定了基础。

![各种 Prompt 优化与 RL 方法全景对比图表](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e61481b-0911-40ff-8d0e-e74bfb67842b_679x358.png)

---

### 4. GEPA 与 GRPO 的工程选型指南

![工程技术选型决策树图示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2947deb4-7e47-4ead-a2f3-d1f9d6cfe724_680x381.png)

- **使用 GEPA**：当你拥有小训练集、高昂采样成本、无法访问模型权重，且评估指标可用自然语言清晰描述时。
- **使用 GRPO**：当你拥有海量廉价采样、开源权重，以及可自动校验的终局奖励时（如代码编译、数学验证）。

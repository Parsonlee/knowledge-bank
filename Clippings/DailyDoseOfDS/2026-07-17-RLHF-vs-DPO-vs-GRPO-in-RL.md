---
title: "RLHF vs. DPO vs. GRPO in RL"
source: "https://mail.google.com/mail/u/0/#inbox/19f721c214ca5038"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-17
created: 2026-07-30
description: "深入解析强化学习微调中 RLHF、DPO 与 GRPO 三种主流算法的原理差异，对比其奖励模型设计、显存占用与梯度更新机制。"
tags:
  - clippings
---

# 大模型 RL 微调三剑客：RLHF vs DPO vs GRPO 深度对比（RLHF vs. DPO vs. GRPO in RL）

在强化学习对齐（RL Alignment）与推理模型训练中，**RLHF**、**DPO** 与 **GRPO** 常被归为同一类算法的变体。然而，它们在奖励建模、显存开销及训练稳定性上存在根本性差异。

![RLHF、DPO 与 GRPO 三种算法架构流程对比图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36114836-0453-49e4-b245-14e80c68b172_2528x1271.jpeg)
*图 1：RLHF、DPO 与 GRPO 架构原理对比*

---

### 三大算法对比与机制拆解

#### 1. RLHF（基于人类反馈的强化学习）
标准 PPO 范式的 RLHF 需要同时维护 4 个模型：Actor 模型、Critic 模型、Reward 模型和 Reference 模型。
* **优点**：能够利用在线采样（Online Sampling）探索新探索路径；
* **缺点**：显存开销极大，训练极为脆弱且超参数极难调优。

#### 2. DPO（直接偏好优化）
DPO 通过数学变换，推导出隐式奖励函数，避开了显式奖励模型与 Critic 模型的训练，将偏好对齐转化为二分类交叉熵损失。
* **优点**：只需训练 Actor 模型，无需采样，显存开销低，训练稳定；
* **缺点**：属于离线算法（Offline Algorithm），无法在训练过程中进行动态自我探索。

#### 3. GRPO（组相对策略优化）
DeepSeek-Math 和 DeepSeek-R1 采用的 GRPO 移除了传统 Critic 价值模型。对于每个输入 Query，策略模型生成一组（Group）回答 $Q = \{o_1, o_2, \dots, o_G\}$，通过组内回答的相对得分计算 Advantage：

$$A_i = rac{r_i - 	ext{mean}(R)}{	ext{std}(R)}$$

* **优点**：大幅节省 Critic 模型占用的显存，保持了在线采样的探索优势，是当前推理模型（Reasoning Models）自我进化训练的首选范式。

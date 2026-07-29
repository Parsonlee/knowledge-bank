title: RLHF vs. DPO vs. GRPO：三大强化学习对齐算法详解 source: https://mail.google.com/mail/u/0/#inbox/19f721c214ca5038 author:

"[[DailyDoseOfDS]]" published: 2026-07-17 created: 2026-07-28 description: 拆解 RLHF（四模型架构）、DPO（隐式偏好优化）与 GRPO（分组相对策略优化）在训练复杂度、数据要求与显存开销上的核心差异。 tags:

clippings

# RLHF vs. DPO vs. GRPO：三大强化学习对齐算法详解

RLHF、DPO 与 GRPO 常被归类为同一种对齐算法的不同变体，但它们在引导模型行为的方式、训练环境搭建以及数据要求上存在本质区别。

## 1. RLHF (Reinforcement Learning from Human Feedback)

机制：通过奖励模型（Reward Model）对 Policy 生成的回复评分，使用 PPO 算法更新策略，并加上 KL 散度惩罚。

架构：需要同时在线运行 4 个模型（待训练 Policy、冻结的 Reference Model、Reward Model、Critic）。

痛点：计算开销巨大，Critic 拟合较慢且容易引入不稳定性。

## 2. DPO (Direct Preference Optimization)

机制：直接利用成对偏好数据（胜者 vs. 败者），通过 Log-Probability 比例在 Policy 内部隐式推导奖励信号。

优势：消除了独立的 Reward Model 与 Critic，只需 Policy 与 Reference 两个模型。

局限：缺乏在线探索（Online Exploration）能力，若偏好数据分布不全面则容易产生脆弱性。

## 3. GRPO (Group Relative Policy Optimization)

机制：由 DeepSeek 于 2024 年提出。为每个 Prompt 生成一组输出，利用组内平均值与标准差计算相对优势（Advantage）。

优势：用组内统计量取代了传统 RLHF 中笨重的 Critic 节点，在保留强化学习在线探索优势的同时大幅降低了显存与计算开销。

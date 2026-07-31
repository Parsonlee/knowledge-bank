---
title: "Training LLM Agents using RL without writing any custom reward"
source: "https://mail.google.com/mail/u/0/#inbox/19cba7e7c4fb570a"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-04
created: 2026-07-30
description: "介绍利用 RULER (from OpenPipe) 规避手动编写自定义奖励函数的方法，通过相对轨迹成对比较与 LLM-as-a-Judge 零显式奖励训练 Agent。"
tags:
  - clippings
---

# 无需编写自定义奖励函数：利用强化学习训练 LLM Agent（Training LLM Agents using RL without writing any custom reward）

使用强化学习（RL）训练 LLM Agent 的最大的瓶颈往往在于**奖励工程（Reward Engineering）**。编写一个稳健、无死角且不被 Agent 找漏洞（Reward Hacking）的奖励函数，通常需要大量的手工规则或标注数据。

OpenPipe 开源的 **RULER** 提供了一种全新的解法：**无需编写任何自定义标量奖励函数，即可利用 RL 训练 Agent。**

![传统奖励函数瓶颈 vs RULER 相对轨迹判定架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38249781-bbde-41e0-9e77-16d7d30b5099_1418x598.png)
*图 1：传统奖励函数瓶颈 vs RULER 相对轨迹判定架构*

---

### 一、 RULER 的核心原理：相对轨迹比较

与其让裁判对单条生成轨迹给出一个绝对的标量分数（绝对评分非常困难且不稳定），不如让 LLM-as-a-Judge 面对同一 Prompt 下的**两条候选轨迹（Trajectories）进行相对成对比较（Pairwise Preference Comparison）**。

事实证明：
1. **相对比较比绝对打分容易得多**。
2. 结合 **GRPO (Group Relative Policy Optimization)** 算法，GRPO 恰好在组内（Group）对优势值（Advantage）进行归一化。因此，只要提供相对偏好次序，即可直接转化为 GRPO 训练所需的梯度信号！

---

### 二、 极简工程落地方案

RULER 的实现极其轻量：

![RULER 开源框架代码调用与评估流程图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6827a19-15c5-4f18-9667-270aeb445cbe_1992x1544.png)
*图 2：RULER 开源框架代码调用与评估流程图解*

- 支持任何 LiteLLM 兼容的模型作为裁判（Judge）。
- 允许添加特定的评审规则（Rubrics）。
- 自动处理组内轨迹两两对比，生成无偏偏好矩阵。

这种范式极大地降低了 Agent 强化学习门槛，让开发者无需繁重的数据标注与奖励函数调试即可快速启动 AgentRL 训练。

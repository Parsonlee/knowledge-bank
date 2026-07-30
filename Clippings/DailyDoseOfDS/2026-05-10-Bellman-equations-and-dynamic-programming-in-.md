---
title: "Bellman equations and dynamic programming in RL."
source: "https://mail.google.com/mail/u/0/#inbox/19e13d76eb927af3"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-10
created: 2026-07-30
description: "强化学习实战课程第 3 部分，深度解析贝尔曼方程（Bellman Equations）与动态规划（Dynamic Programming）的核心原理及代码实现。"
tags:
  - clippings
---

# 强化学习中的贝尔曼方程与动态规划（Bellman equations and dynamic programming in RL.）

我们最近发布了强化学习（Reinforcement Learning, RL）实战课程系列。

第 3 部分现已正式上线！

在前 2 部分中，我们介绍了马尔可夫决策过程（MDP）框架与价值函数（Value Functions）。而第 3 部分将带你深入学习真正计算它们的数学方程与核心算法。

本期涵盖的关键知识点：

- **贝尔曼期望方程（The Bellman expectation equations）**
- **贝尔曼最优方程（The Bellman optimality equations）**
- **建立在其上的动态规划方法**：包括迭代策略评估（Iterative policy evaluation）、策略改进（Policy improvement）、策略迭代（Policy iteration）以及价值迭代（Value iteration），并附带全套从零手写代码实现。

全篇内容从基础概念推导起步，无需预先具备复杂的 RL 背景。

---

### 为什么要关注强化学习？

今天的大多数机器学习从业者对监督学习（Supervised Learning）有着深厚的直觉。

但强化学习运行在一套完全不同的思想体系之上：
- 没有预先标记好的静态数据集；
- Agent 通过与环境交互自行生成训练数据；
- 动作具有延迟的后续影响（Delayed consequences）；
- 探索（Exploration）不是可选步骤，而是学习过程的核心组成部分。

这正是当前 AI 领域复合式突破发生的前沿：
- 推动大语言模型（LLM）取得重大突破的技术（RLHF、GRPO、DPO、Constitutional AI）全都是 RL 的直接应用；
- 每一个能够执行多步动作、调用工具并在长周期内运行的 Agent 系统，本质上都是一个 RL 问题。

在阅读相关论文或博客时，只有真正理解了什么是策略（Policy）、价值函数测量了什么、为什么奖励塑形（Reward shaping）困难重重以及探索机制如何运作，才能真正消化这些前沿技术。本系列课程正是由浅入深构建这一理解基石。

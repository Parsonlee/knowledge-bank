---
title: "Markov decision processes and value functions in RL."
source: "https://mail.google.com/mail/u/0/#inbox/19deeeb458239986"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-03
created: 2026-07-30
description: "系统阐述马尔可夫决策过程（MDP）的五元组定义、马尔可夫性质、价值函数与策略评估，揭示 RL 在大模型 Post-training 中的核心地位。"
tags:
  - clippings
---

# 强化学习中的马尔可夫决策过程与价值函数（Markov decision processes and value functions in RL.）

强化学习（Reinforcement Learning, RL）建立了大模型与智能体行为训练的形式化数学语言。

![MDP 马尔可夫决策过程架构图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feac10488-6a60-4f2f-a4b0-b5b0c28847da_844x588.png)

核心知识框架涵盖：
- **马尔可夫性质（Markov Property）**：未来状态仅取决于当前状态与动作，与历史路径无关，这一性质使得 RL 问题的计算变得易于处理（Tractable）。
- **MDP 五元组**：包含状态空间 $\mathcal{S}$、动作空间 $\mathcal{A}$、状态转移概率 $\mathcal{P}$、奖励函数 $\mathcal{R}$ 以及折扣因子 $\gamma$。
- **片段式（Episodic）与连续性（Continuing）任务**的差异。
- **回报（Returns）与折扣机制（Discounting）**的数值推导。
- **奖励假设（Reward Hypothesis）及其局限性**（例如奖励黑客现象 Reward Hacking）。
- **确定性与随机性策略（Policies）**、状态价值函数 $V(s)$ 与动作价值函数 $Q(s, a)$。

---

### 为什么在当下必须重视 RL？

在过去两年中发布的每一个前沿大语言模型（Frontier LLM），都在其后训练（Post-training）流水线中重度依赖 RL：
- **ChatGPT** 依靠 RLHF（基于人类反馈的强化学习）进行对齐。
- **DeepSeek-R1** 采用 GRPO（组相对策略优化）探索出强大的 Reasoning 推理能力。
- **Claude** 结合 Constitutional AI 与 RL 实现安全与行为控制。

这一发展范式非常明确：**预训练赋予模型知识，而强化学习赋予模型行为（Pre-training gives knowledge, RL gives behavior）。**

![Google Trends 中强化学习检索热度趋势图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde58166a-cecf-479c-97fe-d5d9d78913d1_1549x885.png)

不仅大语言模型如此，具备自主执行动作、调用外部工具并在多步复杂环境中运行的 **Agentic AI 系统**，本质上都是标准的 RL 问题。从机器人学、推荐系统、游戏 AI，到自动驾驶与药物研发，强化学习正是贯穿其中的底层通用主线。

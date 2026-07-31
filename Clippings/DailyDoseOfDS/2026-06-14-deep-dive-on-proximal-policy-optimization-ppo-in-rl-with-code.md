---
title: "Deep dive on proximal policy optimization (PPO) in RL, with code."
source: "https://mail.google.com/mail/u/0/#inbox/19ec7f0bdd27389b"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-14
created: 2026-07-30
description: "深度解析强化学习中的近端策略优化（PPO）算法：原理、信赖域控制、截断代理目标及其在大模型对齐（RLHF）中的应用。"
tags:
  - clippings
---

# 强化学习近端策略优化（PPO）深度解析（Deep dive on proximal policy optimization (PPO) in RL, with code.）

强化学习（Reinforcement Learning）系列课程第 8 部分现已正式推出。

本章深度剖析了 **PPO（Proximal Policy Optimization，近端策略优化）** 算法——该算法为现代大语言模型（LLM）对齐与强化学习奠定了决定性的基石。OpenAI 早期对 ChatGPT 进行人类偏好对齐（RLHF）时，底层核心的强化学习算法正是 PPO。

后续出现的 GRPO、DPO 等每一个主流替代方案，都是直接应对或针对 PPO 的局限性而设计的。

![PPO 算法架构与推导](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d3df8df-a431-4346-b758-ef668c61fbd4_1200x670.png)

### 核心涵盖主题

* **策略崩溃风险**：为什么过大的策略更新（Policy Updates）会导致不可逆的性能崩溃；
* **信赖域保护机制**：信赖域（Trust Regions）如何限制参数更新步长，保障更新安全性；
* **截断代理目标**：截断代理目标（Clipped Surrogate Objective）的数学设计与几何直观；
* **PPO 完整算法**：PPO 完整优化流程的演进逻辑与伪代码；
* **KL 散度惩罚变体**：大语言模型对齐（如 RLHF）中使用的 KL 散度惩罚（KL-penalty）变体；
* **实用训练诊断**：识别不健康训练过程（Unhealthy Training Runs）的实用诊断指标；
* **从零代码实现**：基于 PyTorch 和 LunarLander 环境的从零实现代码；
* **与 RLHF 的连接**：PPO 如何直接连接并应用于大语言模型的人类偏好对齐。

全篇从零基础开始拆解推导，无需深厚的 RL 前置经验。

![PPO 与大语言模型对齐（RLHF）演进逻辑](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88c192b7-c85b-45ee-8349-ffcf686cd876_1200x651.png)

### 为什么必须掌握 PPO？

PPO 是开启当前大语言模型对齐时代的基石算法。

当 OpenAI 最初将语言模型与人类偏好对齐时，底层选用的 RL 算法就是 PPO。此后诞生的每一个主流替代算法，都以 PPO 作为直接的参照物与改进靶心：

* **DPO (Direct Preference Optimization)**：专门为了规避运行 PPO 复杂的强化学习采样循环和高昂显存开销而设计；
* **GRPO (Group Relative Policy Optimization)**：修改了优势估计（Advantage Estimation）逻辑，从而省去了额外训练 Critic 评估网络的需要；
* **Constitutional AI**：重构了奖励信号生成机制，但底层优化器依然保留了信赖域优化思想。

如果不深刻理解 PPO 这个所有方法争相回应的原点算法，就无法真正透彻掌握现代 LLM 对齐技术栈。

此外，在语言模型之外，PPO 至今依然是机器人学（Robotics）、游戏 AI 以及智能体系统（Agentic Systems）中最主流、最通用且极具鲁棒性的 Reinforcement Learning 算法。它之所以能长期保持主导地位，是因为其足够简洁（仅需几百行 PyTorch 代码即可实现），同时具备应对极广泛复杂场景的稳定性。

本章也是强化学习系列教程的核心汇聚点，将价值函数、策略梯度、Actor-Critic 与 GAE（Generalized Advantage Estimation）有机融为一体。

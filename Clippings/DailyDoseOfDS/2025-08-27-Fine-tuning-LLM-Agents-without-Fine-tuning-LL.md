---
title: "无需微调 LLM，也能让 LLM Agent 学习"
source: "https://mail.google.com/mail/u/0/#inbox/198ed2e36353fdf7"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-27
created: 2026-07-30
description: "介绍 Memento：它不更新 LLM 权重，而是以记忆从经验中学习，并将持续学习表述为记忆增强马尔可夫决策过程上的在线强化学习。"
tags:
  - clippings
---

# 无需微调 LLM，也能让 LLM Agent 学习

Memento 的目标是让 AI Agent 从经验中提升表现，同时不触碰模型权重。这类似于人类记住过去经历，并从中学习。

其核心思路是：

- 不更新 LLM 权重，而是通过记忆从经验中学习；
- 将持续学习重新表述为一个记忆增强马尔可夫决策过程（MDP）上的、基于记忆的在线强化学习；
- 可以把它理解成给 Agent 一本笔记本，记录哪些做法成功、哪些失败。

系统分为两个关键组件：

## 1. 基于案例的推理（Case-Based Reasoning，CBR）

CBR 会把复杂任务拆解为子任务，并检索相关的既有经验。这里不需要梯度更新，而是依靠智能的记忆检索。

## 2. 执行器（Executor）

执行器通过 MCP 工具执行每个子任务，并把结果记录到记忆中，以便日后使用。邮件称，借助 MCP，执行器可完成多数真实世界任务，并可访问以下工具：

- 网络研究；
- 文档处理；
- 安全的 Python 执行；
- 数据分析；
- 媒体处理。

作者将此视为构建类人 Agent 的一条有前景路径，并表示会持续跟进，未来分享实战演示。

项目链接： [Memento GitHub 仓库](https://github.com/Agent-on-the-Fly/Memento)。

## 广告 / 推广

邮件推广 Daily Dose of Data Science 的会员资源，并包含面向超过 75 万 AI 从业者的广告投放招揽；这些内容不属于 Memento 的技术介绍。

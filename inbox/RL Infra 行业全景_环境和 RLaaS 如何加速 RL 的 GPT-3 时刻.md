---
title: "RL Infra 行业全景：环境和 RLaaS 如何加速 RL 的 GPT-3 时刻"
source: https://mp.weixin.qq.com/s/-5lMX9oVHn6x0NI6QEZrrA?scene=1
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# RL Infra 行业全景：环境和 RLaaS 如何加速 RL 的 GPT-3 时刻

> [!quote]
> Mechanize 提出了复制训练（Replication Training）的新范式。它的核心思想是：让 AI Agent 去完整复现现有软件产品或其中的特定功能，并以此作为训练任务。任务成功与否，可以通过自动化的方式进行验证，例如 agent 生成的代码是否通过了原始仓库的所有单元测试。这种方法巧妙地将一个开放、模糊的创造性任务，转化为了一个有明确、可验证奖励信号的 RL 问题，从而解决了为长周期、复杂任务设计奖励函数的难题。
> 这个思路利用了人类已经开发的大量软件作为蓝本，可以源源不断生成训练任务，就像预训练用互联网语料一样丰富。软件在互联网中比比皆是，AI可以通过复制这些软件来积累能力。这使扩展RL环境规模成为可能。
> 虽然“逐字复刻”一个程序听起来不是常见的工程目标，但这是现在头部 AI Lab 明确需要的，可以有实验环境供 AI Agent 作为 playground。同时这种任务锻炼了AI一系列核心技能：精确阅读并理解长规格说明、严格 instruction following 不犯错、发现并纠正自身早期步骤中的错误、在长达数万行代码的项目中保持连贯。

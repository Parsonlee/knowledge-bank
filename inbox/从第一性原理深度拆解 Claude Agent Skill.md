---
title: "从第一性原理深度拆解 Claude Agent Skill"
source: https://baoyu.io/translations/claude-skills-deep-dive
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# 从第一性原理深度拆解 Claude Agent Skill

> [!quote]
> 工具做了一件事，返回了一个结果，交互就结束了。技能的运作方式根本不同。技能不是执行离散动作并返回结果，而是注入全面的指令集，修改 Claude 对任务的推理和处理方式。这创造了一个普通工具从未面临的设计挑战：用户需要了解哪些技能正在运行以及它们在做什么的透明度，而 Claude 需要详细的、可能非常冗长的指令来正确执行技能。

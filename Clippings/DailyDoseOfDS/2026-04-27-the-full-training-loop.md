---
title: "完整的训练循环（The full training loop）"
source: "https://mail.google.com/mail/u/0/#inbox/19dd11ff55feb3f6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-27
created: 2026-07-30
description: "解释了结合 RULER 评分和 GRPO 算法的完整训练循环，使模型自动改进以遵循提示词。"
tags:
  - clippings
---

# 完整的训练循环（The full training loop）

为了利用这些分数进行实际训练，需要用真实的模型推理替换硬编码的响应。ART 的 `gather_trajectory_groups` 处理这一编排。

在每一个步骤中：
- 模型使用当前权重为每个场景生成多个响应（轨迹）。
- RULER 对它们进行相对排名评分。
- GRPO 强化高分行为，抑制低分行为。

随着迭代，模型越来越擅长遵循系统提示词。模型会学到获得高分的模式（如忠实度、简洁性）并消除低分模式（如幻觉、无视上下文）。整个过程中无需定义任何硬编码的奖励函数代码。

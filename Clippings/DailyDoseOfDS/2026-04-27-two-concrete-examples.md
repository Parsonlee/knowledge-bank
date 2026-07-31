---
title: "两个具体示例（Two concrete examples）"
source: "https://mail.google.com/mail/u/0/#inbox/19dd11ff55feb3f6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-27
created: 2026-07-30
description: "展示了使用 RULER 的底层 API 获取相对评分和高层 API 处理训练对象的两个具体 RAG 示例。"
tags:
  - clippings
---

# 两个具体示例（Two concrete examples）

RULER 提供了两层 API：

1. 底层 `ruler` 函数：直接处理简单的消息字典。在 RAG 示例中，通过系统提示词，裁判 LLM 会为不同回答给出相对分数。正确的生成得分最高，部分正确（包含幻觉）的得分居中，无视上下文的得分最低。GRPO 利用这种平滑的梯度分数进行训练。
2. 高层 `ruler_score_group` 函数：处理真实的 `Trajectory` 和 `TrajectoryGroup` 对象，这正是 `model.train()` 所需要的结构。裁判甚至能识别出回答过于啰嗦等细微的质量问题，并且能自动适应系统提示词的严格程度变化。

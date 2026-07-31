---
title: "轨迹与分组（Trajectories and Groups）"
source: "https://mail.google.com/mail/u/0/#inbox/19dd11ff55feb3f6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-27
created: 2026-07-30
description: "介绍了 ART 框架中轨迹和轨迹组的概念，它们是 GRPO 训练和 RULER 评分的基础。"
tags:
  - clippings
---

# 轨迹与分组（Trajectories and Groups）

ART 框架将每个代理响应表示为一个轨迹 (Trajectory)。它是一个消息序列（系统、用户、助手），并封装了 GRPO 训练所需的元数据。

针对同一场景的多个轨迹形成一个轨迹组 (TrajectoryGroup)。这是 RULER 评分和 GRPO 训练的基本单元。

- 在 `ruler_score_group` 返回后，每个轨迹的奖励字段会更新为裁判的评分。
- Choice 和 ChatCompletionMessage 对象是 OpenAI 的标准类型。

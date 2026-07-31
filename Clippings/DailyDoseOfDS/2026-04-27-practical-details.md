---
title: "实践细节（Practical details）"
source: "https://mail.google.com/mail/u/0/#inbox/19dd11ff55feb3f6"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-27
created: 2026-07-30
description: "分享了使用 RULER 的实用技巧，包括模型选择、轨迹组大小建议以及上下文去重缓存机制。"
tags:
  - clippings
---

# 实践细节（Practical details）

以下是基于使用 RULER 收集的一些实践经验：
- 不需要最昂贵的模型作为裁判，更便宜的模型（如 Qwen3 32B）通常表现良好。这是一个成本与质量的权衡。
- 建议每组使用 4 到 8 个轨迹，太少不利于比较，太多则增加成本且容易使裁判困惑。
- 当同组内的所有轨迹共享相同的系统提示词和用户消息时，RULER 会自动去除重复的前缀，从而显著降低 Token 消耗。
- RULER 会将裁判的响应缓存到磁盘。如果在调试时重新运行相同的轨迹，它不会再次调用 API。

总结来说，将 RL 应用于代理的瓶颈一直都是奖励信号，而 RULER 使得 LLM 裁判可以通过相对评分解决非验证性任务的奖励问题。

---
title: "用可视化理解 LLM 中的 KV 缓存"
source: "https://mail.google.com/mail/u/0/#inbox/197c270c599ab371"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-30
created: 2026-07-30
description: "通过一项推理演示说明 KV 缓存可加速 LLM 推理：启用缓存为 9 秒，未启用为 40 秒。"
tags:
  - clippings
---

# 用可视化理解 LLM 中的 KV 缓存

KV 缓存是用于加速 LLM 推理的一种常见技术。

邮件给出了一项演示中的速度对比：

- 使用 KV 缓存：**9 秒**；
- 不使用 KV 缓存：**40 秒**，约慢 **4.5 倍**；随着生成的 token 增多，差距还会继续扩大。

邮件通过可视化图示解释其工作方式，并链接到一篇更详细的介绍文章。

- [阅读 KV 缓存的详细说明](https://www.dailydoseofds.com/p/kv-caching-in-llms-explained-visually/)

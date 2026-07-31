---
title: "[实战] 使用 DeepSeek Janus 构建多模态 RAG（[Hands-on] Multimodal RAG with DeepSeek Janus.）"
source: "https://mail.google.com/mail/u/0/#inbox/196ac3a283f20357"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-05-07
created: 2026-07-30
description: "在 DeepSeek-R1 之后，DeepSeek 推出了一系列开源多模态模型（如 Janus-Pro），并在图像理解和生成测试中表现优异，文中展示了在其之上构建复杂多模态 RAG 的实战演示。"
tags:
  - clippings
---

# [实战] 使用 DeepSeek Janus 构建多模态 RAG（[Hands-on] Multimodal RAG with DeepSeek Janus.）

在推出 DeepSeek-R1 之后，DeepSeek 还发布了更多开源的多模态模型——Janus、Janus-Pro 以及 Janus-Flow。

它们不仅能够理解图像，还能根据文本输入生成图像。

此外，在 GenEval 和 DPG-Bench 的基准测试中，它们击败了 OpenAI 的 DALL-E 3 以及 Stable Diffusion。

最近，我们进行了一项实战演示，利用 Janus-Pro 针对复杂文档构建了一个多模态 RAG（检索增强生成）系统。

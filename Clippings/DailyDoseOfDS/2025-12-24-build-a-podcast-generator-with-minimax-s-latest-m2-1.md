---
title: "使用 MiniMax 最新 M2.1 构建播客生成器（Build a podcast generator with MiniMax’s latest M2.1.）"
source: "https://mail.google.com/mail/u/0/#inbox/19b522575aa6f7ef"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-24
created: 2026-07-30
description: "MiniMax 发布了高性价比的 M2.1 模型，本文介绍了如何利用它、Firecrawl 和 Speech 2.6 将网页内容自动生成多说话人的播客。"
tags:
  - clippings
---

# 使用 MiniMax 最新 M2.1 构建播客生成器（Build a podcast generator with MiniMax’s latest M2.1.）

MiniMax 刚刚发布了 M2.1，开发者称之为“成本只需 10% 的 Claude”。

* 72.5% SWE-Multilingual 准确率。击败了 Sonnet 4.5
* 88.6% VIBE-bench 得分。击败了 Gemini 3 Pro

我们使用它构建了一个 AI 工作室，能够将任何网站转换成播客，并在视频中详细介绍了这一过程：

它的工作原理如下：

* 你提供一个网站 URL
* Firecrawl 抓取网页内容
* MiniMax M2.1 对其进行优化并生成播客脚本
* Speech 2.6 将其转化为多说话人的播客

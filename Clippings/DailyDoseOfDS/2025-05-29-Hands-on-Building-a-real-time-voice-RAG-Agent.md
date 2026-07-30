---
title: "实战：构建实时语音 RAG 智能体"
source: "https://mail.google.com/mail/u/0/#inbox/1971dcca96aa74c3"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-05-29
created: 2026-07-30
description: "介绍一个开源实时语音 RAG 智能体：监听音频、使用 AssemblyAI 转写、通过 LlamaIndex 基于文档生成回答，再把回答朗读出来。"
tags:
  - clippings
---

# 实战：构建实时语音 RAG 智能体

与 AI 应用交互时，持续打字可能既繁琐又无趣；原文认为实时语音交互会越来越普及，并展示了一个实时语音 RAG 智能体的构建过程。

该应用的工作流程为：

1. 监听实时音频；
2. 通过 AssemblyAI 将音频转写为文本；
3. 通过 LlamaIndex 使用用户文档生成回答；
4. 将回答再以语音方式说出来。

原文提供了完整的视频演示，用于讲解配置和代码，并说明全部代码均已开源，可在其 GitHub 仓库中获取。

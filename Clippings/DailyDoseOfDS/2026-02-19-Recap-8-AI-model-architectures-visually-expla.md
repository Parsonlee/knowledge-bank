---
title: "[Recap] 8 AI model architectures, visually explained!"
source: "https://mail.google.com/mail/u/0/#inbox/19c7821062a6ceb4"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-02-19
created: 2026-07-30
description: "速览 8 种主流 AI 模型架构：LLM、LCM、LAM、MoE、VLM、SLM、MLM 以及 SAM 的核心概念与典型代表。"
tags:
  - clippings
---
# 【回顾】图解 8 种 AI 模型架构（[Recap] 8 AI model architectures, visually explained!）

大家都在谈论 LLM，但实际上有一整套专业化模型家族在各自领域发挥着巨大作用。

以下是 8 种核心架构的快速梳理：

1. **LLM（大语言模型 Large Language Models）**：文本输入 $\rightarrow$ Token化为 Embedding $\rightarrow$ Transformer 处理 $\rightarrow$ 文本输出。
   * 代表：ChatGPT, Claude, Gemini, Llama。

2. **LCM（大概念模型 Large Concept Models）**：在概念级别而非 Token 级别运行。输入被分段为句子，通过 SONAR 嵌入，再经过扩散（Diffusion）过程生成输出。
   * 代表：Meta 率先提出的 LCM。

3. **LAM（大行动模型 Large Action Models）**：将意图转化为行动。输入经过感知、意图识别、任务拆解，再结合记忆进行行动规划与执行。
   * 代表：Rabbit R1, Microsoft UFO, Claude Computer Use。

4. **MoE（混合专家模型 Mixture of Experts）**：由路由（Router）决定哪些专业“专家”处理请求。仅激活相关专家，结果汇总后输出。
   * 代表：Mixtral, GPT-4, DeepSeek。

5. **VLM（视觉-语言模型 Vision-Language Models）**：图像通过视觉编码器，文本通过文本编码器。两者在多模态处理器中融合，由语言模型生成输出。
   * 代表：GPT-4V, Gemini Pro Vision, LLaVA。

6. **SLM（小语言模型 Small Language Models）**：针对边缘设备优化的语言模型。采用紧凑 Token 化、高效 Transformer 与量化技术。
   * 代表：Phi-3, Gemma, Mistral 7B, Llama 3.2 1B。

7. **MLM（掩码语言模型 Masked Language Models）**：Token 被掩码盖住，转为嵌入后进行双向上下文处理预测被遮挡词。
   * 代表：BERT, RoBERTa, DeBERTa，广泛用于搜索与情感分析。

8. **SAM（Segment Anything 模型）**：提示词和图像分别通过独立编码器输入掩码解码器，生成像素级分割。
   * 代表：Meta SAM，广泛用于照片编辑、医学图像与自动驾驶。

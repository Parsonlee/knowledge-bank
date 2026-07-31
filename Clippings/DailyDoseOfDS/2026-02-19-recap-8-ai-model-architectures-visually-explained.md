---
title: "8 AI model architectures, visually explained"
source: "https://mail.google.com/mail/u/0/#inbox/19c7821062a6ceb4"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-02-19
created: 2026-07-30
description: "图解直观对比 8 种前沿 AI 模型架构（LLM、LCM、LAM、MoE、VLM、SLM、MLM、SAM），剖析各自的输入表示与核心工作流。"
tags:
  - clippings
---

# 8 种 AI 模型架构直观图解！（8 AI model architectures, visually explained）

每个人都在讨论 LLM，但在 AI 家族中还有整整一系列专门化的模型架构在发挥着惊人的作用。

下图对这 8 种核心模型架构进行了速览与总结：

![8 种 AI 模型架构图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faac26608-a354-47e8-b347-b8ede9676f7c_960x949.gif)

---

### 8 种架构详细速览

1. **LLM（大语言模型, Large Language Models）**：
   * 输入文本被 Token 化转化为 Embedding，经过 Transformer 架构处理，最终输出文本。
   * 代表模型：ChatGPT、Claude、Gemini、Llama。

2. **LCM（大概念模型, Large Concept Models）**：
   * 工作在“概念”层级而非简单的 Token 层级。输入分割为句子，通过 SONAR 嵌入后结合扩散过程输出。
   * 代表模型：Meta LCM 开创了这一技术方向。

3. **LAM（大行动模型, Large Action Models）**：
   * 将人类意图转化为实际行动。输入流经感知、意图识别、任务拆解、带记忆的行动规划，最后执行操作。
   * 代表模型：Rabbit R1、Microsoft UFO、Claude Computer Use。

4. **MoE（混合专家模型, Mixture of Experts）**：
   * 由路由（Router）决定哪些专长“专家”处理查询。仅激活相关专家，结果汇总后进行输出。
   * 代表模型：Mixtral、GPT-4、DeepSeek。

5. **VLM（视觉-语言模型, Vision-Language Models）**：
   * 图像通过视觉编码器，文本通过文本编码器，两者在多模态处理器中融合，随后由语言模型生成结果。
   * 代表模型：GPT-4V、Gemini Pro Vision、LLaVA。

6. **SLM（小语言模型, Small Language Models）**：
   * 专为边缘设备优化的 LLM。具备紧凑 Token 化、高效 Transformer 与量化技术，适合本地部署。
   * 代表模型：Phi-3、Gemma、Mistral 7B、Llama 3.2 1B。

7. **MLM（掩码语言模型, Masked Language Models）**：
   * Token 被遮蔽掩码，双向处理上下文以预测被隐藏的词汇。
   * 代表模型：BERT、RoBERTa、DeBERTa，广泛驱动搜索与情感分析。

8. **SAM（分割一切模型, Segment Anything Models）**：
   * 提示词和图像分别通过编码器，喂入掩码解码器生成像素级精确分割。
   * 代表模型：Meta SAM，广泛应用于照片编辑、医学影像与自动驾驶。

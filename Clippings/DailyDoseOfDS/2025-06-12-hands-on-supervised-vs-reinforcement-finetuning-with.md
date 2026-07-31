---
title: "实战：监督微调与强化微调（含代码）"
source: "https://mail.google.com/mail/u/0/#inbox/197658945bda228b"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-12
created: 2026-07-30
description: "对比监督微调（SFT）与强化微调（RFT）：前者基于静态指令—回复标注数据，后者利用在线奖励、输出探索与 GRPO 学习高奖励回答。"
tags:
  - clippings
---

# 实战：监督微调与强化微调（含代码）

[强化微调（RFT）](https://www.dailydoseofds.com/p/hands-on-building-your-reasoning-llm/)可以把任意开源 LLM 转变为强大的推理模型，并且不需要标注数据。邮件列出它与监督微调的主要差异。

## 监督微调（SFT）

- 从静态的、由指令—回复对组成的标注数据集开始；
- 调整模型权重以匹配这些回复；
- 部署表现最佳的 LoRA checkpoint 进行推理。

## 强化微调（RFT）

- 使用在线奖励方法，因此不需要任何静态标签；
- 模型探索不同输出，由奖励函数对其评分；
- 随时间推移，模型使用 GRPO 学习生成奖励更高的答案。

邮件的表述是：SFT 使用静态数据，且经常记忆答案；RFT 是在线方式，从奖励中学习并探索新策略。模型训练完成后，可以将它部署到推理服务器。

作者在[另一封通讯](https://www.dailydoseofds.com/p/hands-on-building-your-reasoning-llm/)中使用 Predibase 进行强化微调，并以 `Qwen-2.5:7b` 为基础模型，构建了自己的推理 LLM。

作者最后询问读者：对于 LLM 微调，RFT 是否比 SFT 是更好的策略？

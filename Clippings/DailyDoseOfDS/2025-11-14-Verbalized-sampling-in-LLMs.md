---
title: "Verbalized sampling in LLMs."
source: "https://mail.google.com/mail/u/0/#inbox/19a841a055b8cd28"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-11-14
created: 2026-07-30
description: "解析大语言模型语言化采样（Verbalized Sampling）技术，有效缓解 RLHF 后的模式崩溃并提升输出多样性。"
tags:
  - clippings
---

# 大语言模型中的语言化采样技术（Verbalized sampling in LLMs.）

后训练对齐技术（Post-training alignment methods，如 RLHF、DPO 等）旨在提升大语言模型（LLM）的有用性与安全性。然而，这些对齐方法会带来一个极大的副效应：**显著降低模型输出的多样性（即模式崩溃/Mode Collapse）**。

![RLHF 对齐导致的模式崩溃现象示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8881e9fe-aecc-4e6d-99c3-73c9f5f1cda8_1572x844.png)

![使用 RLHF 训练后的模型输出偏好狭窄分布](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c3dcd7f-a4ec-4072-b088-a74b74e62ef2_3141x1088.png)

### 模式崩溃的根源

在 RLHF 阶段，标注员对模型的不同回答进行评分与排序，随后模型根据人类偏好建立奖励机制进行强化学习。这一机制会导致模型迅速退化集中到满足平均喜好的狭窄回答范畴内，即使将 Sampling Temperature 调高，生成的文本也只是微小词汇的变化，缺乏思想和方案维度的真正多样性。

![Verbalized Sampling 核心 Prompt 引导机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0fa0ff3-09a9-4afe-a3af-734328f2fb00_998x319.png)

![Prompt 作为心智开关激活不同模式路径](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4fbb743-edba-4858-98c7-e3ef6f9ef301_933x477.png)

### 什么是语言化采样（Verbalized Sampling）？

语言化采样的核心理念是：**Prompt 本身就像一个“心智开关（Mental Switch）”**。

当直接要求模型“提供一个解答”时，它倾向于走收敛的旧路；但当你在 Prompt 中显式要求模型“请列出 N 个截然不同、角度各异的可能解决方案或候选选项”时，模型自身在语言输出中预先展开的多样性视角便激活了潜在的多模式分布。

![语言化采样提升输出多样性 1.6-2.1 倍对比图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff567bb0b-54d3-4672-8156-6ba80833338d_980x733.png)

实测表明，语言化采样能够将模型输出的多样性提升 1.6 至 2.1 倍，同时依然保持甚至进一步增强解答的高质量与准确度。

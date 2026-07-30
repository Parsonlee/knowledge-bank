---
title: "[RECAP] 7 LLM generation parameters."
source: "https://mail.google.com/mail/u/0/#inbox/19ec7f0bdd27389b"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-14
created: 2026-07-30
description: "重温大语言模型生成控制的关键 7 大参数：Max tokens、Temperature、Top-k、Top-p、Frequency penalty、Presence penalty 与 Stop sequences。"
tags:
  - clippings
---

# [重温] 大语言模型生成的 7 大核心参数（[RECAP] 7 LLM generation parameters.）

大语言模型的每一次文本生成，底层都受到一套关键参数的严密调控。

深入理解并熟练调优这些参数，是控制大模型输出确定性、多样性与格式规范的前提条件。以下是影响生成效果最关键的 7 个核心杠杆：

### 1) Max tokens（最大 Token 限制）

* 限制模型单次响应中能够生成的 Token 数量硬性上限；
* 设置过低会导致输出被中途截断；设置过高则可能在异常情况下浪费算力和推理成本。

![Max tokens 参数示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1b0886c-470c-4009-958e-be3856f63c9d_890x156.gif)

### 2) Temperature（采样温度）

* 控制生成过程的随机程度。极低温度（~0）使模型输出趋向确定性（仅选择概率最高的 Token）；
* 较高温度（0.7–1.0）能够显著提升输出的创造性与多样性，但同时也引入了更多的噪声；
* 应用场景：问答/客服等任务宜降低 Temperature，创意写作/头脑风暴任务宜提高 Temperature。

![Temperature 参数示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8c6e298-d4c5-4a39-b844-45d14ef7e13c_890x172.gif)

### 3) Top-k 采样

* 默认生成方式按所有 Token 的概率分布进行采样；Top-k 参数将采样范围严格限制在概率最高的前 $k$ 个候选 Token 中；
* 例如：$k=5$ 时，模型在每一步采样时仅从概率排名前 5 的 Token 中进行选择；
* 能够显著提高生成的聚焦度，但 $k$ 值过小可能引发重复或僵硬的回复。

![Top-k 参数示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2de42ee9-8f69-4efa-a4f8-78f5c507326c_890x172.gif)

### 4) Top-p 采样（Nucleus Sampling / 核采样）

* 与固定候选数量的 Top-k 不同，Top-p 按照累积概率质量进行动态截断；
* 例如：$\text{top\_p}=0.9$ 表示仅保留累积概率达到 90% 的最小 Token 集合进行采样；
* 相比 Top-k 更具自适应性，能在保证连贯性的同时灵活维持生成的多样性。

![Top-p 核采样参数示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8daaad1-f582-4a86-ba4e-ab91f6ae8773_890x172.gif)

### 5) Frequency penalty（频率惩罚）

* 根据 Token 在已生成文本中出现的频率降低其再次被选择的概率；
* 正值能够有效防止模型产生无意义的字词重复，负值则会放大重复倾向；
* 在长文总结（避免车轱辘话）或诗歌创作中具有重要调优价值。

![Frequency penalty 参数示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a903393-cb94-47a8-a604-d6f79a64341f_890x152.gif)

### 6) Presence penalty（存在惩罚）

* 只要某个 Token 在已生成文本中出现过（无论出现几次），就对其施加定额惩罚；
* 较高数值能够鼓励模型引入未曾出现的新概念和词汇，推动生成内容的新颖度；
* 适用于需要丰富灵感和探索新话题的生成场景。

![Presence penalty 参数示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F758936be-8183-4598-aed3-ad5195450310_890x152.gif)

### 7) Stop sequences（停止序列）

* 指定一组自定义字符或 Token，模型一旦生成该序列即刻强制终止生成；
* 在 JSON 等结构化数据输出场景中至关重要，防止模型输出额外的解释性废话；
* 可以在无需复杂 Prompt 工程的前提下确保输出边界干净利落。

![Stop sequences 停止序列示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85ba8849-3eda-4328-aee4-52bf1dc73509_890x152.gif)

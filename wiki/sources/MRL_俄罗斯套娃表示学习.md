---
type: source
tags:
  - RAG/embedding
summary: "Matryoshka Representation Learning (MRL) 俄罗斯套娃嵌入——在同一高维向量中嵌套学习多粒度低维表征，允许截断嵌入维度而保留语义"
sources:
  - title: "OpenAI新模型用的嵌入技术-俄罗斯套娃表示学习"
    url: https://mp.weixin.qq.com/s/h9K06h5YcRXXKCjhzOArBA
    cubox_id: "7153731518270016757"
created: 2026-06-26
updated: 2026-06-26
confidence: high
---

# MRL_俄罗斯套娃表示学习

## 用户高亮 [重点/高亮]

> MRL 通过以嵌套方式对 O(log(d)) 低维向量进行显式优化在同一个高维向量中学习不同容量的表征，因此被称为 Matryoshka「俄罗斯套娃」。

## 背景

OpenAI 推出 text-embedding-3-small 和 text-embedding-3-large 两个新嵌入模型，支持通过 `dimensions` API 参数截断嵌入维度而不丢失概念表征属性。该技术被网友扒出与 2022 年 5 月论文 Matryoshka Representation Learning 方法相同。

## 核心内容

### 论文信息

- 标题：Matryoshka Representation Learning
- 链接：https://arxiv.org/pdf/2205.13147.pdf
- 一作：Aditya Kusupati

### MRL 核心思想

- 以嵌套方式对 O(log(d)) 低维向量进行显式优化，在同一个高维向量中学习不同容量的表征
- Matryoshka 表征的第一个 m-dimensions（m∈[d]）是一个信息丰富的低维向量，精确度不亚于独立训练的 m 维表征
- 信息量随维度增加而增加，形成从粗到细的表征

### 关键效果

- **分类**：使用自适应级联 + MRL 的可变大小表征，ImageNet-1K 上精度与基线相同时表征大小最多可缩小 14 倍
- **检索**：自适应检索中，使用查询嵌入的前几个 dimensions 筛选候选，再用更多 dimensions 重排序；可实现 128 倍理论加速（FLOPS）和 14 倍墙上时钟加速，检索精度与单次检索相当
- **长尾持续学习**：准确率最多可提高 2%，因为 MRL 在不同 dimensions 之间共享更多语义信息

### OpenAI 应用

- text-embedding-3-large 可缩短为 256 维，性能仍优于未缩短的 text-embedding-ada-002（1536 维）
- 在 MTEB 基准上验证
- MRL 一作确认 OpenAI 在 v3 嵌入 API 中默认使用 MRL 用于检索和 RAG

## 关联

- 相关概念：[[概念_Matryoshka表示学习]]、[[概念_Embedding与向量检索]]
- 来源文章：机器之心转载 MLNLP 社区

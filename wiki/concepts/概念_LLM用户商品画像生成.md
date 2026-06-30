---
title: "概念_LLM用户商品画像生成"
tags: [Recommendation]
confidence: high
---

# LLM 用户商品画像生成

[[实体_RLMRec]] 中利用 LLM 为用户和商品生成高质量文本画像的无偏流程，为互信息对齐提供文本侧信号。

## 画像目标

- 用户画像：体现该用户喜欢什么类别商品
- 商品画像：体现该商品会吸引什么样的用户群体

## Item-to-User 生成流程

先商品后用户，顺序生成以确保用户画像可利用商品画像信息。

### 商品画像生成（Item Profile Generation）
- 情况1：数据集有原始商品描述（如 Amazon-book）→ 直接用原始描述构建 Prompts
- 情况2：有属性标签和用户反馈（如 Yelp）→ 用标签+反馈构建 Prompts

### 用户画像生成（User Profile Generation）
- 基于用户购买过的商品+对商品的反馈构建 Prompts
- 配合已生成的商品画像，提供充分直接的信息

## 工程特点

- 每个用户/商品独立生成，可并行处理，提高效率
- 使用思维链（CoT）风格构建 Instruction，引导 LLM 给出理由，提高画像质量
- 完成后为用户-物品交互图每个节点提供高质量文本描述，构建 Text-attributed Graph (TAG)

## 文本编码

- 用文本编码器（Embedder）将画像文本转为特征表示
- 越优异的文本编码器对后续算法性能帮助越大
- 原论文使用 OpenAI text-embedding-ada-002

## 来源

- [[RLMRec_港大百度LLM推荐算法]]

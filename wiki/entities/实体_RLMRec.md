---
title: "实体_RLMRec"
tags: [Recommendation]
confidence: high
---

# RLMRec

港大联合百度推出的模型无关 LLM 推荐框架，通过互信息最大化对齐协同过滤表示与语义表示实现去噪增强。

## 基本信息

- 论文：arxiv:2310.15950
- 代码：github.com/HKUDS/RLMRec
- 团队：香港大学数据智能实验室（HKU-DS）联合百度研究院
- 已落地公司搜索业务

## 核心组件

1. **LLM 画像生成**：Item-to-User 流水线，CoT 风格指令
2. **文本编码**：OpenAI text-embedding-ada-002
3. **两种对齐范式**：
   - RLMRec-Con：双向对比式对齐，抗噪最强
   - RLMRec-Gen：生成式对齐（Mask-autoencoding），预训练场景泛化更好

## 实验性能

- 数据集：Amazon-book / Yelp / Steam
- 基线：GCCF / LightGCN / SGL / SimGCL / DCCF / AutoCF
- 与所有基线组合均取得显著提升

## 理论框架

详见 [[概念_互信息最大化去噪表征]]、[[概念_LLM用户商品画像生成]]

## 来源

- [[RLMRec_港大百度LLM推荐算法]]

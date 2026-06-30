---
title: "RLMRec：港大百度 LLM 推荐算法"
source_url: ""
author: "PaperWeekly"
date_published: ""
confidence: high
tags:
  - Recommendation
  - LLM/arch
  - RAG/embedding
---

# RLMRec：港大百度 LLM 推荐算法

> 港大联合百度提出 RLMRec，通过互信息最大化对齐协同过滤表示与 LLM 语义表示，实现对交互图噪声的去噪增强。

## Key Points

- **论文信息**：arxiv:2310.15950，港大联合百度研究院，已部署于公司搜索业务。

- **核心问题**：协同过滤（CF）从用户-物品交互图中学习的表示含有大量噪声（稀疏交互、长尾用户），单纯依赖行为信号导致推荐质量受限。

- **核心思路**：用 LLM 生成的文本语义表示作为"干净信号"，通过**互信息最大化**与 CF 侧表示对齐，将语义知识注入协同过滤，实现去噪。

- **关键组件**

  1. **LLM Profile 生成**
     - Item-to-User 流水线：先为物品生成描述，再聚合为用户画像。
     - CoT 风格指令：引导 LLM 逐步推理用户偏好，生成结构化文本 profile。
     - 并行生成以降低延迟。

  2. **文本编码**
     - 使用 OpenAI `text-embedding-ada-002` 将 profile 文本编码为稠密向量。
     - 消融实验表明：文本编码器质量与最终推荐性能正相关。

  3. **两种对齐范式**
     - **RLMRec-Con（对比对齐）**：双向对比学习，拉近 CF 表示与语义表示，推远负样本；抗噪能力最强。
     - **RLMRec-Gen（生成对齐）**：掩码自编码，单向从 CF 表示重建文本语义表示；预训练场景下更能避免过拟合。

- **模型无关框架**：可即插即用地接入任意基于 CF 的推荐模型（GCCF / LightGCN / SGL / SimGCL / DCCF / AutoCF），无需修改原始模型结构。

- **实验结果**
  - 数据集：Amazon-Book、Yelp、Steam。
  - 基线：GCCF、LightGCN、SGL、SimGCL、DCCF、AutoCF。
  - RLMRec 在所有数据集和基线上均取得显著提升。

- **消融与分析**
  - 更强的文本编码器 → 更好的推荐性能（编码器质量是瓶颈）。
  - 噪声实验：RLMRec-Con 对交互噪声的抵抗力最强。
  - 预训练场景：RLMRec-Gen 泛化更好，过拟合风险更低。

- **工程部署**：已落地于百度搜索业务，验证了工业级可用性。

## Related Concepts

- [[协同过滤]]
- [[互信息最大化]]
- [[对比学习]]
- [[LightGCN]]
- [[推荐系统]]
- [[用户画像]]
- [[RAG/embedding]]
- [[掩码自编码]]

## Related Entities

- [[香港大学]]
- [[百度]]
- [[PaperWeekly]]
- [[OpenAI text-embedding-ada-002]]

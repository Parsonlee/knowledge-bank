---
type: entity
tags:
  - LLM/training/post-train
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：MoDS

## 基本信息

- 全称：Model-oriented Data Selection
- 类型：SFT 数据筛选方法
- 论文来源：刘聪NLP 系列

## 核心流程

1. **质量过滤**：用 OpenAssistant reward-model-debertav3-large-v2 打分，高于阈值 α 则保留
2. **多样性过滤**：BERT 抽特征 + K-Center-Greedy 算法，选出分布均匀的子集
3. **必要性过滤**：用多样性过滤后数据微调模型 → 对高质量数据推理 → 奖励值低于 β 则保留（模型答不好的才有训练价值）

## 特点

- 三维度完整覆盖（质量/多样性/必要性）
- 必要性过滤直接使用奖励模型验证，比 IFD 更直观但计算成本更高

## 关联

- [[SFT数据挑选方法_质量多样性必要性]]
- [[概念_SFT数据三维度]]
- [[概念_K-Center-Greedy算法]]

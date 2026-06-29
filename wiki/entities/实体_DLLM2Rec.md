---
type: entity
tags:
  - LLM
  - Recommendation
---

# 实体：DLLM2Rec

蚂蚁集团提出的两级蒸馏推荐框架：GPT3.5→LLAMA2-7B→轻量序列推荐模型。来源：[[蚂蚁集团大模型推荐算法与应用]]

## 基本信息

- 来源机构：蚂蚁集团 AI 创新研发部门 NextEvo
- 作者：胡斌斌等
- 应用场景：支付宝推荐系统

## 框架结构

### 第一级蒸馏：GPT3.5 → LLAMA2-7B

- 教师模型：GPT3.5/GPT-4 用 CoT prompt 生成推荐理由（品牌/类目偏好 → 精细化推荐）
- 学生模型：LLAMA2-7B 用生成式 Loss 微调，具备推理能力
- T+1 离线推理：BERT 编码推荐理由为用户行为表征，concatenate+attention 增强下游推荐模型

### 第二级蒸馏：LLAMA2-7B → 序列推荐模型

- 方法：Ranking Loss（排名蒸馏）+ Embedding 对齐
- 排名蒸馏策略：LLAMA2 排名靠前的物品在学生模型中权重更高；目标物品接近程度影响排名
- 支持的 backbone：GRU4Rec / SASRec / SRGNN

## 效果

- 相比 SOTA 大模型推荐方法有明显提升
- 对长期冷启动用户帮助显著（大模型语义知识弥补行为数据稀疏）
- 有效克服 Popularity Bias（流行度偏差），长尾物品推荐更均衡
- LLAMA2-7B 用于离线推理，最终序列模型可线上 serving

## 关联

- [[概念_大模型推荐系统]] — 融合路径二
- [[实体_蚂蚁集团NextEvo]] — 来源机构

---
type: entity
tags:
  - LLM/training/post-train
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：DEITA

## 基本信息

- 全称：Data-Efficient Instruction Tuning for Alignment
- 类型：SFT 数据筛选方法
- 论文来源：刘聪NLP 系列

## 核心流程

1. 指令复杂性打分：小规模数据（2k）经 WizardLM 增强后用 ChatGPT 排序，训练 LLaMA-7B 打分模型
2. 回答质量打分：类似流程，ChatGPT 改写高质量回复后训练打分模型
3. 综合评分：复杂性分 × 质量分
4. 多样性过滤：LLaMA-13B 抽向量，逐个计算最小余弦相似度，保留低于阈值 t 的数据
5. 达到预算阈值后停止

## 特点

- 同时覆盖质量、多样性、必要性（IFD）三个维度
- 训练代理模型替代 ChatGPT 打分，可批量推理

## 关联

- [[SFT数据挑选方法_质量多样性必要性]]
- [[概念_SFT数据三维度]]
- [[概念_IFD指令跟随难度]]

---
type: entity
tags: ["Infra/gpu", "LLM/training"]
summary: "NVIDIA 开源的大规模 Transformer 训练框架，提供张量并行与流水线并行实现"
sources: ["Cubox/[LLM]大模型显存计算公式与优化 - 知乎-2025-05-06.md"]
created: "2026-06-26"
updated: "2026-06-26"
confidence: low
---

# Megatron-LM

## 简介

Megatron-LM 是 NVIDIA 开源的大规模 Transformer 语言模型训练框架，以高效的[[概念_模型并行|模型并行]]实现著称。它通过张量并行将单层矩阵运算切分到多张 GPU，是训练百亿/千亿级参数模型的主流基础设施之一。

## 核心能力

- **张量并行（Tensor Parallelism）**：将 attention 和 MLP 层的权重矩阵按维度切分到多卡
- **流水线并行（Pipeline Parallelism）**：按层切分模型为多个 stage
- **3D 并行**：与数据并行组合（DP × TP × PP）扩展到超大规模
- 配合 [[概念_混合精度训练|混合精度训练]] 和 [[概念_激活重计算|激活重计算]] 进一步优化显存

## 关联

- [[概念_模型并行|模型并行]]
- 来源：[[大模型显存计算与优化]]

> 注：本实体页基于通用领域知识补充，原文未必详述，confidence 标记为 low。

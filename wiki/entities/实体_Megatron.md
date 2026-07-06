---
type: entity
tags:
- LLM/inference
- Infra/gpu
summary: NVIDIA 的大模型训练并行框架，提供 TP/SP/PP 等并行策略及激活值重计算公式。
sources:
- raw/HuggingFace从决策到落地「手把手」教你训练大模型.md
- raw/Mamba2_ SSM和Transformer的大一统 - 知乎.md
- raw/入局AI Infra：程序员必须了解的AI系统设计与挑战知识.md
- raw/大规模神经网络优化：超参最佳实践与规模律.md
- wiki/sources/Mamba2_SSD_大一统.md
- wiki/sources/入局AI_Infra系统设计与挑战.md
- wiki/sources/大规模神经网络优化_超参实践与规模律.md
created: '2026-06-29'
updated: '2026-06-29'
confidence: medium
---

# 实体：Megatron

## 简介

Megatron（Megatron-LM）是 NVIDIA 的大模型训练并行框架。文中引用其论文中的激活值计算公式，并将其作为 TP/SP/PP 等 3D 并行策略的代表框架。

## 在本文语境中的角色

- 提供激活值显存计算公式：`s*b*h*(34 + 5*a*s/h) * L * γ`
- 提供选择重计算方案的公式参考
- 与 [[实体_DeepSpeed]] 并列为常见并行框架

## 相关论文

- Reducing Activation Recomputation in Large Transformer Models (arXiv:2205.05198)

## 关联

- [[概念_训练并行策略]]
- [[概念_激活值重计算]]
- [[实体_DeepSpeed]]
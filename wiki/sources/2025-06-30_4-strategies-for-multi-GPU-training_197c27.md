---
type: source
tags:
- LLM/training
- Infra/gpu
summary: 介绍多 GPU 模型训练的四种核心并行化策略：模型并行、张量并行、数据并行和流水线并行，并说明其优势与局限。
sources:
- raw/articles/2025-06-30_4-strategies-for-multi-GPU-training_197c27.md
updated: '2026-08-03'
---

# 4 strategies for multi-GPU training

## 来源信息
- **作者/来源**: Daily Dose of DS
- **日期**: 2025-06-30
- **原文链接**: [A Beginner-friendly Guide to Multi-GPU Model Training](https://www.dailydoseofds.com/a-beginner-friendly-guide-to-multi-gpu-model-training/)

## 核心要点
1. **默认限制**：默认情况下，深度学习模型即使在有多张 GPU 可用时也仅使用单张 GPU 训练，需要显式实施分布式[[wiki/concepts/概念_训练并行策略|训练并行策略]]。
2. **[[wiki/concepts/概念_模型并行|模型并行 (Model Parallelism)]]**：将模型的不同层放置在不同 GPU 上。适用于单卡无法容纳的巨大模型，但当激活值（activations）需要在 GPU 间传递时，会产生严重的通信瓶颈。
3. **张量并行 (Tensor Parallelism)**：将单个张量操作（如矩阵乘法）拆分成小块并分布在多个 GPU 上并行计算。通常内置在 PyTorch 等现代深度学习框架中。
4. **数据并行 (Data Parallelism)**：在所有 GPU 上复制模型，将训练数据划分为小 batch 分发给各 GPU，各卡独立计算梯度后进行全局聚合（gradients aggregation），并更新所有卡上的模型参数。
5. **流水线并行 (Pipeline Parallelism)**：数据并行与模型并行的结合体。标准模型并行中当一张 GPU 进行前向传播时其他 GPU 会处于闲置状态（气泡）。流水线并行通过引入 micro-batch 流水异步重叠（例如在 GPU 1 处理完当前 micro-batch 的计算并将其激活值传给 GPU 2 的同时，GPU 1 立即加载并计算下一个 micro-batch），从而大幅提高 GPU 利用率。

## 关键引文
- "However, model parallelism also introduces severe bottlenecks as it requires data flow between GPUs when activations from one GPU are transferred to another GPU."
- "Pipeline parallelism addresses this by loading the next micro-batch of data once the 1st GPU has finished the computations on the 1st micro-batch and transferred activations to layers available in the 2nd GPU."

> 📎 **物理文献**：[[raw/articles/2025-06-30_4-strategies-for-multi-GPU-training_197c27.md]]

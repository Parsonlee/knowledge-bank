---
type: entity
tags:
  - LLM/arch
  - LLM/reasoning
confidence: high
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：Minimax-m1

## 基本信息

- **类型**：开源大语言模型
- **开发方**：Minimax
- **发布时间**：2025年6月
- **参数规模**：456B 总参数，每 token 激活 45.9B（约10:1比）
- **架构**：混合 MoE（32个专家）+ 混合注意力（Lightning Attention + softmax）

## 技术特点

- **Lightning Attention**：线性复杂度 O(L) 注意力，每7个线性注意力块插入1个完整 softmax 注意力块；100K 生成时 FLOPs 仅为 R1 的 25%，支持最长 100万 token 上下文
- **CISPO RL 算法**：Clipping Importance Sampling Policy Optimization（GRPO变体），3周完成456B模型RL训练，训练成本约500万美元GPU hours
- **开源**：权重开源

## 性能定位

超长上下文（100万token）和推理能力，整体性能与同期顶尖模型相当。

## 来源

- [[LLM两年发展万字综述_2023-2025]]
- [[MiniMax_vs_Kimi_注意力路线之争]]

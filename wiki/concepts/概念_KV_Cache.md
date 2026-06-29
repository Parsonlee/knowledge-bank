---
type: concept
tags:
  - Infra/AI
  - LLM/inference
summary: KV Cache 缓存 LLM 推理中 X@W_K 和 X@W_V 的已计算结果，空间换时间，避免自回归逐 token 生成时对历史 token 的重复计算。几乎所有 LLM 推理框架（如 vLLM）均已支持。
sources:
  - "wiki/sources/入局AI_Infra系统设计与挑战.md"
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

# 概念：KV Cache

## 定义

KV Cache 是 LLM 推理优化的核心机制。LLM 自回归生成时，每次推理都需将之前生成过的 token 重新输入模型计算 Key 和 Value，复杂度为 O(N²) 存在大量重复计算。KV Cache 将已计算的 K/V 矩阵缓存，后续只需计算新增 token 的 K/V 并拼接，以空间换时间减少计算量。

## 原理

- LLM 模型结构（因果注意力）使得历史 token 的 K/V 计算结果不变
- 缓存 X@W_K 和 X@W_V 的结果上半部分（历史 token 部分）
- 每步仅需计算当前新 token 的 K/V，与缓存拼接后执行注意力计算

## 关联

- [[入局AI_Infra系统设计与挑战]]（来源）
- [[实体_vLLM]]
- [[概念_自注意力复杂度]]

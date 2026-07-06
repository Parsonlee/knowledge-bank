---
type: entity
tags:
- Infra/AI
- LLM/inference
summary: vLLM 是开源 LLM 推理框架，支持 KV Cache、连续批处理（Continuous Batching）、PagedAttention 等核心优化，是当前主流高吞吐低延时推理引擎。
sources:
- wiki/sources/LLM后训练技术全景解读.md
- wiki/sources/MiniMax_vs_Kimi_注意力路线之争.md
- wiki/sources/R1复现认知与误区.md
- wiki/sources/Tongyi DeepResearch的技术报告探秘.md
- wiki/sources/入局AI_Infra系统设计与挑战.md
- wiki/sources/大模型显存占用单卡分析.md
- wiki/sources/推测解码Speculative_Decoding综述.md
- wiki/sources/淘宝直播数字人_TTS语音合成技术.md
created: '2026-06-29'
updated: '2026-06-29'
confidence: high
---

# 实体：vLLM

## 简介

vLLM 是一个开源 LLM 推理框架（UC Berkeley），以高吞吐量和低延时为目标。在全文中被多次提及作为 KV Cache 和连续批处理的代表实现。

## 在本文语境中的角色

- 几乎所有 LLM 推理框架都支持 KV Cache，vLLM 为典型代表
- vLLM 的 Continuous Batching 实现连续批处理

## 关联

- [[入局AI_Infra系统设计与挑战]]（来源）
- [[概念_KV_Cache]]
- [[概念_连续批处理]]
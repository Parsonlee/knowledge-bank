---
type: entity
tags:
  - LLM/inference
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：Medusa

## 概述

Medusa 是一个 LLM 推理加速框架，属于推测解码（Speculative Decoding）的 Self-Drafting 方案。

## 核心机制

在 target LLM 最后一层 decoder layer 之上添加多个额外 FFN Head（Medusa Heads），每个 Head 并行预测未来多个位置的 token，作为推测（Draft）结果，随后由 target LLM 并行验证。

## 特点

- 无需独立的小模型，减少额外资源引入
- Medusa Heads 需要额外训练
- 部署便捷性较好（单一模型体系内）
- GitHub：https://github.com/FasterDecoding/Medusa

## 关联

- [[概念_推测解码]]
- [[推测解码Speculative_Decoding综述]]
- [[实体_vLLM]]

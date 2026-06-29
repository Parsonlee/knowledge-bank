---
type: entity
tags:
  - LLM/reasoning
  - LLM/training/RL
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：Qwen3

## 概述

阿里巴巴通义实验室发布的大语言模型系列，在 Qwen3 中引入了**混合思考（Thinking Mode Fusion）**能力，通过 SFT + RL 实现可控的快慢思考切换。

## 混合思考机制

- SFT 阶段：构造带 `/think` / `/no_think` 标签的混合数据训练
- RL 阶段：format-following 奖励强化指令遵循
- 涌现能力：Thinking Budget（接近 max_tokens 时强制终止思考）
- 局限：需人为控制是否思考，不能完全自主判断

## 参数

- Qwen3 Technical Report：arXiv 2505.09388
- 四阶段训练：语言预训练 → Reasoning 冷启动 → Thinking Mode Fusion（SFT）→ 通用 RL

## 关联

- [[自适应快慢思考推理模型]]
- [[概念_自适应快慢思考]]
- [[概念_自适应长短CoT]]
- [[实体_通义千问]]

---
type: entity
tags:
  - LLM/reasoning
  - LLM/training/RL
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：TinyZero

TinyZero 是 UC 伯克利博士生潘家怡等人开发的 DeepSeek-R1-Zero 复现项目，在 CountDown 数字游戏任务上验证了纯 RL 涌现自我验证和搜索能力。

## 核心发现

- 3B 基础模型纯 RL，成本不到 30 美元，验证了"顿悟时刻"
- 0.5B 模型不能涌现搜索验证；1.5B 起可学会搜索、自我验证和修正
- PPO/GRPO/PRIME 均可涌现长 CoT，具体 RL 算法不关键
- 额外 SFT 并非必须，印证 R1-Zero 设计决策
- 推理行为与任务高度相关（CountDown 学搜索验证，乘法学分布律分解）

## 项目地址

- https://github.com/Jiayi-Pan/TinyZero

## 关联

- [[实体_DeepSeek-R1]] — 被复现的原始模型
- [[概念_推理模型顿悟时刻]] — 验证的涌现现象
- [[DeepSeek-R1复现浪潮]]

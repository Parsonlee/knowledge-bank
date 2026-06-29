---
type: entity
tags:
  - LLM/reasoning
  - LLM/training/RL
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：SimpleRL

SimpleRL 是港科大何俊贤团队（共同一作黄裕振、Weihao Zeng）的 DeepSeek-R1 复现项目，仅用 8K MATH 数据在 7B 模型上复刻了 R1-Zero 和 R1 训练。

## 核心结果

| 基准 | 结果 |
|------|------|
| AIME | 33.3% |
| AMC | 62.5% |
| MATH | 77.2% |

- 超越 Qwen2.5-Math-7B-Instruct
- 媲美使用 50 倍数据的 PRIME 和 rStar-MATH

## 两种训练方式

- **SimpleRL-Zero**：Qwen2.5-Math-7B 基础模型纯 PPO（无 SFT 无奖励模型，8K MATH）
- **SimpleRL**：先 Long CoT SFT 冷启动（8K QwQ-32B-Preview 蒸馏数据）再 PPO，比 Zero 提升 6.9 个百分点

## 关键观察

- 第 44 步出现"顿悟时刻"，自我反思自发出现
- 训练动态：输出长度先减（消除代码输出习惯）后增（自我反思涌现）
- 奖励函数：格式+正确 → +1，答案错误 → -0.5，无答案 → -1
- 基于 OpenRLHF 实现

## 项目地址

- https://github.com/hkust-nlp/simpleRL-reason

## 关联

- [[实体_DeepSeek-R1]] — 被复现的原始模型
- [[概念_推理模型顿悟时刻]] — 实验中观察到
- [[DeepSeek-R1复现浪潮]]

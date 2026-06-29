---
type: entity
tags:
  - LLM/training/RL
summary: "RLVR（可验证奖励强化学习）：以数学/编程有标准答案为基础的强化学习训练范式，DeepSeek-R1/o1 系列的核心技术"
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：RLVR（可验证奖励强化学习）

## 定义

Reinforcement Learning with Verifiable Rewards。用有标准答案的问题（数学、编程）训练 LLM：答对加分、答错扣分。是 o1、DeepSeek-R1 推理能力提升的核心技术。

## 优势

- 奖励信号明确无歧义
- 可以用巨量问题放大效果
- 训练效果立竿见影

## 局限

- **只适用于有唯一正确答案的领域**（数学/编程/逻辑）
- 在医疗/教育/创意写作等开放性领域无效，甚至让模型退步
- 无法将非结构化经验转化为有效学习信号

## 后继方向

通用验证器（Universal Verifier）旨在突破 RLVR 限制：
- 路线一：评分细则（RaR / Rubicon / Writing-Zero）
- 路线二：内部自信度（VeriFree / INTUITOR / RLIF）

## 来源

- [[GPT5通用验证器_Universal_Verifier]]
- 相关概念：[[概念_RLVR]] | [[概念_通用验证器]] | [[概念_奖励函数与验证器]]
- 相关实体：[[实体_DeepSeek-R1]]

---
type: concept
tags:
- AI-Agent/skill
- AI-Agent/coding
summary: Skill 触发评价必须同时评估漏触发（False Negative）与误触发（False Positive），结合 Precision 与 Recall
  指向高风险或关键业务场景。
sources:
- wiki/sources/如何系统评价一个_Agent_Skill.md
updated: '2026-07-22'
---

# 概念：Skill 误触发与漏触发评价

## 定义

**Skill 误触发与漏触发评价** 是针对 Agent Skill 路由与选择阶段的量化测试规范。Skill 的第一道防线是准确被 Agent 识别并加载。评价需兼顾“该用未用”与“不该用而误用”两类偏差。

## 两类误区与评估指标

1. **漏触发（False Negative）**：原本需要 Skill 支持的复杂任务，Agent 未能感知并加载 Skill。
2. **误触发（False Positive）**：简单或无关指令误触发了高开销/强约束 Skill，引入额外的 Token 延迟与行为干扰。

## 指标权衡

$$\text{Precision} = \frac{\text{正确触发次数}}{\text{所有触发次数}}$$
$$\text{Recall} = \frac{\text{正确触发次数}}{\text{所有应该触发的次数}}$$

- **高风险/高成本 Skill**：提升 Precision，严防误触发带来的越权或昂贵 Token 开销。
- **关键核心业务 Skill**：提升 Recall，防止漏触发导致模型自由幻觉。

## 关联

- [[concepts/概念_Agent_Skill系统化评价框架]]
- [[sources/如何系统评价一个_Agent_Skill]]

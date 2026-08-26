---
type: concept
tags:
- AI-Agent/skill
- AI-Agent/coding
summary: Skill 增量收益评估强调评估 Skill 的核心在于对比加载 Skill 与不加载 Skill（With Skill vs Without Skill）的相对提升，而非单看绝对成功率。
sources:
- wiki/sources/如何系统评价一个_Agent_Skill.md
updated: '2026-07-22'
---

# 概念：Skill 增量收益评估 (With vs Without Skill Experimentation)

## 定义

**Skill 增量收益评估** 是评价 Agent Skill 是否有效的第一性准则。其核心机制在于：不能仅盲目评估“加载 Skill 后的 Agent 最终表现”，而必须通过对照实验测量 **“Skill 比基线 Agent 带来了多少边际提升”**。

## 实验设计范式

1. **绝对能力基线（With Skill vs Without Skill）**：
   - 实验组（With Skill）：加载 Skill 后完成任务。
   - 对照组（Without Skill）：不加载 Skill，仅靠原生 Agent 尝试完成任务。
   - 价值判断：若无 Skill 时基线模型成功率为 78%，加载后为 80%，则 Skill 的实际增量价值仅为 2%，需综合衡量额外 Token 成本。
2. **版本迭代基线（New Skill vs Old Skill）**：
   - 将旧版本 SKILL.md 快照作为基线，定量评估修改改动引起的性能与成本变化。

## 关联

- [[concepts/概念_Agent_Skill系统化评价框架]]
- [[sources/如何系统评价一个_Agent_Skill]]

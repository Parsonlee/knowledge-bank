---
type: concept
tags:
- AI-Agent/skill
- AI-Agent/coding
summary: Agent Skill 系统化评价框架覆盖触发与路由准确性、执行过程轨迹、产物质量、效率成本、安全权限控制与可复用性六大维度的完整评估体系。
sources:
- wiki/sources/如何系统评价一个_Agent_Skill.md
updated: '2026-07-22'
---

# 概念：Agent Skill 系统化评价框架

## 定义

**Agent Skill 系统化评价框架** 是针对智能体能力包（Agent Skill）建立的超越传统“输出通过/失败”的完整多维评估体系。由于一个 Skill 由触发描述、执行说明、脚本、参考资料和验证规则构成，评价对象涵盖全链路轨迹：`用户请求 → Skill 检索与触发 → Agent 执行轨迹 → 工具调用 → 输出产物 → 成本与风险`。

## 六大核心评价维度

1. **触发与路由准确性（Triggering & Routing Accuracy）**：名字与描述是否能被 LLM 正确理解，评价误触发（False Positive）与漏触发（False Negative）。
2. **执行过程正确性（Process & Trajectory Correctness）**：步骤遵循率、工具选择准确率、依赖顺序、参数合规性、环境清理等。
3. **最终结果质量（Output Quality）**：产物的清晰度、结构合理性、可维护性与决策价值。
4. **效率与成本（Efficiency & Cost）**：输入/输出 Token 开销、总延迟、工具调用与重试次数、单次成功成本。
5. **安全性与权限控制（Safety & Security）**：敏感数据泄露防护、破坏性命令拦截、越权防范与对抗性提示词注入抵抗。
6. **可复用性与可组合性（Reusability & Composability）**：在未知新泛化场景的适应力与多 Skill 冲突编排能力。

## 关联

- [[concepts/概念_Skill增量收益评估]]
- [[concepts/概念_Skill误触发与漏触发评价]]
- [[concepts/概念_Agent完整轨迹评估]]
- [[concepts/概念_Agent_Skills元工具架构]]
- [[sources/如何系统评价一个_Agent_Skill]]

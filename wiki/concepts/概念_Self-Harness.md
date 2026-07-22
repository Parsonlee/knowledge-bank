---
type: concept
tags:
- AI-Agent/harness
summary: 将 AI 自我改进做成工程闭环的范式，通过“弱点挖掘—修改提议—保留集验证”确保 Harness 代码持续进化且无性能回归。
sources:
- wiki/sources/OpenAI前VP_Lilian_Weng_AI自我改进的近路不是改权重.md
created: '2026-07-22'
updated: '2026-07-22'
---

# 概念：Self-Harness

## 定义

**Self-Harness（自主外壳进化闭环）** 是一种将 [[concepts/概念_RSI递归自我改进|RSI]] 落地为严格工程实践的范式。它让 Agent 系统在不更改模型权重的前提下，自动诊断自身的弱点并重构 [[concepts/概念_Harness_Engineering|Harness]] 代码。

## 三步工程闭环

1. **弱点挖掘（Weakness Mining）**：分析历史失败轨迹与报错模式，定位 Harness 的机制缺陷。
2. **修改提议（Modification Proposal）**：由模型针对缺陷提出具有严格边界的 Harness 代码修改（diff）。
3. **保留集验证（Holdout Verification）**：在保留的验证集上测试修改——必须**既解决弱点模式，又不产生全局回归**，才允许自动合并进入代码库。

## 代表工作

- **Self-Harness (Zhang et al. 2026)**：标准弱点-提议-验证闭环。
- **Darwin Gödel Machine (2025)**：Agent 进化自身代码库，SWE-bench Verified 达 50%。
- **AlphaEvolve (2025)**：进化搜索 + 冻结 LLM 生成 diff，优化 GPU kernel 与矩阵乘法。

## 来源与参考

- [[OpenAI前VP_Lilian_Weng_AI自我改进的近路不是改权重]]
- [[concepts/概念_Harness_Engineering]]

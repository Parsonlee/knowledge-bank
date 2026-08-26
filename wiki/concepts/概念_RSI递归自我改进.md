---
type: concept
tags:
- AI-Agent/coding
- LLM/reasoning
summary: Recursive Self-Improvement（递归自我改进），AI 系统自我迭代优化的机制。在现代 Agent 工程中，RSI 并非直接改写模型权重，而是通过迭代优化外层
  Harness 与工作流实现。
sources:
- wiki/sources/OpenAI前VP_Lilian_Weng_AI自我改进的近路不是改权重.md
updated: '2026-07-22'
---

# 概念：RSI递归自我改进

## 定义

**RSI（Recursive Self-Improvement，递归自我改进）** 指 AI 系统能够反身分析自身性能并改进自身架构或逻辑，从而形成正向反馈闭环的机制。

## 范式转变：权重修改 vs Harness 优化

- **经典科幻/理论剧本**：1965 年 I.J. Good 提出“超智能机器”，2008 年 Yudkowsky 命名 RSI。传统设想集中于模型自我修改神经元权重导致智能爆炸。
- **现代 Harness 范式**：Lilian Weng (2026) 指出，近期的 RSI 不太可能从模型直接改写自身权重开始，而是通过[[concepts/概念_Harness_Engineering|Harness Engineering]] 优化外部编排、工作流与上下文机制。

## 核心前提：基座模型智能底座

RSI 结构本身是不够的。递归自我改进依赖于足够强度的基座模型：
- 当基座模型足够强（如 GPT-4），自我改进循环能带来性能跃升。
- 当基座模型较弱（如 GPT-3.5），自我改进循环容易产生误导，反而越改越差。

## 来源与参考

- [[OpenAI前VP_Lilian_Weng_AI自我改进的近路不是改权重]]
- [[concepts/概念_Harness_Engineering]]
- [[concepts/概念_Self-Harness]]

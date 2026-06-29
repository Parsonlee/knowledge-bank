---
type: entity
tags:
  - AI-Agent
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：LangSmith

LangSmith 是 LangChain 团队开发的 AI Agent 开发者平台，用于调试、测试、评估和监控基于 LLM 的应用。

## 基本信息

- 开发方：LangChain AI
- 定位：LLM 应用的可观测性和评估平台
- 关系：与 LangChain 无缝集成

## 核心功能

- **可视化 Trace**：展示 Agent 每一步思考（Thought）/行动（Action）/观察（Observation）
- **调试支持**：追踪 Agent 内部决策过程
- **测试评估**：对比基线，评估 Agent 输出质量
- **监控**：监控基于任何 LLM 框架构建的应用

## 局限性

- 属于**外部观测工具**，Agent 框架本身未内建可验证机制
- 默认不会记录 trace，需工程师主动启用 CallbackManager
- 观测粒度受限（无法直接追踪上下文裁剪/记忆覆盖等细节）
- "框架给你'看'的能力，却不会替你'控'的问题"

## 在系统化工程中的位置

LangSmith 帮助实现 Agent 三层复杂度中的**可复现性**（仅局部支持），是自建状态与观测层的重要工具之一。

## 关联

- [[Agent系统开发经验]]
- [[实体_LangChain]]
- [[概念_Agent系统化工程]]

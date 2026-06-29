---
tags:
  - AI-Agent/coding
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体：Eino 框架

Golang 生态下的 LLM 应用开发框架，由字节跳动/CloudWego 开源。

- **特点**：基于泛型强类型（Go 1.18+）、编译期类型校验、有向图（Graph）模型编排
- **组件分类**：对话处理（ChatTemplate/ChatModel）、文本语义（Embedder/Retriever）、决策执行（ToolsNode）、自定义（Lambda）
- **切面能力（Callbacks）**：实现 logging/tracing/metrics 横切面功能，与业务逻辑完全解耦
- **HITL 支持（Checkpoint）**：执行到暂停点时保存上下文，等待用户确认后恢复
- **与 tRPC-A2A-Go 配合**：将 Agent 封装为 A2A 协议服务

来源：[[万字长文深入浅出教你优雅开发复杂AI_Agent]]

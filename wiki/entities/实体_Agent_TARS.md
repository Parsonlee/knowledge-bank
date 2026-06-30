---
type: entity
tags:
  - AI-Agent/tools
summary: "Agent TARS 是字节跳动开源的多模态 AI Agent，内置 MCP Server 支持（同进程 Function Call）+ 用户自定义 MCP Server 扩展（Stdio/SSE），是 MCP 工程实践的参考实现"
created: "2026-06-29"
updated: "2026-06-29"
---

## 简介

Agent TARS 是字节跳动开发并开源的多模态 AI Agent 框架。在 MCP 工程实践方面，它展示了"内置工具 + 用户自定义 MCP 扩展"的双轨设计，适合在标准化和灵活性之间取得平衡。

## 工具架构设计

| 类型 | 机制 | 目标用户 | 特点 |
|------|------|---------|------|
| 内置 MCP Servers | 同进程 Function Call 调用 | 普通用户 | 零门槛，无需配置 |
| 用户自定义 MCP Servers | Stdio / SSE 外部进程 | 高级用户 | 灵活扩展，即插即用 |

这一设计说明 Function Call 与 MCP 并非对立，而是在同一应用中分层使用。

## MCP 工程观点

字节跳动金鑫总结的 MCP Server 开发最佳实践（基于 Agent TARS 经验）：

1. 推荐用 **zod** 定义 Schema 再转 JSON Schema（类型安全）
2. 返回值应**语义化**，帮助 LLM 精准理解上下文（而非返回原始二进制或无结构文本）

## 参考来源

- [[基于MCP的AI_Agent应用开发实践]] — 金鑫（字节跳动）MCP 实践分享

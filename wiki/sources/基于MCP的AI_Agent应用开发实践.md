---
type: source
tags:
- AI-Agent/tools
summary: 字节跳动 Agent TARS 开发者以前后端分离类比，阐述 MCP 将工具层从 Agent 解耦的范式转移与落地实践
sources:
- Cubox/基于 MCP 的 AI Agent 应用开发实践-2025-05-12.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- **标题**：基于 MCP 的 AI Agent 应用开发实践
- **作者**：金鑫（字节跳动技术团队）
- **URL**：https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247514365

## 核心要点

- MCP 最重要的价值在于通过标准化协议将工具提供方与 Agent 开发者解耦，类比 Web 前后端分离
- 前 MCP 时代三大痛点：开发耦合度高、工具复用性差、生态碎片化
- MCP vs Function Call：MCP 用 JSON-RPC 支持双向通信和可发现性；Function Call 是 JSON-Schema 的静态函数调用；MCP 适合动态复杂场景，Function Call 适合单一静态调用
- MCP Server 提供三类能力给 LLM：Resources（数据/文档）、Tools（可调用函数）、Prompts（提示词模板）
- Agent TARS 的工具分两类：内置 MCP Servers（同进程 Function Call 调用，对普通用户零门槛）和用户自定义 MCP Servers（高级用户通过 Stdio/SSE 扩展）
- MCP Server 开发实践：推荐用 zod 定义 Schema 再转 JSON Schema；返回值应语义化，帮助 LLM 精准理解上下文
- MCP 生态发展：Cloudflare/Composio/Zapier 通过 SSE 托管 MCP（Endpoint 即一批 Servers）；理想场景是 MCP Server 与 Agent 同跑 Docker 容器（Sidecar 模式）
- MCP Roadmap 三方向：Remote MCP Support（鉴权/服务发现/无状态，Streamable HTTP）、Agent Support、Developer Ecosystem
- 未来挑战：MCP 动态工具库对 RL 训练提出新要求（模型需对新增 MCP 具备泛化理解能力）；Agent K8s 问题（服务发现/恢复/监控）待解决，A2A/ANP 在探索

## 关键引文

> 缺少标准化的上下文和工具集导致开发者的三大痛点：开发耦合度高……工具复用性差……生态碎片化。[重点/高亮]

## 关联

- [[概念_MCP协议]] — MCP 核心概念
- [[概念_MCP五大原语]] — Resources/Tools/Prompts 等原语
- [[概念_MCP与Function_Call对比]] — 两种工具调用机制对比
- [[概念_MCP传输方式]] — Stdio/SSE/Streamable HTTP
- [[实体_Agent_TARS]] — 字节跳动开源多模态 Agent
- [[实体_Anthropic]] — MCP 协议制定方

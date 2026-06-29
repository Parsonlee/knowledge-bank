---
type: entity
tags:
  - AI-Agent/tools
summary: "CherryStudio 是一款开源的 MCP Host 应用，主进程 MCPService.ts 做通信代理，渲染进程 ApiService.ts 承载 AI 逻辑，是 CHS 架构的典型实现案例"
created: "2026-06-29"
updated: "2026-06-29"
---

## 简介

CherryStudio 是一款开源的 AI 桌面应用，支持多模型对话，原生集成 MCP 协议。在 MCP CHS 架构讨论中，它是最常被解剖引用的 Host 实现案例。

## 架构解剖（MCP 视角）

| 组件 | 文件 | 角色 |
|------|------|------|
| 主进程 | `MCPService.ts` | MCP Client —— 只做 MCP 通信代理（协议握手/会话管理/心跳） |
| 渲染进程 | `ApiService.ts` | MCP Host —— 核心 AI 职责（Prompt 构建 + LLM 调用） |

这一架构清晰展示了 CHS 三组件中 Host 与 Client 在同一应用中的职责分离：**Client（通信管道）与 Host（AI 智能）在代码层面是分离的**。

## 意义

CherryStudio 的开源代码是验证"Server/Client 不含 AI 逻辑"这一论断的最直接 SDK 法证之一。

## 参考来源

- [[wiki/sources/别再误会MCP了辟谣指南]] — 通过 CherryStudio 源码解剖 MCP CHS 架构

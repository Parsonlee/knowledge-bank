---
type: entity
tags:
  - AI-Agent/tools
summary: "阿里巴巴智能引擎团队大模型研发平台，Human-in-the-Loop MCP 方案的落地环境"
created: "2026-06-29"
updated: "2026-06-29"
---

# 实体_OpenLM平台

阿里巴巴智能引擎团队（AI·OS）构建的大模型研发平台，是 [[概念_HITL_MCP]] 方案的落地环境。

## 主要特性

- 支持 MCP 工具集成（MCP 市场，公开一方/三方工具）
- MCP 组件默认超时 30 秒
- 基于 QueryString 参数实现多租户共享 MCP Server
- 支持 Human-in-the-Loop（send_inquiry 工具 + HTTP 回答接口）
- SSE 流式响应，透传 MCP Notification 帧给端侧

## 团队

阿里巴巴智能引擎团队，AI 工程系统建设者，主导设计 AI·OS 大数据 AI 工程体系。

## 相关概念

- [[概念_HITL_MCP]]
- [[概念_MCP_Proxy]]
- [[概念_MCP协议]]

## 来源

- [[HumanInTheLoop用MCP实现]]

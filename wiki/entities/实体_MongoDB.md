---
type: entity
tags:
  - AI-Agent/tools
summary: "MongoDB 是流行的文档型 NoSQL 数据库，在 MCP 数据库集成场景中是典型的结构化数据后端，可通过 mcp-mongo-server 接入 MCP 生态"
created: "2026-06-29"
updated: "2026-06-29"
---

## 简介

MongoDB 是开源的文档型 NoSQL 数据库，以 BSON（Binary JSON）格式存储文档。在 MCP 数据库集成场景中，MongoDB 是最常用的演示数据库之一。

## 在 MCP 生态中的角色

通过 `mcp-mongo-server` 包，MongoDB 可接入 MCP 协议：

- Agent 通过自然语言描述查询需求
- MCP Server 将其转为 MongoDB 查询语句（Text-to-Query）
- 实现比 RAG 更精确的结构化数据检索

## mcp-mongo-server 配置

```bash
npx -y mcp-mongo-server mongodb://localhost:27017/mydb
```

## 参考来源

- [[wiki/sources/MCP加数据库]] — MCP+MongoDB 实战配置与 RAG 对比

---
type: entity
tags:
  - AI-Agent/tools
summary: "Cline 是 VS Code 的 AI 编码扩展，原生支持 MCP Client，可通过配置 npx 命令接入任意 MCP Server，是 MCP 数据库集成的常用 Host 之一"
created: "2026-06-29"
updated: "2026-06-29"
---

## 简介

Cline（前身 Claude-Dev）是 VS Code 的开源 AI 编码助手扩展，原生支持 MCP 协议，可作为 MCP Host 连接外部 MCP Server。

## MCP 相关能力

- 在 VS Code 设置中直接配置 MCP Server（`mcpServers` JSON 块）
- 支持 Stdio 模式（npx 启动本地 MCP 进程）
- 可配合 mcp-mongo-server、mcp-filesystem 等 Server 实现自然语言数据库查询、文件操作等

## 典型配置（MongoDB 集成）

```json
{
  "mcpServers": {
    "mongodb": {
      "command": "npx",
      "args": ["-y", "mcp-mongo-server", "mongodb://localhost:27017/mydb"]
    }
  }
}
```

## 参考来源

- [[MCP加数据库]] — VS Code + Cline + mcp-mongo-server 实战

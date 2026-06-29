---
type: concept
tags:
  - AI-Agent/tools
summary: "MCP 支持三种传输方式：Stdio（本地子进程）、SSE（远端流式）、Streamable HTTP（Web 化未来方向）；选型取决于部署场景和实时性需求"
created: "2026-06-29"
updated: "2026-06-29"
---

## 定义

MCP 协议层之下的传输层（Transport Layer）支持多种通信方式，不同传输方式适用于不同部署场景。传输方式的选择不影响 MCP 协议语义，只影响通信的物理方式。

## 三种传输方式

### 1. Stdio（标准输入输出）

- **通信方式**：Host 以子进程方式启动 MCP Server，通过 stdin/stdout 通信
- **典型配置**：`npx @modelcontextprotocol/server-xxx` 启动方式
- **适用场景**：本地部署，同机通信
- **优点**：零网络开销、配置简单、天然隔离
- **缺点**：无法跨机器共享，每个 Host 需独立启动进程
- **现状**：目前绝大多数（1 万+）MCP Server 运行在此模式

```json
// settings 配置示例（VS Code + Cline）
{
  "mcpServers": {
    "mongo": {
      "command": "npx",
      "args": ["-y", "mcp-mongo-server", "mongodb://localhost:27017"]
    }
  }
}
```

### 2. SSE（Server-Sent Events）

- **通信方式**：基于 HTTP 的单向流式推送，Server 向 Client 推送事件
- **适用场景**：远端 HTTP，Server 部署在云端
- **优点**：跨机器访问、可多 Host 共享同一 Server
- **缺点**：单向流式（Server→Client），双向通信需额外处理
- **代表平台**：Cloudflare Workers AI、Composio、Zapier（通过 SSE 托管 MCP，一个 Endpoint 对应一批 Servers）
- **部署形态**：Sidecar 模式（与 Agent 同跑 Docker 容器，推荐的生产形态）

### 3. Streamable HTTP（新标准）

- **通信方式**：HTTP 请求可同步返回 JSON，也可升级为 SSE 流式通道
- **适用场景**：MCP Web 化的未来标准
- **优点**：
  - 兼容无状态 HTTP（可部署为普通 REST 服务）
  - 需要流式时自动升级为 SSE 通道
  - 与 OAuth 2.1 鉴权天然配合
- **状态**：MCP Roadmap 中的 Remote MCP Support 核心组件，正在推进

## Web 化配套技术

Streamable HTTP 解决扩展性问题，但 MCP Web 化还需配套：

**鉴权（OAuth 2.1）**
- 支持 Azure AD、Okta 等企业单点登录
- 解决远端 MCP Server 的身份认证问题

**服务发现**
- 当前：手动配置 Server 地址
- 未来：官方注册中心（MCP Registry），支持自动发现

**无状态化**
- Streamable HTTP 支持无状态部署，便于水平扩展

## 选型建议

| 场景 | 推荐传输方式 |
|------|------------|
| 本地开发、个人工具 | Stdio |
| 团队共享工具、云端服务 | SSE |
| 新项目、面向 Web 化 | Streamable HTTP |
| 生产级 Agent 系统 | Sidecar（SSE）或 Streamable HTTP |

## 参考来源

- [[wiki/sources/MCP五大原语与Web化]] — Streamable HTTP 与 Web 化方向（MCP 联合创建者解读）
- [[wiki/sources/基于MCP的AI_Agent应用开发实践]] — Stdio/SSE 实践与 Sidecar 模式、Roadmap
- [[wiki/sources/MCP加数据库]] — npx Stdio 启动方式实战配置

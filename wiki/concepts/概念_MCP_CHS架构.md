---
type: concept
tags:
  - AI-Agent/tools
summary: "MCP 的正确架构是 Client-Host-Server 三组件，而非 CS 两组件；Host 是 AI 智能唯一承载者，Server/Client 是模型无关的 RPC 管道"
created: "2026-06-29"
updated: "2026-06-29"
---

## 定义

MCP 架构的完整形式是 **Client-Host-Server（CHS）三组件**，这是业界最常见的误解来源——很多人将架构图读成 CS（两组件），从而误以为 Server 含有 AI 智能。

## 三组件精确界定

### Host — AI 智能唯一承载者

- 应用中**唯一**直接与 LLM 交互的组件
- 负责管理对话上下文、构建 Prompt、解析 LLM 响应
- 应用的最终效果和智能水平**完全**取决于 Host 的实现质量
- 典型实现：Claude Desktop、Cursor、CherryStudio 的渲染进程 ApiService.ts

### Client — 无状态协议中间件

- 位于 Host 和 Server 之间
- 职责：协议握手、会话管理、心跳维持
- 将 Host 意图转换为 JSON-RPC 请求发送给 Server
- **不含任何 AI 逻辑**，对自然语言无感知

### Server — 确定性能力执行器

- 标准 RPC 服务，声明并暴露能力（Tools/Resources/Prompts）
- 接收标准化 JSON-RPC 请求，返回确定性结果
- 整个"接收→校验→分发→执行"是机械的路由，**不进行任何推理或决策**
- SDK 源码法证（@modelcontextprotocol/sdk NodeJS）：Server 构造函数只声明能力并注册请求处理器，初始化握手全程只处理协议元数据，不感知任何自然语言

## 最常见误解

| 误解 | 正确认知 |
|------|---------|
| MCP Server 与 LLM 直接交互 | Server 只与 Client 通信，从不直接调用 LLM |
| MCP Server 含有 AI 智能 | Server 是确定性 RPC 服务，相当于 HTTP 协议本身 |
| MCP 是"更高级的 Function Calling" | MCP 是工程协议，Function Call 是模型特性，定位不同 |
| 架构是 CS 两组件 | 完整架构是 CHS 三组件，Host 是独立且核心的层次 |

类比：MCP Server/Client 与 LLM 的关系，就像 HTTP 协议与"理解网页内容"的关系——协议本身不理解内容。

## CherryStudio 案例解剖

- **主进程 MCPService.ts** — 只做 MCP 通信代理（Client 职责）
- **渲染进程 ApiService.ts** — 承担 Host 核心 AI 职责（Prompt 构建 + LLM 调用）

这清晰展示了 Host（AI 智能）与 Client（通信管道）在同一应用中的职责分离。

## 工程层影响

理解 CHS 架构对工程师的关键启示：

1. **提升应用智能的唯一杠杆是 Host**（Prompt 工程、模型选择、任务规划），而非改进 Server
2. **工具 description 是关键字段**：LLM 的工具选择完全依赖 description 的质量
3. **MCP 的价值**：解放工程师处理底层通信与工具适配，让精力聚焦于 Host 的"智能"

## 参考来源

- [[wiki/sources/别再误会MCP了辟谣指南]] — 本概念的核心来源，含 SDK 源码法证

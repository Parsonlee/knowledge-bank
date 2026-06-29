---
type: concept
tags:
  - AI-Agent/tools
summary: "MCP 与 Function Call 的本质区别：MCP 是模型无关的 JSON-RPC 动态协议（支持双向通信+能力发现），Function Call 是与特定模型绑定的 JSON Schema 静态调用"
created: "2026-06-29"
updated: "2026-06-29"
---

## 定义

MCP（Model Context Protocol）与 Function Calling 是两个定位不同的层次，最常见的误解是将 MCP 视为"更高级的 Function Calling"。两者并非替代关系，而是不同抽象层次的工具。

## 核心对比

| 维度 | Function Call | MCP |
|------|--------------|-----|
| **本质** | JSON Schema 静态函数定义 | JSON-RPC 2.0 动态协议 |
| **通信方向** | 单向（Host → 模型 → 工具） | 双向（含 Sampling：Server → Client → LLM） |
| **模型绑定** | 与特定模型 API 绑定（不同厂商格式不同） | 模型无关，一套协议对接所有兼容模型 |
| **能力发现** | 静态声明，需提前确定工具集 | 动态发现（capability discovery），运行时枚举 |
| **适用场景** | 单一、静态工具调用 | 动态、复杂多工具场景 |
| **工具扩展** | 需修改模型接口或重新训练 | 新增 Server 无需修改模型代码 |
| **实现复杂度** | 低（直接 JSON Schema）| 高（协议握手、会话管理） |

## Function Call 的痛点

1. **协议碎片化**：OpenAI、Anthropic、Google 各家 Function Call 格式不统一，同一工具需为不同模型写不同调用代码
2. **功能扩展难**：增加新工具需要修改 prompt 或调整接口，有时需要重新训练
3. **生态孤立**：工具与特定模型生态绑定，无法跨平台复用

## MCP 如何解决

- **统一格式**：标准化请求/响应/错误处理，一次开发对接所有兼容 MCP 的模型
- **动态扩展**：新增 MCP Server 无需修改 Host 代码，即插即用
- **生态兼容**：Server 可同时服务 Claude、Cursor、Cline 等任意 MCP Host

## 误解辨析

**误解**：MCP 是"更高级的 Function Calling"

**正确认知**：
- Function Call 是**模型特性**（模型 API 层面的功能），定义模型如何请求调用工具
- MCP 是**工程协议**（应用架构层面的规范），定义工具如何被发现、注册和调用
- 两者可共存：MCP Host 内部仍然通过 Function Call 与 LLM 交互，MCP 解决的是 Host 与 Server 之间的标准化问题

**误解**：MCP Server 包含 AI 智能

**正确认知**：MCP Server 是确定性 RPC 服务，不含任何 AI 逻辑；AI 智能集中在 Host（参见 [[概念_MCP_CHS架构]]）

## Agent TARS 的实践对比

字节跳动 Agent TARS 的工具分两类，清晰展示了两种方式的共存：

- **内置工具**：同进程 Function Call 调用（对普通用户零门槛）
- **用户自定义工具**：通过 MCP Server（Stdio/SSE）扩展（高级用户）

这说明 Function Call 与 MCP 并非对立，而是在同一应用中分层使用。

## 选型建议

- **简单、单一工具，与特定模型强绑定** → Function Call 更简单直接
- **多工具、跨模型、需动态扩展、需生态复用** → MCP 更合适
- **生产级多 Agent 系统** → MCP 是事实标准选择

## 参考来源

- [[wiki/sources/MCP加数据库]] — Function Call 痛点与 MCP 演进关系
- [[wiki/sources/基于MCP的AI_Agent应用开发实践]] — MCP vs Function Call 对比与 Agent TARS 实践
- [[wiki/sources/别再误会MCP了辟谣指南]] — MCP 与 Function Call 概念边界辨析

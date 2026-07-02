---
type: source
tags:
- AI-Agent/tools
summary: MCP 联合创建者 David 解构五大原语（Prompt/Resource/Tool/Sampling/Roots），并阐述 MCP Web 化（OAuth
  2.1 + Streamable HTTP）的未来方向
sources:
- raw/MCP不止工具调用！MCP联合创建者：绝大多数人用法都太初级！曝MCP五大原语、....md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- **标题**：MCP不止工具调用！MCP联合创建者：绝大多数人用法都太初级！曝MCP五大原语、高阶玩法：丰富人机交互体验；MCP的未来在Web
- **作者**：David Soria Parra（Anthropic MCP 联合创建者）整理：云昭（51CTO）
- **URL**：https://mp.weixin.qq.com/s?__biz=MjM5ODI5Njc2MA==&mid=2655928063

## 核心要点

- MCP 绝大多数人只用到 Tool Calls，但协议远不止于此，包含五大原语
- **Prompt 原语**（用户主动触发）：服务器预设的 AI 交互模板，可动态生成内容；与 Tool 的核心区别是 Prompt 由用户主动触发，Tool 由模型决定何时调用；支持参数补全（弹出选择列表）
- **Resource 原语**（应用主动）：暴露原始内容/数据（文件、DB Schema、网页等），客户端可基于它构建 Embedding 进行 RAG；例：在 Cloud Desktop 暴露 PostgreSQL Schema，Claude 自动绘制数据库结构图
- **Tool 原语**（模型主动）：最熟悉的工具调用，由模型驱动触发确定性动作
- **交互模型**：三者分工——Prompt（用户主导）、Resource（应用主导）、Tool（模型主导），完善 AI 应用需协调三者
- **Sampling 原语**：Server 向 Client 发起"请求补全"调用，由客户端选定模型返回结果；用户掌控成本/安全/隐私；可串联多个 MCP Server 构建链式调用（Chain of MCP Servers）；目前支持较少，计划今年引入官方产品
- **Roots 原语**：MCP 服务向客户端询问当前环境信息（如 VS Code 中打开的项目路径），限定操作范围避免误操作
- **MCP Web 化**：目前 1 万+ MCP 服务运行在本地，未来方向是 Web——MCP 服务将变成网站而非本地 Docker 容器
- Web 化两大核心问题：①鉴权（OAuth 2.1，支持 Azure AD/Okta 企业单点登录）；②扩展性（Streamable HTTP 模式：可同步返回 JSON 或开启流式通道）
- 即将上线功能：异步任务支持、用户交互请求（Elicitation）、官方注册中心、多模态能力、Ruby/Go 新 SDK

## 关联

- [[概念_MCP五大原语]] — 本文核心：Prompt/Resource/Tool/Sampling/Roots
- [[概念_MCP协议]] — MCP 基础
- [[概念_MCP传输方式]] — Streamable HTTP
- [[概念_MCP链式调用]] — Sampling 实现的链式调用
- [[实体_Anthropic]] — MCP 协议制定方
- [[实体_David_Soria_Parra]] — MCP 联合创建者

---
> 📎 **物理文献**：[[raw/MCP不止工具调用！MCP联合创建者：绝大多数人用法都太初级！曝MCP五大原语、....md]]

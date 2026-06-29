---
type: concept
tags:
  - AI-Agent/tools
summary: "MCP 协议定义五大原语：Tool（模型主动）、Prompt（用户主动）、Resource（应用主动）、Sampling（服务器发起补全）、Roots（环境感知），绝大多数人只用到 Tool"
created: "2026-06-29"
updated: "2026-06-29"
---

## 定义

MCP 协议定义了五类基础原语（Primitive），覆盖从用户交互到模型调用的完整 AI 应用场景。绝大多数开发者只用到 Tool，其余四类大幅欠利用。

每类原语的核心区分在于**谁来触发**：

| 原语 | 触发方 | 典型用途 |
|------|--------|---------|
| Tool | 模型主动 | 执行确定性动作 |
| Prompt | 用户主动 | 预设交互模板 |
| Resource | 应用主动 | 暴露数据/内容 |
| Sampling | Server 发起 | 请求模型补全 |
| Roots | Server 查询 | 获取客户端环境信息 |

## 五大原语详解

### 1. Tool — 模型主动触发

- 最常见、最熟悉的原语
- 由**模型**决定何时调用，触发确定性动作（查询数据库、调用 API、读写文件等）
- 工具的 `description` 字段是 LLM 选择调用的核心依据，质量直接影响准确性

### 2. Prompt — 用户主动触发

- 服务器预设的 AI 交互模板，可动态生成内容
- 与 Tool 的核心区别：**Prompt 由用户主动触发，Tool 由模型决定触发**
- 支持参数补全（弹出选择列表，引导用户填入参数）
- 适合：标准化工作流、反复使用的复杂 Prompt 模板

### 3. Resource — 应用主动

- 暴露原始内容/数据（文件、数据库 Schema、网页等）
- 客户端可基于 Resource 构建 Embedding，进行 RAG 检索
- 典型场景：在 Claude Desktop 暴露 PostgreSQL Schema → Claude 自动绘制数据库结构图
- 适合：让 AI 了解系统结构，而非执行具体操作

### 4. Sampling — Server 向 Client 发起补全请求

- 方向与 Tool 相反：**Server → Client → LLM**（而非 Host → Client → Server）
- Server 向 Client 发起"请求补全"调用，由客户端选定模型执行并返回结果
- 核心价值：用户掌控成本/安全/隐私（由 Host 侧选择使用哪个模型）
- 可串联多个 MCP Server 构建**链式调用**（Chain of MCP Servers）
- 当前支持较少，Anthropic 计划引入官方产品

### 5. Roots — 环境感知

- MCP Server 向 Client 询问当前客户端环境信息（如 VS Code 中打开的项目路径）
- 用途：限定 Server 的操作范围，避免误操作其他目录或资源
- 适合：需要感知用户工作环境的工具（文件操作、代码分析等）

## 三原语交互模型

完善的 AI 应用需协调三类主动触发原语：

```
用户 → Prompt（用户主导）
应用 → Resource（应用主导）  
模型 → Tool（模型主导）
```

三者共同构成完整的人机交互体验，单纯使用 Tool 只利用了 MCP 能力的一小部分。

## MCP Web 化与原语扩展

**当前状况**：1 万+ MCP 服务运行在本地（Stdio 模式）

**未来方向**：MCP Web 化——服务变成网站而非本地 Docker 容器

Web 化两大技术问题：
1. **鉴权**：OAuth 2.1，支持 Azure AD / Okta 企业单点登录
2. **扩展性**：Streamable HTTP 模式，可同步返回 JSON 或开启流式通道

**即将上线**：异步任务支持、用户交互请求（Elicitation）、官方注册中心、多模态能力、Ruby/Go 新 SDK

## 参考来源

- [[wiki/sources/MCP五大原语与Web化]] — 本概念核心来源，MCP 联合创建者 David Soria Parra 权威解读
- [[wiki/sources/MCP加数据库]] — Tools/Resources/Prompts/Sampling/Roots 五类能力维度
- [[wiki/sources/基于MCP的AI_Agent应用开发实践]] — Resources/Tools/Prompts 工程实践

---
type: source
tags:
- AI-Agent/coding
summary: 腾讯程序员系统梳理 AI Agent 三级进化（LLM/AI/Multi-Agent）、MCP+A2A 协议对比、CoT/ReAct/Plan-and-Execute
  思考框架，并以 Golang Eino+tRPC-A2A-Go 框架展示生产级多 Agent 实践。
sources:
- raw/万字长文深入浅出教你优雅开发复杂AI Agent.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- 作者：walli（腾讯技术工程）
- 原文：微信公众号 腾讯程序员
- Cubox ID：7339277124500455454

## 核心要点

### Agent 开发范式三级进化

**Level 1 LLM Agent**：聊天机器人形态，Prompt 工程赋予人设，2023 年主流。存在幻觉、不可控问题，难承载严肃场景。

**Level 2 AI Agent**：`Agent = LLM + 记忆 + 规划技能 + 工具使用`，2024 年中起向"好用"迈进。单 Agent 仍难在所有领域达到专家水平。

**Level 3 Multi-Agent**：多专业化 Agent 协作网络，每个 Agent 专注特定领域。核心优势：任务聚焦、独立优化、问题拆解。**Human in the Loop** 作为特殊 Agent 参与协作。

### Agent 协议全景

按交互对象分两类：
- **面向上下文（Context-Oriented）**：MCP，解决 Agent 如何用好工具
- **面向 Agent 间（Inter-Agent）**：A2A，解决多 Agent 如何协作

**Function Call vs MCP**：Function Call 是大模型基础能力（不同厂商接口各异），MCP 是跨模型统一标准（USB-C 类比），包含工具调用 + Prompts + Resources。MCP 落地障碍：生态成熟度不足、企业基建冲突、通用协议场景局限。

**MCP vs A2A**：不互斥，分层协同。MCP 解决"工具调用"，A2A 解决"Agent 间通信"。边界模糊化趋势：工具可视为低自主性 Agent，Agent 可视为高自主性工具。

**ANP**（中国社区发起）：基于 W3C DID 身份认证，目标打造智能体互联网 HTTP 协议，关注度较低（779 Star）。

**A2A 核心功能**：能力发现（Agent Card）、任务和状态管理、协作消息交换、用户体验协商（支持图片/表单/视频内容片段）。

### Agent 思考框架

**CoT（思维链）**：引导模型生成中间推理步骤，代价是增加计算成本和延迟。Sequential Thinking MCP 是使用频率最高的 MCP Server。

**ReAct**：思考（Thought）→ 行动（Action）→ 观察（Observation）迭代循环，解决 CoT 缺乏外部实时交互的问题。

**Plan-and-Execute**：扩展 ReAct，分两阶段：
- 规划阶段：将复杂任务分解为有序子任务（可先呈现给用户审核）
- 执行阶段：逐一用 ReAct 处理子任务，可动态重规划

优势：结构化、上下文优化（减少单次处理长度）、提升鲁棒性、增强可解释性与人机协同。Manus/OWL/OpenManus 均采用此框架。

### Golang 框架：Eino

- 基于泛型强类型，编译期类型校验
- 有向图（Graph）模型编排：Component 为节点，Edge 串联数据流
- **Callbacks 切面**：实现 logging/tracing/metrics 等横切面功能注入，与业务逻辑完全解耦
- **Checkpoint 检查点**：HITL 机制，执行到暂停点时保存上下文，等待用户确认后恢复
- vs Dify/Coze：后者面向业务人员快速原型，Eino 面向技术团队深度定制

Eino 组件分类：
- 对话处理：ChatTemplate、ChatModel（BaseChatModel + ToolCallingChatModel）
- 文本语义：Loader/Transformer、Embedder、Indexer、Retriever
- 决策执行：ToolsNode（InvokableTool / StreamableTool）
- 自定义：Lambda（Invoke/Stream/Collect/Transform 四种交互模式）

### Golang 框架：tRPC-A2A-Go

将 Eino Agent 封装为 A2A 协议服务，步骤：
1. 通过 Callbacks 实现任务状态同步
2. 实现 `TaskProcessor` 接口处理新任务
3. 生成 AgentCard，创建 A2A Server
4. 注册到 tRPC 服务启动

### Demo：多 Agent Supervisor 模式

- 意图识别 Agent（客户经理）→ 领域专家 Agent（旅行规划/深度搜索/文章解读）
- 所有 Agent 通过 A2A 协议封装，可接入 Cherry Studio / QQ 机器人
- 可观测：Langfuse 10 行代码接入，全链路 Trace + 数据标注 + LLM-as-a-judge

## 关联

- [[概念_MCP协议]]
- [[概念_MCP五大原语]]
- [[概念_orchestrator-worker模式]]
- [[概念_多智能体协调]]
- [[概念_Agent感知记忆推理三能力]]
- [[概念_HITL_MCP]]
- [[实体_Agent_TARS]]
- [[实体_CherryStudio]]

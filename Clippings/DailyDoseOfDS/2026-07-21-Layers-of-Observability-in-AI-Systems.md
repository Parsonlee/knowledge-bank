title: AI 系统中的可观测性层级结构：Traces 与 Spans source: https://mail.google.com/mail/u/0/#inbox/19f86be0631f8e2c author:

"[[DailyDoseOfDS]]" published: 2026-07-21 created: 2026-07-28 description: 解析大模型生产环境中的 Trace（端到端请求全过程）与 Span（检索、提示词组装、生成等独立步骤）监控架构，解决 RAG 及 Agent 系统排错与成本追踪问题。 tags:

clippings

# AI 系统中的可观测性层级结构：Traces 与 Spans

随着 AI 系统走向生产环境，传统软件中的分布式追踪（Distributed Tracing）与可观测性架构被全面引入大模型应用中。

以典型 RAG 系统为例，用户的每一次提问都会经过多个独立步骤，单看系统的输入输出无法找出回复不佳的原因（究竟是 Chunk 切分差、检索不准确，还是 LLM 本身产生幻觉）。

## Trace 与 Span 核心概念

Trace（追踪）：代表单个请求从发出到收到最终回复的完整端到端旅程。系统为每次请求生成唯一的 Trace ID。

Span（跨度）：代表 Trace 内部的各个具体子操作。

### 典型 RAG 流程中的 5 大 Span：

Query Span：捕获用户的原始输入、时间戳与 Session 信息。

Embedding Span：记录文本向量化的 Token 消耗与 API 延迟。

Retrieval Span：记录向量数据库匹配过程（Exposure 常见的坏 Chunk、低相关度得分、Top-K 参数不当等问题）。

Context Span：记录拼接进入 System Prompt 的实际上下文，及时发现 Context 过长问题。

Generation Span：记录 LLM 生成回复的输入/输出 Token 数量、延迟与推理过程，用于精确成本核算。

通过 Span 级别的可观测性，团队可以监控模块漂移、精细化追踪成本并对单个组件进行针对性调优。

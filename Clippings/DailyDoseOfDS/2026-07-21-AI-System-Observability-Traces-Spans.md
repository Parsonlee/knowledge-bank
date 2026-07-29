title: "AI 系统中的可观测性层级结构（Traces 与 Spans）" source: "https://mail.google.com/mail/u/0/#inbox/19f86be0631f8e2c" author:

"[[DailyDoseOfDS]]" published: 2026-06-26 created: 2026-07-28 description: "详细拆解 RAG 等 AI Pipeline 中 Trace（全链路跟踪）与 Query/Embedding/Retrieval/Context/Generation 等 Spans 的分层可观测性与成本排查机制。" tags:

clippings

# AI 系统中的可观测性层级结构（Traces 与 Spans）

随着 AI 系统逐渐成为生产级软件，对可观测性（Observability）的需求变得不可或缺。传统软件行业在分布式追踪（Distributed Tracing）、Spans（跨度）和 Instrumentation（仪表化）方面已有数十年成熟实践，而 AI 系统也正在迅速跟进。

将大语言模型应用部署给真实用户时，你必须清楚整个流水线（Pipeline）中每一步的实时运行状况。

## 核心概念：Trace 与 Span

以典型的 RAG（检索增强生成）系统为例，用户的提问会流经多个组件，最终输出回答。每一个步骤都会产生延迟、可能发生异常，并消耗相应的成本。

如果仅观察整个系统的输入和输出，你将永远无法获得全面的掌控力。

Trace（链路跟踪）：代表单次请求的完整生命周期（从用户提交 Query 到最终收到 Response 的完整条带）。系统会为每次请求生成一个唯一的 Trace ID。

Span（步骤跨度）：代表该 Trace 内部包含的具体独立子操作，所有同属一次请求的 Spans 均携带相同的 Trace ID。

## RAG 流水线中的关键 Spans 拆解

Query Span（查询跨度）：用户提交问题。这是 Trace 的起点，捕获原始输入、时间戳与 Session 会话信息。

Embedding Span（向量化跨度）：Query 被送入 Embedding 模型转化为向量，追踪 Token 数量与 API 响应延迟。

Retrieval Span（检索跨度）：向量在向量数据库中进行相似度搜索。实践表明大部分 RAG 问题（如切块不佳、相关性得分低、top-k 配置错误等）都隐匿于此，该 Span 能够彻底暴露这些细节。

Context Span（上下文组装跨度）：检索到的文档块与 System Prompt 进行拼接组装。明确展示送入大模型的最终 Prompt 组合。

Generation Span（生成跨度）：LLM 生成最终回复。这是通常耗时最长、成本最高的一步，记录输入/输出 Token 数量、延迟与 Reasoning 推理过程。

## 为什么需要 Span 级别的可观测性？

精准 Debug 故障排查：如果没有 Span 级别的追踪，你只能知道“回答很差”，却无法判断是因为检索失真、上下文拼接有误，还是大模型发生了幻觉。

精准成本追踪：清晰掌握 Token 开销具体分配在哪个组件与环节。

捕捉漂移与退化：AI 系统会随时间发生性能漂移，通过 Span 指标可早期捕捉性能退化并独立调优各个组件。

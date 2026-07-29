title: "2026 年 AI 工程主技术栈路线图" source: "https://mail.google.com/mail/u/0/#inbox/19f00c2716d4e27d" author:


* "[[DailyDoseOfDS]]" published: "2026-06-25" created: "2026-07-28" description: "全景剖析 2026 年 AI 工程涉及的 10 大核心层级：从模型基础、提示词与上下文工程、Agent 架构，到推理优化与 LLMOps 安全。" tags:
* clippings


________________


2026 年 AI 工程主技术栈路线图
我们梳理了一份 2026 年 AI 工程主技术栈路线图，涵盖从模型本身到生产环境安全运行的 10 个层级：


1. 基础层（Foundations）：决定模型如何表示输入，包括 Token、Embedding、Transformer、注意力机制、上下文窗口、位置编码和混合专家（MoE）。
2. 模型行为（Model Behavior）：覆盖预训练、后训练、采样、Temperature、推理模型、多模态与测试时计算（Test-time Compute）。
3. 提示词工程（Prompt Engineering）：仅通过 Prompt 塑造输出，涉及 System Prompt、Few-shot、思维链（CoT）、结构化输出、Prompt 缓存、自一致性与 Meta-prompting。
4. 检索（Retrieval）：为模型提供未训练过的数据，包括 Chunk 分块、向量数据库、混合搜索、重排序（Reranking）、检索评估、查询重写与 GraphRAG。
5. 智能体（Agents）：让模型具备行动能力，包括 Function Calling、ReAct、规划、反思、多 Agent 协作、Computer Use 与人机回环（Human-in-the-loop）。
6. 上下文工程（Context Engineering）：跨步骤控制上下文窗口内容，涉及上下文管理、压缩（Compaction）、记忆、MCP、Agent Harness、实时检索与结构化记笔记。
7. 微调（Fine-tuning）：当 Prompt 和上下文不满足需求时修改权重，涉及 SFT、LoRA、RLHF、DPO、蒸馏、GRPO 与 RLVR。
8. 推理优化（Inference Optimization）：降低服务成本并提升速度，涉及量化（Quantization）、KV Cache、批处理、投机解码、vLLM 服务、FlashAttention 与 PagedAttention。
9. 评估（Evaluation）：衡量系统正确性，涉及 Benchmark、LLM-as-a-Judge、黄金数据集、幻觉检测、回归测试、轨迹评估与红队测试。
10. LLMOps 与安全（LLMOps & Safety）：保持生产可靠性，涉及可观测性、成本追踪、Guardrails、PII 脱敏、反馈环、Prompt 注入防御与模型路由。
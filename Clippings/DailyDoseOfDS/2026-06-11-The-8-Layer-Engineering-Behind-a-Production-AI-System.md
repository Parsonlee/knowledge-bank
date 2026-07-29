title: "生产级 AI 系统背后的 8 层工程架构" source: "https://mail.google.com/mail/u/0/#inbox/19eb880a3ed57fd8" author:

"[[DailyDoseOfDS]]" published: "2026-06-11" created: "2026-07-28" description: "全景图解生产级 AI 系统的 8 层架构：模型基础、推理服务、上下文工程、Agent Harness、检索记忆、模型微调、评估观测与安全防护。" tags:

clippings

# 生产级 AI 系统背后的 8 层工程架构

两个团队使用相同的基座模型，可能交付完全不同的产品。模型是固定的输入，拉开差距的是包裹在模型周围的 8 层工程架构：

模型基础（Model Foundations）：Tokenization、Embedding、预训练/后训练、上下文窗口、Logits 与采样。

推理与服务（Inference & Serving）：Prefill 与 Decode 阶段分离、KV Cache、Prompt 缓存、投机解码、连续批处理（Continuous batching）、量化（FP8/AWQ）与 Paged Attention（vLLM）。

上下文工程（Context Engineering）：上下文预算、克服 Lost in the Middle、历史压缩、上下文卸载、JIT 检索与结构化记笔记。

Agent 与 Harness 工程：Think-Act-Observe 循环、薄/厚 Harness 设计、子 Agent 编排、MCP 标准协议与验证环（Verification Loops）。

检索与记忆（Retrieval & Memory）：RAG 流水线、Chunking/Re-ranking、向量数据库、混合搜索、知识图谱与情景/时间记忆。

适配与训练（Adaptation & Training）：SFT、PEFT（LoRA/QLoRA）、RLHF/DPO、GRPO、模型蒸馏与合成数据。

评估与可观测性（Evaluation & Observability）：离线/在线评估、LLM-as-a-Judge、轨迹评估、Tracing 与 Spans、Token 成本追踪与回归测试。

安全、防护与可靠性（Safety, Security & Reliability）：Prompt 注入防御、Jailbreak 防范、幻觉缓解、结构化输出约束、PII 脱敏、Failover 容灾与 Guardrails。

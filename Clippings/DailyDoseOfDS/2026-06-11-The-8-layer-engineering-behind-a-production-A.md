---
title: "The 8-layer engineering behind a production AI system."
source: "https://mail.google.com/mail/u/0/#inbox/19eb880a3ed57fd8"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-11
created: 2026-07-30
description: "全景拆解生产级 AI 系统背后的八大工程层级：模型基础、推理服务、上下文工程、Agent 循环、检索记忆、微调对齐、可观测评估与安全防御。"
tags:
  - clippings
---

# 生产级 AI 系统背后的 8 大工程层级全景解析（The 8-layer engineering behind a production AI system.）

两个团队可以使用完全相同的基座模型，却交付出体验与成本截然不同的最终产品。

基座模型是一个固定输入，真正拉开差距的是包裹在模型外部的 **8 大工程层级**——从底层的 Token 渲染服务，到顶层的 Agent 循环控制与安全防御。

![生产级 AI 系统 8 大工程层级全景图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d7650b7-a210-4dd8-950d-301b7b5ba7aa_1450x1450.jpeg)

---

### Layer 1: 模型基础（Model Foundations）

模型基础层涵盖模型如何将原始文本转化为概率分布：

![模型基础层架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b137ee9-37d1-49ff-bed8-bb9fb6c1ce69_996x1016.jpeg)

* **Tokenization（分词）**：在模型处理前将文本切分为子词（Subword）单元，Token 数量直接决定显存开销与上下文预算；
* **Embeddings（词嵌入）**：将 Token 映射到高维向量空间，使语义相似的词在几何距离上相互靠近；
* **Pretraining & Post-training**：预训练从海量无标签文本中学习语言规律，Post-training（SFT、RLHF/DPO）塑形模型的指令遵循与安全对齐能力；
* **Context window（上下文窗口）**：模型在单次推导中所能关注的固定 Token 预算，由 Prompt、历史会话与生成输出共同切分；
* **Logits（未归一化得分）**：词表上的原始概率得分；
* **Sampling（采样）**：控制如何从概率分布中挑选下一个 Token（包含 Temperature 与 Top-p 权衡）。

---

### Layer 2: 推理与服务（Inference and Serving）

推理与服务层是将模型权重转化为高效、低成本 Token 产出的核心基础设施：

![推理与服务优化架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2c0a8ca-e5a4-4697-91cb-1836514b17f8_1932x886.png)

* **Prefill vs Decode 解耦**：Prefill 并行处理整个 Prompt，受限于计算峰值（Compute-bound）；Decode 逐 Token 递进生成，受限于显存带宽（Memory-bound）；
* **KV Cache（键值缓存）**：缓存历史 Token 的 Attention Keys 与 Values，避免每步生成时的重复冗余计算；
* **Prompt/Prefix Caching**：共享公共系统提示词的 KV 状态，使固定 Prefix 在首次调用后近乎免费；
* **Speculative Decoding（投机采样）**：利用小模型草稿预估 Token，再由主模型并行一次性验证，实现显著加速；
* **Continuous Batching（连续批处理）**：在新请求到达时即刻填补已完成请求留下的 GPU 空位，无需等待全 Batch 完成；
* **Quantization（量化）**：将模型权重压缩为更低位数（如 FP8、AWQ），节省显存并提升计算速度；
* **Paged Attention（分页注意力）**：将操作系统虚拟内存的分页思想引入 KV Cache 机制，彻底消除显存碎片化，是 vLLM 核心原理；
* **TTFT & TPOT**：分别衡量首 Token 延迟与后续 Token 吐速。

---

### Layer 3: 上下文工程（Context Engineering）

上下文工程管理模型在执行动作瞬间所能接收到的核心信息：

![上下文工程架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe94e47d9-329e-49c9-aabb-9c8dee9b0222_496x335.png)

* **Context budgeting（窗口预算）**：将有限的窗口视作宝贵资源，仅投入能提升回答质量的 Token；
* **Context rot（上下文腐化）**：随着上下文填满，模型注意力分散，输出质量在达到硬性上限前即开始退化；
* **Lost in the middle（中间迷失）**：模型高度关注上下文头部和尾部，淹没在中间位置的细节容易被忽略；
* **Compaction & summarization（压缩与总结）**：将长历史压缩为高保真总结，让 Agent 开启全新窗口；
* **Context offloading（上下文卸载）**：将庞大细节卸载到外部存储，窗口内仅保留引用句柄；
* **Just-in-time retrieval（准实时检索）**：在具体的步骤按需动态加载数据；
* **Structured note-taking（结构化记事本）**：允许 Agent 在窗口外维护持久化的笔记。

---

### Layer 4: Agent 与 Harness 工程（Agents and Harness Engineering）

将无状态的模型封装为具备复杂任务解决能力的智能体系统：

![Agent 智能体与 Harness 工程架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4a0b45d-acb0-40e2-a514-a0bf6f49baf4_960x959.gif)

* **Agent Loop（智能体循环）**：运行 ReAct 或 TAO（Think, Act, Observe）循环，直至任务完成；
* **Tool use / function calling**：让模型输出结构化工具调用命令，由 Harness 执行后反馈结果；
* **Thin vs Thick Harness**：轻量 Harness 信任模型自行决策；厚重 Harness 用确定性代码硬编码控制流；
* **Subagents & Orchestration**：分派具备独立上下文的专注子 Agent，保持主 Agent 窗口轻量；
* **MCP（Model Context Protocol）**：标准化接口，连接模型与工具，替代复杂的 N×M 自定义集成；
* **Skills, hooks & state**：提供跨步骤存活的复用技能、生命周期钩子与状态持久化；
* **Planning vs Reacting**：预先生成完整 Plan 与实时步步决策之间的平衡；
* **Verification loops（验证闭环）**：利用规则、单元测试或 LLM 裁决关卡，把关输出质量。

---

### Layer 5: 检索与记忆（Retrieval and Memory）

为模型注入其在预训练阶段从未接触过的外部事实与知识：

![检索与记忆层 (RAG) 架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3887fa24-2e65-4d4c-b345-33028d5bd9f5_2752x1536.jpeg)

* **RAG 流水线**：在查询时刻检索相关切片，并拼接到 Prompt 中进行增强生成；
* **Chunking & Re-ranking**：文档切片与重排模型，按真正语义相关性重新排序候选切片；
* **Vector DB（向量数据库）**：高效存储向量 Embedding 并提供大规模近邻搜索（ANN）。

---

### Layer 6: 微调与 Post-Training（Fine-tuning, RLHF, and Post-training）

模型行为定制与特定领域对齐：

![微调、RLHF 与 Post-Training 架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1b11441-2915-4fda-910e-2941510fb5e5_1514x1080.png)

* **SFT（监督微调）**：在高质量输入输出对上训练模型掌握固定格式与行为；
* **RLHF & DPO**：根据人类偏好优化模型，DPO 跳过了独立的奖励模型直接更新；
* **Synthetic Data（合成数据）**：在真实标注数据匮乏时利用强模型自动构造训练集。

---

### Layer 7: 评估、可观测性与测试（Evals, Observability, and Testing）

确保系统持续稳定运行的技术保障：

![评估、可观测性与测试架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9c726d-a974-4fdf-b4e8-0463af4417d1_960x640.png)

* **LLM-as-judge**：使用强模型对规则难以评分的开放式输出进行客观打分；
* **Agent trajectory eval（轨迹评估）**：评估 Agent 探索的全路径而不仅仅是最终答案；
* **Tracing & spans（链路追踪）**：记录每一步工具调用与 Token 流转，精准排查崩溃点；
* **Token & cost tracking**：细粒度归因每个请求与步骤的成本开销；
* **Regression testing（回归测试）**：在修改 Prompt 或更换模型后重新运行 Benchmark 捕捉静默坏退化。

---

### Layer 8: 安全防御（Security, Safety, and Guardrails）

生产环境的最后一道安全防线：

![安全防御与 Guardrails 架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F945c4676-d214-41d9-ac1e-062caf345ae7_1190x1107.png)

* **Prompt injection（提示词注入）**：防范未信任输入中夹带恶意指令劫持模型控制权；
* **Jailbreaks（越狱防护）**：识别防范巧妙绕过模型安全限制的越狱 Prompt；
* **Guardrails（输入输出护栏）**：基于规则或分类器实时阻断不合规的请求与响应。

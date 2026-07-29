title: Context Engineering（上下文工程）的 6 大核心模块 source: https://mail.google.com/mail/u/0/#inbox/19f00c2716d4e27d author:


* "[[DailyDoseOfDS]]" published: 2026-06-25 created: 2026-07-28 description: 拆解上下文工程（Context Engineering）6 大组件：Prompt 技巧、Query 增强、长期记忆、短期历史、知识库检索与工具/MCP 协议。 tags:
* clippings


________________


Context Engineering（上下文工程）的 6 大核心模块
在 AI 应用质量影响因子中，模型选择占 15%，Prompt 占 10%，而上下文工程（Context Engineering）占据了 75% 的决定性作用。
6 大核心组件
1. Prompting Techniques：包括 CoT（链式思考）与 Few-shot，引导模型展开步骤推理。
2. Query Augmentation（查询增强）：针对模糊输入进行 Query Rewriting（重写）、Query Expansion（扩展）与 Query Decomposition（拆解）。
3. Long-term Memory（长期记忆）：结合向量数据库与知识图谱（如 Zep Graphiti），沉淀 Episodic、Semantic 与 Procedural 长期记忆。
4. Short-term Memory（短期记忆）：对话历史的裁剪、总结与 Token 预算管理，避免 Context Rot。
5. Knowledge Base Retrieval（知识库检索）：涵盖文档 Chunking、Hybrid Search 与统一数据同步（如 Airweave）。
6. Tools & MCPs：通过标准 MCP 协议将工具接口由 $N \times M$ 网状复杂度降至 $N+M$ 统一层。
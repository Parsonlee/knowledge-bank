title: 从 RAG、Agentic RAG 到 AI Agent 长期记忆的演进 source: https://mail.google.com/mail/u/0/#inbox/19f6ca0f2c928ca3 author:

"[[DailyDoseOfDS]]" published: 2026-07-16 created: 2026-07-28 description: 阐述从单次只读 RAG、工具调用式 Agentic RAG，到支持读写交互与持续学习的 AI Agent 长期记忆（如 Graphiti）的技术演进。 tags:

clippings

# 从 RAG、Agentic RAG 到 AI Agent 长期记忆的演进

知识检索架构正在经历从静态 RAG 向动态 Agent 记忆（Memory）的范式转移：

传统 RAG (2020-2023)：单次检索 + 生成回复，无决策能力，容易检索出无关上下文。

Agentic RAG：由 Agent 自主判断是否需要检索、选择哪个数据源以及验证结果可用性。但依然是只读模式。

AI Agent Memory：支持读写交互。Agent 不仅能读取外部知识，还能将用户偏好、历史交互经验写入知识库，实现无需重新训练的持续学习（Continual Learning）。

开源知识图谱框架（如 Graphiti）正在帮助 Agent 构建具有程序性、情节性与语义性的真实人脑级记忆。

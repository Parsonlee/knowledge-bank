title: Honeycomb O’Reilly 生产系统调试与可观测性工程 source: https://mail.google.com/mail/u/0/#inbox/19f6ca0f2c928ca3 author:


* "[[DailyDoseOfDS]]" published: 2026-07-16 created: 2026-07-28 description: 编程 Agent 极大地降低了写代码成本，但也带来了未知异常；探讨为何经典 O’Reilly 可观测性工程图书针对大模型应用重写了 27 章内容。 tags:
* clippings


________________


Honeycomb O’Reilly 生产系统调试与可观测性工程
AI 编程 Agent（Coding Agents）极大降低了代码编写成本，但代码校验和测试能力并未同步跟进。传统单元测试只能捕捉预期的异常，预发布环境（Staging）也无法重现生产环境的真实流量。


AI 生成的代码更容易在未知场景（Unknown-unknowns）下崩溃——由于编写时缺乏人类直觉模型，排查变得异常困难。


经典 O'Reilly 著作《Observability Engineering》针对这一技术转变进行了全面重写，新增了 27 章关于 LLM 应用 Instrumentation、生产遥测数据反哺 Evaluation 以及利用 Agent 进行系统调试的内容。


核心观点在于：预设仪表盘（Dashboard）只能回答已知问题；捕捉未知故障必须保留高基数（High-cardinality）原始事件，并在事后按 User ID、Prompt 版本等维度灵活下钻分析。
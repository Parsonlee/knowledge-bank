title: Prompt、Context、Harness 与 Loop 工程四层架构剖析 source: https://mail.google.com/mail/u/0/#inbox/19f29f70428b228f author:


* "[[DailyDoseOfDS]]" published: 2026-07-03 created: 2026-07-28 description: 解析构建生产级 AI Agent 系统必须掌握的 4 层工程架构：Prompt 工程、Context 工程、Harness 工程与 Loop 工程。 tags:
* clippings


________________


Prompt、Context、Harness 与 Loop 工程四层架构剖析
构建一个成熟的 Agent 系统本质上是在最基础的 ReAct while 循环外层包裹 4 层工程抽象：


+-------------------------------------------------------+


|  Loop Engineering (调度、终止条件、事件驱动)              |


|   +-----------------------------------------------+   |


|   |  Harness Engineering (工具解析、重试、校验器)    |   |


|   |   +---------------------------------------+   |   |


|   |   |  Context Engineering (RAG、裁剪、重排) |   |   |


|   |   |   +-------------------------------+   |   |   |


|   |   |   |  Prompt Engineering (CoT, 格式) |   |   |   |


|   |   |   |     [ Base Model ]            |   |   |   |
4 层工程职责
1. Prompt Engineering：关注单次调用的词调与结构（CoT、Few-shot、Output Schema），影响模型内部推理。
2. Context Engineering：管理单轮可见的全部上下文（检索 Chunk、历史对话、内存），对输入进行优先级排序与裁剪。
3. Harness Engineering：构建模型周围的代码支撑（工具定义、异常重试、格式解析、Sub-agent 路由与 Verifier 校验）。
4. Loop Engineering：掌控整个 Task 运行生命周期（设置 Turn/Token 上限、无进展检测、自动化触发与终止信号）。
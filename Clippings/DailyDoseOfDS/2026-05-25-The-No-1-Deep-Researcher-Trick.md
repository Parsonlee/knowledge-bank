title: 排名第一的深度研究 Agent 使用的离经叛道技巧 source: https://mail.google.com/mail/u/0/#inbox/19e60c170373504b author:


* "[[DailyDoseOfDS]]" published: 2026-05-25 created: 2026-07-28 description: 揭秘开源深度研究系统 Onyx 如何通过“剥夺协调 Agent 的搜索权限”和“两层架构限制”，在 DeepResearch 基准测试中超越 Claude 与 ChatGPT。 tags:
* clippings


________________


排名第一的深度研究 Agent 使用的离经叛道技巧
在 DeepResearch Bench 上登顶的开源深度研究系统 Onyx 采用了一个违反直觉的架构设计：负责整体研究策略的协调 Agent（Orchestrator）完全没有搜索与网页访问权限。
为什么剥夺协调者的搜索权限有效？
传统的 Orchestrator 一旦拥有搜索工具，往往会忍不住自己去查资料，导致其陷入低价值搜索的细节中，无法保持全局战略视野。
三阶段流水线：
1. 阶段 1（拆解）：Orchestrator 在无工具状态下将复杂 Query 拆解为最多 6 个独立的研究子方向。
2. 阶段 2（分发执行）：派发 3 个隔离的子研究 Agent，各自进行最多 8 轮搜索、阅读与思考，并允许检索企业内部文档（Slack、Confluence 等）。
3. 阶段 3（聚合）：通过确定性代码进行去重、重新编号，生成附带统一引用地图的高质量报告。
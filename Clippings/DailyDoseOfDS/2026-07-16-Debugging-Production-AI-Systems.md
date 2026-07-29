title: 生产环境大模型系统排错与可观测性工程 source: https://mail.google.com/mail/u/0/#inbox/19f6ca0f2c928ca3 author:

"[[DailyDoseOfDS]]" published: 2026-07-16 created: 2026-07-28 description: 编码 Agent 降低了写代码成本但未降低验证成本，生产环境遥测（Telemetry）成为捕捉未知故障（Unknown-Unknowns）的关键。 tags:

clippings

# 生产环境大模型系统排错与可观测性工程

AI 编码 Agent 极大降低了写代码的成本，但代码验证的能力并没有同步跟上。

AI 生成的代码容易在“未知的未知”（Unknown-unknowns）场景下崩溃，因为开发者在生成代码时没有建立完整的心理模型（Mental Model），无法预测何种输入会导致异常。同样的，Prompt 的微小修改可能通过离线 Eval，但在特定用户群体中产生质量衰退。

生产环境成为了唯一能验证这些代码的地方。传统的静态 Dashboard 只能回答预先设置好的问题，而捕捉未知故障需要记录原始高基数事件（High-cardinality events），并在事后按用户 ID、Prompt 版本等属性切片分析。

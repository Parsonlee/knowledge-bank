title: Agent Loop 循环工程详解：从 ReAct 到自动化终止 source: https://mail.google.com/mail/u/0/#inbox/19ef7234678feae5 author:


* "[[DailyDoseOfDS]]" published: 2026-06-24 created: 2026-07-28 description: 拆解 Agent 核心运行循环，探讨如何通过独立 Verifier 校验器、Token 上限与 Context 压缩预防“死亡循环（Doom Loop）”。 tags:
* clippings


________________


Agent Loop 循环工程详解：从 ReAct 到自动化终止
所有 Agent 框架（LangGraph、OpenAI Agents SDK、Claude Code）底层均运行着相同的 while 循环：Context ➔ Tool Call ➔ Run Tool ➔ Append Result ➔ Re-run。
循环工程的关键突破点
1. 拒绝由模型自我判定“完成”：避免 Agent 未跑测试即汇报完成。引入独立 Verifier 评估器（如测试通过或确定性校验）作为真正的终止信号。
2. Context Rot 与 Doom Loop 防御：循环时间越长，上下文越容易充满无用 Tool 输出与废弃推理，引发“死亡循环”。必须采用 Compaction（压缩）、Offloading（文件卸载）及独立 Sub-agent 分流。
3. 幂等工具设计与明确错误提示：循环重试需要安全且幂等的写工具，且错误提示必须指明“下一步如何修正”，而非仅抛出异常。
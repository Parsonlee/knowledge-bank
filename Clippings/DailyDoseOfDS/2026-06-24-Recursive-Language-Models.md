title: "递归语言模型（Recursive Language Models, RLM）原理与实践" source: "https://mail.google.com/mail/u/0/#inbox/19ef7234678feae5" author:


* "[[DailyDoseOfDS]]" published: "2026-06-24" created: "2026-07-28" description: "MIT 研究团队提出的 RLM 架构，将超长上下文存入 Python REPL 变量中，利用正则筛选与递归子调用彻底解决上下文腐烂问题。" tags:
* clippings


________________


递归语言模型（Recursive Language Models, RLM）原理与实践
随着对话变长，大模型常常出现“上下文腐烂（Context Rot）”，回忆与推理能力显著下降。MIT 研究人员提出了**递归语言模型（RLM）**来解决这一难题。
RLM 运行机制：
* 上下文隔离：在普通 LLM 调用中，Query 和完整上下文一起发送。而在 RLM 中，上下文被单独存储为 Python REPL 环境中的一个变量，主模型不直接接收全部内容。
* 工具化探索：主模型获得窥视（Peek）、正则过滤（Grep）、分块（Partition）等工具。
* 递归自调用：主模型通过正则将 5,000 条日志过滤到 50 条相关记录，然后发起递归子调用让子模型归类，最后汇总结果。


在 10M+ Token 的超长上下文测试中，搭载 GPT-5-mini 的 RLM 在多项硬核 Benchmark 上超越了单次调用的 GPT-5，且单次查询成本更低。
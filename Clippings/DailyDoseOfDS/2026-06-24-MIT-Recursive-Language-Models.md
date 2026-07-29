title: MIT 递归语言模型（Recursive Language Models, RLM） source: https://mail.google.com/mail/u/0/#inbox/19ef7234678feae5 author:


* "[[DailyDoseOfDS]]" published: 2026-06-24 created: 2026-07-28 description: MIT 团队提出 RLM 架构，将超长上下文保存在 Python REPL 变量中，通过正则过滤与递归子调用破解长文本“Context Rot”性能衰退问题。 tags:
* clippings


________________


MIT 递归语言模型（Recursive Language Models, RLM）
传统大模型直接将超长 Context 塞入 Prompt 中，容易引发“Context Rot（上下文腐烂）”并大幅降低推理准确率。


MIT 提出的 Recursive Language Models (RLMs) 将上下文作为变量存放在 Python REPL 环境中，根模型不直接读取全部文本：


* 代码化窥探与过滤：模型通过正则（Regex）或关键词过滤（Grep）快速锁定相关行，将 5000 条记录缩减至 50 条。
* 递归分治调用：将子问题分解并派生递归子调用，解决后再汇总给主模型。


在 10M+ Token 级别的海量文本基准测试中，结合 GPT-5-mini 的 RLM 在准确率上超越了直接输入的原生 GPT-5，且单次查询成本大幅下降。
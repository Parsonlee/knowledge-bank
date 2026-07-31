---
title: "关于生产系统调试的免费O'Reilly书籍（A free O’Reilly book on debugging production systems.）"
source: "https://mail.google.com/mail/u/0/#inbox/19f6ca0f2c928ca3"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-16
created: 2026-07-30
description: "随着AI生成的代码增加了未知的故障模式，O'Reilly的《可观测性工程》进行了更新，引入了关于仪表化LLM应用和基于代理调试的新章节，并提供了免费抢先版章节。"
tags:
  - clippings
---

# 关于生产系统调试的免费O'Reilly书籍（A free O’Reilly book on debugging production systems.）

编码代理大幅降低了编写代码的成本，但验证能力却原地踏步。测试仍然仅仅编码了人们预想到的故障模式，而测试环境（staging）仍然无法重现生产流量。

AI生成的代码让情况变得更糟，因为它在未知的未知情况（unknown-unknowns）下会发生故障。由于在编写代码时没有人形成心智模型，因此没有人能够预测哪些输入会破坏它。

这也同样适用于提示词（prompt）的变化，它们可能通过所有的离线评估，但却在某一个用户群体中出现退化，因为评估集很少能与生产流量完全匹配。

这就使得生产环境成为这段代码接受验证的唯一环境，它需要能回答出无人预料到的问题的遥测技术。

仪表板只回答人们提前想好设置的问题。捕捉未知的故障意味着要保留原始的、高基数的事件，并在事后按用户ID、提示词版本或任何其他属性对它们进行切片。

这就是为什么在2022年出版并成为该主题标准参考书的《可观测性工程》（Observability Engineering），刚刚进行了近乎彻底的重写。

作者围绕这一确切的转变重建了这本书，新增了27章内容，涉及如何对LLM应用进行仪表化监控、将生产环境遥测数据反馈到评估中，以及如何使用代理AI进行调试。

Honeycomb在这一期中与我们合作，并免费提供了早期发布的章节供下载。

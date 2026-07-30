---
title: "斯坦福让 LLM 微调过时了吗？"
source: "https://mail.google.com/mail/u/0/#inbox/199df440e83cc2f8"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-13
created: 2026-07-30
description: "邮件介绍 Stanford 的 Agentic Context Engineering（ACE）：不改模型权重，而让模型依据反馈反复重写上下文；并转述了其在 AppWorld、金融推理、成本与延迟上的结果。"
tags:
  - clippings
---

# 斯坦福让 LLM 微调过时了吗？

邮件介绍一篇 Stanford 的论文 **Agentic Context Engineering（ACE）**。其表述并不是重新训练模型，而是让**上下文自身演化**：模型写出自己的提示词，反思哪些做法有效或无效，再重写它；反复循环后，系统会将失败变成经验、将成功变成规则，如同维护一册持续更新的工作笔记。

邮件转述的结果为：

- 在 AppWorld 上，比 GPT-4 驱动的 Agent 高 **10.6%**；
- 在金融推理任务上提升 **8.6%**；
- 成本和延迟降低 **86.9%**；
- 不需要标注数据，依靠的是反馈循环。

文中以此反驳“提示词应越短越干净”的直觉：ACE 构建的是高密度、持续演化的 playbook，并使经验随时间累积。邮件的结论是，LLM 所需要的未必是简单性，而是上下文密度。

对于如何管理这些信息与经验，邮件提出可为 Agent 构建实时记忆层，并举例开源的图式记忆框架 Graphiti。

- [ACE 论文（arXiv PDF）](https://arxiv.org/pdf/2510.04618)
- [Zep Graphiti GitHub 仓库](https://github.com/getzep/graphiti)

---
title: "面向 LLM 应用的组件级评估"
source: "https://mail.google.com/mail/u/0/#inbox/197c270c599ab371"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-30
created: 2026-07-30
description: "介绍 DeepEval 如何对工具、检索器和生成器分别追踪并挂载指标，以定位 LLM 应用中的组件级问题。"
tags:
  - clippings
---

# 面向 LLM 应用的组件级评估

多数 LLM 评估把应用看作黑盒：输入数据、获得输出，然后对整个端到端系统运行评估。

但问题可能出在黑盒内部的任意位置，例如检索器、工具调用，或 LLM 本身。因此，LLM 应用需要组件级评估和追踪。

邮件以开源的 [DeepEval](https://github.com/confident-ai/deepeval) 为例，给出三步做法：

1. 使用 `@observe` 装饰器追踪单个 LLM 组件，例如工具、检索器和生成器；
2. 为每个部分附加不同的指标；
3. 在测试用例级别和组件级别查看可视化拆解，了解哪些部分正常工作。

对于一个 RAG 应用，邮件说明的操作顺序是：先写入常规导入语句；将 LLM 应用定义在一个带 `@observe` 装饰器的方法中；再为希望追踪的各组件添加组件级指标。随后定义测试用例并对应用运行组件级评估，即可生成评估报告。

还可以检查单个测试，以理解其通过或失败的原因。

邮件强调了两点：

- 无需重构已有的 LLM 应用代码；
- DeepEval 是开源项目（邮件发布时标注为 8,500+ GitHub stars），可以自行托管，使数据留在自己控制的位置。

- [DeepEval GitHub 仓库](https://github.com/confident-ai/deepeval)
- [组件级 LLM 评估文档](https://deepeval.com/docs/evaluation-component-level-llm-evals)

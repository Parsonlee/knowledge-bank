---
title: "画布框架：一种构建生产级 Agent 的结构化方法（The Canvas Framework: A structured approach to building）"
source: "https://mail.google.com/mail/u/0/#inbox/19d64a1fd91e185f"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-06
created: 2026-07-30
description: "MongoDB 发布了针对构建生产级 AI Agent 的 Canvas 框架，通过 POC 和生产两个阶段的规划画布，帮助团队在整合模型前明确产品定义和 Agent 设计。"
tags:
  - clippings
---

# 画布框架：一种构建生产级 Agent 的结构化方法（The Canvas Framework: A structured approach to building）

在基础模型出现之前，构建一个 AI 功能需要收集和标记训练数据，从零开始训练一个自定义模型，然后才能将其集成到产品中。这需要数月的时间和庞大的计算投资，之后团队才能测试用户是否真的需要这个功能。

基础模型消除了这个瓶颈，因为它们是预先训练好的，并且可以通过 API 访问。现在团队可以通过 zero-shot（零样本）或 few-shot（少样本）提示调用 GPT-4 或 Claude，在几天内交付 MVP（最小可行产品），首先验证用户需求，然后再投资策划用于 RAG 或微调的数据。

但是对于 Agentic 系统来说，缺少了一个层级。

Agent 的设计必须紧接着产品定义之后进行，因为 Agent 的能力、工作流和内存（记忆）需求，决定了它需要哪些知识，以及在下游选择哪些模型提供商是有意义的。

MongoDB 发布了 Canvas 框架的详细分解，该框架正是围绕这一顺序构建的。它使用了两个规划画布（planning canvases）。

* POC（概念验证）画布包含 8 个方块，涵盖产品验证、Agent 设计（能力、自治边界、内存需求）、数据需求（知识来源、更新频率、反馈循环）以及模型集成（提供商选择、提示策略、成本验证）。
* 生产（Production）画布增加了 11 个用于规模化的方块，包括容错、多 Agent 协调、跨应用存储、向量搜索和 Agent 内存的统一数据架构，外加安全加固和治理。

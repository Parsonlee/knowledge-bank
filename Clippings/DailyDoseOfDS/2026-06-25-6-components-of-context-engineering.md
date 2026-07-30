---
title: "6 components of context engineering."
source: "https://mail.google.com/mail/u/0/#inbox/19f00c2716d4e27d"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-25
created: 2026-07-30
description: "深度拆解上下文工程的六大核心组件：检索重排、记忆管理、Prompt 结构化、压缩总结、工具输出格式化与窗口预算管理。"
tags:
  - clippings
---
# 上下文工程的六大核心组件（6 components of context engineering.）

在现代化 AI 智能体与大语言模型应用构建中，人们逐渐认识到：**决定大模型输出质量上限的不是提示词的措辞，而是整个上下文信息流水线（Context Pipeline）的设计**。这就是上下文工程（Context Engineering）。

上下文工程包含以下六大核心组件：

---

## 1. 动态检索与重排序（Retrieval & Reranking）

![检索与重排序](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F029fa969-ee3a-45a6-972f-6d7edbe6129b_1930x1852.png)

仅从向量数据库中检索高相关性切片不足以满足需求。需要通过交叉编码器（Cross-encoder）重排序模型对 Top-K 结果进行二次精细打分，剔除无关噪点。

---

## 2. 状态与记忆管理（Memory Management）

![记忆管理机制](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F733113ce-f515-4f91-a7e5-0f2ef4822869_2008x751.png)

区分短期会话记忆（Working Memory）与长期记忆（Long-term Knowledge）。将跨轮次的关键事实抽取并固化至用户画像或结构化键值数据库中。

---

## 3. 上下文结构化摆放（Context Layout & Ordering）

![上下文结构摆放](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9cf66394-2d29-4ecf-80ab-55deb54dc559_1280x968.gif)

模型对窗口两端（开头与结尾）的注意力最高，对中间部分的注意力会发生衰减（Lost in the Middle 现象）。因此需要将最重要的指令和核心检索切片放置在窗口首尾。

---

## 4. 历史总结与上下文压缩（Summarization & Compression）

![上下文压缩示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d2733c3-db89-4900-a596-7551248233e5_994x201.gif)

当多轮对话导致上下文接近上限时，自动触发总结算子，将陈旧的中间步骤压缩为摘要，清理失效的临时变量。

---

## 5. 工具输出规范化（Tool Output Formatting）

![工具输出规范化](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd19ad755-521e-40e5-bfd0-4806f21ec5f7_1024x559.png)

工具（如 API 调用、代码执行结果）返回的原始数据往往包含大量冗余 HTML/JSON。需要清洗并转换为极简格式后再填入上下文，避免浪费计算资源。

---

## 6. 上下文窗口预算与配额管理（Context Window Budgeting）

![窗口预算控制图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c345a35-7c26-40ad-bafe-3cb9b396a319_1478x1371.gif)

按比例分配系统 Prompt、历史记录、检索文档和输出留白（Reserve for Generation）。

![MCP 协议接入架构图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F351b396c-aca5-46f9-9f98-0fa8541e764c_957x266.png)

![网络架构拓扑图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3275ca7-7198-4d6c-be2f-a60c0edad4d2_960x955.gif)

![模型通信流图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c38b38e-7c30-4a2e-a39f-a023d6092076_1024x559.png)

![MCP 工具标准协议对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40f3cb2a-84b5-4556-8bcc-026f43f393d9_1024x559.png)

通过结合 MCP（Model Context Protocol）协议，将传统工具调用的 $N 	imes M$ 点对点工程转化为标准的 $N + M$ 协议对接，实现了上下文基础设施的大幅简化。

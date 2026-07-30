---
title: "Fine-tune any LLM directly from Claude!"
source: "https://mail.google.com/mail/u/0/#inbox/19f6174c7b5adc67"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-14
created: 2026-07-30
description: "介绍由开源 mcp-use SDK 构建的 Hugging Face 微调 Studio MCP App，支持直接在 Claude 界面中配置 LoRA、量化、Batch Size 等参数，并调用 HF AutoTrain 执行大模型微调与推理对话。"
tags:
  - clippings
---

# 直接在 Claude 中微调任意大语言模型（Fine-tune any LLM directly from Claude!）

我们构建了一个 **Hugging Face 微调 Studio**（Hugging Face Fine-tuning Studio），允许你直接在 Claude 界面中微调任意大语言模型（LLM）。

![Hugging Face Fine-tuning Studio MCP App 架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84d76d6d-fed8-4d68-927c-59f502d9ed26_1206x849.png)

该应用连接至 Hugging Face Hub 用于模型与数据集搜索。它能自动处理训练数据的 Chat Template 格式化，并允许你直接在 Claude 中配置 LoRA Rank、量化（Quantization）、Batch Size 以及学习率（Learning Rate）。

实际训练任务通过 AutoTrain 在 Hugging Face 的 GPU 云端基础设施上高效运行。

一旦训练完成，你还可以直接在 Claude 中与微调后的模型（或 HF 上的任意其他 LLM）进行实时对话测试。

---

### 基于 mcp-use SDK 开发

该 Studio 是基于 **[mcp-use SDK](https://github.com/mcp-use/mcp-use)** 构建的——这是一个用于为 Agent 开发 MCP Apps 的开源全栈框架。

在 mcp-use 框架中，**任何 MCP 工具都可以与一个 UI 组件相关联**：

* 你定义一个 Tool Handler，创建一个 React 组件。
* mcp-use 框架会自动处理工具注册、服务器与 Widget 之间的 Prop 属性映射、代码打包以及开发过程中的热重载（Hot Reload）。

这些 UI 组件完全遵循 MCP Apps 标准（受 OpenAI Apps SDK 启发）。

你可以访问 GitHub 仓库获取完整源码：
* [mcp-use 框架 GitHub 仓库](https://github.com/mcp-use/mcp-use)
* [Fine-tuning Studio 示例代码](https://github.com/patchy631/ai-engineering-hub/tree/main/finetune-studio-mcp-app)

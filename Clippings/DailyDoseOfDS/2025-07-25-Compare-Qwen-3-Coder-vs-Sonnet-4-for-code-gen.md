---
title: "比较 Qwen 3 Coder 与 Sonnet 4 的代码生成能力"
source: "https://mail.google.com/mail/u/0/#inbox/198434ae8570344d"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-07-25
created: 2026-07-30
description: "使用 LiteLLM、GitIngest 与 DeepEval 构建代码生成评测管线；邮件报告中，Qwen 3 Coder 在多项 MCP Server 任务中整体优于 Claude Sonnet 4。"
tags:
  - clippings
---

# 比较 Qwen 3 Coder 与 Sonnet 4 的代码生成能力

![Qwen 3 Coder 与 Sonnet 4 的对比图](https://substack-post-media.s3.amazonaws.com/public/images/75926547-c0fa-4917-ae8a-e807e6f6ba94_680x635.png)

Qwen-3 Coder 被邮件称为阿里巴巴最强的开源代码大模型。本文所述流程将它与 Claude Sonnet 4 对比，使用的组件为：

- [LiteLLM](https://www.litellm.ai/)：开源编排工具；
- [DeepEval](https://github.com/confident-ai/deepeval)：开源评测工具；
- Anthropic Claude Sonnet 4 与 Qwen 3 Coder：待比较的 LLM；
- [OpenRouter](https://openrouter.ai/)：本次演示中访问 Qwen 3 Coder 的渠道。

## 工作流

1. 摄取一个 GitHub 仓库，并将其作为两种 LLM 的上下文；
2. 让两个模型各自生成代码；
3. 使用 DeepEval 评估并比较生成结果。

## 实现要点

### 加载 API 密钥

Qwen 3 Coder 是开源模型；但这次演示通过 OpenRouter API 访问它。因此，将 OpenRouter 和 Anthropic 的 API 密钥存进 `.env` 文件，再加载到运行环境中。

### 摄取 GitHub 仓库

使用 GitIngest 将用户指定的 GitHub 仓库转换为适合 LLM 使用的纯文本数据，作为模型回答用户查询时的上下文。

### 建立评测指标

用 DeepEval 为任务定义三类指标：

- **代码正确性**：将生成代码的质量与正确性同参考的真实代码比较；
- **代码可读性**：检查格式、命名的一致性，以及帮助理解代码的注释和 docstring 的质量；
- **最佳实践**：检查代码是否模块化、高效，并实现了恰当的错误处理。

### 生成并评估回答

提示词中带入摄取后的代码库上下文，并行流式获取两个模型的回答。随后使用 GPT-4o 作为裁判 LLM，对两份回答计算上述指标，并为每项指标给出详细推理。

### Streamlit 界面

最后建立一个 Streamlit UI，在同一界面中方便地比较与评估两个模型。

## 测试结果

### 查询 1

**任务**：构建一个 MCP Server，监控 GitHub 仓库的新 issue 并发送到 Telegram 群组。

| 指标 | Sonnet 4 | Qwen 3 Coder |
| --- | ---: | ---: |
| 正确性 | 0.79 | 0.90 |
| 可读性 | 0.91 | 0.90 |
| 最佳实践 | 0.82 | 0.82 |

邮件结论：Qwen 3 Coder 胜出。

### 查询 2

**任务**：当有人把文件放入指定 Google Drive 文件夹时，构建一个 MCP Server 创建新的 Notion 页面。

| 指标 | Sonnet 4 | Qwen 3 Coder |
| --- | ---: | ---: |
| 正确性 | 0.74 | 0.84 |
| 可读性 | 0.90 | 0.91 |
| 最佳实践 | 0.73 | 0.78 |

邮件结论：Qwen 3 Coder 再次胜出。

## 更多评测的汇总

邮件作者还使用 DeepEval 对构建 MCP Server 的任务进行了另外 10 次评估：

- Qwen 3 Coder 获胜 9 次；
- Claude Sonnet 4 获胜 1 次，但该次的正确性得分更低；
- 在这些测试中，Qwen 3 Coder 的正确性分数持续高于 Sonnet 4。

这些结论仅反映邮件所述的评测设置与结果，并不构成对所有代码生成任务的普遍排名。

## 代码

- [本期 newsletter 的示例代码](https://github.com/patchy631/ai-engineering-hub/tree/main/sonnet4-vs-qwen3-coder)

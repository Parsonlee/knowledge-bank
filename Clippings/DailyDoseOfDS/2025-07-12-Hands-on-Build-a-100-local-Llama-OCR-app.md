---
title: "实操：构建 100% 本地运行的 Llama OCR 应用"
source: "https://mail.google.com/mail/u/0/#inbox/1980063d889e559c"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-07-12
created: 2026-07-30
description: "使用 Ollama 与 Llama-3.2 Vision 构建本地 OCR：输入图像，由多模态模型转换为结构化 Markdown，并封装为 Streamlit 应用。"
tags:
  - clippings
---

# 实操：构建 100% 本地运行的 Llama OCR 应用

本示例展示如何构建一个 Llama OCR 应用：它接受图像输入，并借助 Llama-3.2 多模态 LLM 将图像转换为结构化 Markdown。

完整代码（含 Streamlit）位于 [GitHub 的 `llama-ocr` 目录](https://github.com/patchy631/ai-engineering-hub/tree/main/llama-ocr)。

## 操作步骤

1. 前往 [Ollama 官网](https://ollama.com/)，选择操作系统并按说明安装。
2. 下载 `Llama3.2-vision`。

![下载 Llama3.2 Vision 的示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F753959ad-6278-4cdb-987b-7c004cc91d91_2008x676.jpeg)

3. 下载 Ollama Python 包。

![安装 Ollama Python 包的示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70c601cb-bf78-42f5-b1cc-6c2014cc1c17_1456x676.jpeg)

4. 按下图所示使用 Ollama 向 `Llama3.2-vision` 提示图像内容。

![向 Llama3.2 Vision 发送 OCR 提示的示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e79d325-4482-4cfa-acfe-6a38a72cb7bf_3200x1892.jpeg)

完成后，将该流程封装进 Streamlit 应用即可得到演示效果。邮件提供了[视频预览](https://api.filekitcdn.com/e/k7YHPN24SoxyM8nGKZnDxa/5rskya9M4qZV3udSUghdNT/player)。

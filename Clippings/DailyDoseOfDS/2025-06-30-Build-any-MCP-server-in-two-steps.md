---
title: "两步构建任意 MCP 服务器"
source: "https://mail.google.com/mail/u/0/#inbox/197c270c599ab371"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-06-30
created: 2026-07-30
description: "邮件推广了一种借助 GitIngest、FastMCP 与 Factory Droids 生成 MCP 服务器代码的两步流程。"
tags:
  - clippings
---

# 两步构建任意 MCP 服务器

> **广告 / 推广内容**：本节由邮件推荐 FactoryAI，以下保留原邮件所述流程与主张，不代表独立验证。

邮件给出的构建 MCP（Model Context Protocol）服务器的最简流程只有两步：

1. 使用 GitIngest 下载 [FastMCP 仓库](https://github.com/jlowin/fastmcp)；
2. 将仓库交给 [FactoryAI](https://www.factory.ai/)，并明确说明要构建哪一种 MCP 服务器。

邮件称，Factory 的 Droids 可以处理完整工作流，产出可用于生产的代码，以及 README、使用说明和错误处理等内容。

作者展示了一次测试：要求 Droids 在 Factory 中构建一个股票分析 MCP 服务器。邮件称，该次运行在无需继续追问的情况下完成，且没有报错，同时生成了 README、使用指南并实现了错误处理。

- [在 Factory 中构建 MCP 服务器](https://www.factory.ai/)

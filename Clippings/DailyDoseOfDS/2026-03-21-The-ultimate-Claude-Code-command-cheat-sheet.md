---
title: "The ultimate Claude Code command cheat sheet."
source: "https://mail.google.com/mail/u/0/#inbox/19d11dddb3bc89bd"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-21
created: 2026-07-30
description: "整理并解析 Claude Code 终极命令行指令速查表，涵盖日常开发中被忽视但极为高效的内置命令与扩展操作技巧。"
tags:
  - clippings
---

# Claude Code 终极命令行指令速查指南（The ultimate Claude Code command cheat sheet.）

在日常软件工程与 AI 辅助开发中，Claude Code 已经成为提升开发效率的核心工具。然而，普通开发者与高效 AI 工程师之间的巨大鸿沟，往往在于是否能够熟练使用隐藏在 `/help` 中的命令行内置指令。

将 Claude Code 从一个简单的聊天对话框升级为可编程的终端协同伙伴，指令掌握是关键突破口。

![Claude Code 终极命令行速查表顶部看板](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea1e3c2a-3f51-4a56-b980-4749cf7e95ef_416x122.png)
*图 1：Claude Code 终极命令行速查指南*

---

### 一、 核心基础控制指令

![Claude Code 基础控制与会话管理指令集](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51147900-aa18-4967-a246-1a4a757b9e3a_393x64.png)
*图 2：Claude Code 基础控制与会话管理指令集*

- `/help`：查看所有可用的命令行工具、斜杠指令及环境参数。
- `/compact`：压缩当前会话上下文，在保留关键上下文的同时清理冗余历史，避免触及 Token 上限。
- `/clear`：重置当前上下文会话，开启全新的任务讨论。
- `/cost`：实时查看当前会话消耗的 Token 数量以及估计花费（包含 Prompt Tokens 与 Completion Tokens）。

---

### 二、 高级调试与工程管理指令

![Claude Code 终极速查表全景图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e5c94fc-0c59-4484-81d1-a955dc8c7c53_2240x1216.png)
*图 3：Claude Code 终极速查表全景图解与分类归纳*

- `/doctor`：运行环境健康检查，排查 CLI 依赖、API Key 授权、Git 状态及文件权限问题。
- `/config`：交互式配置全局与项目级首选项（如模型版本、工具调用权限控制等）。
- `/init`：在当前代码仓库初始化 `CLAUDE.md` 项目工程规范文件，指导 AI 遵守架构约定与 Build/Test 命令。
- `/bug`：捕获当前环境中的异常状态并生成结构化 Bug 报告。

### 三、 生产实践建议

建议开发者不要尝试一次性记住所有指令，而是将本速查表收藏，并在每周的学习工作流中增量掌握 1~2 个斜杠指令，逐步将 Claude Code 的终端协作效率提升至极致。

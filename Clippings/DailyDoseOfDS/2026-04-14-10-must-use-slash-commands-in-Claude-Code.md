---
title: "10 must-use slash commands in Claude Code"
source: "https://mail.google.com/mail/u/0/#inbox/19d8df42bfdf06fb"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-14
created: 2026-07-30
description: "详细解读 Claude Code CLI 工具中最实用、提高开发效率的 10 个斜杠命令（Slash Commands），涵盖环境初始化、审查、问题诊断与上下文管理。"
tags:
  - clippings
---
# Claude Code 中必知的 10 个斜杠命令（10 must-use slash commands in Claude Code）

在终端环境中配置 Shell 别名（Alias）是大多数开发者的本能习惯。

在使用 Anthropic 推出的 CLI 工具 **Claude Code** 时，灵活运用**斜杠命令（Slash Commands）**同样是倍增开发效率的核心手艺。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1908fc0-67d9-4c76-9b4a-ad7f2f9d6019_1108x552.png)

以下是 10 个不可不知的经典斜杠命令：

1. **`/init`**：初始化当前项目，生成 `.claudecode` 配置文件与架构指导规则。
2. **`/bug`**：快捷归集并提交系统缺陷报告。
3. **`/review`**：自动拉取 Git Diff 对当前改动进行全面的 Code Review。
4. **`/compact`**：压缩并清理当前对话历史，释放 Context Window（上下文窗口）。
5. **`/cost`**：实时查询当前会话已消耗的 Token 数量以及对应美元账单。
6. **`/doctor`**：诊断当前运行环境、依赖组件与 API 连通性状态。
7. **`/terminal-setup`**：配置终端适配、交互快捷键与主题显示。
8. **`/login` / `/logout`**：账号身份认证与 Token 鉴权切换。
9. **`/help`**：调出内置帮助文档与所有可用的命令列表。
10. **自定义命令与扩展**：允许团队通过定义快捷 Prompt 别名建立标准化工作流。

---
title: "你的 Claude Code 配置缺少了什么（What your Claude Code setup is missing.）"
source: "https://mail.google.com/mail/u/0/#inbox/19e6b1b1a122a14a"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-27
created: 2026-07-30
description: "探讨在生产环境故障排查中，为什么需要 CodeRabbit Agent 这样能连接全栈工具和上下文的代理，而不仅是单纯的代码代理。"
tags:
  - clippings
---

# 你的 Claude Code 配置缺少了什么（What your Claude Code setup is missing.）

当生产环境发生故障时，修复方法通常很简单。困难的是故障发生前的 30 分钟，你需要在 Datadog、GitHub、Cloud Run 日志和 Slack 历史记录之间来回跳转，试图找出改变了什么以及为什么。

Claude Code 在这里帮不上忙。它无法查看 APM 追踪、工单历史，也不知道团队上个月做了什么决定。

CodeRabbit Agent 驻留在 Slack 中，并连接到你的代码、工单、文档、监控堆栈和云基础设施。你在一个线索中提到它，它就会拉取追踪数据，交叉引用最近的 PR，打开针对性的修复，并归档事后分析报告。整个事件保存在一个线索中，团队可以看到每一个步骤。

它还保留了团队在不同对话中做出的决定，因此下一次发生故障时不需要重新推导相同的上下文。

新工作空间可获得每位用户 50 美元的免费代理时长。

开始使用 CodeRabbit Agent →

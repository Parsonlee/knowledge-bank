---
title: "将生产环境中的AI组件追踪至确切的代码行（Trace AI components in production to their exact line.）"
source: "https://mail.google.com/mail/u/0/#inbox/19f86be0631f8e2c"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-21
created: 2026-07-30
description: "Checkmarx AI Inventory 提供针对生产环境中 AI 组件（开源模型、LLM API、MCP 服务器等）的治理能力，支持确定性地编目并追踪至具体文件和代码行。"
tags:
  - clippings
---

# 将生产环境中的AI组件追踪至确切的代码行（Trace AI components in production to their exact line.）

现代代码库中的每一个依赖都会出现在清单 (manifest) 中，但 AI 相关的依赖除外。

开源模型、LLM API、MCP 服务器和代理都通过与普通软件包相同的 pull requests 进入生产环境，但没有锁文件（lockfile）会列出它们，也没有依赖扫描器能看到它们。

Checkmarx 发现，70% 的团队预计会在生产环境中使用 AI 组件，而其中 43% 对这些组件毫无治理手段。

Checkmarx AI Inventory（隶属于 Checkmarx One）确定性地对每一个模型、SDK 和 MCP 服务器进行编目，将每一个都追踪至确切的文件和代码行，并导出 AI-BOM 用于合规审计。

Gartner 在其首份软件供应链安全魔力象限报告中将 Checkmarx 命名为领导者。

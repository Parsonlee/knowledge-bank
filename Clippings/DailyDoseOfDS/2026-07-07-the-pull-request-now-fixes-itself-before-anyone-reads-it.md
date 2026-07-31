---
title: "PR 现在在被任何人读取之前就能自动修复（The pull request now fixes itself before anyone reads it.）"
source: "https://mail.google.com/mail/u/0/#inbox/19f3d7ecdb9a83ee"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-07-07
created: 2026-07-30
description: "介绍了 Sonar 旗下的 Gitar，它提供 AI 原生的代码审查和修复功能，能在 PR 阶段利用上下文发现并自动修复代码问题。"
tags:
  - clippings
---

# PR 现在在被任何人读取之前就能自动修复（The pull request now fixes itself before anyone reads it.）

代码审查通常假设作者理解了代码库。但 AI Agent 并没有这个假设。

它编写的代码能够编译通过并通过明显的检查，足以提交 commit。

代码真正的问题往往稍后在 CI 中浮现，而那时你可能已经在它的基础上继续构建了。

Gitar，一款 AI 原生的代码审查和修复产品（现已被 Sonar 收购），专为在 Pull Request（PR）中发现和修复问题而构建。

它结合代码库的上下文（不仅仅是 diff 差异）来阅读代码变更，能够捕捉到语法扫描会遗漏的 bug。

当它发现问题时，会编写一个补丁并在你的 CI 中运行它。直到构建通过，它才算完成工作。

Sonar 将整个循环称为“以 Agent 为中心的开发周期”（Agent Centric Development Cycle，简称 AC/DC）。

Agent 编写代码，Sonar Vortex 引擎在同一会话中进行验证，然后 Gitar 在 PR 阶段修复存在的问题。

不需要人类首先对评论采取行动。

运行这种组合的团队发现，与 AI 生成代码相关的中断事故减少了 44%。

Token 的使用量也下降了高达 36%，因为 Agent 花在重新解析一个没有堆积混乱的代码库上的时间更少了。

---
title: "Agent Memory 与 State 完全是两回事！"
date: 2026-07-27
author: "Avi Chawla & Akshay Pachaar"
source: "https://mail.google.com/mail/u/0/#inbox/19fa5754b2a0ee28"
type: clipping
---

# Agent Memory 与 State 完全是两回事！

如果一个 Agent 忘记了它已经学到的知识，这是一个记忆（Memory）问题；如果它在执行任务的中途忘记了自己处于什么阶段并重新开始，这则是一个状态（State）问题。

我们在测试过程中曾在一个 Agent 执行任务中途强行将其终止，结果再次启动时，它就像之前什么都没发生过一样重新从头执行。正是在那一刻我们意识到：我们一直将两个完全不同的问题混为一谈了。

## State（状态）

状态绑定于当前单次任务运行，代表 Agent 当前正在处理什么任务以及已经找到了什么信息。除非有明确的机制将其持久化记录下来，否则这些信息不会自动保留。

解决方案：在 Agent 每一个已完成的步骤之后添加一个检查点（Checkpoint）来记录进度。这样即使进程挂掉，重新启动时也能从上次断开的精准节点继续执行，而不需要从头再来。

## Memory（记忆）

记忆则是另一码事。它是跨多次任务运行依然存活的经验，包含值得保留的事实、教训与结论。

起初，我们为所有 Agent 使用同一个共享记忆库，认为这已经足够。但很快发现问题：Agent 开始相互读取对方的发现，并将其误认为是自己的研究结论。

解决方案：为每个 Agent 赋予独立的记忆作用域（Scope），例如通过 memory = memory.scope("/agent") 明确隔离。

## 核心要点总结

将 Memory 与 State 明确区分为两个独立的问题。

当发现不应共享时，按 Agent 独立隔离 Memory 作用域。

在每个已完成的任务步骤后写入 Checkpoint（检查点）。

中断运行后，从最新的 Checkpoint 恢复执行。

支持将 Checkpoint 分叉（Fork）出新分支，无需重复之前的执行过程。

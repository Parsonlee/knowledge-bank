---
title: "Anthropic再发Agent神文：像人类工程师一样思考，解决「长程任务」难题"
source: https://mp.weixin.qq.com/s/tmXg0tguoZZplDZMaJWlJQ
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# Anthropic再发Agent神文：像人类工程师一样思考，解决「长程任务」难题

> [!quote]
> 1. 功能列表（Feature List）
> 为了防止Agent一次性蛮干或过早结束，初始化Agent被要求编写一个包含所有功能需求的详细文件。在claude.ai克隆案例中，这包含超过200个功能点。
> 这些功能最初都被标记为“failing”（未通过），为后续Agent提供了清晰的工作全景图
> JSON文件示例：
> {
> "category": "functional",
> "description": "New chat button creates a fresh conversation",
> "steps": [
> "Navigate to main interface",
> "Click the 'New Chat' button",
> "Verify a new conversation is created",
> "Check that chat area shows welcome state",
> "Verify conversation appears in sidebar"
> ],
> "passes": false
> }
> 实验发现，使用JSON格式优于Markdown，因为模型不太容易错误地更改或覆盖JSON文件。同时，提示词需包含强硬指令，禁止删除或编辑测试，只允许更改passes字段的状态

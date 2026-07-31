---
title: "结合 Claude Fable 5 在规则内进行构建（Building inside the lines with Claude Fable 5.）"
source: "https://mail.google.com/mail/u/0/#inbox/19eb880a3ed57fd8"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-11
created: 2026-07-30
description: "当智能体能自主运行数小时并执行数据库修改等操作时，安全与权限控制必须在运行环境中得到保障。将 Claude Fable 5 部署在 Retool 等平台上，可以有效解决身份验证、权限校验及审计日志的问题。"
tags:
  - clippings
---

# 结合 Claude Fable 5 在规则内进行构建（Building inside the lines with Claude Fable 5.）

我们花了很多时间体验 Claude Fable 5，这让我们思考起一个问题：当一个智能体自主运行时，它究竟被允许做些什么？

Fable 5 能够连续运行数小时，数天维持一个目标，并且在不向人类汇报的情况下采取行动。因此，问题已经不再是一个智能体能“构建”什么，而是它在运行时能“触碰”到什么。

我们通过一个简单的内部工具测试了这一点。

Fable 5 一次性编写了 SQL、拉取了真实记录，并添加了一个直接向数据库发起退款的按钮。

构建过程十分简单，但是决定谁能打开这个工具、谁有权限执行退款操作，以及记录所发生事情的审计日志，这些是模型本身无法独自处理的部分。

这部分能力存在于运行环境（runtime）中，而不是模型里。

我们将同一个智能体部署到了 Retool 中，它随即获得了公司 SSO 登录、退款操作的角色权限检查，以及对每个查询和操作的审计日志记录。应用本身没有改变，但是它运行的环境变了。

Retool 将这种方式称为“在规则内构建（building inside the lines）”，一旦你观察了同一个智能体在两种方式下的运行对比，你就会发现其中的显著差异。

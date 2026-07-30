---
title: "Anatomy of the .claude/ folder"
source: "https://mail.google.com/mail/u/0/#inbox/19d1c347f366b9ac"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-23
created: 2026-07-30
description: "全面剖析 Claude Code 项目中的 .claude/ 目录结构，详解 CLAUDE.md、rules/、commands/、skills/、agents/ 和 settings.json 的配置最佳实践。"
tags:
  - clippings
---
# .claude/ 文件夹的剖析（Anatomy of the .claude/ folder）

![.claude 文件夹全景](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc772fb7f-94c1-42e6-83f9-c040ab875309_1068x600.png)

对于许多 Claude Code 用户来说，项目根目录下的 `.claude` 文件夹就像一个黑盒——大家都知道它的存在，但鲜有人主动打开它并搞清楚里面每个文件的作用。

实际上，**`.claude` 文件夹是调教和控制 Claude Code 在你项目中行为的指挥中心。** 它保存着团队规范、自定义斜杠命令、安全权限策略乃至跨 Session 的持久化记忆。

---

## 两个目录，而非一个

在深入细节前，首先需要区分两个不同的 `.claude` 目录：

![双目录示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b81cc25-df87-4ea8-a11b-9a719d5836b1_1166x1176.png)

1. **项目级目录（`<project-root>/.claude/`）**：存放团队共享配置，必须提交到 Git。确保团队中的每位成员拥有完全统一的编码规范、自定义命令与安全策略。
2. **全局用户级目录（`~/.claude/`）**：存放个人偏好设置与本地状态，如历史 Session 记录和自动记忆。

---

## `CLAUDE.md`：Claude 的核心操作手册

这是整个系统中最关键的文件。每次启动 Claude Code 会话时，系统读取的第一份文件就是 `CLAUDE.md`，并将其直接注入 System Prompt。

### 推荐写入的内容（Do's）：
* **构建、测试与 Lint 命令**：例如 `npm run test`, `make build`；
* **关键架构决策**：例如“我们使用 Turborepo 架构”；
* **非显性编码规定**：例如“TypeScript strict mode 开启，禁止使用 `any`”；
* **模块目录规范**：主模块的文件组织风格。

### 切勿写入的内容（Don'ts）：
* 应该由 Formatter/Linter 自动处理的代码格式细节；
* 冗长的外部文档抄录；
* 理论推导长篇大论。

> **最佳实践**：保持 `CLAUDE.md` 在 **200 行以内**。超出 200 行后不仅浪费 Context，模型的指令遵循率也会显著下降。

---

## `.claude/` 内部子目录结构拆解

![子目录结构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bddbd7c-d987-4c70-a38b-44db8104f8d7_680x369.png)

### 1. `CLAUDE.local.md`
用于覆盖个人本地的特殊指令（自动加入 `.gitignore`）。

### 2. `rules/` 目录
放置模块化的工程指令集，支持按文件路径或触发条件动态加载，避免单个 `CLAUDE.md` 过载。

### 3. `commands/` 目录
放置自定义的斜杠命令脚本（Slash Commands）。你可以定义 `/deploy` 或 `/check-api`，并支持传递动态参数。

### 4. `skills/` 目录
存放可复用的复杂工作流与 Agent 工具技能（Skills）。

### 5. `agents/` 目录
配置专门的 Subagent 人设（Personas），例如专精 Code Review、安全审计或文档撰写的分离角色。

### 6. `settings.json`
配置权限管控（Permissions）、自动批准命令白名单与工程设置。

---

## 总结

搞懂 `.claude/` 目录的解构，你就能把 Claude Code 从一个通用的代码生成助手，打造成完全契合你团队架构理念的自动化 AI 工程师。

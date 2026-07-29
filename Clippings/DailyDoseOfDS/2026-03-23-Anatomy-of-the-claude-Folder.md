---
title: Anatomy of the .claude/ Folder
source: https://mail.google.com/mail/u/0/#inbox/19d1c347f366b9ac
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-23
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 Anatomy of the .claude/ Folder 的原理剖析与工程实践。
tags:
  - clippings
---

# Anatomy of the .claude/ Folder

## 1. 核心要点解析

本期内容重点涵盖：
- **Anatomy of the .claude/ Folder**

## 2. 深度拆解与正文翻译

​Master Full-stack AI Engineering (

)​

----------------------
In today's newsletter:
----------------------

* ​Is AI actually saving your engineering team time?
* Anatomy of the .claude/ folder.

TODAY'S ISSUE

together with postman
---------------------

-----------------------------------------------------------------
​Is AI actually saving your engineering team time? (

)​
-----------------------------------------------------------------

Most teams have adopted AI in some form, but the gap between
“using AI” and “getting measurable ROI from AI” is larger than
people realize.

​Postman (

) released a cost savings analysis that looks at six common API
development workflows and benchmarks the actual time and cost
difference when AI is built into the platform versus bolted on
externally.

​
It’s a short, data-driven read that helps engineering leads make
the case for where AI-native tooling actually moves the needle.

​You can grab the guide for free here → (

)​

Claude code
-----------

------------------------------
Anatomy of the .claude/ folder
------------------------------

Claude Code users typically treat the .claude folder like a black
box. They know it exists. They’ve seen it appear in their project
root. But they’ve never opened it, let alone understood what
every file inside it does.

That’s a missed opportunity.

The .claude folder is the control center for how Claude behaves
in your project.

​
It holds your instructions, your custom commands, your permission
rules, and even Claude’s memory across sessions. Once you
understand what lives where and why, you can configure Claude
Code to behave exactly the way your team needs it to.

This newsletter walks you through the entire anatomy of the
folder, from the files you’ll use daily to the ones you’ll set
once and forget.

Two folders, not one
--------------------

Before diving in, one thing worth knowing upfront: there are
actually two .claude directories, not one.

The first lives inside your project, and the second lives in your
home directory:

​
The project-level folder holds team configuration. You commit it
to git. Everyone on the team gets the same rules, the same custom
commands, the same permission policies.

The global ~/.claude/ folder holds your personal preferences and
machine-local state, like session history and auto-memory.

CLAUDE.md: Claude’s instruction manual
--------------------------------------

This is the most important file in the entire system. When you
start a Claude Code session, the first thing it reads is
CLAUDE.md. It loads it straight into the system prompt and keeps
it in mind for the entire conversation.

Simply put: whatever you write in CLAUDE.md, Claude will follow.

If you tell Claude to always write tests before implementation,
it will. If you say “never use console.log for error handling,
always use the custom logger module,” it will respect that every
time.

A CLAUDE.md at your project root is the most common setup. But
you can also have one in ~/.claude/CLAUDE.md for global
preferences that apply across all projects, and even one inside
subdirectories for folder-specific rules. Claude reads all of
them and combines them.

What actually belongs in CLAUDE.md
----------------------------------

Most people either write too much or too little. Here’s what
works.

Write:
------

* Build, test, and lint commands (npm run test, make build, etc.)
* Key architectural decisions (”we use a monorepo with
Turborepo”)
* Non-obvious gotchas (”TypeScript strict mode is on, unused
variables are errors”)
* Import conventions, naming patterns, error handling styles
* File and folder structure for the main modules

Don’t write:
------------

* Anything that belongs in a linter or formatter config
* Full documentation you can already link to
* Long paragraphs explaining theory

Keep CLAUDE.md under 200 lines. Files longer than that start
eating too much context, and Claude’s instruction adherence
actually drops.

Here’s a minimal but effective example:

​
That’s ~20 lines. It gives Claude everything it needs to work
productively in this codebase without constant clarification.

CLAUDE.local.md for personal overrides
--------------------------------------

Sometimes you have a preference that’s specific to you, not the
whole team. Maybe you prefer a different test runner, or you want
Claude to always open files using a specific pattern.

Create CLAUDE.local.md in your project root. Claude reads it
alongside the main CLAUDE.md, and it’s automatically gitignored
so your personal tweaks never land in the repo.

​

The rules/ folder: modular instructions that scale
--------------------------------------------------

CLAUDE.md works great for a single project. But once your team
grows, you end up with a 300-line CLAUDE.md that nobody maintains
and everyone ignores.

The rules/ folder solves that.

Every markdown file inside .claude/rules/ gets loaded alongside
your CLAUDE.md automatically. Instead of one giant file, you
split instructions by concern:

​
Each file stays focused and easy to update. The team member who
owns API conventions edits api-conventions.md. The person who
owns testing standards edits testing.md. Nobody stomps on each
other.

The real power comes from path-scoped rules. Add a YAML
frontmatter block to a rule file and it only activates when
Claude is working with matching files:

​
Claude won’t load this file when editing a React component. It
only loads when it’s working inside src/api/ or src/handlers/.
Rules without a paths field load unconditionally, every session.

This is the right pattern once your CLAUDE.md starts feeling
crowded.

The commands/ folder: your custom slash commands
------------------------------------------------

Out of the box, Claude Code has built-in slash commands like
/hel

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

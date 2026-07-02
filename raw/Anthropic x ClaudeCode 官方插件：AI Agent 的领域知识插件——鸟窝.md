---
title: Anthropic 官方插件：AI Agent 的领域知识插件
source: https://colobu.com/2026/06/28/anthropic-official-plugins-domain-knowledge-ai-agent/
author:
  - 鸟窝
published: 2026-06-28
created: 2026-06-29
description:
tags:
  - Skill/claude-code
---
\## 目录 \[−\]

> "The decisive result came not from the model alone, but from the harness around it."  
> 决定成败的不仅是模型本身，更是其配套的外围系统。
> 
> ——Anthropic Harness Engineering Team

第 2 章讲了 Skills 系统——Matt Pocock 的工程哲学：一个 Markdown 文件定义一种行为，小而可组合。第 6 章讲了 superpowers——社区级 Skills 库，十四个 Skill 覆盖十四个场景。

Anthropic 自己为 Claude Code 开发了 13 个官方插件。截至 2026 年 5 月，全部放在 Claude Code 仓库的 `plugins/` 目录下。和社区 Skills 不同，这些插件是 Anthropic 工程师为 Claude Code 构建的第一方工具——通过 `/plugin` 安装，深度集成到 hooks、agents、skills 三层基础设施中。

**安装。** 所有 13 个插件通过同一命令安装：

```
/plugin install code-review
```

`/plugin install <name>` 从 Anthropic 官方源拉取插件，注册斜杠命令、hooks 和 Agent。 `/plugin marketplace add` 可添加第三方源。安装后插件在 `~/.claude/plugins/` 下，可手动编辑配置。

\## 12.1 为什么需要领域知识插件

Skill 是原子能力——"做 TDD""做代码审查""对齐需求"。Skill 告诉你 Agent 能做什么。

但 Skill 不回答另一个问题： **Agent 应该知道什么。**

一个没有领域知识的编码 Agent 等同于一个刚入职的工程师。它会写代码，但不知道你的项目在用 JWT 还是 Cookie 做认证、SQL 用 Postgres 还是 MySQL、错误处理是抛异常还是返回 Result。它只能靠 grep 猜。

CLAUDE.md 是补这个缺口的基础设施——项目上下文在会话启动时自动注入（第 10 章的 SessionStart hook）。但 CLAUDE.md 是静态文件。它不会主动扫描你的代码库、不会对比你的编码规范、不会在 PR 合并前自动跑审查规则。

领域知识插件让 CLAUDE.md 里的规矩活起来。code-review 插件读你的 CLAUDE.md，对照每一条规范检查 PR 改动。feature-dev 插件读你的代码库架构，基于已有模式生成三个备选方案。security-guidance 插件在你编辑任何文件时静默监控 9 个安全风险大类。

十三个插件，做的都是同一件事：把静态的领域知识变成执行时的动态检查。

\## 12.2 十三个官方插件全景

Claude Code 的 `plugins/` 目录下目前有 13 个插件，通过 `/plugin` 命令管理。每个插件都由 `.claude-plugin/plugin.json` 定义元数据，由 commands（斜杠命令）、agents（专门 Agent）、skills（技能）、hooks（事件钩子）四种机制组合构成。

[![](https://colobu.com/images/image-20260531232015980.png)](https://colobu.com/images/image-20260531232015980.png)

| 插件 | 命令 | 核心机制 | 定位 |
| --- | --- | --- | --- |
| **code-review** | `/code-review` | 4 个并行 Agent + 0-100 信心评分 | PR 自动审查 |
| **feature-dev** | `/feature-dev` | 7 阶段引导 + 3 个专门 Agent | 功能开发全流程 |
| **pr-review-toolkit** | `/pr-review-toolkit:review-pr` | 6 个可组合审查 Agent | 细粒度 PR 审查 |
| **commit-commands** | `/commit`, `/commit-push-pr` | Git 工作流自动化 | 提交/推送/创建 PR |
| **hookify** | `/hookify` | 对话分析 → hook 生成 | 行为护栏自动创建 |
| **security-guidance** | PreToolUse hook（自动） | 9 类安全规则实时监控 | 静默安全守护 |
| **ralph-wiggum** | `/ralph-loop` | Stop hook 拦截退出 | 自主循环开发 |
| **plugin-dev** | `/plugin-dev:create-plugin` | 8 阶段引导 + AI 辅助 | 插件开发工具包 |
| **frontend-design** | 自动触发 Skill | 设计指南注入 | 前端界面设计 |
| **agent-sdk-dev** | `/new-sdk-app` | 项目脚手架 + 2 验证 Agent | Agent SDK 开发 |
| **claude-opus-4-5-migration** | 自动触发 Skill | 代码/prompt 自动迁移 | 模型版本迁移 |
| **explanatory-output-style** | SessionStart hook（自动） | 教育性上下文注入 | 理解实现选择 |
| **learning-output-style** | SessionStart hook（自动） | 决策点互动提问 | 交互式学习 |

插件之间可组合。feature-dev 走完七个 Phase，code-review 在合入前扫一遍 PR。security-guidance 全程静默运行——Agent 执行危险操作前才被感知。

\## 12.3 /code-review：本地 diff 审查

`/code-review` 由 Boris Cherny（Claude Code 的创建者）开发。在 Claude Code 会话中直接审查当前 diff。

[![](https://colobu.com/images/image-20260531232526789.png)](https://colobu.com/images/image-20260531232526789.png)

用法：

- `/code-review` — 审查当前 diff，报告正确性 bug 和代码效率、简化机会。无需安装 GitHub App，在任何 Claude Code 会话中都能运行
- `/code-review --comment` — 将发现作为内联 PR 评论发布
- `/code-review --fix` — 审查后自动将修复应用到工作树
- `/code-review ultra --fix` — 云端运行 deeper ultrareview，结果返回后应用修复

降低 effort level 返回更少但更高可信度的发现； `high` 到 `max` 覆盖更广，可能返回不确定的发现。不传 effort 参数时使用会话当前的 effort。可传路径或 PR 引用审查特定目标。

v2.1.147 之前命令名为 `/simplify` （默认应用修复）。v2.1.154 起 `/simplify` 改为仅做清理审查——只应用修复，不找 bug。之前用 `/simplify` 做 bug 查找的脚本应切换到 `/code-review --fix` 。

**自定义审查行为。** 两个文件控制审查器的行为。

`CLAUDE.md` — 项目共享指令。审查器读它作为项目上下文，把新增违规标为 nit。双向生效：如果 PR 改了代码导致 `CLAUDE.md` 陈述过时，审查器也会标记。

`REVIEW.md` — 根目录的审查专用覆盖文件，注入到审查管道中每个 Agent 的系统提示中，优先级最高。纯明文指令。典型用途：重新定义哪些问题算 Important 级别、限制 Nit 发现数量上限、跳过特定路径（生成代码、锁文件、vendored 依赖）、添加仓库特定检查（"新 API 路由必须有集成测试"）、设置验证门槛（行为声明需 `file:line` 源码引用）、控制重审收敛（首审后只报 Important 级发现）、调整摘要格式。

审查结果包含每条 issue 的 GitHub 永久链接——完整 SHA + `\#L` 行号范围。

\## 12.4 feature-dev：7 阶段引导开发

`/feature-dev` 把一个功能从想法带到代码合并，分成七个阶段。插件作者是 Sid Bidasaria（Anthropic 工程师）。

[![](https://colobu.com/images/image-20260531233037492.png)](https://colobu.com/images/image-20260531233037492.png)

**Phase 1：需求澄清。** 对模糊需求提问。"你想解决什么问题？""有什么约束？"确认理解后再进入下一步。

**Phase 2：代码库探索。** 启动 2-3 个专门 Agent（ `code-explorer` ）并行探索不同维度——类似功能如何实现、相关区域架构、现有模式。每个 Agent 返回入口点（精确到 `文件:行号` ）、执行路径、关键组件、架构洞察和建议阅读的文件清单。Claude 阅读所有标注文件，生成全面摘要。

**Phase 3：澄清问题。** 结合代码库发现和需求，列出不明确的部分：边界条件、错误处理、集成点、向后兼容性、性能需求。关键规则： **回答全部问题之前不得进入设计阶段。**

**Phase 4：架构设计。** 启动 2-3 个专门 Agent（ `code-architect` ），每个走不同侧重：

- **最小改动方案** ——最大化重用已有代码，最小化文件变更
- **干净架构方案** ——关注可维护性和抽象优雅度
- **务实平衡方案** ——速度和质量折中

每个方案附详细取舍分析。Claude 给出推荐意见和原因，最终选哪个由你决定。

**Phase 5：实现。** 等你明确选择方案后，才开始写代码。严格遵循项目已有的命名、风格、模块边界惯例。每一步更新 todo 列表。

**Phase 6：质量审查。** 启动 3 个专门 Agent（ `code-reviewer` ）并行检查：简洁性/DRY/优雅度、Bug/正确性、惯例遵守/抽象设计。高优先级问题（信心 75-100）和中等问题（信心 50-74）分别列出，每个附精确的 `文件:行号` 引用和 CLAUDE.md 规范引用。所有测试通过后才允许进入下一步。

**Phase 7：总结。** 文档化：构建了什么、关键决策是什么、修改了哪些文件、建议的后续步骤。

七个阶段把"开发功能"从"一段 prompt + AI 出代码"变成了结构化的工程流程。第 4 章 Ralph Loop 的核心洞察——AI 说做完了不等于真的做完了——在 feature-dev 里体现为每个可能出问题的节点都设了等待点。需求摸清之前不设计。方案选定之前不实现。审查通过之前不总结。

\## 12.5 pr-review-toolkit：六维度细粒度审查

pr-review-toolkit 是可组合 PR 审查工具箱。和 code-review 的"给一个综合分数"不同，它做的是"挑出你最关心的一两个维度，深度查"。

`/pr-review-toolkit:review-pr` 支持七个可选开关： `--comments` （审查 comment 质量）、 `--tests` （审查测试覆盖）、 `--errors` （审查错误处理）、 `--types` （审查类型设计）、 `--code` （审查代码质量）、 `--simplify` （审查简化机会）、 `--all` （全维度）。

每个开关背后是一个专门 Agent——comment-analyzer、pr-test-analyzer、silent-failure-hunter（找静默失败）、type-design-analyzer、code-reviewer、code-simplifier。

和 code-review 的关系：code-review 是常规武器——每个 PR 自动跑，4 个 Agent 快速扫一遍。pr-review-toolkit 是特种工具——关键 PR 或安全敏感代码，选一两个最关心的维度深度审查。

\## 12.6 security-guidance：9 类安全规则静默守护

security-guidance 是唯一不需要手动触发的插件。安装后在 PreToolUse hook 上注册 9 条安全规则，在 Agent 编辑文件时静默检查：命令注入、XSS 注入、eval 使用、危险的 HTML 构造、pickle 反序列化、os.system 调用、SQL 注入、硬编码密钥、不安全随机数生成。

Agent 每次执行 Edit/Write/Bash 操作前，PreToolUse hook 比对这 9 条规则。匹配到危险模式时，hook 在 Agent 上下文中注入安全提醒——用引导而非强制。

hookify 是 security-guidance 的补充。security-guidance 的规则是 Anthropic 预定义的通用安全模式。hookify 从你自己的对话中学习特定的风险模式——conversation-analyzer Agent 扫描你和 Agent 的交互历史，自动生成对应的 hook 规则。

\## 12.7 其他插件

**frontend-design。** 自动触发 Skill，在前端工作时激活。引导 Agent 避开均匀间距、对称布局、标准配色的"AI 风"界面，注入设计约束：大胆排版、有意图的色彩、微交互、非对称布局。和第 5 章 gstack 的 `/plan-design-review` 目标一致——抵抗 AI Slop。

**explanatory-output-style 和 learning-output-style。** 通过 SessionStart hook 注入教育性上下文。前者为每个实现选择解释原因，后者在关键决策点提问、鼓励手写 5-10 行代码。

**commit-commands。** 三个 Git 快捷命令： `/commit` （生成 conventional commit 消息并提交）、 `/commit-push-pr` （推送并创建 PR）、 `/clean_gone` （清理远端已删除的本地分支）。

**agent-sdk-dev 和 plugin-dev。** Agent 开发者工具： `/new-sdk-app` 创建 Agent SDK 项目脚手架， `/plugin-dev:create-plugin` 用 8 阶段工作流辅助插件创建。

**claude-opus-4-5-migration。** 自动处理从旧模型迁移到 Opus 4.5 的代码和 prompt 变更。

\## 12.8 插件的共同设计模式

[![](https://colobu.com/images/image-20260531233736843.png)](https://colobu.com/images/image-20260531233736843.png)

十三个插件有几条共性：

**专用 Agent 并行审查。** code-review 用 4 个并行 Agent，feature-dev 在不同阶段启动 2-3 个探索 Agent 和 3 个审查 Agent，pr-review-toolkit 用 6 个独立审查 Agent。和第 7 章 autoresearch 的多 Agent 轮转审查逻辑一致——一个 Agent 看不到的东西，换个角度就能看到。包括Claude Code推出的Teams、dynamic workflows的理念一样，充分利用多 Agent 的特性。

**信心评分过滤。** code-review 的 0-100 评分 + 80 阈值是降噪策略。pr-review-toolkit 的 Agent 也使用类似的信心分类（高/中优先级）。"宁愿漏掉一个真问题，不要让十个假问题淹没一个真问题"——给 Agent 用的审查系统需要这个取舍，因为人对噪音的容忍度远低于 Agent。

**结构化阶段门控。** feature-dev 的 7 个 Phase 之间设有明确等待点——Phase 3 的回答、Phase 4 的方案选择、Phase 6 的问题处理。和第 5 章 gstack 的 PreToolUse hook 强制门控本质相同。

**hook + Agent 双引擎。** security-guidance 完全靠 PreToolUse hook 触发，explanatory-output-style 和 learning-output-style 通过 SessionStart hook 加载，hookify 从对话分析自动生成 hook 规则。第 10 章的 Harness Engineering 在这里是最直接的基层——hook 是插件行为的基础设施。

\## 12.9 与全书方法论的对接

| 全书方法论 | 在官方插件中的体现 |
| --- | --- |
| Skills 系统（第 2 章） | frontend-design、claude-opus-4-5-migration 是 Skill 的官方实现 |
| Ralph Loop（第 4 章） | ralph-wiggum 是 Stop hook 循环的第一方实现 |
| gstack（第 5 章） | feature-dev 的 7 阶段门控对应 gstack Sprint；frontend-design 的 AI Slop 检测对应 `/plan-design-review` |
| Harness Engineering（第 10 章） | security-guidance 的 PreToolUse hook、hookify 的自动 hook 生成 |
| Goal Workflow（第 8 章） | feature-dev + commit-commands 组合对应 Goal Workflow 的流水线 |
| autoresearch（第 7 章） | code-review 的 4 Agent 并行审查 + 信心评分对应多 Agent 交叉审查 |

\## 12.10 本章小结

Anthropic 的十三个官方插件是 Claude Code 的工具级"出厂配置"。

从使用角度看这些插件的角色：code-review（每个 PR 该跑，4 Agent 并行 + 80 分阈值过滤噪音）、feature-dev（需求模糊时用，7 阶段引导不允许在不确定状态下写代码）、pr-review-toolkit（需要盯特定维度时用——安全性、类型设计、静默失败）、security-guidance（该装完就忘掉它——静默守护，不需要手动跑）、commit-commands（日常 git 机械操作的自动化）。

共性设计模式——专用 Agent 多视角审查、高信心阈值过滤噪音、结构化阶段门控、hook 驱动的自动触发——第 2 章的 Skills、第 4 章的 Ralph Loop、第 5 章的 gstack、第 7 章的 autoresearch、第 10 章的 Harness Engineering 都能在这些插件中找到一一对应的工程实现。
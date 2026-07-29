title: Claude Code 必用的 10 个斜杠自定义命令（Slash Commands） source: https://mail.google.com/mail/u/0/#inbox/19d8df42bfdf06fb author:


* "[[DailyDoseOfDS]]" published: 2026-04-14 created: 2026-07-28 description: 解决反复输入 Prompt 导致的 Prompt Drift 问题：在 .claude/commands/ 中通过 Markdown 文件定义可版本控制的 Slash Commands，并支持 $ARGUMENTS 占位符与 !command 动态 Shell 上下文。 tags:
* clippings


________________


Claude Code 必用的 10 个斜杠自定义命令（Slash Commands）
开发者在终端里会习惯性配置 Shell Aliases，但在使用 Claude Code 时，很多人却每次都在重新凭记忆敲击 10-15 行的代码审查、单测生成或 Commit 检查指令。


这不仅浪费时间，还会带来 Prompt Drift（提示词漂移）——每次凭记忆输入的措辞差异会导致 LLM 输出质量不稳定。
Claude Code Custom Commands 工作原理
在项目的 .claude/commands/ 目录下创建一个 .md 文件，文件名即为斜杠命令名：


1. 动态参数：使用 $ARGUMENTS 接收命令后输入的参数（例如 /dissect src/auth.ts）。
2. 动态 Shell 上下文：使用 !git diff 或 !pytest 语法，Claude 会在处理 Prompt 之前先执行 Shell 命令并插入最新的输出。
3. YAML Frontmatter 预授权：可设置 allowed-tools 预批准工具权限，避免频繁弹出确认提示。


通过将 .claude/ 提交至 Git 仓库，团队所有成员均可共享并版本化这些最佳 Prompt 工作流。
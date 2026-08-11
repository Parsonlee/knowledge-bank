---
type: "concept"
tags:
  - Claude-Code
  - AI-Tools
  - Config-Architecture
sources:
  - "wiki/sources/2026-03-23_Anatomy-of-the-.claude-folder_19d1c3.md"
updated: "2026-08-03"
summary: "Claude Code 通过项目级与全局 .claude 目录分别管理团队和个人配置，并以 CLAUDE.md、rules、commands、skills、agents 及 settings.json 组织指令、工作流、子智能体和权限。"
---

# Claude Code 核心配置与原语

## 项目级与全局配置的差异
Claude Code 的配置体系通过两个不同的 `.claude/` 目录进行管理，分别应对团队协作和个人定制的需求：

| 配置级别 | 物理路径 | 主要作用 | 版本控制 |
| :--- | :--- | :--- | :--- |
| **项目级** | `<project-root>/.claude/` | 定义项目特有的规范、自定义命令、团队共享规则和权限策略。 | **推荐提交**至 Git 仓库，确保全员配置一致。 |
| **全局** | `~/.claude/` | 保存用户的个人偏好、本地机器状态、跨项目的会话历史以及自动记忆（Auto-Memory）。 | **不提交**至版本控制，属于本地私有配置。 |

此外，在项目根目录下可以使用被 gitignored 的 `CLAUDE.local.md` 和 `.claude/settings.local.json` 进行个人本地覆盖，避免污染团队共享文件。

## CLAUDE.md 的定位与限制
`CLAUDE.md` 是 Claude Code 启动时读取的首要指令手册。
* **定位**：其内容直接被加载进系统 Prompt，在整个会话中作为 Claude 的行为指南。它主要用于放置构建/测试命令、关键架构决策、防踩坑 gotchas 和命名规范。
* **限制**：建议**控制在 200 行以内**。超过此限制会导致 context 占用过多，且大模型的指令遵循度（instruction adherence）会显著下降。

## 五大核心配置模块机制

### 1. `rules/` (模块化指令)
* **机制**：允许在 `.claude/rules/` 目录下放置多个 Markdown 规则文件，避免单个 `CLAUDE.md` 过度膨胀。
* **路径匹配激活**：支持在规则文件的 YAML frontmatter 中声明 `paths` 字段（Glob 模式）。规则仅在 Claude 处理匹配路径的文件时被激活装载，从而节省上下文窗口。
```yaml
---
paths:
  - "src/api/**/*"
  - "src/handlers/**/*"
---
# API 规则正文
```

### 2. `commands/` (自定义斜杠命令)
* **机制**：在 `.claude/commands/` 目录下创建的 Markdown 文件，文件名即注册为斜杠命令（例如 `review.md` 注册为 `/project:review`）。
* **动态 Shell 嵌入**：可在 Markdown 文件中使用反引号加感叹号的语法（如 `!git diff`）嵌入并执行 Shell 命令，在调用时自动将命令输出注入到 Prompt 中。
* **参数传递**：使用 `$ARGUMENTS` 变量接收用户在命令后输入的参数（例如 `/project:fix-issue 234` 中的 `234`）。

### 3. `skills/` (智能触发技能)
* **机制**：与被动等待用户输入 slash命令的 `commands` 不同，`skills` 是基于 YAML 描述由 Claude 自主观察上下文并判断是否触发的打包工作流（以目录形式存在，内含 `SKILL.md` 和相关支撑文档）。
* **自主决策**：当用户提出的任务与 `SKILL.md` frontmatter 中定义的 description 匹配时，Claude 会自动加载该技能包并按照指导执行。

### 4. `agents/` (隔离 Persona 与工具)
* **机制**：通过在 `.claude/agents/` 下编写 Markdown 文件来定义特定的子智能体（subagent）角色。
* **资源与权限隔离**：
  * **工具限制**：可以通过 `tools` 字段显式限制该子智能体拥有的工具（例如只读权限）。
  * **模型配置**：可以为子任务指定不同模型（例如使用 Haiku 执行读取，保留 Sonnet 执行写入）。
  * **上下文隔离**：子智能体在独立的 Context Window 中运行，最终仅将精简后的结论汇报给主会话，极大节省了主会话的 token。

### 5. `settings.json` (白黑名单权限控制)
* **机制**：用来管理 Claude 自动执行工具时的权限。
  * **`allow` 列表**：允许免确认直接运行的命令/工具（如 `npm run test` 或特定文件读取）。
  * **`deny` 列表**：被绝对禁用且不予提示的破坏性指令或敏感路径（如 `rm -rf`，`.env` 等）。
  * **默认行为**：不在 `allow` 且不在 `deny` 的工具执行，Claude 会弹出确认提示供用户选择。

---
> 📎 **来源摘要**：[[wiki/sources/2026-03-23_Anatomy-of-the-.claude-folder_19d1c3.md]]

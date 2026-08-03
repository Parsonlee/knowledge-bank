---
type: "source"
tags:
  - Claude-Code
  - AI-Tools
  - Configuration
summary: "详细剖析 Claude Code 控制中心——`.claude/` 目录的结构和配置原语，涵盖 CLAUDE.md、规则系统、自定义命令、技能（skills）、智能体（agents）以及权限设置 settings.json 的机制。"
sources:
  - "raw/articles/2026-03-23_Anatomy-of-the-.claude-folder_19d1c3.md"
updated: "2026-08-03"
---

# Anatomy of the .claude/ folder

## 来源信息
- **主题**: Anatomy of the .claude/ Folder
- **来源**: Daily Dose of DS (avi@dailydoseofds.com)
- **发布日期**: 2026-03-23

## 核心要点
1. **控制中心定位**：`.claude/` 文件夹是 Claude Code 在项目中的控制中心，包含团队配置、自定义命令、权限规则和跨会话记忆。
2. **双目录架构**：
   - 项目级 `.claude/`：团队共享配置，需提交至 Git 仓库，确保团队规则一致。
   - 全局 `~/.claude/`：个人偏好和本地机器状态（如会话历史和自动记忆）。
3. **CLAUDE.md 指令手册**：首要加载文件，直接注入系统提示词。建议控制在 200 行以内，放置构建/测试/Lint指令、核心架构决策、防踩坑指南等关键信息。支持 `CLAUDE.local.md` 进行个人本地覆盖（已 gitignore）。
4. **模块化规则 (rules/)**：通过将规则拆分为独立的 Markdown 文件避免 CLAUDE.md 过度膨胀，并支持 YAML frontmatter 的 `paths` 字段进行路径激活范围限定。
5. **自定义 slash 命令 (commands/)**：文件名即命令名（如 `/project:review`），支持使用 backtick 语法嵌入运行 shell 命令（如 `` `git diff` ``）并将其输出嵌入 Prompt，支持 `$ARGUMENTS` 参数传递。
6. **主动触发技能 (skills/)**：不同于被动等待的命令，技能是基于 YAML 描述由 Claude 自主识别会话上下文并触发的包，能够携带多个辅助文件。
7. **隔离智能体 (agents/)**：通过 Markdown 定义专属 Prompt、限定 tools 权限（如只读）和指定轻量模型（如 Haiku）的 subagent persona，在大模型自主执行复杂任务时防止主上下文污染。
8. **权限控制 (settings.json)**：使用 JSON Schema 校验，通过 `allow` 列表和 `deny` 列表来精确配置免确认执行的工具（如 npm run, git read 等）与被绝对禁用的命令/路径（如 rm -rf, .env 等）。

## 关键引文
> "The `.claude` folder is the control center for how Claude behaves in your project."
> "Keep `CLAUDE.md` under 200 lines. Files longer than that start eating too much context, and Claude’s instruction adherence actually drops."
> "Commands wait for you. Skills watch the conversation and act when the moment is right."

## 关联概念与实体
- 概念: [[wiki/concepts/概念_Claude_Code核心配置与原语.md|Claude Code 核心配置与原语]]

---
> 📎 **物理文献**：[[raw/articles/2026-03-23_Anatomy-of-the-.claude-folder_19d1c3.md]]

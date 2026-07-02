---
type: source
tags:
- Skill/claude-code
summary: 字节笔记本整理的 Claude Code 2.0.40 版本后新增功能汇总，涵盖自定义输出样式、提示钩子模型参数、Git 命令扩展、[[概念_Subagent子代理|Subagent]]
  生命周期管理和 [[概念_Agent_Skills元工具架构|Skills]] 自动加载等关键更新。
sources:
- raw/Claude Code 2.0.40版本后的一些实用更新.md
created: 2026-06-30
updated: '2026-07-01'
confidence: high
---
# Claude Code 2.0.40 版本后的实用更新

## 来源信息

- **标题**：Claude Code 2.0.40版本后的一些实用更新
- **作者**：字节笔记本
- **URL**：https://mp.weixin.qq.com/s/lEWh_QNOwNRFcjYKVjxTEg


## 概述

字节笔记本整理的 Claude Code 2.0.40 版本后新增功能汇总，涵盖自定义输出样式、提示钩子模型参数、Git 命令扩展、[[概念_Subagent子代理|Subagent]] 生命周期管理和 [[概念_Agent_Skills元工具架构|Skills]] 自动加载等关键更新。

## 核心要点

### 自定义输出样式（Output Styles）
- 2.0.40 后支持修改系统提示词
- 本质是 Claude 的系统提示，完全改变交互方式和行为模式
- 存储路径：全局 `~/.claude/output-styles`，项目级 `.claude/output-styles`
- 通过 `/output-style` 命令切换
- 三种内置样式：
  - **Default**：简洁高效，适合经验开发者
  - **Explanatory**：提供"Insight"块解释设计决策，适合理解新代码库
  - **Learning**：留下 `TODO(human)` 让用户实现，适合学习

### 提示钩子的模型参数（Prompt Hook）
- 钩子类型 `"type": "prompt"` 支持指定模型（如 `claude-haiku-4-5`）
- 将钩子输入+自定义提示发送给快速 LLM，以结构化 JSON 返回决策
- 典型用例：Stop 钩子中用 Haiku 检查任务是否完成

### Git 命令优化
- 扩展无需批准的安全 git 命令范围
- 安全命令：`git status` / `git log` / `git diff` / `git branch`
- 无危险性操作直接放开，提升流程效率

### Subagent 生命周期管理
- **SubagentStop** 钩子新增 `agent_id` 和 `agent_transcript_path` 字段
- 解决多子代理共享 session_id 无法区分具体代理的问题
- 可追踪执行时间、针对特定子代理清理操作
- **SubagentStart** 钩子：子代理启动时触发，用于初始化/加载上下文/记录时间
- 完整生命周期：SubagentStart → PreToolUse → PostToolUse → SubagentStop

### 代理权限控制（permissionMode）
- 自定义代理 frontmatter 新增 `permissionMode` 字段
- 四种模式：
  - `default`：默认交互
  - `plan`：计划模式，不执行修改
  - `acceptEdits`：自动接受编辑
  - `bypassPermissions`：绕过权限检查（谨慎使用）

### Skills 自动加载
- 子代理 frontmatter 中声明 `skills:` 字段
- 运行时自动加载所需技能，无需手动触发
- 渐进式披露：先加载元数据 → 相关则加载完整 SKILL.md → 按需加载辅助文件

### tool_use_id 精确追踪
- PreToolUse/PostToolUse 钩子新增 `tool_use_id` 字段
- 实现工具调用粒度的追踪

### 多代理文档生成流水线示例
- doc-coordinator 协调 code-analyzer / diagram-generator / api-documenter / markdown-compiler
- 结合 SubagentStart/Stop + PostToolUse matcher + Stop prompt hook 实现完整自动化

## 关联概念

- [[概念_Subagent子代理]]
- [[概念_Agent_Skills元工具架构]]
- [[概念_Claude_Code工作流]]
- [[概念_CLAUDE.md最佳实践]]

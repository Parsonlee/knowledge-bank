---
type: concept
tags:
- AI-Agent/coding
summary: 编写 CLAUDE.md 工程宪法以约束 Agent 行为的高级指南与规范范式
sources:
- wiki/sources/写好CLAUDE.md_HumanLayer最佳实践.md
updated: '2026-07-22'
---
# 概念：CLAUDE.md最佳实践

## 定义
CLAUDE.md 是在 AI Agent 代码生成和协助场景下，为 LLM（如 Claude Code/Antigravity）提供核心指令、项目架构和行为约束的“宪法级”文件。最佳实践包括定义清晰的单向推导链、严格约束动刀边界以及规范化输出。

## 核心要点
- **明确权限边界**：清晰定义 Agent 可以做什么（如调用特定脚本）和绝对禁止做什么（如物理删除底层原始数据）。
- **统一工具箱调用**：针对常见任务（如 Lint 或清理）明确规定调用特定的自动化脚本，避免大模型自行臆造清理逻辑。
- **模板与约束**：为生成不同类型文档或代码提供强类型的格式模板和段落结构约束，减少输出的随机性和发散。

## 关联实体 / 概念
- 概念：[[概念_HITL_MCP]]

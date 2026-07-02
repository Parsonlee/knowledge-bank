---
type: source
tags:
- Skill/claude-code
summary: VoltAgent 社区维护的 Claude Code [[概念_Subagent子代理]] 资源集合，包含 100+ 个生产就绪的专用 AI 代理定义，覆盖全栈开发、DevOps、数据科学和业务运营等领域。
sources:
- raw/awesome-claude-code-subagents_ Productio....md
created: 2026-06-30
updated: '2026-07-01'
confidence: high
---
# awesome-claude-code-subagents 资源集合

## 来源信息

- **标题**：awesome-claude-code-subagents资源集合
- **作者**：VoltAgent 社区
- **URL**：https://github.com/VoltAgent/awesome-claude-code-subagents


## 概述

VoltAgent 社区维护的 Claude Code [[概念_Subagent子代理]] 资源集合，包含 100+ 个生产就绪的专用 AI 代理定义，覆盖全栈开发、DevOps、数据科学和业务运营等领域。

## 核心要点

### Subagent 的定义与特征
- 专用 AI 代理，为特定开发任务提供领域级专业知识
- 每个 subagent 拥有**独立上下文窗口**，防止跨任务污染
- 配备精心设计的领域指令，专项任务表现优于通用对话
- 跨项目共享，团队统一开发实践
- 细粒度工具权限控制

### 分类体系（10 大类）
1. **Core Development**（11 个）：api-designer / backend / frontend / fullstack / graphql / microservices / mobile / ui / websocket / wordpress / electron
2. **Language Specialists**（23 个）：TypeScript / Python / Rust / Go / Java / Swift / C++ / C# / PHP / Ruby / Kotlin / Flutter 等
3. **Infrastructure**（12 个）：cloud-architect / devops / k8s / terraform / sre / network / platform 等
4. **Quality & Security**（12 个）：code-reviewer / debugger / penetration-tester / performance / qa / chaos / compliance 等
5. **Data & AI**（12 个）：ai-engineer / data-engineer / ml-engineer / mlops / nlp / prompt-engineer / postgres 等
6. **Developer Experience**（10 个）：build-engineer / cli / documentation / dx-optimizer / git-workflow / legacy-modernizer / [[概念_MCP协议|mcp-developer]] / refactoring 等
7. **Specialized Domains**（11 个）：blockchain / fintech / game / iot / payment / quant / seo 等
8. **Business & Product**（10 个）：business-analyst / product-manager / project-manager / scrum-master / technical-writer / ux-researcher 等
9. **Meta & Orchestration**（8 个）：agent-organizer / context-manager / multi-agent-coordinator / workflow-orchestrator / task-distributor 等
10. **Research & Analysis**（6 个）：research-analyst / search-specialist / trend-analyst / competitive-analyst 等

### Subagent 标准模板结构
```
---
name: subagent-name
description: Brief description of capabilities
tools: List of MCP tools used
---

Role definition and expertise...

## MCP Tool Integration
## Communication Protocol
## Implementation Workflow
```

### 使用方式
- 项目级：`.claude/agents/` → 当前项目可用（高优先级）
- 全局级：`~/.claude/agents/` → 所有项目可用（低优先级）
- 通过 `/agents` 命令创建和管理
- Claude Code 自动检测加载，根据任务自动调度或手动指定

### 核心优势
- **内存效率**：隔离上下文防止主对话被任务细节淹没
- **增强准确性**：专用提示和配置在特定领域表现更优
- **工作流一致性**：团队共享保证统一方法
- **安全控制**：按 subagent 类型限制工具访问

## 关联概念

- [[概念_Subagent子代理]]
- [[概念_Agent_Skills元工具架构]]
- [[概念_Claude_Code工作流]]

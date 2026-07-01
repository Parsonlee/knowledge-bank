---
type: source
tags:
- AI-Agent/skill
summary: 从第一性原理拆解 Claude Agent Skills：提示词模板元工具架构，通过上下文注入扩展 LLM 能力
sources:
- Cubox/Claude Agent Skills：从第一性原理深入剖析-2025-11-06.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- 原文：微信公众号 PaperAgent
- 原始链接：https://mp.weixin.qq.com/s/W3gmYDqqMNIKNTIa3aGeCA

## 核心要点

### Skills 本质

Skills 是"领域专属提示词模板"，不是可执行代码：
- 不运行 Python/JavaScript，无 HTTP 服务
- 不硬编码在系统提示词，存在于 API 请求结构独立字段
- 被触发时：将详细指令注入对话上下文，同时可切换工具权限甚至模型版本

核心公式：**Skill = 提示词模板 + 对话上下文注入 + 执行上下文修改 + 可选数据文件和 Python 脚本**

### 技能选择机制

无算法路由、无意图识别、无嵌入/分类器/正则/关键词匹配。决策完全发生在 Claude 的 Transformer 前向传播中——纯 LLM 推理。

Claude 每次请求收到三件套：用户消息 + 普通工具列表（Read/Write/Bash...）+ Skill 工具（元工具）。Skill 工具的 description 字段包含所有可用技能的目录，Claude 用自然语言理解匹配用户意图。

### SKILL.md 结构

两部分：Frontmatter（配置）+ Markdown 内容（给 Claude 的提示词）

Frontmatter 关键字段：
- `name`（必填）：作为 Skill Tool 的 command 参数
- `description`（必填）：Claude 用来判断何时调用的主要信号
- `allowed-tools`（可选）：无需用户批准即可使用的工具，支持通配符
- `model`（可选）：覆盖会话模型
- `disable-model-invocation`（可选）：禁止 Claude 自动调用，只能用户手动触发
- `mode`（可选）：标记为模式命令，显示在列表顶部

### 技能发现路径

Claude Code 扫描：`~/.config/claude/skills/`（用户）、`.claude/skills/`（项目）、插件提供技能、内置技能

### 四种常见 Skill 模式

1. **脚本自动化**：将复杂计算卸载到 scripts/ 中的 Python/Bash 脚本
2. **读取-处理-写入**：文件转换和数据处理（allowed-tools: Read, Write）
3. **搜索-分析-报告**：Grep 搜索 → 读取上下文 → 生成结构化报告
4. **命令链执行**：多步 CI/CD 类工作流（npm install && lint && test）

### Tools vs Skills 核心区别

| 维度 | 传统工具 | Skills |
|------|---------|--------|
| 执行模式 | 同步直接执行 | 提示词扩展 |
| 目的 | 执行具体操作 | 引导复杂工作流 |
| 返回值 | 即时结果 | 上下文改变 |

## 关键引文

> "Skills就是'领域专属提示模板'。被触发时，它把一段详细指令注入对话上下文，同时可能切换工具权限甚至模型版本。" [重点]

> "技能选择机制在代码层无算法路由或意图分类。Claude Code 不用嵌入、分类器、正则或关键词匹配，而是把所有技能格式化成文本描述嵌入 Skill 工具提示，让 Claude 的语言模型自行决定。" [高亮]

## 关联

- [[概念_MCP代码执行模式]]
- [[从第一性原理深度拆解_Claude_Agent_Skill_宝玉]]
- [[概念_Prompt工程方法]]
- [[概念_Agent开发范式三级进化]]

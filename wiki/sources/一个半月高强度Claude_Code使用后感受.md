---
title: 一个半月高强度Claude Code使用后感受
source_url: https://mp.weixin.qq.com/s/bI4SEWPuL5ljCEAjkWpznw
author: 王巍（喵神）
tags:
  - Skill/claude-code
confidence: high
created: 2026-06-30
---

# 一个半月高强度 Claude Code 使用后感受

## 概述

王巍（喵神），知名 iOS/Unity 开发者，一个半月持续使用 Claude Code（CC）的深度体验总结。涵盖 Vibe Coding 迭代速度、从编辑器 AI 转换到命令行的思维变革、CC 的边界认知、Plan Mode 使用策略、小步迭代 vs 放飞自我、上下文管理、周边工具生态等全方位实践心得。

## 核心要点

### Vibe Coding 迭代速度
- CC 本身是 Anthropic 内部 dogfooding 产物，更新极快
- 一个半月内出现：自定义命令、Hooks、[[概念_Subagent子代理|Subagent]]
- 悖论：所有人都开上"法拉利"，竞争更激烈
- 核心忠告：**在 vibe coding 时代，千万别让工具把自己逼死**

### 从编辑器 AI 到命令行工具的转换
- 编辑器 AI（Cursor/Windsurf/Copilot/Cline）最大问题：**缺少全局感**
- 交互模式把思维框在"当前文件"甚至"当前几行"
- 命令行工具没有编辑器中间层，"强迫"更多依赖 AI
- **人类干预越少，效率和效果反而越好**（反直觉）
- 同步问题：编辑器 AI 容易出现人和 AI 对文件状态认知不一致
- CC 优势：模型质量 + 量大管饱的 token 使用 → 末端质变

### 认识 CC 的边界
- **擅长**：代码分析/理解/总结、算法实现、框架搭建、测试用例
- **不擅长**：全局精确重命名、100% 准确性任务（用脚本替代）
- **训练数据偏差**：前端/TypeScript 如鱼得水；iOS/Swift 幻觉严重
- **软硬件一体优势**：Anthropic 既是模型方又是工具方，垂直整合深度优化

### Plan Mode 策略选择
- **规划魔**（有经验/已有项目）：Plan Mode 充分讨论后执行，代码质量高、掌控好
- **莽夫流**（新技术/探索性项目）：先干起来再迭代，快速验证想法
- 个人偏好：倾向 Plan Mode，日常维护已有代码库占大头
- 隐藏好处：Plan Mode 帮助整理思路（"橡皮鸭调试法"变种）
- 官方推荐 workflow：探索→计划→编码→提交 / 写测试→提交→编码→迭代

### 小步迭代 vs 放飞自我
- **结论：小步迭代往往总是更好的选择**
- 一次性生成上千行修改 → 调试复杂度指数增长 → 最终 git reset
- 小步迭代优势：可控性高/能够理解/质量保证/学习机会
- 放飞自我的建议：TDD 先写测试、做好版本控制、分模块进行、交叉评审

### 上下文窗口管理
- 200k 窗口限制，普通使用十几二十分钟就飙到 90%
- 自动压缩可能导致 agent 混乱/死循环
- **任务拆解是关键**：在 Plan Mode 中让 AI 梳理，文档化保存计划
- **Subagent 使用**：代码分析/代码审查/测试/Git 不同 agent 链式调用
- **手动 compact**：在自然断点主动执行 /compact，优于等待自动压缩
- 独立任务直接新开 session，读取文档快速恢复上下文

### 善用命令和周边工具
- **Command**：重复两次以上的 prompt 应命令化；拥有完整当前会话上下文
- 常用命令：/test-and-fix、/review、/commit-smart
- **MCP 集成**：apple-docs-mcp（获取最新 Apple 文档）、mcp-atlassian（JIRA）、mcp-language-server（LSP 支持）
- **Code 之外用途**：PR 描述、技术文档、JIRA 更新、数据处理、远程 SSH 操作
- **语音输入**：推荐 MacWhisper / VoiceInk / Wispr Flow，配合 LLM 润色

### Opus vs Sonnet 与降智
- Opus 效果远强于 Sonnet（价格 5 倍）
- "时间玄学"：北京时间白天（美国夜里）效果可能更好
- 降智疑云：最近两周体验不如前一个月，社区抱怨增多
- Weekly 限制从 8 月底实施
- 应对策略：分级使用/错峰使用/提高 prompt 质量/合理用 subagent/保持多选择

## 关联概念

- [[概念_Claude_Code工作流]]
- [[概念_Subagent子代理]]
- [[概念_CLAUDE.md最佳实践]]
- [[概念_上下文工程]]
- [[概念_Vibe_Coding]]

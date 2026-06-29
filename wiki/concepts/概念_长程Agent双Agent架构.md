---
tags:
  - AI-Agent/coding
created: "2026-06-29"
updated: "2026-06-29"
---

# 概念：长程 Agent 双 Agent 架构

**来源**：[[Anthropic再发Agent神文_像人类工程师一样思考解决长程任务难题]]

跨多个上下文窗口完成复杂编码任务的 Agent 架构模式，由 Anthropic 为 Claude Agent SDK 开发。

## 核心问题

长程任务（数小时到数天）需分"会话"工作，每个新会话缺乏前次记忆。仅靠上下文压缩不足，表现为两种失败：一次性蛮干耗尽上下文，或过早宣布完工。

## 架构设计

**初始化 Agent（Initializer Agent）**：第一个会话专用，搭建环境脚手架：
- 生成 `init.sh` 脚本（启动开发服务器）
- 创建 `claude-progress.txt` 进度文件
- 建立包含所有功能的 `feature_list.json`（所有功能初始标记 `passes: false`）
- 建立初始 Git 仓库

**编码 Agent（Coding Agent）**：后续每个会话按 5 步标准流程接班：
1. `pwd` 查看目录
2. 读 Git 日志 + 进度文件
3. 读功能列表，选最高优先级未完成功能
4. 运行 `init.sh`
5. 运行端到端基础测试

## 三大支柱

- **功能列表**：JSON 格式（比 Markdown 更防模型错误修改），禁止删除测试只允许改 `passes` 字段
- **增量进展**：每次只做一个功能，完成后 Git 提交 + 进度文件摘要
- **端到端测试**：Puppeteer MCP server 浏览器自动化，截图可见即修复

## 关联

- [[概念_orchestrator-worker模式]]
- [[概念_上下文工程]]
- [[实体_Anthropic_Research系统]]

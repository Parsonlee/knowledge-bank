---
type: source
tags: [AI-Agent/tools, AI-Agent/skill]
summary: "评测腾讯开源的本地桥接工具 BrowserSkill，通过 CLI 与现有浏览器扩展通信，赋予 AI Agent 复用用户真实登录态进行浏览器操作的能力。"
sources: ["raw/实测腾讯开源的 BrowserSkill：让 AI 直接用你登录好的浏览器.md"]
updated: "2026-07-02"
---

# 实测腾讯开源的 BrowserSkill：让 AI 直接用你登录好的浏览器

## 核心贡献与摘要

为了解决 AI 自动化浏览器时遇到“未登录无法访问内网/SaaS”以及“多实例抢窗口/冷启动慢”的痛点，腾讯开源了本地桥接方案 **BrowserSkill** (MIT 协议)。通过 `bsk` 命令行与浏览器扩展配合，AI 可以在用户日常已登录的浏览器中开辟专属 Agent Window 进行操作，既完美复写用户登录态，又不打扰用户正常办公。

## 关键要点与引文

1. **复用登录态与隔离不抢占**：
   无需像 Playwright/Selenium 一样冷启动无登录态的新实例，也无需在 Prompt 中明文塞入账号密码。AI Agent 操作专属高亮窗口，与日常标签页隔离。
2. **纯本地架构与 Agent 中立性**：
   全链路仅走本机回环 `127.0.0.1`，无任何外部数据上报。`bsk` 作为一个普通 CLI 命令，天然兼容各类 Agent 框架（自动检测并适配 Claude Code、Codex、OpenClaw 等）。
3. **高效 DOM 操作（无障碍树快照）**：
   实测中 `bsk snapshot` 提供带 `@e1/@e2` 编号的可交互元素树，AI 直接通过 `bsk click @e12` 操作，比直接喂整页 DOM 或全屏截图 **大幅降低 Token 消耗并提高准确性**。
4. **五款浏览器方案横向对比**：
   文章对比了 BrowserSkill、Playwright(MCP)、Claude in Chrome、OpenClaw Relay 与 BrowserAct。结论明确：**要官方调试选 Claude，要全自动化 CI 选 Playwright，要登录态+纯本地中立选 BrowserSkill**。

## 关联实体与概念

- 概念关联：[[概念_私域知识工程]]、[[概念_智能体能力金字塔]]
- 实体关联：[[实体_腾讯混元TurboS]]

---
> 📎 **物理文献**：[[raw/实测腾讯开源的 BrowserSkill：让 AI 直接用你登录好的浏览器.md]]

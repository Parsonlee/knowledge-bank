title: Anthropic 最火爆功能 Generative UI 的开源替代方案 source: https://mail.google.com/mail/u/0/#inbox/19dfa25648e2f2cb author:

"[[DailyDoseOfDS]]" published: 2026-05-05 created: 2026-07-28 description: 介绍 CopilotKit 推出的 Open Generative UI 开源框架，如何在聊天窗口中安全流式渲染大模型生成的动态 HTML/SVG 界面。 tags:

clippings

# Anthropic 最火爆功能 Generative UI 的开源替代方案

CopilotKit 推出的 Open Generative UI 是 Anthropic 动态生成界面能力的 100% 开源实现：

实时 Token 流式渲染：Agent 在运行时生成 HTML/SVG，流式注入聊天框中的沙箱 iframe 内，用户可实时观看界面组装过程。

彻底隔离安全：iframe 无法访问宿主 App 的 DOM 或敏感数据，即使模型输出非法 JS 也不会造成安全泄漏。

原生适配广泛：基于 AG-UI 协议，原生支持 LangGraph、CrewAI、Mastra、Google ADK 以及 Cursor/Claude Code MCP 服务。

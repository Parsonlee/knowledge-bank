---
type: source
tags:
- AI-Agent/tools
- AI-Agent/multi-agent
summary: 阿里云实践：用 Qwen3-0.6b 做 MCP 工具选择节省 token，Qwen3-235b-a22b 负责生成，混合部署兼顾成本与效果
sources:
- Cubox/多快好省，Qwen3混合部署模式引爆MCP-2025-06-18.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- 标题：多快好省，Qwen3混合部署模式引爆MCP
- 作者：翎薇（阿里云开发者）
- URL：https://mp.weixin.qq.com/s/2tjoXMOK-iPHs0mlFJhvrQ

## 核心要点

- MCP 工具选择本质是 prompt engineering：将所有工具的名称、description、参数以文本形式传给模型，让模型决定调用哪个工具
- 工具描述/docstring 的质量决定模型能否正确选择和调用工具
- MCP 两步核心流程：
  1. **工具选择**：LLM 读取所有工具的 description，输出结构化 JSON 调用请求
  2. **结果反馈**：执行工具后将结果连同 system prompt 重新发给模型，生成最终回答
- 工具描述来源：`@mcp.tool()` 装饰器自动从函数名和 docstring 提取 name/description
- 混合部署策略：
  - 工具选择步骤使用本地 Ollama 部署的 **Qwen3-0.6b**（节约 token，182 token 对应一个简单工具描述）
  - 结果生成步骤使用 **Qwen3-235b-a22b**（保证输出稳定性，效果与 DeepSeek-R1 相当）
- Qwen3 主要特点：
  - MoE 架构，总参数 235B，激活 22B，成本约 DeepSeek-R1 的 1/3
  - 混合推理模型：快思考（非思考模式）+ 慢思考（思考模式）一体
  - 原生支持 MCP，BFCL Agent 能力评测 70.8，超过 Gemini2.5-Pro 和 OpenAI-o1
  - 支持 119 种语言
  - 4张 H20 可部署满血版
- Qwen3 四阶段后训练：长CoT冷启动 → 推理RL → 思维模式融合 → 通用RL（20+任务）
- 预训练：36T tokens，分三阶段（4K→32K context），使用 Qwen2.5-VL 从 PDF 提取文本
- 工具文档至关重要：任何模型都适配 MCP，只要提供工具描述文本

## 关联

- [[概念_MCP协议]]
- [[概念_MCP_CHS架构]]
- [[实体_Qwen3]]
- [[概念_自适应快慢思考]]
- [[别再误会MCP了辟谣指南]]
- [[MCP五大原语与Web化]]

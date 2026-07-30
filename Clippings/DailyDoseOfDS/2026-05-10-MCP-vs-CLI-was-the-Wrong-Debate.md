---
title: "MCP vs CLI was the wrong debate."
source: "https://mail.google.com/mail/u/0/#inbox/19e13d76eb927af3"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-05-10
created: 2026-07-30
description: "深入剖析 Agent 工具调用领域的“MCP vs CLI”争论，解释为什么真正的范式革新是 Anthropic 提出的 Code Mode（代码模式）。"
tags:
  - clippings
---

# MCP 与 CLI 之争是一个错误的辩题（MCP vs CLI was the wrong debate.）

在 2025 年的大部分时间里，AI 工程师们都在为 Agent 应该如何调用工具而争论不休。

一方主张使用 **MCP（Model Context Protocol）**——Anthropic 推出的用于将 Agent 连接到外部服务的通用协议；另一方则主张使用传统的 **CLI（命令行工具）**。

双方都有各自切实的依据，但双方也都忽略了最核心的焦点。

---

### 双方各自看对了什么

- **质疑 MCP 的工程师** 测量了 MCP 服务器在 Context 中占用的真实开销：把每一个工具的完整 JSON Schema 都载入 Prompt 中，还没开始提问就已经消耗了上万 Token。
- **支持 MCP 的工程师** 则强调多租户与类型安全：在企业级场景下，需要统一的标准规范、鉴权机制与类型约束。

如果你在思考“究竟哪一种方式会赢？”，那你就掉入了错误的思维陷阱中。

---

### 问题的重构：Code Mode 的诞生

2025 年 11 月 4 日，Anthropic 发表了 *《Code execution with MCP》*，一举改变了整个对话格局。

**问题从来不在于协议本身，而在于过去习惯于在 Agent 一启动时就将每一个工具的全量描述一股脑塞进 Context 中。**

如果加上这些工具返回的原始数据，并在每一步推理中反复跨模型传递，单个工作流的 Token 消耗就会瞬间爆炸。

Anthropic 提出的解决方案是**颠覆模型的工作机制**：模型不再直接通过上下文环境去单步调用工具，而是直接**编写代码（Write Code）**来组合与调用它们。

在 Anthropic 的示例中，需要将 Google Drive 中的会议转录记录同步更新到 Salesforce CRM。传统做法是将两个 Tool 的 Schema 全部载入 Context 中；而新的做法是让 Agent 编写一段小脚本来完成数据拉取与转化。

Cloudflare 随后将这一模式推向了极致：他们将其包含 2,500 个端点的庞大 API 从 **117 万 Token 的 Schema 载入量，一举缩减到了仅 1K Token！**

---

### 新的 Code Mode 范式

Code Mode 是一种全新的运行时，Agent 在其中编写融合了以下两大原语的代码：

1. **Bash**：适用于系统已安装的经典命令行工具（如 `git`, `curl`, `grep`）。模型在预训练数据中早已见过这些命令，完全不需要额外载入工具定义 Schema，Shell 会自动高效执行。
2. **带类型的模块导入（Typed module imports）**：适用于专有 API（如 Salesforce, Stripe 或公司内部微服务）。类型签名随着 import 动态引入，Agent 在严格的类型契约下编写代码。

类型契约随导入生效，Agent 在明确的接口约束下编写代码，不仅绝无幻觉，而且中间处理过程（如过滤、循环、数组转换）全都在代码运行时中完成，无需模型多次 Round-trip。

---

### 总结

MCP 赋予了我们严谨的类型契约，而 CLI 赋予了我们按需延迟加载的能力。**Code Mode 并没有取代它们，而是将两者的优点有机融合在了一起。**

“MCP 已死”是对这场讨论的错误误读。协议不仅没有死亡，反而使用率暴增。真正走向终结的是“在启动时把所有工具描述装载进上下文”的陈旧做法。

在 2026 年构建 Agent 时，黄金法则非常明确：**工具定义属于代码，而非上下文。模型编写代码来驱动工具，运行时负责高效执行。**

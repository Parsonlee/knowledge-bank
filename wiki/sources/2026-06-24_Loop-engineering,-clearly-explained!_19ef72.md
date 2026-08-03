---
type: source
tags:
  - agent
  - loop-engineering
  - harness-engineering
  - context-rot
  - maker-checker
summary: 探讨了智能体架构中的循环工程（Loop Engineering），解构了智能体底层的 Tool Call 循环，并深入分析了 Done 终局判定偏误、上下文腐烂与末日死循环、循环下工具设计的特殊性以及 Maker-Checker 校验机制。
sources:
  - raw/articles/2026-06-24_Loop-engineering,-clearly-explained!_19ef72.md
updated: 2026-08-04
---

# Loop engineering, clearly explained! (Source 摘要)

## 来源信息
- **标题**: Loop engineering, clearly explained!
- **发送人**: Daily Dose of DS
- **日期**: 2026-06-24
- **原始文章**: [[raw/articles/2026-06-24_Loop-engineering,-clearly-explained!_19ef72.md]]

## 核心要点
- **智能体底层循环 (Agent Loop)**：不管是何种框架，智能体底层基本都在运行同一个循环：发送上下文 -> 模型返回 Tool Call -> 运行工具 -> 将结果追加到上下文 -> 再次发送，直至模型决定不使用任何工具退出。
- **循环工程 (Loop Engineering)**：在 Harness Engineering 的最外圈，用于决定智能体该做什么、以及何时结束循环的控制机制。
- **终局判定与自动校验**：不能完全信任模型自身宣称的 "Done"，需要外部环境强加独立约束（如 Max Iterations 限制、Token 与时间/金钱 Budget 预算、No-progress 停滞检测），以及基于可验证指标（如测试通过）的自动校验机制。
- **上下文腐烂 (Context Rot) 与末日死循环 (Doom Loop)**：随着循环运行，无用工具输出、 stale reasoning 等不断堆积导致模型表现变差（Context Rot）。更严重的是，这会诱发模型做出更糟的决策进而生成更多噪音，陷入“Doom Loop”。应采用 Compaction（压缩）、Offloading（将大输出存入文件）与 Sub-agents（分派子任务）进行应对。
- **循环场景下的工具设计**：应保持工具集小而聚焦（少即是多）；写操作必须支持幂等性（安全可重试）；错误信息应当是“引导式”的（告诉模型下一步该怎么做）。
- **Maker-Checker 机制**：将执行（Maker）与校验（Checker）在模型层面上解耦，不要让生成代码的模型同时做校验。Karpathy auto-research 的理念也是：设定清晰可衡量的指标，让系统依靠外在反馈自转。

## 关键引文
- "Ending a turn is not finishing the job... Since you can’t trust the model’s own stop signal, you add conditions it doesn’t control."
- "The longer a loop runs, the more its context fills with junk... Model quality drops as that pile grows, which the field calls context rot."
- "Don’t tell it what to do, give it success criteria and watch it go." (Andre Karpathy)

## 联动概念
- [[wiki/concepts/概念_Loop_Engineering循环工程.md|概念_Loop_Engineering循环工程]]

> 📎 **物理文献**：[[raw/articles/2026-06-24_Loop-engineering,-clearly-explained!_19ef72.md]]

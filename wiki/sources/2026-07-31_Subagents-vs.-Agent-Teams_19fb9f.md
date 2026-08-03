---
type: source
tags: [multi-agent, sub-agents, agent-teams, architecture]
summary: 对比了 Claude 提供的两种多智能体范式：Sub-agents（基于隔离实现并行与 Context 压缩，单向反馈）和 Agent Teams（基于协同通信与共享状态，双向协作），并从第一性原理探讨了以上下文为中心的分治逻辑。
sources: ["raw/articles/2026-07-31_Subagents-vs.-Agent-Teams_19fb9f.md"]
updated: 2026-08-04
---

# Subagents vs. Agent Teams

## 来源信息
- **来源**: Daily Dose of DS
- **作者**: Avi
- **日期**: 2026-07-31
- **原文链接**: [Subagents vs. Agent Teams](https://fff97757.click.kit-mail3.com/v8uqlqw04vhrhvw8lw8ighvz3og4oi9hpqloo/7qh7h8h9r9g6woizh6/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vYWktYWdlbnRzLWNyYXNoLWNvdXJzZS1wYXJ0LTEtd2l0aC1pbXBsZW1lbnRhdGlvbi8=)

## 核心要点
- **多智能体架构选择**：选择多智能体的关键不在于“是否使用”，而在于“该任务需要何种协同模式”。
- **Sub-agents 范式（并行与隔离）**：核心在于 **Context 压缩**。每个 Sub-agent 运行在独立的上下文窗口，拥有特定 Prompt 和工具。完成后仅向 Parent 传递压缩后的最终结果，不污染 Parent 的上下文。Sub-agents 之间相互隔离、不可通信，且不能嵌套创建。
- **Agent Teams 范式（协同与通信）**：长生命周期的协同团队。通过**共享任务列表（Shared Task List）**管理依赖（如 `blockedBy` 字段）实现自主调度，团队成员之间支持 peer-to-peer 直接通信与协商，支持外部直接与其成员交互。
- **第一性原理：以上下文为中心的分治 (Context-centric Decomposition)**：
  - **反模式**：按角色（如 Planner, Implementer, Tester）划分智能体，导致 handoff 信息传递降级（Telephone game）。
  - **正模式**：按上下文重合度划分边界，重合度高的任务由同一个智能体 inline 完成。例如，编写功能代码和单元测试的上下文高度重合，应由同一个智能体处理。
- **研发警告与编排**：
  - 多 Agent 并发写代码会引入冲突的 implicit 设计假设，合并时 Git 冲突极难解决，建议 coding 时 Sub-agents 仅作为只读调研工具。
  - 五大经典编排：Chaining, Routing, Parallelization, Orchestrator-worker, Evaluator-optimizer。
  - 三大失败诱因：Vague 任务定义导致重复工作、Verifier 虚假确认（无实据通过）、Token 复合膨胀。

## 关联概念/实体
- 关联概念：[[wiki/concepts/概念_Claude_Code多智能体协同机制]]

## 关键引文
> "The point of sub-agents isn’t just parallelism, it’s compression. You’re distilling a vast amount of exploration into a clean signal, without polluting your parent agent’s context with noise."
> "Design around context boundaries, not around roles or org charts. Start with a single agent. Push it until you find where it breaks."

---
> 📎 **物理文献**：[[raw/articles/2026-07-31_Subagents-vs.-Agent-Teams_19fb9f.md]]

---
type: source
tags:
- AI-Agent/coding
summary: 介绍智能体循环（Agent Loops）的四种主要设计类型（单步交互式、目标驱动式、时间触发式、事件主动式），分析每种类型的触发机制、适用场景以及对自主性的分担。
sources:
- raw/articles/2026-07-14_The-four-types-of-agent-loops_19f617.md
updated: 2026-08-04
---

# The four types of agent loops (Source 摘要)

## 来源信息
- **来源**: Daily Dose of DS
- **作者**: Avi
- **日期**: 2026-07-14
- **原始物理文献**: [[raw/articles/2026-07-14_The-four-types-of-agent-loops_19f617.md]]
- **关联概念**: [[wiki/concepts/概念_Loop_Engineering循环工程.md|循环工程 (Loop Engineering)]]

## 核心要点
1. **循环工程的本质**：设计控制和引导智能体的系统，而不是人工一步步手动控制。该系统需要解答两个问题：什么启动了运行，以及什么决定了工作已完成。
2. **四种循环结构类型**：
   - **单步交互式（Turn-based）**：用户 Prompt 触发，单步执行后由人工校验并决定下一步。适用于需求尚不明确、且每一步输出都会改变后续方向的探索性任务。
   - **目标驱动式（Goal-based）**：由包含成功指标与预算的 `/goal` 触发，系统利用评估模型（Evaluator）校验目标是否达成。适用于结果可衡量、但执行路径不需要人工干预的任务。
   - **时间触发式（Time-based）**：时钟定时触发，运行固定任务，由系统校验。适用于任务已知且仅需周期性重复的场景（通过 `/loop` 在本地运行，`/schedule` 部署到云端）。
   - **事件主动式（Proactive）**：事件或调度触发，全自动分流且无人在场，在运行时决定工作流形态（如分类、修复和评审智能体协作）。适用于无人值守、且输入无法提前预测的常驻职责。
3. **自主性与职责让渡**：从单步交互到主动式，系统分担的职责逐步递增。单步交互式将两个问题都交由人处理；目标驱动式自动化了校验；时间触发式自动化了启动；主动式则同时自动化了两者，并在运行时动态决定工作流。

## 关键引文
> Loop engineering keeps getting talked about as one thing, when it’s actually a choice between four structures, each fitting a different kind of task.
> The mapping question isn’t which loop is most advanced. It’s whether the task is exploratory, measurable, recurring, or standing.

---

> 📎 **物理文献**：[[raw/articles/2026-07-14_The-four-types-of-agent-loops_19f617.md]]

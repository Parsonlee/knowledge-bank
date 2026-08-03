---
type: "concept"
tags:
  - Claude-Code
  - Multi-Agent
  - Orchestration
  - Dynamic-Workflows
summary: "拆解并对比 Claude Code 的三大协同原语（Subagents、Agent Teams、Dynamic Workflows），详述动态工作流在 JS 编排执行、并发扇出、上下文解耦和抗灾恢复力方面的机制，并阐述对抗性验证（Adversarial Verification）的收敛逻辑。"
sources:
  - "wiki/sources/2026-06-01_Claude-Code-dynamic-workflows,-explained!_19e84f.md"
updated: "2026-08-04"
---

# 概念: Claude Code 多智能体协同机制

随着大语言模型（LLM）在软件开发领域从“单次交互助手”向“自主软件工程智能体”的演进，多智能体协同（Multi-Agent Collaboration）成为处理大规模长程任务（Long-horizon tasks）的核心架构。在 Claude Code 中，存在三种不同层级、不同设计哲学的多智能体协同原语。

---

## 1. 三大协同原语拆解

### ① 轻量级子智能体 (Subagents)
- **定义**：由主 Session 运行时按需派生出的临时轻量级 Worker 智能体（通常在 `.claude/agents/` 中定义）。
- **运行逻辑**：主 Agent 将任务拆分并指派给某个 Subagent，Subagent 独立在单独的 Context Window 中执行任务，然后向主 Agent 汇报执行结果。
- **缺点**：Subagent 之间是**彼此隔离且无状态**的，无法实现子智能体间的直接通信（Peer-to-Peer Communication）。主 Agent 充当中央编排器（Orchestrator），所有的子任务结果都必须回传到主 Agent 的上下文窗口中，这使得主 Agent 成为严重的上下文和推理瓶颈。

### ② 智能体团队 (Agent Teams)
- **定义**：伴随 Opus 4.6 推出的一套多智能体协作原语，允许多个相对平等的 Claude 实例协同完成任务。
- **运行逻辑**：多个 Agent 实例通过一个**共享任务列表（Shared Task List）**和**直接消息（Direct Message）**机制进行双向自主协作。
- **缺点**：虽然打破了 Subagent 的主上下文单点瓶颈，但是编排逻辑需要开发人员预先进行设计；其实际协作规模通常仅能支撑 3-5 个成员，超过该限制会导致协作混乱与信息冗余；此外，Agent Teams 是**内存态易失会话**，如果运行环境发生中断/崩溃，整个 Team 的上下文和进度将全部丢失。

### ③ 动态工作流 (Dynamic Workflows)
- **定义**：伴随 Opus 4.8 推出的高阶多智能体编排架构。
- **运行逻辑**：主 Agent 并不直接在自己的上下文或多轮对话中控制并监视整个编排过程，而是直接输出一段**可执行的 JavaScript 编排脚本**。该 JS 脚本即为“计划本身”。
- **运行时调度**：主 Agent 将 JS 脚本传递给本地的 JavaScript 运行时（如内置的 Node.js/Deno 引擎）执行。JS 运行时代替 LLM 充当编排引擎，控制工作流的扇出（Fan-out）、并行子任务的分流、以及汇聚（Fan-in）校验。它支持最大 16 个并发 Agent 同时运行，整套工作流累积支持高达 1000 个子 Agent 的执行。
- **交叉链接**：此机制与 [[wiki/concepts/概念_Claude_Code核心配置与原语]] 中由 `agents/` 定义的静态角色起到了很好的动静互补作用。

---

## 2. 核心维度对比：Subagents vs. Agent Teams vs. Dynamic Workflows

| 对比维度 | Subagents (子智能体) | Agent Teams (智能体团队) | Dynamic Workflows (动态工作流) |
| :--- | :--- | :--- | :--- |
| **编排核心载体** | LLM 内存（主 Agent 上下文） | 共享任务列表 (Shared Task List) | **JavaScript 编排脚本** (JS 运行时执行) |
| **协同通信模式** | 放射状（主子单向回传，无子间通信） | 网状拓扑（通过 DM 进行 P2P 协作） | JS 运行时统一管理（扇出与扇入） |
| **上下文瓶颈** | **高**（所有过程和细节均回流主上下文） | 中（多轮对话易导致上下文冗余） | **极低**（主 Agent 仅接收 JS 运行时收敛后的最终结果） |
| **实际并发/规模** | 极低（往往只能顺序执行或几个子进程） | 较低（通常 3-5 人，多则失控） | **极高**（16+ 并发，总计可达 1000+ 子 Agent） |
| **抗灾恢复力** | 中等（主 Agent 可选择重新生成子智能体） | **无**（会话中断即崩溃，进度彻底丢失） | **极强**（支持检查点 checkpoint，中断可原地恢复） |
| **编排设计负担** | 中等（主 Agent 需实时掌控每一步骤） | 高（需要预先定义团队分工和协同规则） | **零负担**（用户只需描述目标，JS 运行时动态编排） |

---

## 3. 对抗性验证 (Adversarial Verification) 机制

在复杂的软件工程任务中（例如安全审计、边界测试或重构设计），Dynamic Workflows 可以自发引入**对抗性验证机制**。

1. **分歧发散 (Divergence)**：JS 运行时接收到主任务后，会指派多个独立的子智能体，从不同的角度、不同的假设前提下同时对一个代码缺陷或重构任务进行方案设计。
2. **对抗驳斥 (Refutation)**：生成方案后，运行时会交叉指派另一组“审查/对抗”智能体。这些智能体不以“如何实现”为目标，而是以“如何找出缺陷、推翻对方结论”为导向，编写对抗性测试用例或逻辑漏洞说明，尝试 refute 对方。
3. **循环迭代 (Iteration)**：开发智能体根据驳斥报告进行代码修正，验证智能体再次攻击，JS 运行时不断循环此步骤。
4. **收敛共识 (Convergence)**：当对抗双方达成共识，且所有对抗测试用例均通过时，JS 运行时将此共识和最终代码回传。这避免了单智能体因“盲区”或“过度自信”导致的错误输出，极大地保证了代码的可靠性。

---
关联概念：
- [[wiki/concepts/概念_Claude_Code核心配置与原语]]
- [[wiki/concepts/概念_聚类算法分类综述]]

> 📎 **来源摘要**：[[wiki/sources/2026-06-01_Claude-Code-dynamic-workflows,-explained!_19e84f.md]]

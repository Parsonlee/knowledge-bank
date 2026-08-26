---
type: concept
tags:
- Skill/claude-code
- AI-Agent/multi-agent
- AI-Agent/coding
summary: 拆解并对比 Claude Code 的三大协同原语（Subagents、Agent Teams、Dynamic Workflows），详述动态工作流在
  JS 编排执行、并发扇出、上下文解耦和抗灾恢复力方面的机制，并从第一性原理探讨了以上下文为中心的分治逻辑与编排模式。
sources:
- wiki/sources/2026-06-01_Claude-Code-dynamic-workflows,-explained!_19e84f.md
- wiki/sources/2026-07-31_Subagents-vs.-Agent-Teams_19fb9f.md
updated: '2026-08-04'
---

# 概念: Claude Code 多智能体协同机制

随着大语言模型（LLM）在软件开发领域从“单次交互助手”向“自主软件工程智能体”的演进，多智能体协同（Multi-Agent Collaboration）成为处理大规模长程任务（Long-horizon tasks）的核心架构。在 Claude Code 中，存在三种不同层级、不同设计哲学的多智能体协同原语。

---

## 1. 三大协同原语拆解

### ① 轻量级子智能体 (Subagents)
- **定义**：由主 Session 运行时按需派生出的临时轻量级 Worker 智能体（通常在 `.claude/agents/` 中定义）。
- **运行逻辑**：主 Agent 将任务拆分并指派给某个 Subagent，Subagent 独立在单独的 Context Window 中执行任务，最后向主 Agent 汇报执行结果。
- **核心特性**：其**核心是 context 压缩，隔离 Parent 干扰噪点**。主 Agent 不需要承受中间步骤的冗余 Token 干扰，子智能体在完全独立的 Context 中跑通工具并得出确切结论，返回给 Parent 的仅仅是高度精简的最终信号。
- **缺点**：Subagent 之间是**彼此隔离且无状态**的，无法实现子智能体间的直接通信（Peer-to-Peer Communication）。虽然能够通过隔离过滤噪声，但在没有外部运行时编排时，主 Agent 作为中央编排器（Orchestrator）可能因频繁调度多路子智能体而面临推理和总上下文瓶颈。

### ② 智能体团队 (Agent Teams)
- **定义**：伴随 Opus 4.6 推出的一套多智能体协作原语，允许多个相对平等的 Claude 实例协同完成任务。
- **运行逻辑**：多个 Agent 实例通过一个**共享任务列表（Shared Task List）**和**直接消息（Direct Message）**机制进行双向自主协作。
- **核心特性**：其设计精髓在于通过 **Shared Task List 看板以 `blockedBy` 依赖关系来驱动任务执行的生命周期**，实现去中心化的自适应调度；同时，团队成员之间支持 **peer-to-peer 协商与直接消息传递**，不必所有交互都通过 Team Lead 进行中转。
- **缺点**：虽然打破了 Subagent 的单点分发瓶颈，但是编排逻辑需要开发人员预先进行设计；其实际协作规模通常仅能支撑 3-5 个成员，超过该限制会导致协作混乱与信息冗余；此外，Agent Teams 是**内存态易失会话**，如果运行环境发生中断/崩溃，整个 Team 的上下文和进度将全部丢失。

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

## 4. 多智能体架构的第一性原理：以上下文为中心的分治 (Context-centric Decomposition)

多智能体系统的设计并非愈复杂愈好，其本质在于如何进行高效的上下文管理与分治。

### ① 划分边界：反模式 vs. 正模式
- **反模式（Role-based Split）**：按照组织架构/角色分工（如 Planner 规划器、Implementer 执行器、Tester 测试器）来划分不同智能体。这会导致“传话游戏”（Telephone game）效应，前一步的上下文在手持传递（handoff）到下一步时严重降级，导致开发质量逐步退化。
- **正模式（Context-centric Decomposition）**：上下文重合度边界划分。评估每个子任务实际需要的上下文。若两个任务所需上下文高度重合，必须将其合并（inline）在同一个智能体内执行。例如，编写功能代码和为该功能编写单元测试应该由同一个 Agent 承载，以防上下文丢失。

### ② 研发警告（Git 并发冲突）
在多智能体团队中，如果允许多个 Agent 并发地去修改/编写同一个项目的代码，它们会引入各自不兼容的 implicit 设计假设，合并代码时会在 Git 里引入极其复杂的冲突，调试成本极高。因此，面向 Coding 的 Sub-agents 宜限制为**只读模式（Read-only）**，仅做调研、探索与问题定位，而不宜多 Agent 并发写代码。

### ③ 5 大经典编排模式
1. **Chaining（链式模式）**：前后依赖的线性序列，后一步基于前一步的输出运行。
2. **Routing（路由模式）**：分类器分流。将简单请求分流至更便宜/更快速的模型，复杂请求路由至高能力模型。
3. **Parallelization（并行化模式）**：针对独立子任务的扇出。可分为同质任务的多模型投票（Voting），和异质任务的切片分工（Sectioning）。
4. **Orchestrator-worker（编排-执行模式）**：中央智能体拆解任务、分发给多个 Worker 并汇总结果。这是绝大多数多智能体系统的首选主架构。
5. **Evaluator-optimizer（评估-优化模式）**：一个生成，一个评估并提供反馈，在闭环中迭代直至达标。

### ④ 3 大失败诱因
1. **Vague 任务定义**：导致智能体职责不清，两个智能体重复做同样的事且彼此没有察觉。
2. **Verifier 虚假确认**：验证智能体在缺乏明确、客观事实依据（如跑通测试套件、通过编译等）的前提下，仅凭自然语言感官“宣布胜利”，产生虚假通过。
3. **Token compounding 复合膨胀**：多智能体交互的轮数和人数增加会导致 Token 消耗指数级膨胀。解决之道是智能分级（Tiering）使用模型，将例行工作交给小模型。

---
关联概念：
- [[wiki/concepts/概念_Claude_Code核心配置与原语]]
- [[wiki/concepts/概念_聚类算法分类综述]]

> 📎 **来源摘要**：[[wiki/sources/2026-06-01_Claude-Code-dynamic-workflows,-explained!_19e84f.md]], [[wiki/sources/2026-07-31_Subagents-vs.-Agent-Teams_19fb9f.md]]

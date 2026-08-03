---
type: concept
tags:
- AI-Agent/harness
- AI-Agent/coding
summary: 围绕基础大模型构建的宿主与编排系统（Harness Engineering），负责编排执行、思考规划、工具行动、上下文感知管理、产物存储与评估。
sources:
- wiki/sources/OpenAI前VP_Lilian_Weng_AI自我改进的近路不是改权重.md
- wiki/sources/DeepSeek Agent开发岗三面，再面一轮就offer啦！！！.md
- wiki/sources/快手data agent一面，我裂开了！！！.md
- wiki/sources/美团AICoding面试，跪了！！！.md
- wiki/sources/2026-04-06_The-Anatomy-of-an-Agent-Harness_19d64a.md
created: '2026-07-22'
updated: '2026-08-04'
---

# 概念：Harness Engineering

## 定义

**Harness Engineering（外壳工程 / 宿主工程）** 是围绕基础模型（Raw Model）构建的那套系统工程。它编排 Agent 的执行逻辑，决定模型如何思考规划、调用工具行动、感知管理上下文、存储中间产物以及评估输出结果。

在行业中存在一个经典共识：**“如果你不是模型，你就是 Harness（If you’re not the model, you’re the harness）”**。

Beren Millidge 将其进行了精确的硬件系统类比：
- **Raw LLM**：CPU（无 RAM、无 Disk、无 I/O）
- **Context Window（上下文窗口）**：RAM（高速但空间受限）
- **External Databases（外部数据库）**：Disk（容量大但速度慢）
- **Tool Integrations（工具集成）**：Device Drivers（设备驱动）
- **Harness（宿主系统）**：Operating System（操作系统 / OS），负责调度和管理上述所有部件，如同 Lilian Weng 所说，它封装了复杂的底层逻辑，保持接口规范简洁。

## Harness 的三大设计模式

1. **工作流自动化（Workflow Automation）**：目标导向的计划-执行-观察-改进循环，驱动模型自主分析运行轨迹与失败原因。
2. **文件系统即持久记忆（Filesystem as Persistent Memory）**：避开受限的上下文窗口，将实验日志、代码 diff、错误追踪落盘为物理文件，利用 shell/bash 标准接口进行读写。
3. **子代理与后台任务（Sub-agents & Background Tasks）**：主代理派生子代理进行并行任务分工，配套显式的进程管理（启动、查看日志、取消、合并结果）。

## 编码智能体标准工具箱

一个完备的编码 Harness 包含：文件系统工具（glob/grep/read/write/edit）、shell/git、MCP 协议组件、搜索与浏览器、后台任务与子代理委托。

## 可靠执行控制

两篇 Agent 面试项目复盘补充了生产控制面的具体做法：权限默认最小化，写入与 Shell 执行分级授权；暂时性故障采用有上限的退避重试，权限不足等确定性错误直接返回；循环侧设置最大步数、重复工具调用与状态停滞检测；高风险代码则在限制资源、网络和系统调用的沙箱内运行。

对内容删除等不可逆业务动作，Harness 还应把模型限制在“判断与建议”角色，由服务端依据置信度、风险级别和权限策略执行实际操作，并保留可追溯的决策证据与审计日志。

## 生产级 Harness 的 11 大核心组件

根据业界前沿实践（如 Anthropic Claude Code、OpenAI Agents SDK 等），一个生产级的 Harness 包含以下 11 个核心模块：

1. **Orchestration Loop（编排循环）**：系统的“心脏”，实现 Thought-Action-Observation (TAO) / ReAct 心跳循环，管理 Turn 轮次。
2. **Tools（工具层）**：定义工具 Schema（参数与描述），负责沙箱执行、结果捕获与格式化反馈。
3. **Memory（记忆层）**：包含单会话短期记忆（聊天历史）和跨会话长期记忆（如 `CLAUDE.md` 项目索引、JSON Store 等）。
4. **Context Management（上下文管理）**：对抗“上下文 rot（退化）”，通过压缩历史、Observation 遮蔽、懒加载等手段筛选最高信号的 Token。
5. **Prompt Construction（提示词构建）**：分层堆叠系统提示词、工具定义、记忆文件和历史，保证关键上下文放置在两端。
6. **Output Parsing（输出解析）**：配合原生工具调用（tool_calls），基于 Pydantic 等 Schema 进行强约束解析，辅以重试机制。
7. **State Management（状态管理）**：利用图/字典维护运行状态，支持 super-step 级别的 Checkpoint 与断点恢复。
8. **Error Handling（错误处理）**：对故障进行分类处理（瞬时退避重试、LLM 反馈可恢复、用户干预、确定性崩溃），防范 Compound Error。
9. **Guardrails（护栏与安全）**：输入/输出/工具执行的多级审核与 tripwire 瞬间熔断机制，实现权限隔离。
10. **Verification Loops（校验回路）**：整合静态测试/Lint/推理校验，给 Agent 自我纠错与验证机会，能显著提升交付质量。
11. **Subagent Orchestration（子代理编排）**：支持 Fork（同上下文拷贝）、Teammate（多终端协作）与 Worktree（独立 Git 分支隔离）等协同模式。

## Ralph Loop 工程协作模式

针对长生命周期且跨 context window 的复杂任务，业界提出了 **Ralph Loop（双阶段协作模式）**：
1. **Initializer Agent（初始化阶段）**：负责一次性地设置开发脚手架，包括运行初始化脚本、建立进度追踪文件（Progress File）、列出功能清单，以及提交初始 Git commit。
2. **Coding Agent（增量迭代阶段）**：在后续的每个会话中，该 Agent 通过读取物理文件（Git 日志、进度文件）来恢复上下文，挑选优先级最高且未完成的任务进行编码、验证与 Commit，并在退出前更新进度摘要。

该模式利用**物理文件系统（Filesystem）**作为跨上下文窗口的连续性载体，极大地增强了智能体长周期复杂任务的完成率。

## 代表实践

- [[entities/实体_Claude_Code|Claude Code]]：Anthropic CLI 编码智能体，高度集成了 Harness 工程哲学。
- [[entities/实体_Codex|Codex]]：OpenAI 编码智能体系统。

## 来源与参考

- [[OpenAI前VP_Lilian_Weng_AI自我改进的近路不是改权重]]
- [[concepts/概念_RSI递归自我改进]]
- [[concepts/概念_Harness优化阶梯]]
- [[sources/2026-04-06_The-Anatomy-of-an-Agent-Harness_19d64a|The Anatomy of an Agent Harness]]

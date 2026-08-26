---
type: source
tags:
- AI-Agent/prompt-engineering
- AI-Agent/context-engineering
- AI-Agent/coding
summary: 详细拆解了围绕 LLM 运作的四层工程阶梯（Prompt、Context、Harness、Loop Engineering），它们由内而外包裹，各自承担着大模型应用在推理阶段的不同层级优化与控制面职责。
sources:
- raw/articles/2026-07-03_Prompt,-context,-harness-&-loop-engineering_19f29f.md
updated: '2026-08-04'
---

# 来源：Prompt, context, harness & loop engineering

## 来源信息
- **原邮件主题**: Prompt, Context, Harness & Loop Engineering
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Fri, 03 Jul 2026 21:51:22 +0000
- **ID**: 19f29f70428b228f
- **原始链接**: [Daily Dose of DS Substack](https://www.dailydoseofds.com/p/loop-engineering-clearly-explained/)

## 核心要点
1. **Agent 的本质循环**：在最底层，AI Agent 的运行本质是一个 `while` 循环，即模型运行 -> 触发工具调用 -> 工具返回结果至上下文 -> 模型再次运行，直至模型停止请求工具。这正是 ReAct 框架的经典闭环。
2. **四层工程嵌套结构**：在 Agent 循环之外，包裹着四层互不竞争、层层递进的工程优化手段：
   - **提示词工程 (Prompt Engineering)**：定义单次调用的输入（角色、指令、Few-shot、格式），调节模型的内部推理与步骤。
   - **上下文工程 (Context Engineering)**：管理单次交互前模型能看到的全部信息。通过检索、排序、摘要和去噪手段最大化高信号 Token 密度。
   - **装备工程 (Harness Engineering)**：模型周边的系统代码。定义工具、解析调用、重试故障、路由工作、执行测试和验证。
   - **循环工程 (Loop Engineering)**：外层控制面。将“人类在每轮读结果写提示词”的任务交给智能体本身，设定目标和硬性停止条件（Cap 限制、无进展检测、客观校验）让其自主运行。
3. **嵌套而非竞争**：这四层工程手段由内而外层层包裹，随着层次从 Prompt 到 Loop 的提升，工程师的关注点也从“如何写好单次提示词”转变为“如何设定目标和停机条件，以实现系统的闭环自转”。

## 关键引文
- "Each one wraps the last, and the model sits in the middle, so none of them compete with the others. Instead, they just zoom one level further out."
- "By this layer [Loop Engineering], you’re operating on the whole run, so the engineering moves from writing each prompt to setting the goal and the stop conditions up front and letting it run."

> 📎 **物理文献**：[[raw/articles/2026-07-03_Prompt,-context,-harness-&-loop-engineering_19f29f.md]]

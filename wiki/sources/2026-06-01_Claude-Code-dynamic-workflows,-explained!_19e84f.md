---
type: source
tags:
- Skill/claude-code
- AI-Agent/multi-agent
- AI-Agent/coding
summary: 解析了 Claude Code 在 Opus 4.8 时代引入的 Dynamic Workflows（动态工作流）机制，对比了 Subagents、Agent
  Teams 与 Dynamic Workflows 在编排、规模、通信和灾备上的差异，探讨了其内部的 JS 脚本执行与对抗性验证原理。
sources:
- raw/articles/2026-06-01_Claude-Code-dynamic-workflows,-explained!_19e84f.md
updated: '2026-08-04'
---

# Claude Code dynamic workflows, explained!

## 来源信息
- **来源**: Daily Dose of DS
- **原始链接**: [Claude Subagents vs. Agent Teams](https://www.dailydoseofds.com/p/claude-subagents-vs-agent-teams/)
- **归档物理文件**: [[raw/articles/2026-06-01_Claude-Code-dynamic-workflows,-explained!_19e84f.md]]

## 核心要点
1. **Opus 4.8 时代的编排飞跃**：伴随 Opus 4.8 发布的 **Dynamic Workflows** 特性对大规模智能体编程的实际效能起到了革命性的作用。它克服了以往智能体协同中的上下文瓶颈和可靠性痛点。
2. **第一代原语 (Subagents)**：由主 session 派生出的轻量级 worker，仅负责特定任务。其瓶颈在于主 Agent 充当中央分发器，所有子任务的结果必须回传至主上下文，容易引发上下文过载。
3. **第二代原语 (Agent Teams)**：智能体间基于 Shared Task List 进行任务编排并通过直接消息协作。虽然去除了中央上下文瓶颈，但实用上限为 3-5 人，编排需预定义，且极易因 session 中断/崩溃而丢失进度。
4. **第三代编排 (Dynamic Workflows)**：打破了 LLM 记忆编排的局限。Claude 不再把计划留存在上下文，而是生成一段 **JavaScript 编排脚本**，由本地 JS 运行时（如 Node.js/Deno）执行，自动扇出数十至数百个并行 subagent 运行。
5. **规避上下文膨胀**：主 Agent 的上下文只需接收汇聚后的最终结果，中间数百步的复杂运行日志和子输出完全被 JS 运行时隔离，彻底释放了上下文额度。
6. **动态工作流的独特优势**：
   - **大并发**：支持高达 16 个并发 agent 运行，整个 workflow 支持多达 1000 个 agent 调用。
   - **对抗性验证 (Adversarial Verification)**：支持不同智能体从相反立场出发进行辩论与结果推翻，直至答案收敛。
   - **状态恢复力**：中间结果持续持久化，遭遇异常中断后可原地恢复，而非如 Agent Teams 般彻底丢失。
   - **自适应设计**：用户只需描述最终目标，编排与验证策略由 Claude 自动逆向设计生成。

## 关键引文
- "Instead of Claude holding the plan in its context window, it writes a JavaScript orchestration script. That script becomes the plan. A JS runtime executes it, fanning work across tens to hundreds of parallel subagents automatically."
- "Claude’s context window only ever sees the final converged answer. Not the intermediate results of hundreds of steps."

---
关联概念：
- [[wiki/concepts/概念_Claude_Code多智能体协同机制]]
- [[wiki/concepts/概念_Claude_Code核心配置与原语]]

> 📎 **物理文献**：[[raw/articles/2026-06-01_Claude-Code-dynamic-workflows,-explained!_19e84f.md]]

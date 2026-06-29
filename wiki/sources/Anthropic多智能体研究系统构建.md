---
type: source
tags:
  - AI-Agent/multi-agent
  - AI-Agent/tools
summary: "Anthropic 工程实践：多智能体研究系统从原型到生产的架构、提示词、评测与可靠性全解析，多智能体比单智能体提升 90.2%"
sources:
  - "Cubox/How we built our multi-agent research system - Anthropic-2025-06-21.md"
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

## 来源信息

- 标题：How we built our multi-agent research system
- 作者：Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford（Anthropic）
- URL：https://www.anthropic.com/engineering/built-multi-agent-research-system

## 核心要点

### 为什么用多智能体
- 研究任务开放性强，无法预先规划固定路径，动态路径依赖
- 多智能体优势：子智能体并行运行各自上下文窗口，探索不同方向后压缩最重要信息给主智能体
- 内部评测：Claude Opus 4 主智能体 + Claude Sonnet 4 子智能体，比单智能体 Claude Opus 4 提升 **90.2%**
- BrowseComp 评测分析：token 用量解释 80% 性能差异，工具调用次数和模型选择是另外两个因素
- 多智能体 token 消耗约为 chat 的 **15×**，单智能体约为 **4×**
- 不适合多智能体的场景：需要共享上下文、智能体间依赖多（如大多数编码任务）

### 架构
- orchestrator-worker 模式：主智能体（LeadResearcher）协调，子智能体（Subagents）并行探索
- 完整流程：LeadResearcher 思考并将计划存入 Memory → 创建子智能体并行搜索 → 子智能体用 interleaved thinking 评估工具结果 → 汇总给 LeadResearcher → CitationAgent 处理引用 → 返回用户
- Memory 用于保存研究计划（上下文超 200k token 会被截断，计划须持久化）
- 子智能体输出写入文件系统，传递轻量引用给协调者，避免"传话游戏"信息损耗

### 提示词工程 8 条原则
1. **像智能体一样思考**：用 Console 复现相同 prompt 和工具，逐步观察智能体行为，发现失败模式
2. **教会协调者如何分配任务**：每个子智能体需要目标、输出格式、工具/数据源指引、任务边界；指令模糊会导致重复工作或遗漏
3. **按查询复杂度缩放努力**：简单事实查询1个智能体3-10次工具调用；复杂研究>10个子智能体；写入提示词避免过度投入
4. **工具设计与选择至关重要**：错误工具等于徒劳，每个工具需有清晰目的和描述；用工具测试智能体自动重写工具描述，使任务完成时间减少 **40%**
5. **让智能体自我改进**：Claude 4 可以诊断失败原因并优化提示词
6. **先广后窄**：从短宽泛查询开始，评估可用内容再逐步收窄
7. **引导思考过程**：主智能体用 extended thinking 规划；子智能体用 interleaved thinking 评估工具结果
8. **并行工具调用**：主智能体同时启动 3-5 个子智能体，子智能体同时调用 3+ 工具，复杂查询研究时间缩短最高 **90%**

### 评测
- 传统评测假设固定路径，多智能体路径不确定，需灵活评测方法
- 从 ~20 个查询开始小样本评测，早期 prompt 调整效果显著（30%→80%）
- LLM-as-judge：单次调用输出 0-1 分 + pass/fail，评估准确性/引用准确性/完整性/来源质量/工具效率
- 人工评测发现 LLM 评测遗漏的问题：如智能体偏向 SEO 内容农场而非权威来源

### 生产可靠性
- 错误会复合传播：一步失败会导致智能体走向完全不同的轨迹
- 构建从错误发生点恢复的机制，结合 retry 逻辑和定期 checkpoint
- 使用 rainbow deployment 渐进迁移流量，避免破坏运行中的智能体
- 全量生产追踪诊断失败原因，监控决策模式而不监控具体对话内容（保护隐私）
- 当前子智能体同步执行是瓶颈，异步执行是下一步方向

## 关联

- [[概念_多智能体协调]]
- [[概念_orchestrator-worker模式]]
- [[概念_Agent感知记忆推理三能力]]
- [[概念_MCP协议]]
- [[概念_思维链CoT高级方法]]
- [[实体_Claude]]
- [[MCP遇上代码执行]]
- [[从CoT到Agent综述_上交]]

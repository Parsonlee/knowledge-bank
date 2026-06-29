---
type: source
tags:
  - LLM/reasoning
  - AI-Agent
summary: "上交大综述：从 CoT 基本原理到 Agent，覆盖 Prompt 模式/推理结构/应用场景三条路径及 Agent 挑战"
sources:
  - "Cubox/从 CoT 到 Agent，最全综述来了！上交出品-2023-11-26.md"
created: "2026-06-29"
updated: "2026-06-29"
confidence: high
---

## 来源信息

- **标题**：从 CoT 到 Agent，最全综述来了！上交出品
- **作者**：小戏、Python（夕小瑶科技说）；综述作者：上海交通大学张倬胜
- **URL**：https://mp.weixin.qq.com/s/bJYqfHF4RrYS8GkXfOMYGA
- **论文**：*Igniting Language Intelligence: The Hitchhiker's Guide From Chain-of-Thought Reasoning to Language Agents*（arxiv 2311.11797）

## 核心要点

### 什么是 CoT

- CoT（思维链）：通过让模型逐步分解问题并依次求解，完成 `<input→reasoning chain→output>` 映射
- 一个完整 CoT Prompt = 指令（Instruction）+ 逻辑依据（Rationale）+ 示例（Exemplars）
- Zero-Shot-CoT：仅加"Let's think step by step"；Few-Shot-CoT：示例中详述推理步骤

### CoT 的四大好处

- 增强推理能力（分解复杂问题）、可解释性（展示推理步骤）、可控性（中间步骤可干预）、灵活性（适用于多种模型和任务）

### 何时使用 CoT

- 适用条件：20B 以上参数模型 + 任务需要复杂推理 + 参数增加不能带来显著提升
- 训练数据中变量有局部簇结构（强相互关联）时 CoT 效果最好
- CoT 的作用可能在于**强迫模型推理**，而非教会模型如何推理

### CoT 三条发展方向

**1. Prompt 模式**
- 手动指令生成：Zero-Shot CoT、Plan-and-Solve（制定计划再执行）
- 自动指令生成：APE（自动 Prompt 工程）、OPRO（提示优化，LLM 自动选最优 Prompt）
- 范例生成：Few-Shot-CoT → ActivePrompt（不确定性采样）→ Auto-CoT（聚类+代表性问题生成）

**2. 推理结构**
- CoT 构造：PoT（程序化思维，用代码解计算问题）、Tab-CoT（表格结构推理）、ToT（树状推理，多路探索+回溯）、GoT（图状推理，控制器管理 GoO+GRS）
- 推理聚合：Self-consistency CoT（多路采样+多数投票）
- CoT 验证：Self-Verification（多候选采样+后向验证打分）、CRITIC（外部工具验证+循环修改）、AuRoRA（多来源知识组合提炼）
- 注意：大模型能力不足时自我验证可能过度纠正，跳过正确答案

**3. 应用场景**
- 多模态 CoT：MM-CoT（输入多模态）、GoT-Input（GNN 统一文本/图像/CoT）、VCoT（输出多模态图像生成）
- 其他领域：SumCoT（摘要）、MAPS（机器翻译）、ChemCrow（化学）、Med-PaLM（医学）

### CoT 与 Agent 的关系

- Agent = 主体 + 工具 + 环境；大模型 Agent 需要感知、记忆、推理能力，CoT 从这三方面赋能
- **感知 CoT**：逐步关注接收信息，理解意图，自我纠错；多模态感知（语言/图像/多模态中心）
- **记忆 CoT**：短期记忆（动态上下文历史动作链）；长期记忆（可训练参数 or 外部记忆库）；树搜索（Reflection Tree）和矢量检索用于高效增删改查
- **推理 CoT**：CoT 弥合推理与行动的差距（AgentBench 思考+行动；行动链技术）；工具扩展 Agent 能力边界

### Agent 六大挑战

1. 未知领域泛化能力（缺少具身交互）
2. 过度交互问题（空转循环、日志存储）
3. 个性化 Agent（定制 Prompt/微调/模型编辑三路，无统一方案）
4. 多智能体社会（计算开销巨大）
5. Agent 安全问题（隐私/权限/有毒内容/对齐）
6. Agent 评价（传统刷榜不适用，需超越成功率的新指标）

## 关键引文

> CoT 应当被用于 20B 以上参数规模的模型之中，并且模型的训练数据应当于任务问题相关且彼此相互有较强的联结。 `[重点/高亮]`

> 而当序列长度变长，线性链条式的记忆链效率出现下降时，为了实现针对"记忆"高效的增删改查，一些工作探索了树搜索与矢量检索的方法。 `[重点/高亮]`

## 关联

- [[概念_思维链CoT高级方法]] — CoT 核心技术
- [[概念_Prompt工程方法]] — Prompt 设计
- [[概念_智能体能力金字塔]] — Agent 能力
- [[概念_Agentic_RAG]] — Agent + RAG
- [[概念_Memory_RAG]] — 长期记忆机制

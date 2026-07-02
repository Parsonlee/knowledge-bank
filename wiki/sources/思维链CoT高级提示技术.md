---
type: source
tags:
- LLM/reasoning
- AI-Agent/prompt-engineering
summary: CoT 高级提示工程综述：从 Zero-shot CoT 到 CoT-SC、Decoding CoT、Tree of Thoughts + MCTS，及成本权衡
sources:
- raw/思维链高级提示付费文章.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- 标题：Medium上20万次阅读的思维链高级提示付费文章
- URL：https://mp.weixin.qq.com/s/11QEniDzmFRS_jO5u1snmA
- 原文：https://towardsdatascience.com/advanced-prompt-engineering-chain-of-thought-cot-8d8b090bf699

## 核心要点

### CoT 基础
- Chain-of-Thought 由 DeepMind Brain 团队 2022 年论文《Chain-of-Thought Prompting Elicits Reasoning in Large Language Models》提出
- Zero-shot：提示末尾加"让我们一步步思考"；Few-shot：给出示例推理步骤
- DeepMind 报告 CoT 显著提升模型表现，尤其在数学和复杂推理任务

### 采样参数
- **temperature**：越高分布越平坦，越倾向于选择低概率 token（创造力）
- **top_p**：限制/扩展候选 token 池；高 temperature + 高 top_p → 更多创新输出 `[重点/高亮]`
- **贪婪解码（Greedy Decoding）**：do_sample=False，每步选概率最高 token；在 MMLU/BigBench 有小幅提升，但复杂问题无改善；小模型易陷入重复循环

### CoT 链（Chain of CoT）
- Benjamin Klieger 的 g1 项目（Groq + Llama 3.1 70B）：将思维拆成多个独立 LLM 调用，每个链条设标题并判断是否需要继续
- 测试结论：Claude Sonnet 3.5 在 Putnam 高级数学上使用 CoT 链达到 68.75%，超过 o1-preview（63%）；Sonnet 高级数学提升达 81%
- 简单问题使用 CoT 可能反而更差（过度分析）

### CoT-SC（Self-Consistency）
- 生成多条推理路径，选取最一致答案；DeepMind 报告算术推理提升 1%~8%

### Decoding CoT
- 无需提示；启动 k 个初始 top token，各自生成不同推理路径，根据 logits 计算置信度得分，返回最高概率答案路径 `[重点/高亮]`
- 来源：DeepMind 2024 论文《Chain-of-Thought Reasoning Without Prompting》（arXiv 2402.10200）
- 实现：optillm（github.com/codelion/optillm）

### Tree of Thoughts（ToT）+ MCTS
- 普林斯顿+DeepMind 2023 提出；多路径动态评估，边生成边剪枝，无效路径早退出
- MCTS 扩展：引入外部奖励（UCB 统计），允许回溯改进早期决策，比简单 ToT 更复杂

### 成本权衡
- CoT 链每个问题成本平均高出最多 8 倍
- 《To CoT or not to CoT?》（arXiv 2409.12183）：CoT 改进主要集中在数学和复杂推理，简单问题不适用
- 实践建议：先用模型判断问题难度，难题用 CoT，简单问题直接回答

## 关键引文

> 将高 temperature 与高 top_p 结合使用会生成更多创新和创意的输出，因为更多 token 会成为候选项。 `[重点/高亮]`

> 系统首先启动 k 个初始的 top token，然后从每个 token 生成不同的推理路径。一旦答案生成后，系统会根据不同路径中各个 token 的概率（logits）计算置信度得分。最终，模型返回具有最高概率的答案或路径。这种方法被称为"解码CoT"（Decoding CoT）。 `[重点/高亮]`

## 关联

- [[概念_思维链CoT]] — CoT 基本原理与 Zero/Few-shot 方法
- [[概念_自洽性CoT_SC]] — 多路径 + 一致性选择
- [[概念_Decoding_CoT]] — 无提示 CoT，logits 置信度选路
- [[概念_思维树ToT]] — 树形多路推理 + 动态剪枝
- [[概念_Prompt工程方法]] — 更广泛的 Prompt 工程方法清单
- [[概念_自适应长短CoT]] — Qwen3 等模型的动态 CoT 触发

---
> 📎 **物理文献**：[[raw/思维链高级提示付费文章.md]]

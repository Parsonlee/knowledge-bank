---
type: concept
tags:
- AI-Agent/eval
summary: Agent 完整轨迹评估（Full Trajectory Evaluation） 是一种面向复杂大模型智能体的评估范式。由于智能体完成一个任务通常涉及多步规划、工具调用、信息检索与多轮会话，不能像传统搜索评测那样仅依据最终输出文本（Final
  Response）打分，而必须对智能体从输入到输出的整个...
created: '2026-07-06'
updated: '2026-07-06'
sources:
- wiki/sources/Dropbox基于DSPy优化Dash Chat评估与提示词.md
---


# 概念：Agent 完整轨迹评估

## 定义

**Agent 完整轨迹评估（Full Trajectory Evaluation）** 是一种面向复杂大模型智能体的评估范式。由于智能体完成一个任务通常涉及多步规划、工具调用、信息检索与多轮会话，不能像传统搜索评测那样仅依据**最终输出文本（Final Response）**打分，而必须**对智能体从输入到输出的整个决策路径与中间状态进行系统化评估**。

## 核心评估维度

1. **意图遵循（Intent Understanding）**：智能体是否准确识别了用户的根本目标与隐藏约束。
2. **上下文选择（Context Selection）**：在海量记忆或检索结果中，智能体是否挑出了真正相关的关键上下文。
3. **工具调用（Tool Use）**：调用搜索、读取、代码执行等工具的时机是否合理，参数传递是否正确。
4. **归纳与真实性（Synthesis & Grounding）**：最终生成的内容是否严格基于收集到的证据，无额外捏造或幻觉。
5. **多轮对齐（Turn-by-turn Adaptation）**：在遇到歧义或错误反馈时，能否自我修正或主动发问澄清。

## 评估驱动工程闭环

- **细粒度人工监督**：对抽样轨迹不光打分，更需标注**失败编码（Failure Codes）**与**推理理由（Reasoning Notes）**。
- **校准 LLM-as-a-Judge**：利用人工标注数据与 [[实体_DSPy]] 等工具，优化裁判模型的提示词，使得自动化评分与专家认知高度吻合。
- **反事实回放（Counterfactual Replay）**：在离线代表性数据集上回放智能体决策，利用对准的裁判输出定量信号，指导系统提示词与架构优化。

## 来源与参考

- [[Dropbox基于DSPy优化Dash Chat评估与提示词]]
- [[概念_LLM应用评估体系]]
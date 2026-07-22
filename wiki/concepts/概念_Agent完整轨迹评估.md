---
type: concept
tags:
- AI-Agent/eval
summary: Agent 完整轨迹评估（Full Trajectory Evaluation） 是一种面向复杂大模型智能体的评估范式。对智能体从输入到输出的整个决策路径（包含 Skill 加载、参考读取、工具选择、参数合规与环境清理）进行系统化评估。
created: '2026-07-06'
updated: '2026-07-22'
sources:
- wiki/sources/Dropbox基于DSPy优化Dash Chat评估与提示词.md
- wiki/sources/如何系统评价一个_Agent_Skill.md
---


# 概念：Agent 完整轨迹评估

## 定义

**Agent 完整轨迹评估（Full Trajectory Evaluation）** 是一种面向复杂大模型智能体的评估范式。由于智能体完成一个任务通常涉及多步规划、工具调用、信息检索与多轮会话，不能像传统搜索评测那样仅依据**最终输出文本（Final Response）**打分，而必须**对智能体从输入到输出的整个决策路径与中间状态进行系统化评估**。

## 核心评估维度

1. **意图遵循（Intent Understanding）**：智能体是否准确识别了用户的根本目标与隐藏约束。
2. **上下文选择与 Skill 加载**：在海量记忆、检索结果或 Skill 库中，智能体是否挑选并加载了正确的技能包与参考文件。
3. **工具调用与参数合规**：调用搜索、读取、代码执行等工具的时机是否合理，工具参数与依赖顺序是否正确，是否有重复重试。
4. **归纳与真实性（Synthesis & Grounding）**：最终生成的内容是否严格基于收集到的证据，无额外捏造或幻觉。
5. **多轮对齐与环境清理**：在遇到歧义或错误反馈时能否自我修正，任务结束后是否正确清理临时文件并维持环境安全。

## 评估驱动工程闭环

- **程序化确定性检查（Deterministic Checks）**：优先使用代码检查（文件存在、JSON 合规、命令执行成功、单元测试通过）替代高成本且易波动的 LLM Judge。
- **细粒度人工监督与标注**：对抽样轨迹打分并标注**失败编码（Failure Codes）**与**推理理由（Reasoning Notes）**。
- **校准 LLM-as-a-Judge**：利用人工标注数据与 [[实体_DSPy]] 等工具，优化裁判模型的提示词，使得自动化评分与专家认知高度吻合。
- **反事实回放（Counterfactual Replay）**：在离线代表性数据集上对比测试 `With Skill` 与 `Without Skill`（或候选模版与 Baseline）的轨迹轨迹，定量评估边际增量。

## 来源与参考

- [[sources/Dropbox基于DSPy优化Dash Chat评估与提示词]]
- [[sources/如何系统评价一个_Agent_Skill]]
- [[concepts/概念_LLM应用评估体系]]
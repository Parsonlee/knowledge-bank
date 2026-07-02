---
type: source
tags:
- AI-Agent/tools
- AI-Agent/prompt-engineering
summary: 蚂蚁集团实践：通过'思考和规划'工具强制模型在多工具调用前结构化思考，显著提升 Agent 效果
sources:
- raw/如何让 Agent 规划调用工具.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
---
## 来源信息

- 标题：如何让 Agent 规划调用工具
- 作者：峙岳（阿里云开发者 / 蚂蚁集团）
- URL：https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247549662

## 核心要点

- 根据 OpenAI 和 Anthropic 建议，多工具 Agent 在调用工具前引入结构化规划可显著提升效果
- OpenAI 方案：Prompt 引导显式规划（"你在每次调用函数之前必须进行充分的规划"），在 SWE-bench 上通过率提升 4%；但该效果依赖后训练，开源模型直接用 Prompt 效果打折
- Anthropic 方案：定义 `think` 工具让模型调用前/后思考；在 τ-bench 评测：
  - 航空领域：pass^1 从 0.370 → 0.570，相对提升 54%
  - 零售领域：pass^1 从 0.783 → 0.812
- 以工具形式指令遵循效果优于纯 Prompt，原因：工具有固定参数格式（thought/plan/action/thoughtNumber），调用工具是明确可执行的指令，"做一个规划"是模糊指令
- 作者团队扩展 Anthropic think 工具，加入 `plan`（分解步骤）和 `action`（下一步工具）字段，形成「思考和规划」工具
- 系统 Prompt 核心规则：每次调用业务工具前**必须先调用**「思考和规划」工具，思考完成后可并行调用多个任务工具
- 并行工具调用：默认关闭（对模型要求高，易出现先调用依赖工具的步骤幻觉），DeepSeek V3 表现较好
- 模型选型：DeepSeek V3（而非 R1），原因：R1 思考时间长且多工具调用能力弱于 V3；V3 工具调用和指令遵循更好，延时更低
- 生成多样性参数建议设为 0.3
- 推理模型的思维链历史会被 chat template 删除（Claude 只保留第一次调用前的思考），思考工具可保留全程上下文，对复杂多工具调用有益
- 与 Manus 类规划执行分离方案对比：该方案较轻量，适用快速任务；长程任务（15~30分钟以上）建议 OpenManus 架构

## 关键引文

无 Cubox 高亮

## 关联

- [[概念_MCP协议]]
- [[概念_Agent感知记忆推理三能力]]
- [[概念_思维链CoT高级方法]]
- [[实体_DeepSeek-V3]]
- [[实体_Qwen3]]
- [[MCP遇上代码执行]]
- [[如何让Agent规划调用工具]]

---
> 📎 **物理文献**：[[raw/如何让 Agent 规划调用工具.md]]

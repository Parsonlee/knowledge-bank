---
type: "source"
tags: ["AI-Agent/skill", "AI-Agent/eval"]
summary: "系统拆解 Agent Skill 的六大评估维度（触发、执行轨迹、产物质量、效率成本、安全权限、可复用性）与对比实验设计范式"
sources: ["raw/articles/如何系统评价一个 Agent Skill？.md"]
created: "2026-07-14"
updated: "2026-07-22"
---

## 来源信息

- 原文：如何系统评价一个 Agent Skill？
- 原始链接：https://mp.weixin.qq.com/s/y2px6sE2N57xrzbQwiHNVQ
- 作者：[[entities/实体_Coggle]]
- 发布时间：2026-07-14

## 核心要点

1. **Skill 评价的增量对比原则（With vs Without Skill）**：评价 Skill 不能仅看加载后的绝对成功率，其核心价值在于“比不使用 Skill 时带来了多少增量提升”。每个测试用例必须对比 `With Skill` 与 `Without Skill` 两组实验（或 `New Skill` vs `Old Skill`）。
2. **触发与路由准确性评价**：Skill 的第一道关口是被正确选择。评估需构建显式触发、隐式触发、上下文触发及相邻/冲突负例测试集，同时覆盖“漏触发”（False Negative）与“误触发”（False Positive），结合 Precision 和 Recall 量化评价。
3. **执行过程轨迹（Trace）与确定性检查**：评价不能仅看最终产物，需全程捕获工具选择、参数、顺序、重试与环境清理等轨迹。优先使用程序化确定性检查（如 JSON 语法、文件存在、命令执行、单元测试）替代高成本且易波动的 [[concepts/概念_LLM_as_a_Judge校准|LLM-as-a-Judge]]。
4. **效率成本与安全权限评估**：评估需引入输入/输出 Token 消耗、延迟、工具调用数及单次成功成本；安全侧需防范越权操作、数据泄露、破坏性命令及对抗性提示词注入（如输入文件中混入恶意指令）。
5. **规范化测试集与目录设计**：建议单个 Skill 从 10-20 个真实 Prompt 起步，涵盖正例、负例、边界及对抗案例；标准化测试空间拆分 baseline 与 candidate 轨迹，便于自动化版本迭代对比。

## 关键引文

> "一个 Skill 通常不只是几段提示词，而是由触发描述、执行说明、脚本、模板、参考资料和验证规则组成的可复用能力包。"

> "Skill 的核心价值不是‘Agent 最终表现如何’，而是：与不使用 Skill 相比，Skill 让 Agent 提升了多少。"

> "如果某些检查可以通过程序完成，就不应完全交给大模型判断。确定性检查比 LLM Judge 更稳定、成本更低，也更容易定位问题。"

## 关联图谱

- [[concepts/概念_Agent_Skill系统化评价框架]]
- [[concepts/概念_Skill增量收益评估]]
- [[concepts/概念_Skill误触发与漏触发评价]]
- [[concepts/概念_Agent完整轨迹评估]]
- [[concepts/概念_Agent_Skills元工具架构]]
- [[entities/实体_Coggle]]

---
> 📎 **物理文献**：[[raw/articles/如何系统评价一个 Agent Skill？.md]]

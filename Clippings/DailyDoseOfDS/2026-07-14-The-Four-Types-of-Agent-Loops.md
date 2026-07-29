title: AI Agent 循环工程（Loop Engineering）的四种范式 source: https://mail.google.com/mail/u/0/#inbox/19f6174c7b5adc67 author:


* "[[DailyDoseOfDS]]" published: 2026-07-14 created: 2026-07-28 description: 深入解析 Agent Loop 的 4 种系统结构：Turn-based、Goal-based、Time-based 与 Proactive Loops，及其适用场景与自动化控制边界。 tags:
* clippings


________________


AI Agent 循环工程（Loop Engineering）的四种范式
循环工程（Loop Engineering）旨在设计掌控 Agent 行为的系统结构，代替人工逐步提示。其核心在于解决两个问题：何时启动以及何时判定任务完成。
Agent 循环的 4 种主流结构
1. Turn-based Loops（基于轮次）：由用户 Prompt 触发。Agent 在单轮内收集上下文、执行并自我检查，随后等待人类审查。适用于需求尚不明确的探索性任务。
2. Goal-based Loops（基于目标）：由包含成功标准与预算的 /goal 命令触发。每次 Agent 试图停止时，独立 Evaluator 模型会校验目标是否达成，未达成则退回继续工作。适用于结果可客观衡量的任务。
3. Time-based Loops（基于时间）：由定时器（Clock）触发，定期运行固定 Prompt（如 /loop 本地或 /schedule 云端）。适用于已知的例行重复任务。
4. Proactive Loops（主动响应）：由事件（Event）监听自动触发，无需人类在场。自动分发给 Triage Agent、Fix Agent 与 Reviewer Agent 组合协同。适用于长效驻留职责。
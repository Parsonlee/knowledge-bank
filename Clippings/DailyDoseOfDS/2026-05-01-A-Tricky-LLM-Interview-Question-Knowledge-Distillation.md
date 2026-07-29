title: AI 工程师面试难题：为什么更弱的 Teacher 模型微调效果反而更好？ source: https://mail.google.com/mail/u/0/#inbox/19de58fc0d126e4b author:

"[[DailyDoseOfDS]]" published: 2026-05-01 created: 2026-07-28 description: 解析知识蒸馏与合成数据微调中的容量错配（Capacity Mismatch）现象：为什么用顶尖模型生成的数据微调小模型，效果反而不如较弱的 Teacher 模型。 tags:

clippings

# AI 工程师面试难题：为什么更弱的 Teacher 模型微调效果反而更好？

在为代码生成任务微调小模型（如 Qwen3-8B）时，使用最强模型（如 GPT-4 / Claude Opus）生成的合成数据进行微调，其表现往往不如使用较弱 Teacher 模型生成的数据。

Fastino Labs 的研究（Pioneer 自动微调 Agent）验证了这一现象。

## 核心原因剖析

容量错配 (Capacity Mismatch)： 超大模型在解决简单问题时，习惯使用高度抽象的模式、复杂的类型提示与精构的错误处理。小模型（如 8B 参数）缺乏足够的参数容量来拟合这些高维抽象表示，强行学习会导致其学习到不稳定的近似解。

遗忘预训练知识 (Forgetting Pretrained Knowledge)： 小模型在预训练阶段已经具备基础代码能力。如果微调数据过于复杂，小模型在试图模仿超大模型的复杂风格时，会破坏并覆盖其原本已有的基础能力。

训练数据过度复杂 (Over-complexity)： 简单 Teacher 模型给出的解答更为直接且匹配任务的真实复杂度，小模型能够干净利落地吸收并泛化。

工程启示：在蒸馏或合成数据微调时，务必根据 Student 模型的参数容量选择合适等级的 Teacher 模型，盲目追求最大最强模型往往适得其反。

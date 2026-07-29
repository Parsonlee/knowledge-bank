title: 在 Claude 中直接微调任意 Hugging Face 大模型 source: https://mail.google.com/mail/u/0/#inbox/19f6174c7b5adc67 author:


* "[[DailyDoseOfDS]]" published: 2026-07-14 created: 2026-07-28 description: 介绍基于 mcp-use SDK 构建的 Fine-tuning Studio，使开发者可以直接在 Claude 界面内完成数据集检索、LoRA 参数配置与 Hugging Face AutoTrain 训练。 tags:
* clippings


________________


在 Claude 中直接微调任意 Hugging Face 大模型
我们基于开源 mcp-use SDK 构建了一个 Hugging Face Fine-tuning Studio，实现了在 Claude 对话界面中直接发起大模型微调：
核心功能与工作流
1. 模型与数据集检索：连接 Hugging Face Hub 搜索目标基座模型与训练数据集。
2. 可视与参数化配置：在 Claude UI 挂载的 Widget 中配置 Chat Template、LoRA Rank、量化级别、Batch Size 及学习率。
3. 云端训练与交互：直接调用 Hugging Face AutoTrain 算力进行训练；训练完成后可直接在 Claude 窗口中与微调后的模型对话。


mcp-use 实现了 MCP Tool 与前端 React 组件的无缝绑定，遵循 MCP Apps 协议标准，为 Agent 交互提供了富媒体 UI 支持。
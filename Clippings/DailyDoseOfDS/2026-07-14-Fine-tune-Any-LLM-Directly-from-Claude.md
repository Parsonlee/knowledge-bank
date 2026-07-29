title: 直接在 Claude 中微调任何大语言模型：mcp-use 与 Hugging Face source: https://mail.google.com/mail/u/0/#inbox/19f6174c7b5adc67 author:


* "[[DailyDoseOfDS]]" published: 2026-07-14 created: 2026-07-28 description: 基于开源 mcp-use SDK 构建 Hugging Face 微调 App，允许用户在 Claude 界面内直接搜索数据集、配置 LoRA 参数并调用 AutoTrain 微调。 tags:
* clippings


________________


直接在 Claude 中微调任何大语言模型：mcp-use 与 Hugging Face
通过全新的 Hugging Face Fine-tuning Studio，开发者可以直接在 Claude 界面中完成全套 LLM 微调流程。
核心功能与架构
1. Hub 交互与格式化：直接从 Claude 搜索 Hugging Face Hub 上的模型和数据集，自动将训练数据转换为聊天模板（Chat Template）；
2. 参数配置 UI：在 Claude UI 界面中直接配置 LoRA Rank、量化位数、Batch Size 以及学习率；
3. 云端训练与对话：训练通过 Hugging Face AutoTrain 部署在云端 GPU 基础设施上运行。训练完成后，用户可直接在 Claude 界面中与微调后的模型进行测试对话。
底层技术：mcp-use SDK
该 Studio 基于开源框架 mcp-use SDK 开发。mcp-use 遵循 MCP Apps 标准（受 OpenAI Apps SDK 启发），允许将任意 MCP Tool 与前端 React UI 组件绑定，自动处理服务端与 Widget 之间的属性映射（Prop Mapping）、打包和热重载。
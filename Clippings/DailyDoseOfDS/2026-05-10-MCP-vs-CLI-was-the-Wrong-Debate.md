title: MCP 与 CLI 之争是个错误的辩题 source: https://mail.google.com/mail/u/0/#inbox/19e13d76eb927af3 author:


* "[[DailyDoseOfDS]]" published: 2026-05-10 created: 2026-07-28 description: 解析 Anthropic 推出的“Code Mode with MCP”架构模式，阐述如何结合 MCP 的类型化契约与 CLI 的按需加载，大幅降低大模型工具调用的 Token 消耗。 tags:
* clippings


________________


MCP 与 CLI 之争是个错误的辩题
2025 年关于 Agent 应该调用 MCP 工具还是直接使用 CLI 命令行争论不休：MCP 提供了类型契约，但预先加载所有 Schema 会白白烧掉 50k+ Token；CLI 延迟加载节省 Context，但缺乏类型约束。


全新 Code Mode 范式将两者结合：


* 模型不直接调用工具，而是编写一小段代码（TypeScript/Python/Bash）在运行时中执行。
* 按需导入（Lazy Imports）：模型仅导入当下需要的类型化工具，工具定义保存在代码而非 Prompt 提示词中，Token 消耗暴降 98.7%！
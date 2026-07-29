title: 构建 100% 本地运行的 AI 第二大脑 source: https://mail.google.com/mail/u/0/#inbox/19e0470d88335c78 author:

"[[DailyDoseOfDS]]" published: 2026-05-07 created: 2026-07-28 description: 剖析 Karpathy 的 LLM Wiki 模式在处理动态工作流时的局限，介绍基于实体与关系图谱的开源本地 AI 第二大脑应用 Rowboat。 tags:

clippings

# 构建 100% 本地运行的 AI 第二大脑

Karpathy 提出的 LLM Wiki 将资料编译为持久的 Markdown 文章，适合相对稳定的学术概念；但在实际工作中，决策与截止日期随对话不断演进，单纯的 Wiki 无法有效追踪事实真值（Ground Truth）。

Rowboat 是一款开源本地桌面应用（支持 Obsidian 共享存储）：

知识图谱而非纯摘要：将人、决策、承诺与截止日期作为独立节点抽离，形成相互关联的实体网格。

100% 本地与隐私安全：数据存储在 ~/.rowboat/ 本地 Markdown 中，支持对接 Ollama 或云端模型。

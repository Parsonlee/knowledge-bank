title: 生产环境中精准追踪 AI 组件到具体代码行 source: https://mail.google.com/mail/u/0/#inbox/19f86be0631f8e2c author:

"[[DailyDoseOfDS]]" published: 2026-07-21 created: 2026-07-28 description: 传统依赖项有 Manifest 文件记录，而开源模型、LLM API 和 MCP 服务缺乏管理；Checkmarx AI Inventory 能自动编目并生成 AI-BOM 以满足合规审计。 tags:

clippings

# 生产环境中精准追踪 AI 组件到具体代码行

现代代码库中的每一个传统软件依赖项都会显式记录在清单（Manifest）文件中，但 AI 组件除外。

开源模型、LLM API、MCP 服务器以及 Agent 往往通过与普通软件包相同的 Pull Request 进入生产环境，但没有 Lockfile 记录它们，现有的依赖项扫描工具也无法感知它们的存在。

Checkmarx 的调查显示：70% 的团队预计在生产环境中使用 AI 组件，而其中 43% 对这些组件完全缺乏治理。

## 解决方案：Checkmarx AI Inventory

Checkmarx AI Inventory（Checkmarx One 的一部分）能够确定性地编目每个模型、SDK 和 MCP 服务器，将其精确追溯到具体的文件和代码行，并导出 AI-BOM（AI 软件物料清单） 以应对合规审计。

Gartner 已将 Checkmarx 评为软件供应链安全魔力象限的领导者。

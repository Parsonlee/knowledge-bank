title: "生产环境中精准追踪 AI 组件到代码行" source: "https://mail.google.com/mail/u/0/#inbox/19f86be0631f8e2c" author:


* "[[DailyDoseOfDS]]" published: 2026-06-26 created: 2026-07-28 description: "介绍如何使用 Checkmarx AI Inventory 在生产代码库中精准盘点开源模型、SDK 与 MCP 服务，生成 AI 软件物料清单（AI-BOM）并追踪至具体代码行。" tags:
* clippings


________________


生产环境中精准追踪 AI 组件到代码行
现代代码库中的每一个第三方依赖项都会出现在清单（Manifest）文件中，唯独 AI 相关的组件例外。


开源模型、大语言模型 API、MCP 服务器以及各类 Agent 通常会通过与普通软件包相同的 Pull Request 进入生产环境，但既没有 Lockfile 锁文件对其进行罗列，也没有常规的依赖项扫描工具能识别到它们的存在。


Checkmarx 的调查研究发现：70% 的技术团队预估生产环境中已包含 AI 组件，但其中 43% 的团队对这些 AI 组件完全处于零监管状态。


________________


Checkmarx AI Inventory 解决方案
Checkmarx AI Inventory（作为 Checkmarx One 平台的一部分）提供了针对 AI 组件的治理能力：


* 确定性盘点：自动盘点代码库中的每一个 AI 模型、SDK 和 MCP 服务器。
* 精准追踪：将每一个 AI 组件追踪并定位到具体的代码文件与精准行号。
* 合规导出：导出 AI 软件物料清单（AI-BOM），满足合规性审计要求。


Gartner 已将 Checkmarx 评为软件供应链安全魔力象限的领导者（Leader）。
---
id: "7395002192941286835"
cubox_url: https://cubox.pro/web/card/7395002192941286835
url: https://baoyu.io/translations/claude-skills-deep-dive
tags:
  - AI-Agent/context-engineering
  - AI-Agent/skill
---
# 从第一性原理深度拆解 Claude Agent Skill | 宝玉的分享

执行工作流 (The Lifecycle)
当 Claude 决定使用某个 Skill（例如 pdf 处理技能）时，系统会执行以下非传统的工具调用流程：
1. 调用阶段：Claude 发出工具调用请求 Skill(command="pdf")。
2. 拦截与注入 (The Injection - 核心步骤)：
系统不执行该命令并返回结果。
相反，系统读取 pdf 技能的 SKILL.md 文件。
上下文修改：系统将 Markdown 中的详细指令作为新的用户消息 (User Messages) 插入到对话历史中。
执行环境修改：系统更新当前会话的权限（例如临时授予读取文件和运行特定 Bash ...

[Read in Cubox](https://cubox.pro/web/card/7395002192941286835)  
[Read Original](https://baoyu.io/translations/claude-skills-deep-dive)  

---

\## Annotations  

> 工具做了一件事，返回了一个结果，交互就结束了。技能的运作方式根本不同。技能不是执行离散动作并返回结果，而是注入全面的指令集，修改 Claude 对任务的推理和处理方式。这创造了一个普通工具从未面临的设计挑战：用户需要了解哪些技能正在运行以及它们在做什么的透明度，而 Claude 需要详细的、可能非常冗长的指令来正确执行技能。  

[Link️](https://cubox.pro/web/annotations/cards/7395002192941286835?highlight=7395008116699430955)


---

\## 📖 正文全文

# 从第一性原理深度拆解 Claude Agent Skill

[baoyu.io](https://baoyu.io/translations/claude-skills-deep-dive)

**作者：** Han Lee

Claude 的 Agent `Skills`（技能）系统代表了一种精妙的、基于提示词（Prompt）的"元工具"架构。它通过注入专门的指令，极大地扩展了大语言模型（LLM）的能力。与传统的函数调用或代码执行不同，`Skills` 不编写可执行代码，而是通过 **提示词扩展（Prompt Expansion）** 和 **上下文修改（Context Modification）** 来改变 Claude 处理后续请求的方式。

这篇深度文章将从第一性原理出发，解构 Claude 的 Agent `Skills` 系统。我们将记录这个架构的运作方式：一个名为 `Skill` 的工具充当"元工具"，将特定领域的提示词注入到对话上下文中。我们将以 `skill-creator` 和 `internal-comms` 技能为例，完整复盘其生命周期------从文件解析、API 请求结构，一直到 Claude 的决策过程。

\## Claude Agent Skill 概览

Claude 使用 `Skills` 来提升其执行特定任务的表现。`Skills` 本质上是包含指令、脚本和资源的文件夹，Claude 可以在需要时加载它们。Claude 使用一套 **声明式的、基于提示词的系统** 来发现和调用技能。

AI 模型（即 Claude）是根据系统提示词中的文本描述，自主决定是否调用 `Skills` 的。**代码层面不存在算法式的"技能选择器"或 AI 意图检测模块**。所有的决策都发生在 Claude 的推理过程中，完全基于提供的技能描述。

`Skills` 不是可执行代码。它们 **不运行** Python 或 JavaScript，后台也没有 HTTP 服务器或函数调用。它们也不是硬编码在 Claude 系统提示词里的。`Skills` 存在于 API 请求结构的一个独立部分中。

那么，它们到底是什么？`Skills` 是专门的提示词模板，用于将领域特定的指令注入到对话上下文中。当一个技能被调用时，它会同时修改对话上下文（通过注入指令提示词）和执行上下文（通过改变工具权限，甚至可能切换模型）。技能不是直接执行动作，而是展开成详细的提示词，让 Claude **准备好** 去解决特定类型的问题。每一个技能都像是动态添加到 Claude 工具库中的新能力。

当用户发送请求时，Claude 会收到三样东西：用户消息、可用的工具（Read, Write, Bash 等），以及 `Skill` 工具。`Skill` 工具的描述包含了一个格式化的列表，列出了所有可用技能的 `name`（名称）、`description`（描述）等字段。Claude 阅读这个列表，利用其自然语言理解能力将你的意图与技能描述进行匹配。如果你说"帮我创建一个日志技能"，Claude 看到 `internal-comms` 技能的描述（"当用户想要用公司喜欢的格式编写内部通讯时..."），识别出匹配项，并调用 `Skill` 工具，参数为 `command: "internal-comms"`。
> **术语说明**：
>
> * `Skill` tool（大写 S）：管理所有技能的"元工具"。它与 Read, Write, Bash 等并列出现在 Claude 的 `tools` 数组中。
>
> * **skills** （小写 s）：具体的单个技能，如 `pdf`, `skill-creator`, `internal-comms`。这些是 `Skill` 工具加载的专门指令模板。

下图更直观地展示了 Claude 如何使用 `skills`。

![](https://image.cubox.pro/cardImg/4e5iyi4dsn5nfrahfhfwnp797drfhv2ka16lq36bnkhjbda0lx.png?imageMogr2/quality/90/ignore-error/1)

技能选择机制在代码层面没有算法路由或意图分类。Claude Code 不使用嵌入（Embeddings）、分类器或模式匹配来决定调用哪个技能。相反，系统将所有可用技能格式化为文本描述，嵌入到 `Skill` 工具的提示词中，让 Claude 的语言模型来做决定。这是纯粹的 LLM 推理。没有正则表达式，没有关键词匹配，没有基于机器学习的意图检测。决策发生在 Claude 在 Transformer 模型的 **前向传播（Forward Pass）** 中，而不是在应用程序代码里。

当 Claude 调用一个技能时，系统遵循一个简单的工作流：加载 markdown 文件（`SKILL.md`），将其扩展为详细指令，将这些指令作为新的用户消息注入到对话上下文中，修改执行上下文（允许的工具、模型选择），然后在这个增强的环境中继续对话。这与传统的工具（执行并返回结果）有本质区别。技能是 **让 Claude 准备好** 去解决问题，而不是直接解决问题。

下表有助于更好地区分"传统工具"和"技能"及其能力的差异：

|----------|--------------------------|-----------------------------------|
| 维度       | 传统工具 (Traditional Tools) | 技能 (Skills)                       |
| **执行模式** | 同步，直接执行                  | 提示词扩展                             |
| **目的**   | 执行具体操作                   | 引导复杂的工作流                          |
| **返回值**  | 即时结果                     | 对话上下文 + 执行上下文的改变                  |
| **例子**   | `Read`, `Write`, `Bash`  | `internal-comms`, `skill-creator` |
| **并发性**  | 通常安全                     | 非并发安全                             |
| **类型**   | 多种多样                     | 始终为 `"prompt"`                    |

\## 构建 Agent Skill

现在，让我们通过研究 Anthropic 技能库中的 `skill-creator` 技能 作为案例，深入了解如何构建技能。提醒一下，Agent `skills` 是包含指令、脚本和资源的文件夹，Agent 可以动态发现和加载它们，以便更好地执行特定任务。`Skills` 通过将你的专业知识打包成 Claude 可组合的资源，扩展了 Claude 的能力，将通用 Agent 转变为适合你需求的专用 Agent。
> **核心洞察**：技能 (Skill) = 提示词模板 + 对话上下文注入 + 执行上下文修改 + 可选的数据文件和 Python 脚本

每个 `Skill` 都在一个名为 `SKILL.md`（大小写不敏感）的 markdown 文件中定义，并在 `/scripts`（脚本）、`/references`（参考资料）和 `/assets`（资源）下包含可选的绑定文件。这些绑定文件可以是 Python 脚本、Shell 脚本、字体定义、模板等。以 `skill-creator` 为例，它包含 `SKILL.md`、用于许可的 `LICENSE.txt`，以及 `/scripts` 文件夹下的一些 Python 脚本。`skill-creator`没有任何 `/references` 或 `/assets`。

![](https://image.cubox.pro/cardImg/4pz1bioierd8z8jv6h0hq0msx3ll6euuqubc04o086juxnsyfw.png?imageMogr2/quality/90/ignore-error/1)

技能可以从多个来源发现和加载。Claude Code 会扫描用户设置（`~/.config/claude/skills/`）、项目设置（`.claude/skills/`）、插件提供的技能以及内置技能，以构建可用技能列表。对于 Claude Desktop，我们可以像下面这样上传自定义技能。

![](https://image.cubox.pro/cardImg/1nuvjx5ys04j04561n2lobk4io0e6tzq271fy04v9xyvbx66n7.png?imageMogr2/quality/90/ignore-error/1)
> **注意：** 构建技能最重要的概念是 **渐进式披露（Progressive Disclosure）** ------只展示足够的信息来帮助 Agent 决定下一步做什么，然后根据需要披露更多细节。在 `agent skills` 的案例中，它：
>
> 1. 披露 Frontmatter（前置元数据）：最少量的信息（名称、描述、许可证）
>
> 2. 如果选中某个 `skill`，加载 SKILL.md：全面但聚焦的内容
>
> 3. 然后在执行 `skill` 时，加载辅助资源、参考资料和脚本

\## 编写 SKILL.md

`SKILL.md` 是技能提示词的核心。它是一个 markdown 文件，遵循两部分结构------Frontmatter（前置元数据）和内容。Frontmatter 配置技能 **如何** 运行（权限、模型、元数据），而 markdown 内容告诉 Claude **做什么** 。[Frontmatter](https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter) 是用 YAML 编写的文件头。


    ┌─────────────────────────────────────┐
    │ 1. YAML Frontmatter (元数据)        │ ← 配置
    │    ---                              │
    │    name: skill-name                 │
    │    description: 简要概述            │
    │    allowed-tools: "Bash, Read"      │
    │    version: 1.0.0                   │
    │    ---                              │
    ├─────────────────────────────────────┤
    │ 2. Markdown 内容 (指令)             │ ← 给 Claude 的提示词
    │                                     │
    │    目的解释                         │
    │    详细指令                         │
    │    示例和指南                       │
    │    分步流程                         │
    └─────────────────────────────────────┘

Frontmatter 包含控制 Claude 如何发现和使用技能的元数据。以 `skill-creator` 的 Frontmatter 为例：

    ---
    name: skill-creator
    description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
    license: Complete terms in LICENSE.txt
    ---

让我们逐一浏览 Frontmatter 的字段。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fbaoyu.io%2Fuploads%2F2025-11-25-04-claude-skill-frontmatter%281%29.png&valid=false)

\#\#\## name (必填)

不言自明。`skill` 的名称。一个 `skill` 的 `name` 被用作 `Skill Tool` 中的 `command`（命令）。
> `skill` 的 `name` 被用作 `Skill Tool` 中的 `command`。

\#\#\## description (必填)

`description` 字段提供了技能功能的简要总结。这是 Claude 用来决定何时调用技能的主要信号。在上面的例子中，描述明确指出"当用户想要创建新技能时应使用此技能"------这种清晰、面向动作的语言有助于 Claude 将用户意图与技能能力相匹配。

系统会自动将来源信息附加到描述后（例如 `"(plugin:skills)"`），这有助于在加载多个技能时区分不同来源的技能。

\#\#\## when_to_use (未文档化------可能已弃用或为未来功能)

> ⚠**重要提示** ：`when_to_use` 字段在代码库中广泛出现，但 **并未出现在任何 Anthropic 官方文档中**。此字段可能是：
>
> * 一个正在被逐步淘汰的弃用功能
>
> * 一个尚未正式支持的内部/实验性功能
>
> * 一个计划中但尚未发布的功能
>
> **建议** ：依赖详细的 `description` 字段。在生产环境的技能中避免使用 `when_to_use`，直到它出现在官方文档中。

尽管未文档化，以下是 `when_to_use` 目前在代码库中的工作方式：

    function formatSkill(skill) {
      let description = skill.whenToUse
        ? `${skill.description} - ${skill.whenToUse}`
        : skill.description;

      return `"${skill.name}": ${description}`;
    }

当存在时，`when_to_use` 会通过连字符附加到描述后面。例如：

    "skill-creator": Create well-structured, reusable skills... - When user wants to build a custom skill package with scripts, references, or assets

这个组合字符串就是 Claude 在 Skill 工具提示词中看到的内容。然而，由于此行为未记录，它可能会在未来版本中更改或删除。更安全的方法是将使用指南直接包含在 `description` 字段中，如上面的 `skill-creator` 示例所示。

\#\#\## allowed-tools (可选)

`allowed-tools` 字段定义了技能无需用户批准即可使用的工具，类似于 Claude 的 allowed-tools。

这是一个逗号分隔的字符串，会被解析为允许的工具名称数组。你可以使用通配符来限定权限范围，例如，`Bash(git:*)` 仅允许 git 子命令，而 `Bash(npm:*)` 允许所有 npm 操作。skill-creator 技能使用 `"Read,Write,Bash,Glob,Grep,Edit"` 来赋予其广泛的文件和搜索能力。一个常见的错误是列出所有可用工具，这会产生安全风险并破坏安全模型。
> 只包含你的技能实际需要的工具------如果你只是读写文件，`"Read,Write"` 就足够了。

    # ✅ skill-creator 允许使用多个工具
    allowed-tools: "Read,Write,Bash,Glob,Grep,Edit"

    # ✅ 仅限特定的 git 命令
    allowed-tools: "Bash(git status:*),Bash(git diff:*),Bash(git log:*),Read,Grep"

    # ✅ 仅限文件操作
    allowed-tools: "Read,Write,Edit,Glob,Grep"

    # ❌ 不必要的攻击面（权限过大）
    allowed-tools: "Bash,Read,Write,Edit,Glob,Grep,WebSearch,Task,Agent"

    # ❌ 不必要的攻击面，允许所有 npm 命令
    allowed-tools: "Bash(npm:*),Read,Write"

\#\#\## model (可选)

`model` 字段定义了技能可以使用哪个模型。默认情况下，它继承用户会话中的当前模型。对于像代码审查这样的复杂任务，技能可以请求更强大的模型，如 Claude Opus 或其他开源中文模型（懂的都懂）。

    model: "claude-opus-4-20250514"  # 使用特定模型
    model: "inherit"                 # 使用会话的当前模型（默认）

\#\#\## version, disable-model-invocation, 和 mode (可选)

技能支持三个可选的 Frontmatter 字段用于版本控制和调用控制。`version` 字段（例如 version: "1.0.0"）是一个用于跟踪技能版本的元数据字段，主要用于文档和技能管理。

`disable-model-invocation` 字段（布尔值）防止 Claude 通过 `Skill` 工具自动调用该技能。当设置为 true 时，该技能将从向 Claude 展示的列表中排除，只能由用户通过 `/skill-name` 手动调用，这使其非常适合危险操作、配置命令或需要明确用户控制的交互式工作流。

`mode` 字段（布尔值）将技能归类为修改 Claude 行为或上下文的"模式命令"。当设置为 true 时，该技能会出现在技能列表顶部的特殊"模式命令"部分（与常规实用技能分开），这使得像 debug-mode（调试模式）、expert-mode（专家模式）或 review-mode（审查模式）这样建立特定操作上下文或工作流的技能更加突出。

\#\## SKILL.md 提示词内容

Frontmatter 之后是 markdown 内容------即调用 `skill` 时 Claude 收到的实际提示词。在这里你需要定义 `skill` 的行为、指令和工作流。编写有效技能提示词的关键是保持聚焦并使用 **渐进式披露**：在 SKILL.md 中提供核心指令，并引用外部文件以获取详细内容。

这是一个推荐的内容结构：

    ---
    # Frontmatter 在这里
    ---

    # [简短的目的陈述 - 1-2 句话]

    \## 概览 (Overview)
    [此技能做什么，何时使用，提供什么]

    \## 前置条件 (Prerequisites)
    [需要的工具、文件或上下文]

    \## 指令 (Instructions)

    \#\## 第一步：[第一个动作]
    [祈使句指令]
    [如果需要，提供示例]

    \#\## 第二步：[下一个动作]
    [祈使句指令]

    \#\## 第三步：[最终动作]
    [祈使句指令]

    \## 输出格式 (Output Format)
    [如何构建结果]

    \## 错误处理 (Error Handling)
    [失败时怎么做]

    \## 示例 (Examples)
    [具体的使用案例]

    \## 资源 (Resources)
    [如果绑定了 scripts/, references/, assets/ 文件夹，在此引用]

举个例子，`skill-creator` 技能包含以下指令，指定了创建技能所需的每个工作流步骤。

    \## Skill Creation Process (技能创建流程)

    \#\## Step 1: Understanding the Skill with Concrete Examples (通过具体示例理解技能)
    \#\## Step 2: Planning the Reusable Skill Contents (规划可复用的技能内容)
    \#\## Step 3: Initializing the Skill (初始化技能)
    \#\## Step 4: Edit the Skill (编辑技能)
    \#\## Step 5: Packaging a Skill (打包技能)

当 Claude 调用此技能时，它会收到整个提示词作为新指令，并预置了基础目录路径。`{baseDir}` 变量解析为技能的安装目录，允许 Claude 使用 Read 工具加载参考文件：`Read({baseDir}/scripts/init_skill.py)`。这种模式保持了主提示词简洁，同时按需提供详细文档。

**提示词内容的最佳实践：**

* 字数控制在 5,000 词（约 800 行）以内，以免上下文过载。

* 使用祈使语气（"分析代码..."）而不是第二人称（"你应该分析..."）。

* 引用外部文件获取详细内容，而不是把所有东西都塞进去。

* 使用 `{baseDir}` 作为路径，永远不要硬编码绝对路径如 `/home/user/project/`。

```

```

❌ Read /home/user/project/config.json ✅ Read {baseDir}/config.json

当技能被调用时，Claude 仅获得 `allowed-tools` 中指定工具的访问权限，如果在 Frontmatter 中指定了模型，则可能会覆盖当前模型。系统会自动提供技能的基础目录路径，使绑定的资源可被访问。

\#\## 随技能绑定资源

当你将支持资源与 `SKILL.md` 绑定在一起时，`Skills` 会变得非常强大。标准结构使用三个目录，每个目录服务于特定目的：

    my-skill/
    ├── SKILL.md              # 核心提示词和指令
    ├── scripts/              # 可执行的 Python/Bash 脚本
    ├── references/           # 加载到上下文中的文档
    └── assets/               # 模板和二进制文件

**为什么要绑定资源？** 保持 SKILL.md 简洁（低于 5,000 词）可以防止挤爆 Claude 的上下文窗口。绑定资源允许你提供详细文档、自动化脚本和模板，而不会使主提示词臃肿。Claude 仅在需要时通过渐进式披露加载它们。

\#\#\## scripts/ 目录

`scripts/` 目录包含 Claude 通过 Bash 工具运行的可执行代码------自动化脚本、数据处理器、验证器或执行确定性操作的代码生成器。

例如，`skill-creator` 的 SKILL.md 引用脚本的方式如下：

    当从头开始创建一个新技能时，始终运行 `init_skill.py` 脚本。该脚本方便地生成一个新的模板技能目录，自动包含技能所需的一切，使技能创建过程更加高效可靠。

    用法：

    `scripts/init_skill.py <skill-name> --path <output-directory>`

    该脚本：
      - 在指定路径创建技能目录
      - 生成带有正确 Frontmatter 和 TODO 占位符的 SKILL.md 模板
      - 创建示例资源目录：scripts/, references/, 和 assets/
      - 在每个目录中添加可自定义或删除的示例文件

当 Claude 看到这条指令时，它会执行 `python {baseDir}/scripts/init_skill.py`。`{baseDir}` 变量会自动解析为技能的安装路径，使技能在不同环境中都能移植。

**scripts/ 适用于** 复杂的多步操作、数据转换、API 交互，或任何比起自然语言更适合用代码表达的精确逻辑。

\#\#\## references/ 目录

`references/` 目录存储 Claude 在被引用时读入其上下文的文档。这是文本内容------markdown 文件、JSON 模式、配置模板或 Claude 完成任务所需的任何文档。

例如，`mcp-creator` 的 SKILL.md 引用资料的方式如下：

    \#\#\## 1.4 研究框架文档

    **加载并阅读以下参考文件：**

    - **MCP 最佳实践**: [📋 查看最佳实践](./reference/mcp_best_practices.md) - 所有 MCP 服务器的核心指南

    **对于 Python 实现，还需加载：**
    - **Python SDK 文档**: 使用 WebFetch 加载 `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
    - [🐍 Python 实现指南](./reference/python_mcp_server.md) - Python 特有的最佳实践和示例

    **对于 Node/TypeScript 实现，还需加载：**
    - **TypeScript SDK 文档**: 使用 WebFetch 加载 `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
    - [⚡ TypeScript 实现指南](./reference/node_mcp_server.md) - Node/TypeScript 特有的最佳实践和示例

当 Claude 遇到这些指令时，它使用 Read 工具：`Read({baseDir}/references/mcp_best_practices.md)`。内容被加载到 Claude 的上下文中，提供了详细信息而不会弄乱 SKILL.md。

**references/ 适用于** 详细文档、大型模式库、检查清单、API 模式，或任何对任务必要但对 SKILL.md 来说太冗长的文本内容。

\#\#\## assets/ 目录

`assets/` 目录包含 Claude 通过路径引用但不加载到上下文中的模板和二进制文件。可以将其视为技能的静态资源------HTML 模板、CSS 文件、图像、配置样板或字体。

在 SKILL.md 中：

    使用 {baseDir}/assets/report-template.html 处的模板作为报告结构。
    参考 {baseDir}/assets/diagram.png 处的架构图。

Claude 看到文件路径但不会读取内容。相反，它可能会将模板复制到新位置，填充占位符，或在生成的输出中引用该路径。

**assets/ 适用于** HTML/CSS 模板、图像、二进制文件、配置模板，或任何 Claude 通过路径操作而不是读入上下文的文件。

`references/` 和 `assets/` 之间的关键区别在于：

* **references/**：通过 Read 工具加载到 Claude 上下文中的文本内容

* **assets/**：仅通过路径引用，不加载到上下文中的文件

这种区别对上下文管理至关重要。`references/` 中一个 10KB 的 markdown 文件在加载时会消耗上下文 Token。`assets/` 中一个 10KB 的 HTML 模板则不会。Claude 只是知道路径存在。
> **最佳实践：** 始终使用 `{baseDir}` 作为路径，永远不要硬编码绝对路径。这使得技能在不同用户环境、项目目录和安装中都可移植。

\#\## 常见技能模式

正如工程中的所有事物一样，理解常见模式有助于设计有效的技能。以下是工具集成和工作流设计中最有用的模式。

\#\#\## 模式 1：脚本自动化

**用例：** 需要多个命令或确定性逻辑的复杂操作。

这种模式将计算任务卸载到 `scripts/` 目录中的 Python 或 Bash 脚本。技能提示词告诉 Claude 执行脚本并处理其输出。

**SKILL.md 示例：**

    在目标目录上运行 scripts/analyzer.py：

    `python {baseDir}/scripts/analyzer.py --path "$USER_PATH" --output report.json`

    解析生成的 `report.json` 并展示发现。

**所需工具：**

    allowed-tools: "Bash(python {baseDir}/scripts/*:*), Read, Write"

\#\#\## 模式 2：读取 - 处理 - 写入 (Read - Process - Write)

**用例：** 文件转换和数据处理。

最简单的模式------读取输入，按照指令转换，写入输出。适用于格式转换、数据清理或报告生成。

**SKILL.md 示例：**

    \## 处理工作流
    1. 使用 Read 工具读取输入文件
    2. 根据格式解析内容
    3. 按照规范转换数据
    4. 使用 Write 工具写入输出
    5. 报告完成并提供总结

**所需工具：**

    allowed-tools: "Read, Write"

\#\#\## 模式 3：搜索 - 分析 - 报告 (Search - Analyze - Report)

**用例：** 代码库分析和模式检测。

使用 Grep 在代码库中搜索模式，读取匹配的文件以获取上下文，分析发现，并生成结构化报告。或者，搜索企业数据存储以获取数据，分析检索到的数据，并生成结构化报告。

**SKILL.md 示例：**

    \## 分析流程
    1. 使用 Grep 查找相关代码模式
    2. 读取每个匹配的文件
    3. 分析漏洞
    4. 生成结构化报告

**所需工具：**

    allowed-tools: "Grep, Read"

\#\#\## 模式 4：命令链执行 (Command Chain Execution)

**用例：** 具有依赖关系的多步操作。

执行一系列命令，其中每一步都取决于前一步的成功。常用于类似 CI/CD 的工作流。

**SKILL.md 示例：**

    执行分析流水线：
    npm install && npm run lint && npm test

    报告每个阶段的结果。

**所需工具：**

    allowed-tools: "Bash(npm install:*), Bash(npm run:*), Read"

\#\## 高级模式

\#\#\## 引导式多步工作流 (Wizard-Style Multi-Step Workflows)

**用例：** 每一步都需要用户输入的复杂流程。

将复杂任务分解为离散步骤，每个阶段之间都有明确的用户确认。适用于设置向导、配置工具或引导式流程。

**SKILL.md 示例：**

    \## 工作流

    \#\## 第一步：初始设置
    1. 询问用户项目类型
    2. 验证先决条件是否存在
    3. 创建基础配置
    等待用户确认后再继续。

    \#\## 第二步：配置
    1. 展示配置选项
    2. 询问用户选择设置
    3. 生成配置文件
    等待用户确认后再继续。

    \#\## 第三步：初始化
    1. 运行初始化脚本
    2. 验证设置成功
    3. 报告结果

\#\#\## 基于模板的生成 (Template-Based Generation)

**用例：** 从存储在 `assets/` 中的模板创建结构化输出。

加载模板，用用户提供或生成的数据填充占位符，并写入结果。常用于报告生成、样板代码创建或文档编写。

**SKILL.md 示例：**

    \## 生成流程
    1. 从 {baseDir}/assets/template.html 读取模板
    2. 解析用户需求
    3. 填充模板占位符：
       - {{name}} → 用户提供的名称
       - {{summary}} → 生成的总结
       - {{date}} → 当前日期
    4. 将填充后的模板写入输出文件
    5. 报告完成

\#\#\## 迭代优化 (Iterative Refinement)

**用例：** 需要多次扫描且深度递增的流程。

首先进行广泛分析，然后逐步深入研究已识别的问题。适用于代码审查、安全审计或质量分析。

**SKILL.md 示例：**

    \## 迭代分析

    \#\## 第一轮：广度扫描
    1. 搜索整个代码库的模式
    2. 识别高层级问题
    3. 对发现进行分类

    \#\## 第二轮：深度分析
    对于每个高层级问题：
    1. 读取完整文件上下文
    2. 分析根本原因
    3. 确定严重程度

    \#\## 第三轮：建议
    对于每个发现：
    1. 研究最佳实践
    2. 生成具体修复方案
    3. 估算工作量

    展示包含所有发现和建议的最终报告。

\#\#\## 上下文聚合 (Context Aggregation)

**用例：** 结合多来源信息以建立全面理解。

从不同文件和工具收集数据，综合成连贯的图景。适用于项目总结、依赖分析或影响评估。

**SKILL.md 示例：**

    \## 上下文收集
    1. 读取项目 README.md 获取概览
    2. 分析 package.json 获取依赖
    3. Grep 代码库查找特定模式
    4. 检查 git 历史记录获取最近更改
    5. 将发现综合成连贯的总结

\## Agent Skill 内部架构

涵盖了概览和构建过程后，我们现在可以检查技能在底层是如何实际工作的。技能系统通过一个"元工具"架构运行，其中一个名为 `Skill` 的工具充当所有单独技能的容器和调度器。这种设计从实现和目的上将技能与传统工具从根本上区分开来。
> `Skill` 工具是管理所有技能的元工具

\## Skills 对象设计

传统工具如 `Read`、`Bash` 或 `Write` 执行离散动作并返回即时结果。技能运作方式不同。它们不直接执行动作，而是将专门的指令注入对话历史，并动态修改 Claude 的执行环境。这通过两条用户消息来实现------一条包含用户可见的元数据，另一条包含从 UI 中隐藏但发送给 Claude 的完整技能提示词------并通过改变 Agent 的上下文来更改权限、切换模型，并在技能使用期间调整思维 Token 参数。

|--------------|-----------------------------------------|-------------------------------------------------------------------------|
| 特性           | 普通工具                                    | Skill 工具                                                                |
| **本质**       | 直接动作执行者                                 | 提示词注入 + 上下文修改器                                                          |
| **消息角色**     | assistant → tool_use user → tool_result | assistant → tool_use Skill user → tool_result user → skill prompt ← 注入！ |
| **复杂度**      | 简单 (3-4 条消息)                            | 复杂 (5-10+ 条消息)                                                          |
| **上下文**      | 静态                                      | 动态 (每轮修改)                                                               |
| **持久性**      | 仅工具交互                                   | 工具交互 + 技能提示词                                                            |
| **Token 开销** | 极小 (\~100 tokens)                       | 巨大 (\~1,500+ tokens 每轮)                                                 |
| **用例**       | 简单、直接的任务                                | 复杂、引导式工作流                                                               |

其复杂性是巨大的。普通工具产生简单的消息交换------一个助手工具调用后跟一个用户结果。技能则注入多条消息，在动态修改的上下文中运行，并带来显著的 Token 开销，以提供指导 Claude 行为的专门指令。

理解 `Skill` 元工具的工作原理揭示了这个系统的机制。让我们检查它的结构：

    Pd = {
      name: "Skill",  // 工具名称常量：$N = "Skill"

      inputSchema: {
        command: string  // 例如："pdf", "skill-creator"
      },

      outputSchema: {
        success: boolean,
        commandName: string
      },

      // 🔑 关键字段：这生成技能列表
      prompt: async () => fN2(),

      // 验证和执行
      validateInput: async (input, context) => { /* 5 种错误代码 */ },
      checkPermissions: async (input, context) => { /* 允许/拒绝/询问 */ },
      call: async *(input, context) => { /* 产出消息 + 上下文修改器 */ }
    }

`prompt` 字段将 Skill 工具与其他如 `Read` 或 `Bash` 等具有静态描述的工具区分开来。Skill 工具不使用固定字符串，而是使用动态提示词生成器，通过聚合所有可用技能的名称和描述在运行时构建其描述。这实现了 **渐进式披露** ------系统只加载最少的元数据（Frontmatter 中的技能名称和描述）到 Claude 的初始上下文中，只提供足够的信息让模型决定哪个技能匹配用户意图。完整的技能提示词只有在 Claude 做出选择后才加载，防止上下文膨胀，同时保持可发现性。

    async function fN2() {
      let A = await atA(),
        {
          modeCommands: B,
          limitedRegularCommands: Q
        } = vN2(A),
        G = [...B, ...Q].map((W) => W.userFacingName()).join(", ");
      l(`Skills and commands included in Skill tool: ${G}`);
      let Z = A.length - B.length,
        Y = nS6(B),
        J = aS6(Q, Z);
      return `Execute a skill within the main conversation

    <skills_instructions>
    When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively. Skills provide specialized capabilities and domain knowledge.

    How to use skills:
    - Invoke skills using this tool with the skill name only (no arguments)
    - When you invoke a skill, you will see <command-message>The "{name}" skill is loading</command-message>
    - The skill's prompt will expand and provide detailed instructions on how to complete the task
    - Examples:
      - \`command: "pdf"\` - invoke the pdf skill
      - \`command: "xlsx"\` - invoke the xlsx skill
      - \`command: "ms-office-suite:pdf"\` - invoke using fully qualified name

    Important:
    - Only use skills listed in <available_skills> below
    - Do not invoke a skill that is already running
    - Do not use this tool for built-in CLI commands (like /help, /clear, etc.)
    </skills_instructions>

    <available_skills>
    ${Y}${J}
    </available_skills>
    `;
    }

与某些助手（如 ChatGPT）将工具放在系统提示词中不同，Claude 的 **agent skills 不存在于系统提示词中** 。它们作为 `Skill` 工具描述的一部分存在于 `tools` 数组中。单个技能的名称作为 `Skill` 元工具输入模式的 `command` 字段的一部分。为了更好地可视化它的样子，这是实际的 API 请求结构：

    {
      "model": "claude-sonnet-4-5-20250929",
      "system": "You are Claude Code, Anthropic's official CLI...",  // ← 系统提示词
      "messages": [
        {"role": "user", "content": "Help me create a new skill"},
        // ... 对话历史
      ],
      "tools": [  // ← 发送给 Claude 的工具数组
        {
          "name": "Skill",  // ← 元工具
          "description": "Execute a skill...\n\n<skills_instructions>...\n\n<available_skills>\n...",
          "input_schema": {
            "type": "object",
            "properties": {
              "command": {
                "type": "string",
                "description": "The skill name (no arguments)"  // ← 单个技能的名称
              }
            }
          }
        },
        {
          "name": "Bash",
          "description": "Execute bash commands...",
          // ...
        },
        {
          "name": "Read",
          // ...
        }
        // ... 其他工具
      ]
    }

`<available_skills>` 部分存在于 Skill 工具的描述中，并为每个 API 请求重新生成。系统通过聚合当前从用户和项目配置加载的技能、插件提供的技能以及任何内置技能来动态构建此列表，但受默认 15,000 个字符的 Token 预算限制。这一预算限制迫使技能作者编写简洁的描述，并确保工具描述不会压垮模型的上下文窗口。

\## 技能对话和执行上下文注入设计

大多数 LLM API 支持理论上可以携带系统提示词的 `role: "system"` 消息。事实上，OpenAI 的 ChatGPT 在其系统提示词中携带其默认工具，包括用于记忆的 `bio`，用于任务调度的 `automations`，用于控制画布的 `canmore`，用于图像生成的 `img_gen`，以及 `file_search`、`python` 和 `web`。最后，工具提示词占据了其系统提示词中约 90% 的 Token 计数。如果我们要加载大量工具和/或技能到上下文中，这种方法虽然有用，但效率很低。

然而，系统消息具有不同的语义，使其不适合技能。系统消息设置了贯穿整个对话的全局上下文，以比用户指令更高的权威性影响所有后续轮次。

技能需要临时的、有作用域的行为。`skill-creator` 技能应该只影响技能创建相关的任务，而不是在剩余会话中将 Claude 永久转变为 PDF 专家。使用 `role: "user"` 配合 `isMeta: true` 让技能提示词对 Claude 表现为用户输入，保持其临时性和局限在当前交互中。技能完成后，对话返回到正常的对话上下文和执行上下文，没有残留的行为修改。

像 `Read`、`Write` 或 `Bash` 这样的普通工具具有简单的通信模式。当 Claude 调用 `Read` 时，它发送文件路径，接收文件内容，然后继续工作。用户在记录中看到"Claude 使用了 Read 工具"，这对于透明度来说已经足够了。工具做了一件事，返回了一个结果，交互就结束了。技能的运作方式根本不同。技能不是执行离散动作并返回结果，而是注入全面的指令集，修改 Claude 对任务的推理和处理方式。这创造了一个普通工具从未面临的设计挑战：用户需要了解哪些技能正在运行以及它们在做什么的透明度，而 Claude 需要详细的、可能非常冗长的指令来正确执行技能。如果用户在聊天记录中看到完整的技能提示词，UI 会被成千上万字的内部 AI 指令弄得杂乱无章。如果技能激活完全被隐藏，用户就会失去对系统代表他们做什么的可见性。解决方案要求将这两个通信通道分成具有不同可见性规则的独立消息。

技能系统在每条消息上使用 `isMeta` 标志来控制它是否出现在用户界面中。当 `isMeta: false`（或标志被省略默认为 false）时，消息会在用户看到的对话记录中渲染。当 `isMeta: true` 时，消息作为 Claude 对话上下文的一部分发送到 Anthropic API，但永远不会出现在 UI 中。这个简单的布尔标志实现了复杂的双通道通信：一条流面向人类用户，另一条面向 AI 模型。给元工具用的元提示词（Meta-prompting for meta-tools）！

当技能执行时，系统向对话历史注入两条独立的用户消息。第一条携带 `isMeta: false` 的技能元数据，作为状态指示器对用户可见。第二条携带 `isMeta: true` 的完整技能提示词，将其从 UI 中隐藏但提供给 Claude。这种分离解决了透明度与清晰度之间的权衡，既向用户展示正在发生的事情，又不用实现细节淹没他们。

元数据消息使用简洁的 XML 结构，前端可以解析并适当显示：

    let metadata = [
      `<command-message>${statusMessage}</command-message>`,
      `<command-name>${skillName}</command-name>`,
      args ? `<command-args>${args}</command-args>` : null
    ].filter(Boolean).join('\n');

    // 消息 1: 没有 isMeta 标志 → 默认为 false → 可见
    messages.push({
      content: metadata,
      autocheckpoint: checkpointFlag
    });

例如，当 PDF 技能激活时，用户在其记录中看到一个干净的加载指示器：

    <command-message>The "pdf" skill is loading</command-message>
    <command-name>pdf</command-name>
    <command-args>report.pdf</command-args>

这条消息故意保持极简------通常 50 到 200 个字符。XML 标签使前端能够对其进行特殊格式化，验证是否存在正确的 `<command-message>` 标签，并维护会话期间执行了哪些技能的审计跟踪。因为省略 `isMeta` 标志默认为 false，此元数据会自动出现在 UI 中。

技能提示词消息采取相反的方法。它加载来自 `SKILL.md` 的完整内容，可能增加额外的上下文，并显式设置 `isMeta: true` 以对用户隐藏：

    let skillPrompt = await skill.getPromptForCommand(args, context);

    // 如果需要，增加前置/后置内容
    let fullPrompt = prependContent.length > 0 || appendContent.length > 0
      ? [...prependContent, ...appendContent, ...skillPrompt]
      : skillPrompt;

    // 消息 2: 显式 isMeta: true → 隐藏 (HIDDEN FROM UI, SENT TO API)
    messages.push({
      content: fullPrompt,
      isMeta: true  // 从 UI 隐藏，发送给 API
    });

一个典型的技能提示词包含 500 到 5,000 个词，提供全面的指导以改变 Claude 的行为。PDF 技能提示词可能包含：

    You are a PDF processing specialist. (你是一个 PDF 处理专家。)

    Your task is to extract text from PDF documents using the pdftotext tool.

    \## Process

    1. Validate the PDF file exists
    2. Run pdftotext command to extract text
    3. Read the output file
    4. Present the extracted text to the user

    \## Tools Available

    You have access to:
    - Bash(pdftotext:*) - For running pdftotext command
    - Read - For reading extracted text
    - Write - For saving results if needed

    \## Output Format

    Present the extracted text clearly formatted.

    Base directory: /path/to/skill
    User arguments: report.pdf

此提示词建立了任务上下文，概述了工作流，指定了可用工具，定义了输出格式，并提供了特定于环境的路径。带有标题、列表和代码块的 markdown 结构有助于 Claude 解析和遵循指令。有了 `isMeta: true`，这整个提示词会被发送到 API，但永远不会弄乱用户的记录。

除了核心元数据和技能提示词外，技能还可以注入额外的条件消息，用于附件和权限：

    let allMessages = [
      createMessage({ content: metadata, autocheckpoint: flag }),  // 1. 元数据
      createMessage({ content: skillPrompt, isMeta: true }),       // 2. 技能提示词
      ...attachmentMessages,                                       // 3. 附件 (条件性)
      ...(allowedTools.length || skill.model ? [
        createPermissionsMessage({                                 // 4. 权限 (条件性)
          type: "command_permissions",
          allowedTools: allowedTools,
          model: skill.useSmallFastModel ? getFastModel() : skill.model
        })
      ] : [])
    ];

附件消息可以携带诊断信息、文件引用或补充技能提示词的额外上下文。权限消息仅在技能于 Frontmatter 中指定了 `allowed-tools` 或请求模型覆盖时出现，提供修改运行时执行环境的元数据。这种模块化组合允许每条消息都有特定用途，并根据技能配置包含或排除，扩展了基本的双消息模式以处理更复杂的场景，同时通过 `isMeta` 标志保持相同的可见性控制。

\#\## 为什么是两条消息而不是一条？

单条消息的设计会迫使我们做出不可能的选择。设置 `isMeta: false` 会使整条消息可见，将数千字的 AI 指令倾倒进用户的聊天记录。用户会看到类似这样的东西：

    ┌─────────────────────────────────────────────┐
    │ The "pdf" skill is loading                  │
    │                                             │
    │ You are a PDF processing specialist.        │
    │                                             │
    │ Your task is to extract text from PDF       │
    │ documents using the pdftotext tool.         │
    │                                             │
    │ \## Process                                  │
    │                                             │
    │ 1. Validate the PDF file exists             │
    │ 2. Run pdftotext command to extract text    │
    │ 3. Read the output file                     │
    │ ... [500 more lines] ...                    │
    └─────────────────────────────────────────────┘

UI 变得不可用，充满了给 Claude 看的内部实现细节，而不是给人看的。或者，设置 `isMeta: true` 会隐藏一切，不提供关于哪个技能被激活或它接收了什么参数的透明度。用户将完全无法看到系统代表他们在做什么。

双消息分离通过给每条消息不同的 `isMeta` 值解决了这个问题。消息 1 (`isMeta: false`) 提供面向用户的透明度。消息 2 (`isMeta: true`) 为 Claude 提供详细指令。这种精细控制实现了透明度而没有信息过载。

这些消息也服务于根本不同的受众和目的：

|---------|-------------|---------------|
| 维度      | 元数据消息       | 技能提示词消息       |
| **受众**  | 人类用户        | Claude (AI)   |
| **目的**  | 状态/透明度      | 指令/指导         |
| **长度**  | \~50-200 字符 | \~500-5,000 词 |
| **格式**  | 结构化 XML     | 自然语言 Markdown |
| **可见性** | 应该可见        | 应该隐藏          |
| **内容**  | "正在发生什么？"   | "如何做？"        |

代码库甚至通过不同的路径处理这些消息。元数据消息被解析以获取 `<command-message>` 标签，经过验证并格式化以用于 UI 显示。技能提示词消息直接发送到 API 而不进行解析或验证------它是仅供 Claude 推理过程使用的原始指令内容。将它们合并会迫使一条消息通过两个不同的处理管道服务于两个不同的受众，从而违反单一职责原则。

\## 案例研究：执行生命周期

涵盖了 Agent Skills 内部架构后，让我们通过检查使用假设的 `pdf` 技能的完整执行流程，来复盘当用户说"Extract text from report.pdf"（从 report.pdf 中提取文本）时会发生什么。

当 Claude Code 启动时，它扫描技能：

    async function getAllCommands() {
      // 并行从所有来源加载
      let [userCommands, skillsAndPlugins, pluginCommands, builtins] =
        await Promise.all([
          loadUserCommands(),       // ~/.claude/commands/
          loadSkills(),             // .claude/skills/ + 插件
          loadPluginCommands(),     // 插件定义的命令
          getBuiltinCommands()      // 硬编码命令
        ]);

      return [...userCommands, ...skillsAndPlugins, ...pluginCommands, ...builtins]
        .filter(cmd => cmd.isEnabled());
    }

    // 特定的技能加载
    async function loadPluginSkills(plugin) {
      // 检查插件是否有技能
      if (!plugin.skillsPath) return [];

      // 支持两种模式：
      // 1. skillsPath 中的根 SKILL.md
      // 2. 带有 SKILL.md 的子目录

      const skillFiles = findSkillMdFiles(plugin.skillsPath);
      const skills = [];

      for (const file of skillFiles) {
        const content = readFile(file);
        const { frontmatter, markdown } = parseFrontmatter(content);

        skills.push({
          type: "prompt",
          name: `${plugin.name}:${getSkillName(file)}`,
          description: `${frontmatter.description} (plugin:${plugin.name})`,
          whenToUse: frontmatter.when_to_use,  // ← 注意：下划线！
          allowedTools: parseTools(frontmatter['allowed-tools']),
          model: frontmatter.model === "inherit" ? undefined : frontmatter.model,
          isSkill: true,
          promptContent: markdown,
          // ... 其他字段
        });
      }

      return skills;
    }

对于 pdf 技能，这产生：

    {
      type: "prompt",
      name: "pdf",
      description: "Extract text from PDF documents (plugin:document-tools)",
      whenToUse: "When user wants to extract or process text from PDF files",
      allowedTools: ["Bash(pdftotext:*)", "Read", "Write"],
      model: undefined,  // 使用会话模型
      isSkill: true,
      disableModelInvocation: false,
      promptContent: "You are a PDF processing specialist...",
      // ... 其他字段
    }

\#\## 第二阶段：第一轮 - 用户请求与技能选择

用户发送请求："Extract text from report.pdf"。Claude 收到此消息以及工具数组中的 `Skill` 工具。在 Claude 决定调用 pdf 技能之前，系统必须在 Skill 工具的描述中展示可用技能。

\#\#\## 技能过滤与展示

并非所有加载的技能都会出现在 Skill 工具中。技能必须在 Frontmatter 中有 `description` 或 `when_to_use`，否则会被过滤掉。过滤标准：

    async function getSkillsForSkillTool() {
      const allCommands = await getAllCommands();

      return allCommands.filter(cmd =>
        cmd.type === "prompt" &&
        cmd.isSkill === true &&
        !cmd.disableModelInvocation &&
        (cmd.source !== "builtin" || cmd.isModeCommand === true) &&
        (cmd.hasUserSpecifiedDescription || cmd.whenToUse)  // ← 必须有一个！
      );
    }

\#\#\## 技能格式化

每个技能都被格式化到 `<available_skills>` 部分。例如，我们需要格式化 `pdf` 技能： `"pdf": Extract text from PDF documents - When user wants to extract or process text from PDF files`

    function formatSkill(skill) {
      let name = skill.name;
      let description = skill.whenToUse
        ? `${skill.description} - ${skill.whenToUse}`
        : skill.description;

      return `"${name}": ${description}`;
    }

\#\#\## Claude 的决策过程

现在，当用户提示："Extract text from report.pdf"。Claude 收到带有 `Skill` 工具的 API 请求，阅读 `<available_skills>`，并推理（假设，因为我们看不到推理痕迹）：

    内部推理:
    - 用户想要 "extract text from report.pdf"
    - 这是一个 PDF 处理任务
    - 查看可用技能...
    - "pdf": Extract text from PDF documents - When user wants to extract or process text from PDF files
    - 这个匹配！用户想要从 PDF 提取文本
    - 决定: 调用 Skill 工具，参数 command="pdf"

注意这里没有算法匹配。没有词法匹配。没有语义匹配。没有搜索。这是纯粹的 LLM 根据技能描述对其决策进行的推理。完成后，Claude 返回工具使用：

    {
      "type": "tool_use",
      "id": "toolu_123abc",
      "name": "Skill",
      "input": {
        "command": "pdf"
      }
    }

\#\## 第三阶段：Skill 工具执行

Skill 工具现在执行。这对应于序列图中黄色的"SKILL TOOL EXECUTION"（SKILL 工具执行）框，它执行验证、权限检查、文件加载和上下文修改，然后产出结果。

\#\#\## 第一步：验证

    async validateInput({ command }, context) {
      let skillName = command.trim().replace(/^\//, "");

      // 错误 1: 空
      if (!skillName) return { result: false, errorCode: 1 };

      // 错误 2: 未知技能
      const allSkills = await getAllCommands();
      if (!skillExists(skillName, allSkills)) {
        return { result: false, errorCode: 2 };
      }

      // 错误 3: 无法加载
      const skill = getSkill(skillName, allSkills);
      if (!skill) return { result: false, errorCode: 3 };

      // 错误 4: 禁用模型调用
      if (skill.disableModelInvocation) {
        return { result: false, errorCode: 4 };
      }

      // 错误 5: 非基于提示词
      if (skill.type !== "prompt") {
        return { result: false, errorCode: 5 };
      }

      return { result: true };
    }

pdf 技能通过所有验证检查 ✓

    async checkPermissions({ command }, context) {
      const skillName = command.trim().replace(/^\//, "");
      const permContext = (await context.getAppState()).toolPermissionContext;

      // 检查拒绝规则
      for (const [pattern, rule] of getDenyRules(permContext)) {
        if (matches(skillName, pattern)) {
          return { behavior: "deny", message: "Blocked by permission rules" };
        }
      }

      // 检查允许规则
      for (const [pattern, rule] of getAllowRules(permContext)) {
        if (matches(skillName, pattern)) {
          return { behavior: "allow" };
        }
      }

      // 默认：询问用户
      return { behavior: "ask", message: `Execute skill: ${skillName}` };
    }

假设没有规则，用户被提示："Execute skill: pdf?" 用户批准 ✓

\#\#\## 第三步：加载技能文件并生成执行上下文修改

验证和权限获得批准后，Skill 工具加载技能文件并准备执行上下文修改：

    async *call({ command }, context) {
      const skillName = command.trim().replace(/^\//, "");
      const allSkills = await getAllCommands();
      const skill = getSkill(skillName, allSkills);

      // 加载技能提示词
      const promptContent = await skill.getPromptForCommand("", context);

      // 生成元数据标签
      const metadata = [
        `<command-message>The "${skill.userFacingName()}" skill is loading</command-message>`,
        `<command-name>${skill.userFacingName()}</command-name>`
      ].join('\n');

      // 创建消息
      const messages = [
        { type: "user", content: metadata },  // 用户可见
        { type: "user", content: promptContent, isMeta: true },  // 用户隐藏，Claude 可见
        // ... 附件，权限
      ];

      // 提取配置
      const allowedTools = skill.allowedTools || [];
      const modelOverride = skill.model;

      // 产出带有执行上下文修改器的结果
      yield {
        type: "result",
        data: { success: true, commandName: skillName },
        newMessages: messages,

        // 🔑 执行上下文修改函数
        contextModifier(context) {
          let modified = context;

          // 注入允许的工具
          if (allowedTools.length > 0) {
            modified = {
              ...modified,
              async getAppState() {
                const state = await context.getAppState();
                return {
                  ...state,
                  toolPermissionContext: {
                    ...state.toolPermissionContext,
                    alwaysAllowRules: {
                      ...state.toolPermissionContext.alwaysAllowRules,
                      command: [
                        ...state.toolPermissionContext.alwaysAllowRules.command || [],
                        ...allowedTools  // ← 预批准这些工具
                      ]
                    }
                  }
                };
              }
            };
          }

          // 覆盖模型
          if (modelOverride) {
            modified = {
              ...modified,
              options: {
                ...modified.options,
                mainLoopModel: modelOverride
              }
            };
          }

          return modified;
        }
      };
    }

Skill 工具产出其结果，包含 `newMessages`（元数据 + 技能提示词 + 用于对话上下文注入的权限）和 `contextModifier`（工具权限 + 用于执行上下文修改的模型覆盖）。这完成了序列图中的黄色"SKILL TOOL EXECUTION"框。

\#\## 第四阶段：发送到 API（第一轮完成）

系统构建完整的消息数组以发送到 Anthropic API。这包括来自对话的所有消息加上新注入的技能消息：

    // 发送到 API 的第一轮完整消息数组
    {
      model: "claude-sonnet-4-5-20250929",
      messages: [
        {
          role: "user",
          content: "Extract text from report.pdf"
        },
        {
          role: "assistant",
          content: [
            {
              type: "tool_use",
              id: "toolu_123abc",
              name: "Skill",
              input: { command: "pdf" }
            }
          ]
        },
        {
          role: "user",
          content: "<command-message>The \"pdf\" skill is loading</command-message>\n<command-name>pdf</command-name>"
          // isMeta: false (默认) - 用户在 UI 中可见
        },
        {
          role: "user",
          content: "You are a PDF processing specialist...\n\n\## Process\n1. Validate PDF exists\n2. Run pdftotext...",
          isMeta: true  // 从 UI 隐藏，发送给 API
        },
        {
          role: "user",
          content: {
            type: "command_permissions",
            allowedTools: ["Bash(pdftotext:*)", "Read", "Write"],
            model: undefined
          }
        }
      ]
    }

上图显示了我们到目前为止所做的工作。应用了执行上下文修改器，预批准 `Bash(pdftotext:*)`、`Read` 和 `Write` 以供后续工具调用。请求被发送到 Anthropic API。这结束了技能执行。如果这是一个普通工具，我们就完成了。然而，技能是不同的。Agent Skill 仅仅注入了对话上下文和执行上下文。这意味着我们仍然需要调用 Claude Agent，带上所有这些注入的上下文来完成用户的请求！

\#\## 第五阶段：Bash 工具执行（带技能上下文的工具使用！）

Claude 收到带有注入对话上下文的 API 响应。技能提示词已经改变了 Claude 的行为，为其提供：

* 专门的 PDF 处理指令（对话上下文）

* 对 `Bash(pdftotext:*)`、`Read` 和 `Write` 工具的预批准访问权限（执行上下文）

* 一个清晰的遵循工作流（对话上下文）

Claude 处理上下文并遵循 pdf 技能的工作流：

    我将从 report.pdf 中提取文本。让我处理这个文件。

    [遵循 pdf 技能的指令]
    1. 验证 report.pdf 是否存在
    2. 运行 pdftotext 命令提取文本
    3. 读取输出文件
    4. 向你展示提取的文本

Claude 使用 Bash 工具（预批准，无需用户提示）：

    {
      "type": "tool_use",
      "id": "toolu_456def",
      "name": "Bash",
      "input": {
        "command": "pdftotext report.pdf output.txt",
        "description": "Extract text from PDF using pdftotext"
      }
    }

Bash 工具成功执行，返回结果。Claude 然后使用 Read 工具读取输出文件并将提取的文本展示给用户。技能通过将指令注入到对话上下文并修改执行上下文以获取工具权限，成功地引导 Claude 完成了专门的 PDF 提取工作流。

*** ** * ** ***

\## 结论：思维模型回顾

Claude Code 中的技能是 **基于提示词的对话和执行上下文修改器**，通过元工具架构工作：

**关键要点：**

1. 技能是 `SKILL.md` 文件中的 **提示词模板**，不是可执行代码。

2. **Skill 工具** （大写 S）是 `tools` 数组中管理单个技能的元工具，不在系统提示词中。

3. 技能通过注入指令提示词（通过 `isMeta: true` 消息）**修改对话上下文**。

4. 技能通过更改工具权限和模型选择 **修改执行上下文**。

5. 选择是通过 **LLM 推理** 进行的，不是算法匹配。

6. 工具权限通过执行上下文修改 **限定在技能执行范围内**。

7. 技能每次调用注入两条用户消息------一条用于用户可见的元数据，一条用于发送给 API 的隐藏指令。

**优雅的设计：** 通过将专业知识视为 *修改对话上下文的提示词* 和 *修改执行上下文的权限* ，而不是 *执行的代码*，Claude Code 实现了传统函数调用难以企及的灵活性、安全性和可组合性。

*** ** * ** ***

\## 参考文献

* [Introducing Agent Skills](https://www.anthropic.com/news/skills)

* [Equipping Agents for the Real World with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

* [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/overview)

* [Anthropic API Reference](https://docs.anthropic.com/en/api/messages)

* [Official Documented Frontmatter Fields](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview\#skill-structure)

* [Internal Comms Skill](https://github.com/anthropics/skills/tree/main/internal-comms)

* [Skill Creator Skill](https://github.com/anthropics/skills/tree/main/skill-creator)

* [ChatGPT 5 System Prompt (leaked, not official)](https://github.com/elder-plinius/CL4R1T4S/blob/main/OPENAI/ChatGPT5-08-07-2025.mkd)


    @article{
        leehanchung_bullshit_jobs,
        author = {Lee, Hanchung},
        title = {Claude Agent Skills: A First Principles Deep Dive},
        year = {2025},
        month = {10},
        day = {26},
        howpublished = {\url{[https://leehanchung.github.io](https://leehanchung.github.io)}},
        url = {[https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)}
    }

*** ** * ** ***

来源：<https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/>

[Read in Cubox](https://cubox.pro/web/card/7395002192941286835)

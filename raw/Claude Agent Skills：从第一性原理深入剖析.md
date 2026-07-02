---
id: "7385928570654164664"
cubox_url: https://cubox.pro/web/card/7385928570654164664
url: https://mp.weixin.qq.com/s/W3gmYDqqMNIKNTIa3aGeCA
tags:
  - AI-Agent/skill
---
# Claude Agent Skills：从第一性原理深入剖析



[Read in Cubox](https://cubox.pro/web/card/7385928570654164664)  
[Read Original](https://mp.weixin.qq.com/s/W3gmYDqqMNIKNTIa3aGeCA)  

---


---

## 📖 正文全文

# Claude Agent Skills：从第一性原理深入剖析

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/W3gmYDqqMNIKNTIa3aGeCA)PaperAgent


Claude 的 Agent Skills 系统是一套基于提示的元工具架构，通过"注入专门指令"来扩展大模型能力。它既不是传统意义上的函数调用，也不执行实际代码，而是借助"提示展开"与"上下文改写"，让 Claude 在后续对话中换一种"大脑配置"去处理任务，而无需写一行可执行程序。

本文从第一性原理拆骨式解构 Claude 的 Agent Skills 系统，完整记录"Skill"这一元工具如何把领域专属提示注入对话上下文的机制。我们将以 skill-creator（技能生成器）与 internal-comms（内部通讯）两条技能为案例，走完文件解析、API 请求结构、Claude 决策流程等全生命周期。

## 一、Claude Agent Skills 全景速览

Claude 用 Skills 来"把特定任务做得更专业"。一个 Skill 就是一个文件夹，内含指令、脚本与资源；Claude 在需要时动态加载。整个系统采用"声明式、纯提示"的发现与调用逻辑：

*
  没有算法级技能路由，也没有代码层的意图识别。
*
  是否调用、调用哪一个，全由 Claude 自己读描述后推理决定。
*
  Skills 不是可执行文件------不跑 Python、不跑 JavaScript，更不启 HTTP 服务。
*
  它们也不硬编码在系统提示里，而是躺在 API 请求结构的独立字段。

> 一句话：Skills 就是"领域专属提示模板"。被触发时，它把一段详细指令注入对话上下文，同时可能切换工具权限甚至模型版本。

对用户请求，Claude 每次收到三件套：

1.
   用户消息
2.
   普通工具列表（Read、Write、Bash...）
3.
   Skill 工具（元工具）

Skill 工具的描述字段里拼好了所有可用技能的"目录"，Claude 用原生语义理解把用户意图与技能描述匹配。例如用户说"帮我写一封公司内部公告"，Claude 看到 internal-comms 的描述"当用户想按公司惯用格式写内部通讯时"，即判断匹配，于是调用 Skill 工具并传入参数 "internal-comms"。

### 1、术语对照


|          术语          |                           含义                            |
|----------------------|---------------------------------------------------------|
| **Skill 工具** （首字母大写） | 出现在工具数组里的唯一元工具，负责加载所有技能。                                |
| **skills** （小写）      | 单个技能，如 pdf、skill-creator、internal-comms，本质上是一段待注入的提示模板。 |


可视化调用流程:
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PXTEar8rBSBA7W0v0VlIgJDicBq2CRAg4ic0KkhhnyrHyw1EnQicX9fQ8vQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0&valid=false)

技能选择机制在代码层无算法路由或意图分类。Claude Code 不用嵌入、分类器、正则或关键词匹配，而是把所有技能格式化成文本描述嵌入 Skill 工具提示，让 Claude 的语言模型自行决定。这是纯 LLM 推理，决策发生在 transformer 前向传播中，而非应用代码。

调用技能时，系统：加载 SKILL.md 文件 → 展开为详细指令 → 作为新用户消息注入对话上下文 → 修改执行上下文（允许工具、模型）→ 继续对话。与传统工具"执行并返回结果"不同，Skills "让 Claude 准备好解决问题"。

下表区分 Tools 与 Skills 及其能力：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PX5z9tuNuhpaYSYicptiaibWG0jKtMX3S0NSTmXt1SWM04QvXtxOVfVwxjw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D1&valid=false)

### 2、构建Agent Skills

现在让我们深入了解如何通过检查来自Anthropic的"skill-creator"来构建Skills。Skill从Anthropic的skill库作为案例研究。作为提醒，agent skills是动态发现的文件夹，包含指令、脚本和资源，这些资源允许agents发现和读取动态执行能力，以包括可组合的资源供Claude使用，将通用目的agents转换为适合您需求的专门agents。

**关键见解：**
> Skill = 提示模板 + 对话上下文注入 + 执行内容修改 + 可选数据文件和Python脚本

每个Skill都在一个名为SKILL.md（区分大小写）的markdown文件中定义，其中包含技能的元数据。SKILL.md文件可以是Python脚本、shell脚本、字体定义、模板等。使用skill-creator作为示例，它包含SKILL.md、LICENSE.txt for the license，以及tech/scripts文件夹skill-creator：不包含任何/references或/assets。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PX2fo8kRe6fbotRKDJ4arPhrsSI5hq1tWkkwq1GlqaFT64jSxKZibhIIw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D2&valid=false)

每个技能都定义在一个名为 SKILL.md（不区分大小写）的 Markdown 文件中，并附带一些可选的捆绑文件，这些文件存储在 /scripts、/references 和 /assets 目录下。这些捆绑文件可以是 Python 脚本、Shell 脚本、字体定义、模板等。以 skill-creator 为例，它包含 SKILL.md、用于说明许可证的 LICENSE.txt 文件，以及 /scripts 文件夹下的几个 Python 脚本。skill-creator 没有 /references 或 /assets 目录。

Skills 可以从多个来源被发现并加载。Claude Code 会扫描用户设置目录（\~/.config/claude/skills/）、项目设置目录（.claude/skills/）、插件提供的技能以及内置技能，以构建可用技能列表。对于 Claude Desktop，我们可以按以下方式上传自定义技能。![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PXrjbJ6a8wBBfRrUa7rZdrOp9GuRDnsibG6KTicIEPnWH0YUnOoKWVzicLg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D3&valid=false)

### 3、编写SKILL.md

SKILL.md是skill提示的核心。它是一个遵循两部分组成结构的markdown文件：frontmatter和内容。frontmatter配置skill如何运行（权限、模型、元数据），而markdown内容告诉Claude使用YAML编写frontmatter的头部。![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PXIeEoeibibdBeiaDxA7v9jptkOdA7pA3d3uckROeZBShZnA0tUPmLAGnRg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D4&valid=false)

**3.1、Frontmatter**

Frontmatter包含控制Claude如何发现和使用skill的元数据。例如，以下是skill-creator的frontmatter：

    name: skill-creator
    description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
    license: Complete terms in LICENSE.txt

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PXXnibpxV9dCSWTDPicrY5ibR7ummibicN6IdoRqF0GPeAUPP7yVEerUaG7Zg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D5&valid=false)

**3.2、SKILL.md提示内容**

在frontmatter之后是markdown内容：Claude在调用skill时接收的实际提示。这是您定义skill行为、指令和工作流程的地方。技能的markdown内容应以SKILL.md中定义的指令提供核心指令，并减少外部文件或详细内容的引用。

推荐的内容结构：
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PXuIicfDYGvrZ5WSYibK3G4CGzBkYj4ViaRYHxXym2sKPElFyhGm32cQgBg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D6&valid=false)

**3.3、常见技能模式**

正如所有工程实践一样，理解常见模式有助于设计出高效的技能。以下是工具集成与工作流设计中最实用的几种模式。

**模式1：脚本自动化**

**用例** ：完成需要多个命令或确定性逻辑的复杂任务。此模式将计算任务卸载到Python或Bash脚本中。技能提示告诉Claude执行脚本并将输出作为结果。

**SKILL.md 示例** :

    Run scripts/analyzer.py on the target directory:

    `python {baseDir}/scripts/analyzer.py --path "$USER_PATH" --output report.json`

    Parse the generated `report.json` and present findings.

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PXBCSbBxjx1TRa6P26gFG5kuSIdGA4U0ou9cufvHWmEVroCKCodYaIDg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D7&valid=false)

    allowed-tools: "Bash(python {baseDir}/scripts/*:*), Read, Write"

**模式2：读取-处理-写入**

**用例** ：文件转换和数据处理。

最简单的模式------读取输入，按照以下指令转换，写入输出。适用于格式转换、数据清理或报告生成。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PXqsm8wRnGfor8g2y1LYMFyItKGvAFflHcVbicI3aseFPic7j6ODLsROkw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D8&valid=false)

**SKILL.md 示例** :

    ## Processing Workflow
    1. Read input file using Read tool
    2. Parse content according to format
    3. Transform data following specifications
    4. Write output using Write tool
    5. Report completion with summary

**所需工具：**

    allowed-tools: "Read, Write"

**模式3：搜索-分析-报告**

**用例** ：代码库分析和模式检测。

使用Grep搜索代码库中的模式，读取匹配文件的上下文，分析发现，并生成结构化报告。或者，搜索企业数据存储以获取数据，分析检索的数据以获取信息，并生成结构化报告。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PXicxPT9rxYnNQYNmKF59C03OflacxgZkQs0gaZl0iaENoJnf4qMOZKKqA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D9&valid=false)

**SKILL.md 示例** :

    ## Analysis Process
    1. Use Grep to find relevant code patterns
    2. Read each matched file
    3. Analyze for vulnerabilities
    4. Generate structured report

**所需工具：**

    allowed-tools: "Grep, Read"

**模式4：命令链执行**

**用例** ：带依赖的多步骤操作。

执行一系列命令，其中每一步都依赖于前一步的成功完成。常见于类似 CI/CD 的工作流。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FAE74ia62XricGn7BqglH3w6GtxkKqrd1PXFF0eInzbJ1Qibdh1ZcpJibuLN6d7RCt4WTKK4vlz5MAB41k1SluwZl3w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D10&valid=false)

**SKILL.md 示例** :

    Execute analysis pipeline:
    npm install && npm run lint && npm test
    Report results from each stage.

**所需工具：**

    allowed-tools: "Bash(npx install;*), Bash(npx run;*), Read"

**下文待续\~**   

推荐阅读


[动手设计AI Agents：（编排、记忆、插件、workflow、协作）](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247492838&idx=2&sn=1e25832e7300ef312721325d0def30b4&scene=21#wechat_redirect)

[一篇92页大模型Vibe Coding技术全面综述](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247498057&idx=1&sn=04ef65879b687f4a196581d93087d014&scene=21#wechat_redirect)

[快手开源多模态Keye-VL-1.5-8B，本地视觉Agent有救了](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247497114&idx=1&sn=8bf1d9630e5cfbbdbda874121f189daa&scene=21#wechat_redirect)  

[一篇最新自演化AI Agents全新范式系统性综述](https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247497640&idx=1&sn=beb015fa84617bd1930222684ec9def8&scene=21#wechat_redirect)


*** ** * ** ***

每天一篇大模型Paper来锻炼我们的思维\~已经读到这了，不妨点个👍、❤️、↗️三连，加个星标⭐，不迷路哦\~


[Read in Cubox](https://cubox.pro/web/card/7385928570654164664)

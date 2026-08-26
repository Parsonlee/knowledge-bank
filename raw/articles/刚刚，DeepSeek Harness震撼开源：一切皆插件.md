---
title: 刚刚，DeepSeek Harness震撼开源：一切皆插件
source: https://mp.weixin.qq.com/s/mcVfdDVUVlEYJj61sJWKZA
author:
- '[[机器之心]]'
published: 2026-08-13
created: 2026-08-14
description: deepseek harness 简述
tags:
- AI-Agent/coding
---
关注DSH的 机器之心 *2026年8月13日 20:58*

编辑｜Panda

今天凌晨， [DeepSeek V4 Pro 正式版发布](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651050016&idx=1&sn=d89cdb2934ba065e9c5995f8710b228f&scene=21#wechat_redirect) ，引发热潮。现在，半天过去，DeepSeek Harness （开发者预览版）也来了！

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqFC7xV4j4m52AiclCenIyuicq2jzfn1KuPKmibX2243ZJBm3qmzbj458fpYnyBWF0fvNvesrc7cPeWBlsr2q5apBOzlkNib0RPDSys/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

当然，这并不意外，毕竟该项目之前已经铺垫了很久了，比如 DeepSeek Harness 团队的崔添翼就一直在社交网络上发预热贴以及为该团队招募人才。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqGOD78uNmiawTAX2otBWyfF5icrlZMpUS51xTGWsiaP9dqaumZJlQyUZFAhicemn5JHVzamlDsNic4QrUYMjuewuHXiaOicgzOVWrZqG8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

我们也在 8 月初获得了 DeepSeek Harness 的内测资格，提前享受到了这个注定又会给 AI 社区带来新变革的智能体框架。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqFq0FicCkciamDMAgK0ctaDMTCu6I21Gzia56zRlMxGzVrqXp2ibMy8dql4MstbW15y9ySMakyKbVqLOYhyuVcvntdLXXxSyOCWiaNQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

开源地址：https://github.com/deepseek-ai/deepseek-harness

比如这里，我们让配置了官方 DeepSeek-V4-Flash 的 DeepSeek Harness 我们构建了一个第一人称丧尸射击游戏。我们没有中途施加任何干预，就在 30 多分钟得到了一个虽不完美但已经相当可玩的成品：

考虑到近日 Andrej Karpathy 用 AI 生成 3D 世界的思路非常火爆，我们也让 DeepSeek Harness（V4-Flash）挑战了「华强买瓜」基准：基于文本描述将「华强买瓜」经典片段复现成 3D 动画（同样是 one-shot 提示的结果）：

整体来看，虽然离完美距离还很远，但这个动画的故事剧情大体还原，人物关系也大体能看出。相较之下，我们使用同样提示词，用配置了 GPT-5.6 sol-xhigh 的 Codex 制作出来的动画就差多了：

，时长02:20

<video src="https://mpvideo.qpic.cn/0b2e3qaegaaafiagtnl5drvfbxgdipoaaqya.f10002.mp4?dis_k=4a80483f3b996ca0cf88260ce72911d7&amp;dis_t=1786674370&amp;play_scene=10120&amp;auth_info=as2g3Po/W1pK59nq6nEmFTROPWQaZBdQeDJYUBh1bWVbKk1IaRRAFz0MFjw/Gys1IEQ=&amp;auth_key=7ee9648c1a50875e0ff8ff9f1c8e8d6b&amp;vid=wxv_4647215410961235984&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

要知道，DeepSeek-V4-Flash 的参数规模远低于 GPT-5.6 sol。可以想见，DeepSeek Harness 应是立了大功。

今天随着 DeepSeek V4 Pro 正式版的发布，我们也将该模型接入了 DeepSeek Harness 再跑了一遍：

，时长01:59

<video src="https://mpvideo.qpic.cn/0bc3xmbauaacoqacbtd73nvffo6dbk5qecqa.f10002.mp4?dis_k=029f212550c549a8686f434ea0085ebf&amp;dis_t=1786674370&amp;play_scene=10120&amp;auth_info=a6bDqMRuXQgQ69uw6nlzSzoQO2EeYhNXejNcBB4kaTZafEtBaEdGRWcAFGY/E35rLho=&amp;auth_key=8bfee7604f117f2c141a140836205c04&amp;vid=wxv_4647214759216644096&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

效果确实好一些了。

接下来，看看项目结构，非常惊人：仓库已经包含超过 230 个 workspace 成员，代码分布在 packages/、apps/、examples/、python/、native/、vendor/、website/ 等区域。文件系统、终端、子进程、PTY、语言服务器、网页访问、技能、子智能体、工作流、计划模式、会话持久化、设置、凭据、遥测，几乎每一项能力都有自己的包。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqFQicgPUIKPmoM5dl9hyXSsLQkXnSNNN6Gus7xLxN7BMq6e2u24sN9nRX8RlCK6vQRqvBUObflhx9uOh7rWicHGdJN80HbLnJnEU/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

如果把普通的 Agent 项目比作一台已经装好的电脑，那么 DeepSeek Harness 更像一块尺寸惊人的洞洞板：模型、工具、界面、存储、安全策略和上下文管理都可以插上去，也都可以拔下来。

它提供了一套默认组装方案，但看得出来，DeepSeek 真正想创造的并非某个固定形态的「DeepSeek 编程助手」，而是一种组装智能体的方式。

DeepSeek Harness 是什么？

先厘清一个容易混淆的问题：DeepSeek Harness 并非新的 DeepSeek 模型，也非一个单纯的 API 客户端。它是一套用来构建、运行和扩展智能体的 SDK 与应用框架，默认可以连接 DeepSeek 模型（也可方便地自定义连接其它模型），让模型读取项目、修改文件、运行命令、管理任务、分配子任务，并通过 Web UI、全屏终端、Headless 命令或自动化协议与用户交互。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqHapexn3yYtRyiaTS2bLibDjG09iaKbohQV7ZF6KDT3WlKuWSyIeKYELlsy5dnuzrbDBMFjqYMEB3pEJ2ewQU9NFy1VVpCUavt2a0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

DeepSeek Harness 网页端提供了直接配置其它模型服务的便捷入口，无需用户手动编辑配置文件

当今的 AI 社区对 Harness 这个词已经不陌生了。其原本的含义是马具、线束、约束装置等，向上抽象一下，其作用是把力量连接到可以工作的机构上，同时又不让这股力量脱缰。具体到 AI 上，Harness 负责的是把模型接到文件系统、Shell、代码编辑器、网页和其他 Agent 上，同时记录它做了什么、限制它能做什么，并在出错时决定是重试、取消、压缩上下文，还是把问题交还给用户。

==这或许也能解释为什么这个项目的代码量和包数量会如此庞大，毕竟这其中涉及的任务和工具选择非常多，包括工具调用是否可并行，取消命令能否真正停止子进程，工具结果是否会污染上下文，用户在模型运行中发来的新消息应该插到哪里，会话恢复后怎样重建当时的模型输入，子智能体拥有哪些工具，文件写入是否越过工作区，界面回放时看到的内容能否和实时运行一致。==

DeepSeek Harness 试图把这些问题都变成正式的系统能力。

一切皆插件

DeepSeek Harness 最醒目的设计主张是「一切皆插件」，甚至连 Agent Loop 本身也被视为插件。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqHP6mbxmibRTU5iaUvOt7a9KOP8ib6Bhg69K4xlzLREjG9ZiaGXAyGbqiaMKQt9eXgHqWiaIsajAGHvLq3rV1qzXdtUytDqeEbYMVvTw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

项目建立在 Cordis 微内核之上，运行中的 Harness 本质上是一个 Cordis Context。不同包向 Context 注册服务、事件和能力，最终由配置文件把它们组合成一套可以运行的智能体。

packages/core/ 是整个系统的核心，其中包含 Session、System Prompt、Tools、Agent 和 Agent Loop。它们解决的是最基本的问题：会话是什么，系统提示词如何组装，工具如何注册和调用，Agent 如何创建，以及一轮对话怎样从用户输入走到模型请求、工具执行和最终回答。

核心之外是大量能力包：

- packages/llm/ 负责模型适配器和流式输出；
- packages/shell/、packages/subprocess/ 与 packages/terminal/ 负责一次性命令、进程树和持续终端；
- packages/fs/ 负责文件读写、编辑、搜索与策略限制；
- packages/lsp/ 连接语言服务器，让 Agent 不只能用文本搜索，也能获得语义级代码导航；
- packages/web/ 负责搜索与网页抓取；
- packages/skill/ 管理可复用技能；
- packages/subagent/ 和 packages/workflow/ 则把单个 Agent 扩展为可以委派和编排的多智能体系统。

再往外看，计划、目标、待办事项、后台任务、上下文压缩、会话查询、会话标题、凭据、用户设置、审批机制和遥测同样被拆成独立能力。这个结构最有意思的地方，是它体现了一种近乎执拗的边界意识：谁拥有接口，谁负责实现，谁把能力呈现给模型，尽量不要混在一起。

项目文档把典型能力拆成三层：接口、实现和消费者。

以 Bash 为例，接口定义「执行命令」是什么，本地实现负责真正创建进程，而面向模型的工具包负责把这项能力变成模型可理解的 schema 和结果。将来如果本地 Shell 要换成远程容器、云端沙箱或企业执行平台，理论上只需替换实现层，而不必重写模型工具和 Agent Loop。

这是一种典型的框架思维。它会让仓库在早期显得庞大，却也说明 DeepSeek Harness 的目标不是做一个只有官方团队能维护的成品，而是让不同部署方能换模型、换存储、换安全策略、加工具，甚至换掉智能体循环。

在这里，我们也看到了 DeepSeek 一直坚持的真・开源！

cordis.yml

一份配置组装出不同的 Agent

插件化架构最终通过 cordis.yml 落到开发者手里。配置文件列出插件名称、稳定 ID 和参数，决定当前 Agent 究竟拥有哪一组能力。

同一套代码可以被组装成完全不同的产品形态。加入 DeepSeek LLM 适配器、文件系统、Bash 和 TUI，就得到终端里的编程智能体；把交互界面换成 Web 插件，就得到浏览器应用；使用 Headless 入口，它会接受一个任务，完成模型与工具轮次，打印答案后退出；换成 ACP 或 JSON-RPC 前门，它又能成为其他程序可以驱动的自动化服务。

配置还支持覆盖层。TUI 和 Web UI 可以共享一份基础配置，再叠加各自的界面插件和参数；个人配置则位于最后一层。这样，部署方不必复制整棵配置树，只需要对指定插件做替换。不过这里也有一个需要留意的细节：配置补丁替换的是目标插件的整个 config，不是深度合并。如果只写一个新字段，原有的 API Key、基础地址或其他参数可能会一起消失。它很明确，但并不一定符合初次使用者的直觉。

项目还允许在 YAML 中通过!!js 读取环境变量和运行时表达式，例如从 DEEPSEEK\_API\_KEY 获取密钥。配置只引用凭据名称，密钥在实际调用时解析。Web UI 会把密钥写入 $DSH\_HOME/.credentials.yaml，而环境变量和.env 可作为自动化或本地开发中的回退来源；密钥不应直接写入 cordis.yml 或进入会话日志。

Agent Loop

不是一个循环，而是一套交通规则

许多早期 Agent 项目的核心代码可以简化成几行：把消息发给模型，如果模型返回工具调用，就执行工具，再把结果发回模型，直到模型输出文本。DeepSeek Harness 当然也做这件事，但它把这个过程拆成了严格的生命周期。

一次用户输入会开启一个 Turn，一个 Turn 中可以包含多个 Step；一个 Step 对应一次模型请求及其后续工具执行。请求前，系统会组装稳定的系统提示词、当前运行环境、工具 schema 和会话消息；请求后，模型的流式 chunk、完整消息、工具调用、工具结果和结束原因都会进入事件流。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqEFeg4WDEJWk5nngZGLA2I2Pawfk7nqU5JxDviafEUT4fCbudQeIF54325x3Y3P5zT9kLhDvW97CuI1qAY5uAkx5bnVkBroYEjw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

上述丧尸射击游戏执行了 3 turn，127 setp

==工具也不是「拿到函数名就调用」。它会经过前置策略、不可逆的安全守卫、实际执行、后置处理、内容整理和结果通知。允许或拒绝、超时、重试、指标统计、附加上下文，都可以从流水线的不同位置接入。工具可以声明某类参数下的调用是并发安全的，调度器便会让连续的只读任务并行；一旦碰到修改状态或无法确定安全性的调用，就把它当作屏障，等待前面的任务结束后独占执行。==

这种设计看起来有些像在一条乡间小路上安装航空管制系统，但当 Agent 开始同时搜索十个文件、运行测试、接受用户追加指令，并且还要允许随时取消时，这些规则很快就会从「过度设计」变成「事故调查报告里最想早点拥有的东西」。

它还认真处理了运行中消息的去向。用户在 Agent 工作时发送的新内容，可能是下一轮任务，也可能是对当前工作的转向指令。系统区分排队消息、注入上下文和 Steering，并通过回执确认某条转向指令是否真正进入了某次模型请求。换句话说，它不只关心「消息收到了」，还关心「模型究竟在哪一步看到了它」。

Session Log

整个系统真正的权威来源

DeepSeek Harness 另一个值得关注的设计是 Session Log。

==项目规定，凡是模型看见的内容，都必须能够从日志中重建。用户消息、运行环境上下文、模型请求信息、流式输出、工具调用和结果、压缩事件、权限切换、取消原因，都会以事件形式进入追加式会话流。界面、持久化、恢复、Fork、遥测和回放，不应该各自维护一份「差不多正确」的状态，而应从同一个事件源派生。==

==这项原则解决了 Agent 系统里一个非常棘手的问题：当一次任务出错时，我们究竟能不能知道模型当时看到了什么？==

==如果系统只保存最终聊天文本，许多关键因素会丢失。也许模型请求前刚刚注入了工作区状态，也许工具结果被裁剪过，也许系统自动切换了模型路由，也许用户在流式输出中途改变了方向。DeepSeek Harness 会在请求边界保存足以重建消息的记录，原始流式 chunk 也会保留，以便界面和回放维持一致。==

会话持久化本身仍然是插件。项目提供 JSONL 和 SQLite 等后端，查询能力可以优先访问实时会话，也可以通过 SQLite 全文检索历史记录。Resume 会沿用原会话继续工作，Fork 则从一个确定的历史边界派生新会话。对开发者而言，这能为调试、评估、审计和自动化提供了统一基础。

从一个 Agent 到一群 Agent

DeepSeek Harness 已经内置了多种子智能体和工作流能力。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqEkLRRALpXHSb8vdYtB8n2g9JCg2Kp90d0bSJpxMiaQhWInjpnIfQKTiaRSsvCRXSC5AMzibic10YLnibONNdiaoOygKGianjtiaT9jkFE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

主 Agent 可以把任务委派给子 Agent，子 Agent 可以是全新创建的实例，也可以从已有会话的完成边界 Fork，或者通过 ACP 连接外部子进程。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqH4ibiakOibGBSK6DVMSCiaGIFV6ycUQ7X5Zmh9EFsdhKznG6msBfxPMaYAaFbv4Op4LFan4VicKk6l8Px27n0xKum5ywa5sYLMMR74/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

上述丧尸射击游戏创建了 5 个并行执行的子智能体

这里的作用域设计很重要。每个 Agent 拥有自己的上下文层，可以看到特定的工具、提示词和命令。某个子 Agent 可以被限制为只做搜索和分析，另一个则被允许修改文件。注册在 Agent 作用域里的能力会随 Agent 生命周期自动清理，不必依赖全局名称约定维持隔离。

工作流则更进一步：它允许用脚本驱动多智能体编排，把多个子任务、结构化输出和继续执行连接起来。项目同时提供目标、计划、待办事项和后台任务，它们并不是四个名称相近的 UI 小组件，其实是不同生命周期的协作状态。计划模式记录当前协作阶段，目标可以跨同一会话持续存在，待办事项为模型提供轻量任务清单，后台任务则负责管理仍在运行的实际工作。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqHLwDvFn0f8OicSONXawD2g4UFhEIkqEzov5mfWiasvZ24ollyvIA7PYI211kzctrFxzxBlSUniaxfBhJbKcAJgnBCtbnnniaWvDs0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

这说明 Harness 想覆盖的不只是「一问一答式编程」。它希望支持长任务、并行调查、自动化运行和外部系统协调。至于模型能否稳定驾驭如此多的机制，是另一场测试；至少框架先把方向盘、仪表盘和刹车做了出来。

Web、TUI、Headless 与 SDK

面向普通用户，项目推荐 Web UI，默认监听 http://127.0.0.1:3080。它提供对话、会话侧栏、权限选择、计划模式、工具卡片和工作区交互。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqGhCN57yXa0kia8iciaDtB108o5kS0HX94UvbPGHRpibaXfsV1ibJy2biakGZDJqPzumBePjPlmGsrib0DolRR3KhtGE6Dwia4bHBAyFCI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

Web UI 还提供了四种 Agent 预设模式。它们并非四套彼此独立的 Agent，也不只是改变提示词风格，而是基于同一套 Harness 宿主，为当前会话装配不同的工具、提示词和运行时能力：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqHC28N1VfJtetofge3GtClO62ibzX4S2qtsSVEia8Uv2tnveicibAAcoicwfwKP958qAl7mzkxKXF7IjrqddRpmVLZABiafrTCiagRhT0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)
- 标准模式：功能最完整的通用编码 Agent，提供文件编辑、Shell、文件与网页检索、Skills、计划、目标、子 Agent 和工作流，适合绝大多数日常开发任务；
- PTC 模式：保留标准模式的全部能力，同时通过 Code Mode SDK 向模型呈现工具。模型可以编写一段 TypeScript 程序，在一次 run\_code 中组合多步操作，减少模型与工具之间反复往返的开销，更适合调用链较长的复杂任务；
- 极简模式：只提供持久 Bash 与 str\_replace\_editor 两项工具。较小的工具集合减少了选择和上下文负担，适合路径明确、希望 Agent 直接动手的编码任务；
- 创造模式：在标准模式之上加入 Cordis 运行时检查、临时插件实验和 Agent preset 创作指导。Agent 不仅可以使用现有工具，还能探索并重新组合自己的运行时，进而创建新的自定义预设。由于它能够运行模型编写的插件代码，这是一个面向高级用户的高信任模式。

这组预设或许是「一切皆插件」最直观的产品化表达：底层的模型路由、会话持久化、沙箱和审批仍由共享宿主提供，预设只决定一个 Agent Context 中具体装入哪些能力。同一个 Web UI，因此可以从双工具的极简 Agent，切换成能够编排子 Agent 的标准模式，甚至进一步变成可以改装自身的创造模式。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqGrForfoEKWUIO3GTZSCHPYgibZ4mJ5F97eqwz6m1O5GITQc3zeuqQdjn6A70VL1fiaAQtlr5WMsuo2QR0dZ09O7ibBaiaEKiaMXzXM/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

举个例子，这里我们在创造模式下，让接入了 DeepSeek V4 Pro 的 DeepSeek Harness 创建了一个官方 Web UI 没有的「三栏模式」：

，时长00:25

<video src="https://mpvideo.qpic.cn/0bc3xiatkaabyialcll4cjvfdowdgw5acnia.f10002.mp4?dis_k=d5a9b6b8e0c12a4f7173f93ee70e5ddc&amp;dis_t=1786674370&amp;play_scene=10120&amp;auth_info=XbeE+1RQXUO93rvqdSNEPUE8NBM0FwJ9OwxUGCY6YFZ7QBJsEEsQNFYRbT8fLmQpSw==&amp;auth_key=9f7e9204e18e9e5c48985f5c6ec6b836&amp;vid=wxv_4647599842645704706&amp;format_id=10002&amp;support_redirect=0&amp;mmversion=false" controls="">您的浏览器不支持 video 标签</video>

Web UI 之外，TUI 则面向喜欢留在终端中的开发者。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqFj7MXENeAK5Xxl38qGJic8icfleBMGkhX0AHUNon42ptZssphOhvTLiaibleJbZwbQ6tlibDbibicH6KjVETDHicMeOeDATQUoWLXt6ia0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

Headless 模式适合脚本和 CI：它接受一个任务，等待 Agent 完全停稳，输出最后一条有效回复后退出。如果程序需要结构化事件和持续控制，则应使用 ACP 或 JSON-RPC/Python SDK。

自动化方面，项目提供 ACP 服务和 JSON-RPC 入口。Python SDK 驱动随附的 JSON-RPC 运行时，让 Python 应用可以启动会话、发送任务、接收通知，而不必直接嵌入 Node 内核。仓库还包含 Code Mode、自指 Cordis、MCP 记忆服务等示例。

值得注意的是，这些入口并不是四套各自演化的 Agent。它们共享核心能力模型、会话事件语义和大部分基础插件，但并非简单替换一层 UI，而是通过不同 bundle 组装出 Web、一次性任务和自动化服务等产品形态。这正是「一切皆插件」最直观的成果。

Agent 可以检查甚至改装自己

DeepSeek Harness 还提供了一组自指 Cordis 工具。它们不会进入标准、PTC 或极简模式，而是通过 Web UI 中的「创造模式」作为明确的高级入口提供。选择这一预设后，Agent 可以检查当前运行时的插件树，并动态挂载或卸载临时插件。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqGZT4iaaXfUETZnv1gnMVXXibRIC5LUctNSqp28icjxW7ciaG9PBFlrZiaDDQmZtpwUxINWQ1hibSmsia1rPPfjDJUrwLP0LrNrib6ibgPw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

这听上去有点像让汽车在高速公路上给自己换发动机，因而项目没有默认打开它。它适合研究或高级自动化场景：模型可以临时编写事件监听器、注册新工具、提供一个服务，再在任务完成后卸载。

自修改式 Agent 很容易沦为概念演示，但 Harness 至少把它放进了已有插件生命周期中。动态插件仍然运行在 Cordis 的 Context 和 Effect 机制下，注册项有明确的清理路径。

它还远谈不上安全无忧，却展示了这套架构真正想抵达的地方：智能体不只使用能力，也能在受控边界内重新组合自己的运行时。

Cordis 背后的设计，可以参考官方同步发布的论文《A Programming Paradigm for Spatiotemporal Composability》：

![图片](https://mmbiz.qpic.cn/mmbiz_png/5L8bhP5dIqEYPMEOJ2mmYZaibV2InWNZrbVIfFhSXna1DtEnbJsv0q1ovlBfySl1BNcaxFicjQTwZzvmwE8t9icc5XjYxQtsQ9O9XAYp1aLslg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

论文地址：https://github.com/cordiverse/paper

安全策略

编程智能体一旦获得文件系统和 Shell 权限，就可以修改代码、安装依赖、启动进程，甚至触碰工作区之外的主机环境。DeepSeek Harness 显然把这件事当作基础架构问题，而不是在界面上增加一个确认弹窗便草草收工。

项目默认采用 workspace-write 模式，将命令执行和文件修改限制在当前工作区及允许的临时目录中，并配合 ask 审批策略处理需要扩大权限的操作。更宽松的 danger-full-access 模式也存在，但必须由部署方明确选择；它不会被包装成一个看似无害的兼容选项。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5L8bhP5dIqHn4mg5OXUtYnmUq5Av5o78rwTmG29b86RQT4hiczC6guHhssBTtNQba2pkK2mAWjicHaIKufOoSAkicdibBkYc6xvg8yEbOnxvcd0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

工具调用还要经过前置策略、单调安全守卫、执行包装和后置处理。被守卫拒绝的操作不能被后续插件重新放行；需要扩大权限的命令必须说明原因，并通过审批机制重试。文件系统、Bash 和子进程共享同一套沙箱策略，避免出现「命令受限制，但文件工具可以绕过去」的割裂边界。

更值得肯定的是，DeepSeek Harness 采用「失败关闭」原则。如果系统无法确认隔离机制真正生效，它会拒绝执行，而不是悄悄退化为无保护运行。权限切换、审批请求、工具参数、执行结果和取消原因也会进入 Session Log，为事后审计和问题复现保留依据。

这套设计并不能消除智能体执行本地操作的全部风险，但它体现了一种难得的工程态度：安全是贯穿配置、执行、审批、日志与恢复机制的系统约束。模型可以提出行动，真正决定行动能否发生的，仍然是 Harness。

DeepSeek 想做的不止是「又一个 Codex」

如果只看 Web UI 或 TUI，很容易把 DeepSeek Harness 理解为 DeepSeek 版本的 Codex、Claude Code 或其他编程助手。但从仓库结构看，它的目标明显更底层。

默认应用当然重要，它让开发者可以直接获得一个能读写项目、运行命令、规划任务和调用子 Agent 的工具。但真正占据项目中心的，是可替换的能力接口、事件驱动的生命周期、权威会话日志和声明式组合。换言之，成品 Agent 更像这套 SDK 的第一位客户。

这也给 DeepSeek 的模型生态补上了一块过去不够显眼的拼图。模型决定智能上限，Harness 决定这些智能如何进入真实环境，如何使用工具，如何保留状态，又如何在权限边界内工作。对于企业开发者而言，后者往往比聊天窗口多几个按钮更重要，因为它决定了系统能否被审计、扩展、替换和长期维护。

DeepSeek Harness 现在还远没有到「安装完成，一切丝滑」的阶段，但它已经展示出一套相当完整的技术判断：Agent 不应该是一段越来越臃肿的循环，而应该是一组可以组合、观察和替换的能力；会话不应该只是聊天记录，而应该是运行事实；工具不应该只是函数，而应该同时拥有策略、日志和呈现协议。

因此，DeepSeek Harness 最值得关注的，并非它今天能否替代你正在使用的编程助手，而是它把 DeepSeek 对 Agent 工程的答案公开到了什么程度。

© THE END

转载请联系本公众号获得授权

投稿或寻求报道：liyazhou@jiqizhixin.com

AI开源项目 · 目录

闪记

复制 LaTeX 公式
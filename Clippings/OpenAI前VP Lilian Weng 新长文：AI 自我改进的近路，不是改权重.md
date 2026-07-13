---
title: OpenAI前VP Lilian Weng 新长文：AI 自我改进的近路，不是改权重
source: https://mp.weixin.qq.com/s/-ovpNjFsUYrLuKUpZusObA
author:
  - "[[Mountain Gu]]"
published: 2026-07-07
created: 2026-07-13
description: 今天下午，很多 AI 从业者的时间线闪了一下。Lilian Weng 更新了。博文落款是 7 月 4 日，推文是几个小时前发的。
tags:
  - clippings
  - AI-Agent/harness
---
Mountain Gu AgenticAI *2026年7月7日 17:51*

今天下午，很多 AI 从业者的时间线闪了一下。

Lilian Weng 更新了。博文落款是 7 月 4 日，推文是几个小时前发的。

在这个圈子里，“她更新了”这四个字本身就是新闻——Lil'Log 一年只有几篇，但几乎篇篇都会变成行业的公共教材。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UA4ABKCY6OzfjAKp3qZoY9ArroOJM6poTeS73u4VkxP4elusetoicosGjKlj8xu09ibAhTmKmibBrofl8eIByxmlnw4eeECOsANCLdBDHzTr2w/640?wx_fmt=jpeg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

Lilian Weng 发文推特，发布约 4小时 5.7 万浏览

简单介绍一下她是谁：前 OpenAI 安全研究 VP，现在是 Thinking Machines Lab 的联合创始人。2023 年那篇《LLM Powered Autonomous Agents》就是她写的——“Agent = LLM + 规划 + 记忆 + 工具”这张被无数课程和 PPT 引用的架构图，出处就是她。

三年前她定义了 Agent。

这次，她给另一个东西正了名：\*\*Harness Engineering\*\*。

![图片](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6Oz4TxIzlY9LwjU0Jxf2ic6P7ahicTmckKOaNwWYjMbqKv7z4qwcibcp1l7ib9xlIvs2aGYK4ALMc8hvMha4FM1jAP0NZIzfWwicRFWE/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

博客原文：《Harness Engineering for Self-Improvement》，Lil'Log

先铺一层背景。

AI 圈关于“递归自我改进”（RSI）的想象，有 60 年历史了：1965 年 I.J. Good 提出“超智能机器”——能设计出比自己更好的机器；2008 年 Yudkowsky 给这个反馈循环起了名字。此后它一直是科幻小说和末日论者共同的核心剧本：AI 改写自己的权重，然后，智能爆炸。

而 Lilian 这篇文章开头不远处，就给这个流传了 60 年的剧本泼了盆冷静的水：

「近期的 RSI 路径，不太可能从模型直接改写自己的权重开始。」

那从哪开始？从模型外面那层“壳”开始。

01

==Harness 是什么==

==她的定义值得逐字读：==

==「Harness 是围绕基础模型的那套系统：它编排执行，决定模型怎么思考和规划、怎么调用工具和行动、怎么感知和管理上下文、怎么存储产物、怎么评估结果。」==

==更重的是下面这句判断：==

==「raw model 和真实世界上下文之间的那一层，看起来和模型的原始智能同样重要。」==

==证据？她直接点名：Claude Code 和 Codex 这些成功的编码智能体产品。同一个模型，套上不同的 harness，产品力天差地别——这件事过去一年整个行业都体感过了。==

==她还给了一个漂亮的类比：harness 之于模型，就像操作系统之于硬件——把复杂逻辑封装起来，把接口保持简单。而且和 OS 一样，配置、工具接口、协议会逐渐在行业里标准化。==

02

三个设计模式

文章把当下 harness 的实践归纳为三个模式，做 Agent 的读者可以直接当自查清单：

\*\*模式一，工作流自动化\*\*：目标导向的循环——计划、执行、观察、改进、再执行，让模型分析自己的轨迹和失败。

\*\*模式二，文件系统即持久记忆\*\*：别什么都塞上下文窗口，实验日志、代码 diff、错误追踪统统落盘成文件——反正模型早就精通 bash。

\*\*模式三，子代理与后台任务\*\*：主代理派生子代理并行干活，配上进程管理——启动、查日志、取消、合并结果，并行必须显式、可检查。

她还解剖了编码智能体的标准工具箱：文件系统（glob/grep/read/write/edit）、shell、git、MCP、搜索、浏览器、后台任务、子代理委托——

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/UA4ABKCY6OwkbgVLuZo2opQibyUQ4VpxT99MqLssicN6HFg4CAkGicjia1dLVVXsn04aYibBhUfJ3T7FXibnbAjcgCZJZyTIGMIW76sfZ3J5NPI2s/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

博客配图：编码智能体 harness 的核心接口（Lil'Log 自制图）

如果你用过 Claude Code，会发现这张图就是它的 X 光片。

03

==优化的阶梯==

==真正的干货从这里开始。她梳理出一条清晰的演进线——我们优化的对象在一级级上移：==

==先是优化提示词，然后是优化结构化上下文，再是优化工作流，接着是优化 harness 代码本身，最后——优化“优化器”的代码。==

每一级都有代表作：ACE 把上下文当成一本不断进化的战术手册（生成器、反思器、策展器三件套）；MCE 做双层优化，把“上下文里放什么”和“怎么管理上下文”分开调；Meta-Harness 干脆是“优化 harness 的 harness”；AFlow 把工作流表示成图，用蒙特卡洛树搜索去搜最优结构。

![图片](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OwKnnFB4yl7fbUuFovHFAFtMsIa3lA5UddaQgibKdefHnWthNmz8ga4HUKzc9e2nsSVnLV1YWAz7oFIq19eMXOkfocBmKoyXCDc/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

博客配图：AFlow 用 MCTS 在工作流空间中搜索（Zhang et al. 2025）

看出来了吗？这条阶梯的尽头，就是系统自己改自己。

04

==会自我改进的 harness，和一盆冷水==

==自我改进这条线上，最有戏剧性的是三个工作。==

STOP（2023）：不改答案，改“改进器”本身——让改进器去改进自己。它自己发现了遗传算法、模拟退火、束搜索这些人类的经典优化策略。

![图片](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OwY3yVOP8U9JyeS8D1zTTwkGMHRQ10Yu5UZX2V1tH5mp1qRzMlgxvzDvFicUexWpiacKMqmEUOcWicCvv2PG9pp8G9Uw4AQCMyibaY/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

博客配图：STOP 自己发现的改进策略（Zelikman et al. 2023）

但 STOP 也留下了全文最重要的一盆冷水：用 GPT-4 跑，性能持续提升；换成 GPT-3.5 和 Mixtral，反而越改越差。Lilian 的总结是——

「递归结构本身是不够的。基座模型必须足够强，才能改进机制。harness 的改进让模型部署得更好，但智能仍然是核心。」

Self-Harness（2026）：把“自我改进”做成了工程闭环——先从失败轨迹里挖弱点模式，再让同一个模型提出有边界的 harness 修改，最后在保留数据上验证：既要解决弱点，又不能出现回归，二者同时满足才合并。

![图片](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OxpoUE6JEO7a5jeRD5uyHY8CAibnAsUMYVUMc6qVX2Z2p6QuZciaBnvU6qJVcb51G968k4nYvMdw0IBuiceLe5BcibZTAS0xV1bqnQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

博客配图：Self-Harness 的弱点挖掘—提议—验证循环（Zhang et al. 2026）

Darwin Gödel Machine（2025）：让编码智能体直接进化自己的 harness 代码仓库，SWE-bench Verified 从 20% 干到 50%，追平甚至超过了人类手工打造的 agent。同路线的 AlphaEvolve 用进化搜索 + 冻结 LLM 生成 diff，已经在矩阵乘法、GPU kernel 这类“评估清晰”的领域拿到真实成果。

![图片](https://mmbiz.qpic.cn/mmbiz_png/UA4ABKCY6OwjdjHbhFEZnKoia2zTibg9ASIAmkKlFLOHfV96Sw6cX1UdQyNCYSGUcQ6UgLqICicILVZv4pDkJTslq16fyf1NvukreFV9FDqKfA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

博客配图：AlphaEvolve 的进化搜索流程（Novikov et al. 2025）

05

==七块硬骨头==

==按她一贯的风格，文章末尾没有画饼，而是列了七个没解决的问题。挑几个最扎的：==

==评估器又弱又糊== ==——自我改进循环在有客观可测指标时才好使，但“研究品味”“长期科学价值”怎么测？==

==模型不擅长认输== ==——人类文献报喜不报忧，训练在这些数据上的模型，可能天然不善于放弃假设、承认失败。而从失败中学习，恰恰是修剪搜索空间最好的方式。==

==多样性坍塌== ==——进化和 RL 循环都爱抱着已知的高分模式薅，开放式研究里最好的路径，初期往往看起来更差。==

==Reward hacking== ==——优化单测就过拟合单测，优化评委就学会讨好评委。她的处方：评估器和权限控制必须放在循环外面。==

==长期健康没人管== ==——编码智能体确实提高了日常生产力，但没有明显的机制在乎一个几百人共同维护的仓库的长期健康：可维护性、所有权边界、向后兼容，这些都不在沙箱训练的奖励函数里。==

==还有一条关于人的，值得单独放一行：==

==「人类应该在栈上往上走，而不是被请出循环。」==

06

为什么这篇文章重要

说点原文之外的判断。

第一，这是一次命名权时刻。“harness”这个词在工程师的黑话里已经流通了几年——今天上午 Anthropic 发的 Claude Code 官方口述史里，研究员 Dawn Drain 回忆 2022 年就在攻“harness design”（在容器里搭持久 shell，让模型真的能动手）。民间实践了四年的东西，今天被 Lilian 写成了带定义、带分类、带优化理论的领域综述。一个领域被正名，通常意味着它要进课程表了。

第二，她对 RSI 的三段预测，比“智能爆炸”叙事务实得多：harness 工程先走向元方法论（改进“获取答案的机制”而不是答案）；成熟的 harness 撑起自动研究；最终大量 harness 改进被内化进模型——但接口不死。她在推文里补了一句：

「即使很多 harness 的改进最终被内化进核心模型，指定目标和上下文的需要也不会消失。」

这句话对每个做 Agent 基建的人都是定心丸——prompt engineering 的手艺被内化成了背景知识，但“把目标和上下文说清楚”的需求活了下来；harness engineering 大概率会走同一条路。

（利益相关：笔者正在写一本关于 harness engineering 的书，现在读到这篇的感觉，像是被人剧透了大纲，又像是被人盖章了选题。）

文章的最后一句话，替所有人把边界说死了：

「归根结底，我们造这项技术是为了人类更好的未来，而不是反过来。」

◇ ◆ ◇

相关链接

• 原文：https://lilianweng.github.io/posts/2026-07-04-harness/

• 推文：https://x.com/lilianweng/status/2074372369213428144

• 她 2023 年的 Agent 综述：https://lilianweng.github.io/posts/2023-06-23-agent/

• Making of Claude Code（文中提到的口述史）：https://www.anthropic.com/features/making-of-claude-code

**微信扫一扫赞赏作者**

闪记

复制 LaTeX 公式
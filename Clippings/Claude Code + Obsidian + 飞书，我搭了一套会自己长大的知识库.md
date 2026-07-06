---
title: Claude Code + Obsidian + 飞书，我搭了一套会自己长大的知识库
source: https://mp.weixin.qq.com/s/QTSqMJm4rXKHHzPLae5xKw
author:
  - "[[翻斗花园二蛋]]"
published: 2026-04-14
description: LLM wiki
tags:
  - Skill/knowledge-bank
---
翻斗花园二蛋 翻斗花园二蛋 *2026年4月14日 22:42*

事情是这样的。

昨天晚上我躺在沙发上刷手机，看到一篇讲 AI Coding 知识管理的文章，觉得挺有意思。

以前我的做法是，收藏，然后大概率再也不看。

但这次不一样。我打开飞书，给我的 Claude Code 小助手发了一条消息，「把这篇文章加入我的知识库」，然后把链接甩了过去。

过了大概两分钟，它回我了。说已经完成了 Ingest，原始素材保存好了，新建了 3 个 wiki 页面，索引也更新了。

我打开电脑上的 Obsidian，知识图谱里多了几个亮闪闪的新节点，跟之前的概念自动连上了线。

![图片](https://mmbiz.qpic.cn/mmbiz_png/GvmyiccCUFbxO54oDjuiaHnxsoDSSFiaYzWicTwf5pqLS4RutdbUahE8QfUSsfickvkJ6IAjzRuHdkGNNeY37K8NdeagbFntMhBdnGhd8hcXZeibo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

我当时就愣住了。

这玩意，真的跑通了。

。。。

OK 回到这件事怎么开始的。其实我跟大多数人一样，知识管理这个事儿，折腾了无数次，放弃了无数次。

Notion 建了几十个数据库，看着特别漂亮，但每次要找东西的时候还是靠搜索。flomo 写了几百条碎片笔记，回头翻的时候发现全是没头没尾的只言片语。微信收藏夹里躺着上千篇文章，你问我收藏了什么，我是真的想不起来。

**收集知识很容易。**

**整理知识要命。**

这是每一个爱学习的人都会掉进去的死循环，你越想整理，堆积的就越多，越堆积就越不想动，越不想动就越焦虑。最后的结果就是，打开笔记软件看了一眼，默默关掉，假装什么都没发生。

后来 RAG 火了。就是那个把文档丢进向量数据库，然后用 AI 搜索回答的方案。我也搞过，花了一个周末配环境、搭服务、灌数据。

听着特别美好对吧？把你所有的笔记、文章、PDF 全扔进去，然后想问什么问什么，AI 帮你从里面找答案。

但实际用下来。。。

怎么说呢，RAG 的问题不是不好用，是没有积累。

你想想看，每次你问 AI 一个问题，它干的事情是什么？去向量数据库里搜一圈，找几个最相关的文本片段，拼在一起给你一个回答。下次你问一个差不多的问题，它又从头来一遍。什么都没记住。

就像考试的时候翻课本。每次考试都翻，翻来翻去翻的是同一本课本， **但从来不做笔记。**

更头疼的是，当你需要综合 5 篇不同文章的知识来回答一个问题的时候，RAG 就很吃力了。它能找到每篇文章里最相关的一小段，但把这些碎片串起来变成一个有逻辑的回答？不是它擅长的。

向量检索返回的就是碎片。它不知道这些碎片之间是什么关系，不知道这个概念在那篇文章里被深入展开了，不知道这两个观点其实互相矛盾。

你积累了一年的文档，知识库里有几百篇文章，但从知识管理的角度看，什么都没积累。每次查询还是从零开始。

**没有复利。**

这里要解释一下「复利」这个词。后来我看到 Karpathy 在他的方案里反复强调一个英文词，compounding，就是复利、复合增长的意思。他说的是，知识管理应该像投资一样有复利效应，你今天存进去的一个概念，明天会跟新加入的概念产生关联，后天又会被另一篇文章补充完善。每一次新增都不是孤立的，而是在已有的网络上生长。时间越久，节点越多，连接越密，价值是指数级增长的。

RAG 没有这个。每次查询完就散了，什么都没留下。

这个问题困扰了我挺久的，直到有一天刷到了 Karpathy 发的那个 gist。

Andrej Karpathy，前 Tesla AI 总监、OpenAI 联合创始人，AI 圈的顶级大佬。他提了一个叫 LLM Wiki 的东西，思路跟 RAG 完全反着来。

他的核心想法特别简单， **不要在查询的时候才去处理知识，要在摄入的时候就把它整理好。**

你感受一下这个区别。RAG 是你把课本丢给 AI，每次考试 AI 现场翻书找答案。LLM Wiki 是 AI 平时就帮你把笔记整理好了，考试的时候直接看笔记。

一个是临时抱佛脚，一个是平时就用功。

Karpathy 设计了一个三层架构。最底层是原始资料，你的文章、笔记、PDF，这些东西 AI 只读不改，保持原貌。中间层是 Wiki，AI 读完原始资料之后，主动把关键信息拆出来，写进对应的 wiki 页面，建立概念之间的引用关系。最上层是 Schema，一个配置文件，告诉 AI 怎么理解和处理你的知识。

他用了一个特别妙的比方， **Obsidian 是 IDE，LLM 是程序员，Wiki 是代码库。**

AI 不是搜索引擎，它是知识库管理员。 **它的工作不是帮你搜东西，而是帮你整理东西。**

这里面有一个特别关键的洞察。人类为什么总是放弃维护知识库？不是因为懒，是因为维护成本太高了。你读完一篇文章，想把关键信息摘出来，想想这个观点跟之前哪个概念有关系，更新一下索引，检查有没有矛盾。这些「记账」的活儿，随着知识库变大，成本是指数增长的。

**但 AI 不嫌烦。**

它可以一次操作更新十几个文件，维护引用关系、保持摘要最新、标注矛盾、检查一致性。维护成本趋近于零。而且知识库越大，每加一篇新素材带来的交叉引用就越多，价值增长是复利的。

有赞的技术团队后来也发了一篇类似思路的文章，叫 Knowledge Wiki。他们在企业级项目里落地了这套方法，发现 AI Coding 的瓶颈根本不是模型能力，而是「上下文信息熵」，就是你每次向 AI 传达任务所需要的信息量。知识库要做的事情就是提前把这些信息结构化好，降低每次协作的传递成本。

他们还提了一个我觉得特别有意思的方案，叫渐进式披露。不用向量检索，让 AI 沿着目录结构一层一层往下读。workspace 级看全局，app 级看应用，context 级看具体细节。每个文件开头有一段摘要，AI 读个摘要就能判断相不相关，根本不用读全文。

这个思路一下子戳中我了。

说真的，看完 Karpathy 的 gist 和几篇实操教程之后，我就一直想把这套东西搭起来。但我有一个额外的需求，我不想每次都得坐在电脑前才能往知识库里加东西。

我的很多阅读是在手机上完成的。地铁上、午休的时候、睡前刷一刷。看到好文章的那一刻，我希望能直接把它丢给 AI 处理，而不是先收藏等回家再说。

因为回家大概率就忘了，你懂的。

所以我的方案是三件套，Claude Code + Obsidian + 飞书。

**Claude Code 是大脑。** 它负责所有的知识处理工作，读原始素材、拆解关键信息、写 wiki 页面、更新索引、维护交叉引用。它工作的依据是一个叫 CLAUDE.md 的文件，这是整个知识库的「规则书」，告诉 AI 这个知识库关注什么领域，目录结构长什么样，wiki 页面该怎么写，摄入新素材要走什么流程。

![图片](https://mmbiz.qpic.cn/mmbiz_png/GvmyiccCUFbwqfNOLLNajKequeVpzicWsdjklFxSBeEAkz3pEHzg4rsXQM3YceoYOEnoX4SibtJnrLLu6fV45ExVL6XQpiad1cI71TM1fG4X3uI/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

你可以把 CLAUDE.md 理解成一本员工手册。新来的 AI「员工」读完这个文件，就知道自己该怎么干活了。知识库的关注领域、命名规范、页面格式、操作流程，全在里面。

**Obsidian 是眼睛。** 它直接打开知识库的文件夹作为 Vault，所有 Markdown 文件即时可见。最爽的是它的 Graph View，也就是知识图谱，每个概念是一个节点，概念之间的引用关系是连线。你能直观地看到哪些知识是密集关联的，哪些还是孤岛。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/GvmyiccCUFbwJWTVsjOicRicFyg84qXANI9pGEGr4XrBPoDMWVGicLdheOr3icBkAhhEdc6uXPH2jlYNp2ZcxZmHl3fF0Y3h3dEueNicFzDF0Z3Mc/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**飞书机器人是手。** 通过一个叫 Claude-to-IM 的开源项目，我把飞书和本地的 Claude Code 打通了。手机上发一条消息，就能触发电脑上的 Claude Code 执行操作。

这是整个闭环里最关键的一环。 **它让知识收集从「回家再说」变成了「现在就搞」。**

整个知识库的目录结构长这样。

![图片](https://mmbiz.qpic.cn/mmbiz_png/GvmyiccCUFbw34M9lAs9KlD5Bmy7qszPlpRNH13z1xeGC0L0GQNfqHHNMWazmLVD7wOZuicazaRTzm4c7d3JdmibBxibeklYCLOUMyNPALfNP3Q/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

(trellis相关的忽略,trellis也是非常的好用呀！)

raw 文件夹放原始素材，只读不改，只增不删，保持原始面貌。wiki 文件夹是 AI 维护的结构化知识库，里面按 concepts（概念）、practices（实操）、cases（案例）、entities（实体）分类。CLAUDE.md 就是刚才说的 Schema，规则书。

顺着这块再往下聊，给你们看看实际跑起来是什么效果。

我在飞书的「LLMWiki 知识收集」群里发了一条消息，@ 了 Claude Code 小助手，让它把一篇微信公众号文章加入知识库，然后把链接贴上去。

![图片](https://mmbiz.qpic.cn/mmbiz_png/GvmyiccCUFbw2icosqqweU9fEmMRiblmunnxvwysGIGxcqvuKytAlaNQibTERmYbyg56sCCKXhIs8lXOUgicFS8XCpCb9Qv9nmOcpoIibATBIa9ac/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

Claude Code 接到消息之后，先用浏览器打开链接抓取文章内容。这里插一个小细节，微信公众号有反爬机制，普通的 HTTP 请求会被拦截，必须用真实浏览器加载页面才行。Claude Code 会自动调用 Playwright 浏览器来处理这种情况，这个坑我已经帮它记在记忆里了，下次遇到微信链接它会直接走浏览器，不会再傻乎乎地发 HTTP 请求。

抓到文章内容之后，它按照 CLAUDE.md 里定义的 Ingest 流程开始工作。

先把原始文章保存到 raw/articles/ 目录。然后分析这篇文章涉及哪些概念，判断应该创建哪些新 wiki 页面，或者更新哪些已有页面。一篇文章通常会触及 3 到 10 个 wiki 页面，不是简单地复制粘贴，而是把知识点拆出来，放到它该去的地方，建立跟已有知识的关联。

每个 wiki 页面都有标准格式。开头是 frontmatter，记录标题、创建时间、标签和来源。然后是一段两三句话的摘要，正文用清晰的结构组织。最后是相关链接，用 Obsidian 的双链语法关联到其他概念页面。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/GvmyiccCUFbxxUIZ0JNT2WfclMg9ficcQtwiaOC2ibib0CibrhfRPRMfhosJbMKsWjwqcOXEzbDQ0Qz13p0iaCkoBK9oibXyUib1Nq3y5xTP3ouiaRa5g/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

(wiki文章结构化)

全部写完之后，更新 INDEX.md 全局索引和 LOG.md 操作日志。整个过程大概两三分钟。

这是基础操作。

更骚的在后面。

不只是能往知识库里「存」东西，还能从知识库里「取」东西。

有一次我在外面，突然想回顾一下之前看过的模型蒸馏相关的知识。我掏出手机，在飞书里跟 Claude Code 说，「阅读我知识库，给我模型蒸馏知识」。

它先查看了知识库的目录结构，找到了相关的文件。然后读取所有跟蒸馏有关的 wiki 页面，把分散在好几个页面里的知识综合起来，给了我一个完整的知识全景。五代技术演进、贯穿每一代的核心问题链、关键洞察，全都串起来了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/GvmyiccCUFbxLy1RhIiako9ZvFKbtfEsTMQcuL5ppSdqicekJOugricdq1yrObXRDTgIShIu8YciamgfmSDaaNfAaCbLCYvs6XMzj5ff0kTjzQH4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

你感受一下，这些知识来自不同时间摄入的不同文章。但因为在 Ingest 的时候就已经被结构化处理过了，它们之间的关系是明确的。查询的时候不需要做任何「拼凑」工作，直接综合已经编译好的知识就行。

这就是 LLM Wiki 和 RAG 最大的区别。RAG 每次查询都在拼凑。 **LLM Wiki 的拼凑工作在摄入的时候就完成了。**

**复利。**

。。。

坦率的讲，搭这套东西的过程没有我前面说的这么丝滑。

特别是接入飞书那一步，在 Windows 上折腾了我好几个小时。愚钝如我，差点没搞定。

最坑的是 Windows 的路径问题，反斜杠在进程启动链路里被当转义字符吃掉了，试了 5 种方案才搞定，最后靠 PowerShell 绕过了整条 bash 链路。

说实话中间好几次差点放弃了，「这玩意该不会跑不了吧」。但最终跑通的时候。

太爽了。

回到 RAG 和 LLM Wiki 这块，我觉得不是谁取代谁的问题，是适用场景不同。

RAG 适合大规模文档搜索。你有几万份合同、几千份技术文档，需要快速定位某个具体信息。这种场景 RAG 很强，因为你不需要「理解」这些文档之间的关系，你只需要找到那个特定的片段。

LLM Wiki 适合知识积累。你在持续学习新东西，看文章、读论文、记笔记，你需要这些知识形成一个有结构的、互相关联的网络，而且这个网络得能持续生长。

RAG 没有积累，每次查询从零开始。LLM Wiki 有复利，每加一篇新素材，整个知识库都在增值。

RAG 依赖向量数据库和 Embedding 服务，基建成本不低。LLM Wiki 只需要文件夹和 Markdown 文件，零基建依赖。你的知识存在本地的.md 文件里，随便哪个编辑器都能打开。

RAG 的知识存储形态是向量，人看不懂。LLM Wiki 的知识存储是 Markdown，打开 Obsidian 就能看，Graph View 还能帮你看到全局的知识网络。

但我觉得最关键的区别其实不在技术层面。

RAG 的思维方式是「我有一堆文档，AI 帮我搜」。

LLM Wiki 的思维方式是「AI 帮我整理知识，我随时用」。

前者是被动的，后者是主动的。

顺着这个往上想一层。我觉得我们正在经历一个挺重要的转变，从「信息存储」到「知识编译」。

过去十年，工具解决的问题是怎么存。Evernote 帮你存网页，Notion 帮你存数据库，flomo 帮你存碎片想法。存得越来越方便了，但存完之后呢？

堆在那里。

因为整理是人在做，而人的精力有限。知识管理的瓶颈从来不在收集，在整理。

现在 AI 把整理这件事接过去了。它不嫌烦，不怕量大，一次操作同时更新十几个文件。维护成本趋近于零。

**这不是工具升级。**

**这是范式转变。**

从你往仓库里堆东西，变成有个管理员在帮你不停地整理仓库。 **而且这个管理员越整理越懂你的知识体系，越懂就整理得越好。**

我不知道这套方案能不能一直用下去，我自己也还在摸索。目前知识库里有二十多个 wiki 页面，十几个概念、几个实体，说多不多。但每次打开 Obsidian 看到那个图谱在慢慢变大，节点之间的连线越来越密，就觉得这次可能真的不一样。

以前整理知识是「我应该做但就是不想做」的事情。现在变成了「发条消息就搞定」的事情。

下次在地铁上刷到好文章，我不用纠结要不要收藏了。

打开飞书，甩给小助手就行。

以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～

谢谢你看我的文章，我们，下次再见。

**参考和工具链接**

Karpathy 的 LLM Wiki 原始 gist： https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Claude-to-IM（飞书/微信接入 Claude Code 的开源项目）： https://github.com/op7418/Claude-to-IM

Obsidian（本地 Markdown 知识库工具）： https://obsidian.md

Claude Code（Anthropic 的 CLI Agent 工具）： https://docs.anthropic.com/en/docs/claude-code

> / 作者：翻斗花园二蛋

**微信扫一扫赞赏作者**

闪记

复制 LaTeX 公式
---
title: "10 天暴涨 1.5 万 Star，Firecrawl 新工具开源。"
source: "https://mp.weixin.qq.com/s/pnpdXkzyFUn5fNv6CCnRYg"
author:
  - "[[小 G]]"
published: 2026-08-13
created: 2026-08-14
description: "anydoc，将各种输入转化为md"
tags:
  - "clippings"
---
小 G GitHubDaily *2026年8月13日 17:05*

平时在使用 Claude Code、Codex 的时候，想让 AI 帮我们处理各种文件。

将里面的内容提取出来，每种格式的文件要用不同工具来处理，说实话效率很低。

而且质量还参差不齐，有时候表格丢了，有时候公式乱了，甚至会无法提取。

这种情况，对我们做知识库或训练大模型给它喂文档，会带来很严重的影响。

为了解决这些问题，Firecrawl 团队开源了 **anydoc** 工具，短短 10 天，狂揽 15000+ Star。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/snxIHWuwQokVPa8a8ot3WSeiaiapoIQXzicIIBYZMLfuoJQ6tV0lCxxKKVYibiaoXBVuJjtyLhstR7qibNSkUdwUQDyGl7AxQlpMU6h0JCqMoZWy0/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

眼熟的朋友可能还记得，在昨天 ZCode 实测文章里，给它做了一个在线可用 Web 工具。

没想到不少朋友留言，能不能详细介绍一下 anydoc，那今天就跟大家讲讲。

Firecrawl 很多人都用它来抓取网页内容，转成大模型易读的 Markdown 文件。

这次他们再次开源 anydoc，在我看来，算是把本地文档这一块的处理也给补上。

它支持将 Word、PPT、Excel、PDF、EPUB等文件，一键转成干净的 Markdown。

覆盖 8 大类格式、14 种扩展名，就连 2003 年的老.doc、.ppt 这些古老的文件都支持。

![image-20260813140448026](https://mmbiz.qpic.cn/mmbiz_png/snxIHWuwQokmq9CCsA0fwydicmLF9F5VUumkia7vHzmkfN6uS0SqVqXYZKnF40OMQkkMiaPiam8Vnof1IXvdCDS8XIHdGPj7rpcXhsJmoz6dchs/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

我看了下它的实现思路，不管什么格式文件，它都会先把文件读懂，整理成一份统一格式的中间稿。

而这份中间稿只记内容和结构，哪里是标题、哪里是表格、哪里是列表，全部标得清清楚楚。

最后再把中间稿转换成 Markdown 文件，这样做带来的好处，能让文档维护变得更加容易。

比如在转换成 Markdown 的时候，发现一个表格转换的 Bug 能直接跟着内容随手修好。

对于文件格式的识别压根不看扩展名，靠的是读文件字节里的特征标记，即便文件名标错也没事。

转换速度这块是它的强项，纯 Rust 实现，不依赖 ML 模型和外部服务，最快仅需要 4.4 毫秒。

官方实测，拿 100 份真实文档，与 libreoffice、markitdown、pandoc、docling 等同类工具横向对比测试。

结果 anydoc 是唯一能把 14 种文件格式全支持到，而且质量和速度方面均拿下第一名。

![image-20260813140505453](https://mmbiz.qpic.cn/mmbiz_png/snxIHWuwQolNlZCKtDZuib8rNPLuCMKVQoS6dAGcPhelXxE7EsTEciacaiaW7ZZVdgetdxQmQMw2qsqfJs91Anv0uSyelkYI8kwmT8BBu5RT2I/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

至于细节方面处理，像合并单元格的表格、脚注、代码块，甚至 PPT 里的备注都能保留。

文档若有图片，会以引用文本形式呈现，原始图片留在缓存目录上，需要的话可以自己取。

项目有多种使用方式，提供 Node、Python、Rust 等开发语言的依赖包，方便我们集成到项目。

也可以通过 Skill 方式，安装到我们常用的 Claude Code、Codex 等 Agent 工具使用。

```bash
npx skills add firecrawl/anydoc
```

装完之后，就能直接让 Agent 更容易读懂任何格式的文件，也能转成 Markdown 文档。

另外还提供了在线网页版本，只需打开浏览器就能用，都在本地转换完成，不会上传到服务器。

偶尔转一两份文件，或者文档比较敏感不敢往在线工具传的朋友，用这个最合适。

![image-20260813145906279](https://mmbiz.qpic.cn/sz_mmbiz_png/snxIHWuwQonxgZGyrPdV0VBAV5zIaicmhq6feq3sGLJvuzj9FJxCSfrq9sqiaPxpPespygia8j4oqPZiazznGjDPdnUawA183DnSVrNaQJpOwpE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

目前 anydoc 还不完善，本地只能处理常规 PDF，对于扫描件纯图片的 PDF 读不出来。

但官方也提供了解决方案，可以用他们的托管 API，接上他家 OCR 模型就能处理。

另外对于加密和带密码保护的文档也转不了，会直接报错，这个我觉得正常。

昨天我已经实测过一轮，对于 docx、pptx、xlsx 这些常见格式的文件转换都没问题。

甚至连 rtf、odt、epub 这些比较小众且不常见的文件，都能转换成干净的 Markdown。

![image-20260811095102804](https://mmbiz.qpic.cn/mmbiz_jpg/snxIHWuwQokHD5CVGahJiayHwibSGsvIGvf8cC3NNr1gxiaEibj9pSxib5LNRkvaibkuYZnMfmalqibXEZ0xzlBuO9ZfzTbvKXRLudMwE3LYGULibOU/640?wx_fmt=webp&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

image-20260811095102804

### 写在最后

这两年，身边不少朋友都在做 RAG 知识库，或开发 Agent 相关的应用。

在文档解析这块处理，最容易出问题而且不易发现，比如表格转丢一半，导致检索不准。

而 Firecrawl 团队先把网页转 Markdown 实现，现在又补上对本地文档的处理。

在我看来，这两个给 AI 喂数据比较重要的入口，都被 Firecrawl 占上了。

往后，它会不会像 ffmpeg 在音视频领域的地位一样，也成为 AI 数据管道里的默认底座。

还未可知，但从目前来看，大家的选择是，谁家工具做得又快又干净，就会用谁的。

GitHub 项目地址：https://github.com/firecrawl/anydoc

今天的分享到此结束，感谢大家抽空阅读，我们下期再见，Respect！

AI · 目录

闪记

复制 LaTeX 公式
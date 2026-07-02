---
id: "7286690657786136595"
cubox_url: https://cubox.pro/web/card/7286690657786136595
url: https://mp.weixin.qq.com/s/qG02XjSV9nuRIonGy_VOwQ
tags:
  - RAG
  - RAG/query
---
# RAG从入门到精通系列4：Query Construction（查询构造）

生成特定领域数据源所需的查询语句或格式化内容

[Read in Cubox](https://cubox.pro/web/card/7286690657786136595)  
[Read Original](https://mp.weixin.qq.com/s/qG02XjSV9nuRIonGy_VOwQ)  

---


---

## 📖 正文全文

# RAG从入门到精通系列4：Query Construction（查询构造）

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/qG02XjSV9nuRIonGy_VOwQ)南七无名式 PyTorch研习社


LLM（Large Language Model，大型语言模型）是一个功能强大的新平台，但它们并不总是使用与我们的任务相关的数据或者是最新的数据进行训练。

RAG（Retrieval Augmented Generation，检索增强生成）是一种将 LLM 与外部数据源（例如私有数据或最新数据）连接的通用方法。它允许 LLM 使用外部数据来生成其输出。

要想真正掌握 RAG，我们需要学习下图所示的技术（技巧）：

![](https://image.cubox.pro/cardImg/2tofsitxtpibxotyebymmk7f8wvbv1v3xteqnpeld4am58om51?imageMogr2/quality/90/format/gif/ignore-error/1)

我们从《[RAG从入门到精通系列3：Routing（路由）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495394&idx=1&sn=fe6c0e48aa97c9eded45d996041a88b1&scene=21#wechat_redirect)》中学习了 ****Routing**** ，在本文中我们将进入下一个节点：**Query Construction**（查询构造）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicRwlC67ibqX1RQicOxmMia6pdqqGf48RUOPAIWC4ezPPzEsIdzQrhwMENQmudSlqe8V0JAeaHpJvhug%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

**Query Construction** 是指根据用户输入的自然语言问题，通过语义解析、上下文理解以及路由后的结果，生成特定领域数据源所需的查询语句或格式化内容。这一过程的目标是最大化数据源检索的准确性和相关性。

比如，许多 Vector Store 都有 meta data（元数据），我们可以将用户的查询"Videos on chat langchain published after 2024"（2024年之后发布的 chat langchain 视频）转成可用于 meta data 过滤的结构化查询：  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu9Zw1DvX6aOxjescOcwibYNSKvqs283pgEicjb2icfdTAYiaCsEJWezXcA7ZHAr3yDX3iazMV6fViaVfYMw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

首先我构造一个假的 Document 对象，其中包含了一些假的 meta data：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicRwlC67ibqX1RQicOxmMia6pdIGckUmBDSsLee48Nh6jD4GhyN2icKzG6oAKnibGqiaic86BLdARO5DTbqg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

假设我们已经建立了一个索引：

* 允许我们对每个文档的 content 和 title 进行非结构化搜索

* 并对`view count、``publication date 和 length`使用范围过滤。

我们希望将自然语言转换为结构化搜索查询。

我们可以为结构化搜索查询定义一个架构：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicRwlC67ibqX1RQicOxmMia6pdCBwGic3SXmlafVe4305ibibt3MIMmwibVAHn8kJX5LLoDUMHtr3ozSiagag%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

现在，我们写一个让 LLM 可以将自然语言转成合适的结构化查询的 Prompt：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicRwlC67ibqX1RQicOxmMia6pdmmicH3zOXDxU6yvKrYy8YLcYx9UiapA3W18xqQ7MDtGUwFEm8zUOHftQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

整体的运行结果还是不错的：  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicRwlC67ibqX1RQicOxmMia6pdln6n4tuSzj1XFuf3nhDT6J41A8s1td7xiaM43XqvY3fVa0wr1NbHicBQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)


**GitHub 链接：**

https://github.com/realyinchen/RAG/blob/main/04_Query_Construction.ipynb  


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FYSugV5KTRwUe3icAJT8QUSoK7ybHA7ds62KDx6ibQibff6Yv0EYlA8VIDH5vyjH6IdiaEqeNRMAIMRpUJrdbgGI4EA%2F640%3Fwx_fmt%3Dgif%26wxfrom%3D5%26wx_lazy%3D1%26tp%3Dwebp&valid=false)


[Read in Cubox](https://cubox.pro/web/card/7286690657786136595)

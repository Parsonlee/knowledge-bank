---
id: "7281570011020266757"
cubox_url: https://cubox.pro/web/card/7281570011020266757
url: https://mp.weixin.qq.com/s/4IOMT5JaL9flv6dbZjif4g
tags:
  - RAG

---
# RAG从入门到精通系列3：Routing（路由）

根据用户的查询内容，智能地选择最适合的检索路径或推理逻辑

[Read in Cubox](https://cubox.pro/web/card/7281570011020266757)  
[Read Original](https://mp.weixin.qq.com/s/4IOMT5JaL9flv6dbZjif4g)  

---


---

\## 📖 正文全文

# RAG从入门到精通系列3：Routing（路由）

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/4IOMT5JaL9flv6dbZjif4g)南七无名式 PyTorch研习社


LLM（Large Language Model，大型语言模型）是一个功能强大的新平台，但它们并不总是使用与我们的任务相关的数据或者是最新的数据进行训练。

RAG（Retrieval Augmented Generation，检索增强生成）是一种将 LLM 与外部数据源（例如私有数据或最新数据）连接的通用方法。它允许 LLM 使用外部数据来生成其输出。

要想真正掌握 RAG，我们需要学习下图所示的技术（技巧）：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8bchx6XOFHAkoCAVrOh1N5MycECIYib1InAKy7T6ibI91aWzkGOToGVIaFmnJp8NUkRTfcX3PA3Wlw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

我们从《[RAG从入门到精通系列2：Query Translation（查询翻译）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495307&idx=1&sn=fed449f41e11c4ef2fe033b38d3d8dc8&scene=21\#wechat_redirect)》中学习了 **Query Translation** ，在本文中我们将进入下一个节点：**Routing**（路由）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu9Zw1DvX6aOxjescOcwibYNSErHYOfPR5I7lUSlV1TlRCXaeIfyl0PpZ8CMyTGiaQmAeANpuVA6NxcA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

**Routing**是指根据用户的查询内容，智能地选择最适合的检索路径或推理逻辑，以更高效地获取答案。这种动态选择的过程在多数据源、多检索器或多任务场景下尤为重要，能够显著提升系统的性能和准确性。

**Routing** 在 RAG 中的实现类型：

* Logical Routing（逻辑路由）

* Semantic Routing（语义路由）


**Logical Routing**


* 基于明确的规则或分类模型对查询进行分流。例如，将查询分类到不同的数据库、知识库或 API。

* 适用于结构化问题或明确的数据源场景。

首先我们定义了 python_docs、js_docs 和 golang_docs 这三个数据源：

通过使用 with_structured_output，你可以将模型的生成结果格式化成特定的结构化数据格式（如 JSON 或字典）。

然后我们定义了一个根据用户问题中的编程语言选择数据源的 prompt：  

最后我们组成了一个 router chain：  

router 可以根据用户问题中的编程语言自动选择数据源。  

我们可以写一个简单的路由函数来选择数据源：  


**Semantic Routing**


* 基于向量化的语义相似性动态选择最优路径。例如，通过嵌入技术匹配最合适的 Prompt 或检索器。

* 适用于模糊查询或需要灵活响应的场景。

比如我们可以写两个用于回答不同领域（物理和数学）问题的 Prompt：


然后我们的 Prompt 路由函数 prompt_router 根据用户的问题和每个 Prompt 的语义相似程度（在这里是余弦相似度）选择合适的 Prompt。  


**GitHub 链接：**

https://github.com/realyinchen/RAG/blob/main/03_Routing.ipynb  


[Read in Cubox](https://cubox.pro/web/card/7281570011020266757)

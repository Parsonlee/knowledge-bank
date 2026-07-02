---
id: "7286745671065928830"
cubox_url: https://cubox.pro/web/card/7286745671065928830
url: https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495615&idx=1&sn=022d4b59324ae486b7b65b280b74eb80&chksm=eaecf500dd9b7c164f038ce9502c1d48f2cebb05e753d79c45ce734c51ec6a105df430ea4f4a&cur_album_id=3689450339863740420&scene=189
tags:
  - RAG
  - RAG/retrieval
---
# RAG从入门到精通系列6：Retrieval（检索）



[Read in Cubox](https://cubox.pro/web/card/7286745671065928830)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495615&idx=1&sn=022d4b59324ae486b7b65b280b74eb80&chksm=eaecf500dd9b7c164f038ce9502c1d48f2cebb05e753d79c45ce734c51ec6a105df430ea4f4a&cur_album_id=3689450339863740420&scene=189)  

---


---

\## 📖 正文全文

# RAG从入门到精通系列6：Retrieval（检索）

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495615&idx=1&sn=022d4b59324ae486b7b65b280b74eb80&chksm=eaecf500dd9b7c164f038ce9502c1d48f2cebb05e753d79c45ce734c51ec6a105df430ea4f4a&cur_album_id=3689450339863740420&scene=189)南七无名式 PyTorch研习社


LLM（Large Language Model，大型语言模型）是一个功能强大的新平台，但它们并不总是使用与我们的任务相关的数据或者是最新的数据进行训练。

RAG（Retrieval Augmented Generation，检索增强生成）是一种将 LLM 与外部数据源（例如私有数据或最新数据）连接的通用方法。它允许 LLM 使用外部数据来生成其输出。

要想真正掌握 RAG，我们需要学习下图所示的技术（技巧）：

![](https://image.cubox.pro/cardImg/2tofsitxtpibxotyebymmk7f8wvbv1v3xteqnpeld4am58om51?imageMogr2/quality/90/format/gif/ignore-error/1)

我们已经学习了 **Query Translation**《[RAG从入门到精通系列2：Query Translation（查询翻译）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495307&idx=1&sn=fed449f41e11c4ef2fe033b38d3d8dc8&scene=21\#wechat_redirect)》、**Routing** 《[RAG从入门到精通系列3：Routing（路由）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495394&idx=1&sn=fe6c0e48aa97c9eded45d996041a88b1&scene=21\#wechat_redirect)》、 **Query Construction**《[RAG从入门到精通系列4：Query Construction（查询构造）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495560&idx=1&sn=7762f8e5842b5cc997875a756365e744&scene=21\#wechat_redirect)》和 **Indexing**《[RAG从入门到精通系列5：Indexing（索引）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495567&idx=1&sn=3c2f6d114a792093f28e8a2b95851de6&scene=21\#wechat_redirect)》。

现在我们继续要按照上图的节点顺序回到《[RAG从入门到精通系列1：基础RAG](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495255&idx=1&sn=562e184d49d101f7be545b412a236e46&scene=21\#wechat_redirect)》中介绍过的 **Retrieval**（检索）。

在传统的 RAG 系统中，基本的流程是：

1. Retrieval（检索）：从数据库中检索出与用户查询相关的候选文档。

2. Generation（生成）：根据检索到的文档和查询生成回答。

3. Output（输出）：最终生成的答案。

为了提升 RAG 系统的准确性，我们可以：

* Ranking：在初步检索到一组候选文档后，通过进一步的评估对这些文档进行重新排序，以便提高相关性和生成质量。

* Refinement：在检索文档阶段进行更细致的筛选和优化，确保用于生成的文档更加精准。目标是优化检索结果，并在生成之前提升生成的基础质量。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8nKU3GjTh6GQJ7rGq1FpzShDJpn1SicFUzfdiaQ3H7bqibUkqRm1Vd4GYicBQYib8PWvtGvI84QnPV6WQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)


**Ranking**


我们这里主要说一下 Re-Rank：对检索到的候选文档进行重新排序的过程。这个步骤通常是为了提高生成模型的质量，确保生成的答案或内容更相关、更精确。  

具体来说，Re-Rank的做法一般有以下几种：

1. **基于相似度的排序**：可以使用基于查询和文档之间相似度的度量方法，如余弦相似度、点积等。

2. **基于深度学习的排序模型**：一些更复杂的 Re-Rank 方法会利用深度学习模型，比如使用 BERT 或 T5 等预训练语言模型，进一步评估候选文档和查询之间的相关性。

3. **使用回归模型**：有时可以将候选文档的特征（如长度、相似度、标题等）输入回归模型，预测每个文档的重要性得分，最终根据得分对文档排序

在《[RAG从入门到精通系列2：Query Translation（查询翻译）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495307&idx=1&sn=fed449f41e11c4ef2fe033b38d3d8dc8&scene=21\#wechat_redirect)》中介绍过了 RAG Fusion：生成多个用户查询来检索多篇文档，然后利用 RRF（Reciprocal Rank Fusion）对检索结果进行重新排名。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8nKU3GjTh6GQJ7rGq1FpzS2V0KJb06jMOGrMe4VlEkjUEPpNRmsywLmHcn31TaSCVKzQw2QbMUbg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Buib02aUGlGKOTroKic46Sa1or9BziaKTO5wIb8jmCiaAccACcDk4r32hBGoQIWwI5zsG5DptKQcRRPYLA%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1%26tp%3Dwebp&valid=false)

相关的代码在：

https://github.com/realyinchen/RAG/blob/main/02_Query_Translation.ipynb


**Refinement**


Self-reflection RAG 是一个相对较新的概念，通常是指在 RAG 系统中，结合自我反思的机制来改进生成结果。这个过程会在生成步骤中加入自我审视，帮助模型更好地理解和修正之前的生成结果，以提高最终的输出质量。

**CRAG**

CRAG（Corrective Retrieval Augmented Generation）是一种为 RAG 设计的策略，它将自我反思/自我评分机制应用于检索到的文档。

* 如果文档正确，则对文档进行知识细化，去除与用户查询无关的部分。

* 如果文档模棱两可，那么：

  * 对文档进行知识细化，去除与用户查询无关的部分。

  * 进行网络搜索相关知识。

* 如果文档不正确，那么进行网络搜索相关知识。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8nKU3GjTh6GQJ7rGq1FpzSkweuy6SbIPADvvPoGOHFmPpvnXZFda00ic8rB1jBECHxm0VI0Rp7AKQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

论文地址：  

https://arxiv.org/pdf/2401.15884

我们将在这里借助于 Qwen + BAAI + LangChain + LangGraph + Qdrant 实现一种简单的 CRAG（Corrective RAG）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8T88jeDsaZqrhgiaolric7GnJKFrZiamtQKSWUDUfbBPSzhOzIka6bTIPpzBfy6vIFJ5OcA3zUxgRrQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

想象一个状态字典 state 依次经过上图的节点，每个节点都会更新或者不更新 state。简单地来说就是：

1. 根据用户查询（question）检索文档（documents）；

2. 将 question 和 documents 输入评分节点判断 documents 是否不相关：

   1. 如果不相关，则改写查询并执行网络搜索，然后开始准备生成回答；

   2. 如果相关，则开始准备生成回答。

我们可以使用 LangGraph 实现上述的流程，具体代码链接在文末。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8T88jeDsaZqrhgiaolric7GnL9A8BGUibGLNhNkIxa1DqHlerI53VknYNbHfzsnNhgDw7ndr8Uhk1qA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

我分别提了两个问题：

1. 第一个问题可以在知识库中检索到；

2. 第二个问题是关于 DeepSeek-R1 的，显然知识库中没有，只能借助于网络搜索。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8T88jeDsaZqrhgiaolric7GnvQpPia5YYKyszOx1oPsHHZeLFM2owJAMKCUEFn41sqpmZ0fxJL76hQg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

**Self-RAG**

Self-RAG（Self-Reflective Retrieval-Augmented Generation）是一种结合了自我反思或自我评估的 RAG 策略，用于提升从检索到生成的整个流程的质量。它在传统 RAG 框架的基础上，引入了额外的"自我检查"步骤，以更高效地评估和改进检索和生成结果。

原始论文地址：

https://arxiv.org/abs/2310.11511

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8T88jeDsaZqrhgiaolric7GnSbvqz1SBQGjr04wdvg4iaRNjxgSpBic7pBbMPPKZZ0hNTSnrr6SovnFg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

我们接着用 LangGraph 实现上述简单的 Self-RAG 流程，具体代码链接在文末。  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8T88jeDsaZqrhgiaolric7Gngvr1GKHS1iasTqr8KDGXQjTtjtibiaBIwtS4AHOwWIHu6Sl9BvQEeHkOw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

然后我们询问一个问题，可以清楚看到整个 Self-RAG 流程是按照上述的工作流进行的：  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu8T88jeDsaZqrhgiaolric7GnMs36oOS5RLmkicxnIm2lbCiaE7sOftOL1xtDuorIndvjojLajVaicQmsQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)


**GitHub 链接：**

https://github.com/realyinchen/RAG/blob/main/06_Retrieval.ipynb  


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_gif%2FYSugV5KTRwUe3icAJT8QUSoK7ybHA7ds62KDx6ibQibff6Yv0EYlA8VIDH5vyjH6IdiaEqeNRMAIMRpUJrdbgGI4EA%2F640%3Fwx_fmt%3Dgif%26wxfrom%3D5%26wx_lazy%3D1%26tp%3Dwebp&valid=false)


[Read in Cubox](https://cubox.pro/web/card/7286745671065928830)

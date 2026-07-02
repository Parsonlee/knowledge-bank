---
id: "7250870008719344095"
cubox_url: https://cubox.pro/web/card/7250870008719344095
url: https://mp.weixin.qq.com/s/UZV4ztL0j5k2qPV8U_wZVg
tags:
  - RAG
  - RAG/query
---
# RAG高级优化：一文看尽query的转换之路

本文将介绍三种query理解的方法，以增强检索增强生成(RAG)系统中的检索过程，每种技术都旨在通过修改或扩展原始查询来提高检索信息的相关性和全面性。

[Read in Cubox](https://cubox.pro/web/card/7250870008719344095)  
[Read Original](https://mp.weixin.qq.com/s/UZV4ztL0j5k2qPV8U_wZVg)  

---


---

\## 📖 正文全文

# RAG高级优化：一文看尽query的转换之路

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/UZV4ztL0j5k2qPV8U_wZVg)哎呀AIYA 哎呀AIYA

准确地找到与用户查询最相关的信息是RAG系统成功的关键，如何帮助检索系统提升召回的效果是RAG系统研究的热门方向，之前的文章介绍了在分块阶段的优化方法：[RAG高级优化：基于问题生成的文档检索增强](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484125&idx=1&sn=0490793590a7061bf0593749f1a58474&chksm=c310482bf467c13dc718c0601c3b2ec0072e8d376cfa0c3b5d0d71406dbfa39bb1b09c684cfc&scene=21\#wechat_redirect)。本文将介绍三种query理解的方法，以增强检索增强生成(RAG)系统中的检索过程：

* **查询重写：** 重新定义查询，使其更加具体和详细。

* **Step-back提示：** 生成更广泛的查询，以获得更好的上下文检索。

*
  **子查询分解：** 将复杂查询分解为更简单的子查询。


每种技术都旨在通过修改或扩展原始查询来提高检索信息的相关性和全面性。

query转化的优点

RAG系统在检索最相关的信息时经常面临挑战，特别是在处理复杂或模糊的查询时。这些查询转换技术通过重新制定查询以更好地匹配相关文档或检索更全面的信息来解决这个问题。

* **提升相关性:** 查询重写有助于检索更具体和相关的信息。

* **更好的上下文:** 后退提示允许检索更广泛的上下文和背景信息。

* **综合结果:**子查询分解支持检索涵盖复杂查询的不同方面的信息。

* **灵活性:** 每种技术可以单独使用，也可以结合使用，这取决于具体的用例。

**示例介绍**

**示例查询**:"气候变化对环境的影响是什么?"

**查询重写** ，将其扩展到包括特定方面，如温度变化和生物多样性。

**step-back提示** ，将其概括为"气候变化的一般影响是什么?"

**子查询分解** ，将其分解为生物多样性、海洋、天气模式和陆地环境等问题。


**结论**

这些查询转换技术为增强RAG系统的检索能力提供了强大的方法。通过以各种方式重新表述查询，它们可以显著提高检索信息的相关性、上下文和全面性。这些方法在查询复杂或多方面的领域中特别有价值，例如科学研究、法律分析或全面的事实查找任务。


方案介绍

**1. 查询重写**

**目的:** 使查询更加具体和详细，提高检索相关信息的可能性。

**方案:** 重写的确认样不仅与原始查询相似，而且还提供不同的角度或透视图，从而提高最终生成的质量和深度。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliaZVHx6aOVxb5Iawd5sq8kehsSZk2iclHZUooFYHWL3U8gaqgicqYWgiaVzYK6Y8icm60IAgMLLpfDcNdQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

**2. Step-back提示**

**目的:** 生成更广泛、更通用的查询，帮助检索相关的背景信息。

**方案:** 后退提示（Step-Back Prompting）旨在通过考虑高层次的概念和原则来解决复杂问题，与直接解决问题的方法形成对比。"抽象的目的不是为了让你更迷糊，而是创建了绝对精确的新的语义层次"。


**3. 子查询分解**

**目的:** 将复杂查询分解为更简单的子查询，以便更全面地检索信息。

**方案:** Query分解关键思想是将一个复杂问题分解成一系列更简单的子问题，然后依次解决它们。解决每个子问题都得益于之前解决的子问题的答案。


方案实现和举例

\#\## 本节我们将介绍上述方法的具体实现，同时给出对应的prompt，并举例说明效果：所有技术都使用大模型进行查询转换；自定义提示模板用于指导模型生成适当的转换，代码为每种转换技术提供了单独的功能，允许轻松地集成到现有的RAG系统中。


**1 -查询重写**

重新表述查询以改进检索。

* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 

    query_rewrite_template = """You are an AI assistant tasked with reformulating user queries to improve retrieval in a RAG system. Given the original query, rewrite it to be more specific, detailed, and likely to retrieve relevant information.
    Original query: {original_query}
    Rewritten query:"""
    query_rewrite_prompt = PromptTemplate(    input_variables=["original_query"],    template=query_rewrite_template)


运行例子：

* 
* 
* 
* 
* 
* 

    # example query over the understanding climate change datasetoriginal_query = "气候变化对环境的影响是什么?"rewritten_query = rewrite_query(original_query)print("Original query:", original_query)print("\nRewritten query:", rewritten_query)


效果展示：  

* 
* 
* 

    Original query: 气候变化对环境的影响是什么?
    Rewritten query: 气候变化对各种生态系统的具体影响是什么，包括温度、降水模式、海平面和生物多样性的变化?


**2 -退步提示**

生成更广泛的查询，以便更好地检索上下文。

* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 

    # Create a prompt template for step-back promptingstep_back_template = """You are an AI assistant tasked with generating broader, more general queries to improve context retrieval in a RAG system.Given the original query, generate a step-back query that is more general and can help retrieve relevant background information.
    Original query: {original_query}
    Step-back query:"""
    step_back_prompt = PromptTemplate(    input_variables=["original_query"],    template=step_back_template)


运行例子

* 
* 
* 
* 

    original_query = "气候变化对环境的影响是什么?"step_back_query = generate_step_back_query(original_query)print("Original query:", original_query)print("\nStep-back query:", step_back_query)


效果展示：  

* 
* 
* 

    Original query: 气候变化对环境的影响是什么?
    Step-back query: 气候变化的一般影响是什么?


**3-子查询分解**

将复杂查询分解为更简单的子查询。

* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 

    subquery_decomposition_template = """You are an AI assistant tasked with breaking down complex queries into simpler sub-queries for a RAG system.Given the original query, decompose it into 2-4 simpler sub-queries that, when answered together, would provide a comprehensive response to the original query.
    Original query: {original_query}
    example: What are the impacts of climate change on the environment?
    Sub-queries:1. What are the impacts of climate change on biodiversity?2. How does climate change affect the oceans?3. What are the effects of climate change on agriculture?4. What are the impacts of climate change on human health?"""

    subquery_decomposition_prompt = PromptTemplate(    input_variables=["original_query"],    template=subquery_decomposition_template)


运行例子：

* 
* 
* 
* 
* 

    original_query = "气候变化对环境的影响是什么?"sub_queries = decompose_query(original_query)print("\nSub-queries:")for i, sub_query in enumerate(sub_queries, 1):    print(sub_query)


效果展示：

* 
* 
* 
* 
* 
* 

    Sub-queries:Original query: 气候变化对环境的影响是什么?1. 气候变化如何影响生物多样性和生态系统?2. 气候变化对海洋环境和海洋生物有什么影响?3. 气候变化如何影响天气模式和极端天气事件?4. 气候变化对陆地环境，如森林和沙漠有什么影响?


如果对内容有什么疑问和建议可以私信和留言，也可以添加我加入大模型交流群，一起讨论大模型在创作、RAG和agent中的应用。  

好了，这就是我今天想分享的内容。如果你对大模型应用感兴趣，别忘了点赞、关注噢\~


往期推荐


[RAG文本切分LV3：轻松定制Markdown切分](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484120&idx=1&sn=51fdd215151fe9be2d0ab8290eed6a1e&chksm=c310482ef467c13880ca7633fafbac9bedb57c318a7629ce08d27ea7609baa3e42c7ab70992a&scene=21\#wechat_redirect)  


[支持大模型流式输出的JSON提取工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483821&idx=1&sn=6f34d91291fbcab03a79142eaa3ed56f&chksm=c3104b5bf467c24d7c4184784831d2cab8ce97f47cfc86d40da172650e67dba9a0860a7411b0&scene=21\#wechat_redirect)  


[RAG高级优化：基于问题生成的文档检索增强](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484125&idx=1&sn=0490793590a7061bf0593749f1a58474&chksm=c310482bf467c13dc718c0601c3b2ec0072e8d376cfa0c3b5d0d71406dbfa39bb1b09c684cfc&scene=21\#wechat_redirect)  


[一款优秀的开源项目，PDF扫描件识别也超容易](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484167&idx=1&sn=b6dbd57396f03cbfe1dbad2a58424293&chksm=c31049f1f467c0e7f37cf29359bdb4ae8f319ce1ba346bbf5bb6c716c8b533a1f907c79d1673&scene=21\#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7250870008719344095)

---
id: "7250872929913668335"
cubox_url: https://cubox.pro/web/card/7250872929913668335
url: https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484209&idx=1&sn=0ce7bb6bbb6a0ff5efb4ad10ce2765a7&chksm=c31049c7f467c0d1eae08bc1e7a589b3769d96971ed8149daa55a4e1c6000a0a56b47227aa64&cur_album_id=3621348003472015367&scene=189
tags:
  - RAG
  - RAG/retrieval
---
# RAG高级优化：检索后处理模块成竹在胸

本文我们将介绍在将召回片段送入大模型之前的一些优化手段，它们能帮助大模型更好的理解上下文知识

[Read in Cubox](https://cubox.pro/web/card/7250872929913668335)  
[Read Original](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484209&idx=1&sn=0ce7bb6bbb6a0ff5efb4ad10ce2765a7&chksm=c31049c7f467c0d1eae08bc1e7a589b3769d96971ed8149daa55a4e1c6000a0a56b47227aa64&cur_album_id=3621348003472015367&scene=189)  

---


---

## 📖 正文全文

# RAG高级优化：检索后处理模块成竹在胸

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484209&idx=1&sn=0ce7bb6bbb6a0ff5efb4ad10ce2765a7&chksm=c31049c7f467c0d1eae08bc1e7a589b3769d96971ed8149daa55a4e1c6000a0a56b47227aa64&cur_album_id=3621348003472015367&scene=189)哎呀AIYA 哎呀AIYA

通过上文的方法[RAG高级优化：一文看尽query的转换之路](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484174&idx=1&sn=f993d1ac4fe041a857783e2f133789a5&chksm=c31049f8f467c0ee6fac4b4a3402f43649db341c734284932f1385cdfeb6152e00766887468f&scene=21#wechat_redirect)，我们召回了一些相关片段，本文我们将介绍在将召回片段送入大模型之前的一些优化手段，它们能帮助大模型更好的理解上下文知识，给出最佳的回答：

*

  ### Long-text Reorder

*

  ### Contextual compression

*

  ### Refine

*

  ### Emotion Prompt

### **Long-text Reorder**

根据论文 Lost in the Middle: How Language Models Use Long Contexts，的实验表明，大模型更容易记忆开头和结尾的文档，而对中间部分的文档记忆能力不强，因此可以根据召回的文档和query的相关性进行重排序。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2Fr8c4hf2wliaagtl6ELaXbTmdrXTRNXZ5ZBqkJ3XuFciaIaskAeOQTNIYNSyib8G2YrfqV977LL5AicS0juYazjyUaA%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

核心的代码可以参考langchain的实现：

    def _litm_reordering(documents: List[Document]) -> List[Document]:
        """Lost in the middle reorder: the less relevant documents will be at the
        middle of the list and more relevant elements at beginning / end.
        See: https://arxiv.org/abs//2307.03172"""

        documents.reverse()
        reordered_result = \[\]
        for i, value in enumerate(documents):
            if i % 2 == 1:
                reordered_result.append(value)
            else:
                reordered_result.insert(0, value)
        return reordered_result

### **Contextual compression**

本质上利用LLM去判断检索之后的文档和用户query的相关性，只返回相关度最高的k个。

    from langchain.retrievers import ContextualCompressionRetriever
    from langchain.retrievers.document_compressors import LLMChainExtractor
    from langchain_openai import OpenAI

     llm = OpenAI(temperature=0)
    compressor = LLMChainExtractor.from_llm(llm)
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )

     compressed_docs = compression_retriever.get_relevant_documents(
        "What did the president say about Ketanji Jackson Brown"
    )
    print(compressed_docs)

### **Refine**

对最后大模型生成的回答进行进一步的改写，保证回答的准确性。主要涉及提示词工程，参考的提示词如下：

    The original query is as follows: {query_str}
    We have provided an existing answer: {existing_answer}
    We have the opportunity to refine the existing answer (only if needed) with some more context below.
    ------------
    {context_msg}
    ------------
    Given the new context, refine the original answer to better answer the query. If the context isn't useful, return the original answer.
    Refined Answer:

### **Emotion Prompt**

同样是提示词工程的一部分，思路来源于微软的论文：
> Large Language Models Understand and Can Be Enhanced by Emotional Stimuli

在论文中，微软研究员提出，在提示词中增加一些情绪情感相关的提示，有助于大模型输出高质量的回答。

**参考提示词如下：**

    emotion_stimuli_dict = {
        "ep01": "Write your answer and give me a confidence score between 0-1 for your answer. ",
        "ep02": "This is very important to my career. ",
        "ep03": "You'd better be sure.",
        # add more from the paper here!!
    }

     # NOTE: ep06 is the combination of ep01, ep02, ep03
    emotion_stimuli_dict\["ep06"\] = (
        emotion_stimuli_dict\["ep01"\]
        + emotion_stimuli_dict\["ep02"\]
        + emotion_stimuli_dict\["ep03"\]
    )

      from llama_index.prompts import PromptTemplate

      qa_tmpl_str = """\
    Context information is below.
    ---------------------
    {context_str}
    ---------------------
    Given the context information and not prior knowledge, \
    answer the query.
    {emotion_str}
    Query: {query_str}
    Answer: \
    """
    qa_tmpl = PromptTemplate(qa_tmpl_str)

如果对内容有什么疑问和建议可以私信和留言，也可以添加我加入大模型交流群，一起讨论大模型在创作、RAG和agent中的应用。  

好了，这就是我今天想分享的内容。如果你对大模型应用感兴趣，别忘了点赞、关注噢\~


往期推荐


[RAG高级优化：一文看尽query的转换之路](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484174&idx=1&sn=f993d1ac4fe041a857783e2f133789a5&chksm=c31049f8f467c0ee6fac4b4a3402f43649db341c734284932f1385cdfeb6152e00766887468f&scene=21#wechat_redirect)  


[支持大模型流式输出的JSON提取工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483821&idx=1&sn=6f34d91291fbcab03a79142eaa3ed56f&chksm=c3104b5bf467c24d7c4184784831d2cab8ce97f47cfc86d40da172650e67dba9a0860a7411b0&scene=21#wechat_redirect)  


[RAG高级优化：基于问题生成的文档检索增强](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484125&idx=1&sn=0490793590a7061bf0593749f1a58474&chksm=c310482bf467c13dc718c0601c3b2ec0072e8d376cfa0c3b5d0d71406dbfa39bb1b09c684cfc&scene=21#wechat_redirect)  


[一款优秀的开源项目，PDF扫描件识别也超容易](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484167&idx=1&sn=b6dbd57396f03cbfe1dbad2a58424293&chksm=c31049f1f467c0e7f37cf29359bdb4ae8f319ce1ba346bbf5bb6c716c8b533a1f907c79d1673&scene=21#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7250872929913668335)

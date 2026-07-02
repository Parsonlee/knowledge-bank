---
id: "7249427872513786838"
cubox_url: https://cubox.pro/web/card/7249427872513786838
url: https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484125&idx=1&sn=0490793590a7061bf0593749f1a58474&chksm=c310482bf467c13dc718c0601c3b2ec0072e8d376cfa0c3b5d0d71406dbfa39bb1b09c684cfc&scene=21
tags:
  - RAG
  - RAG/query
---
# RAG高级优化：基于问题生成的文档检索增强

本文中介绍一种文本增强技术，该技术利用额外的问题生成来改进矢量数据库中的文档检索。

[Read in Cubox](https://cubox.pro/web/card/7249427872513786838)  
[Read Original](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484125&idx=1&sn=0490793590a7061bf0593749f1a58474&chksm=c310482bf467c13dc718c0601c3b2ec0072e8d376cfa0c3b5d0d71406dbfa39bb1b09c684cfc&scene=21)  

---

## Annotations  

> 通过用相关问题丰富文本片段，我们的目标是显著提高识别文档中包含用户查询答案的最相关部分的准确性。  

[Link️](https://cubox.pro/web/annotations/cards/7249427872513786838?highlight=7249427872559925724)


---

## 📖 正文全文

# RAG高级优化：基于问题生成的文档检索增强

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484125&idx=1&sn=0490793590a7061bf0593749f1a58474&chksm=c310482bf467c13dc718c0601c3b2ec0072e8d376cfa0c3b5d0d71406dbfa39bb1b09c684cfc&scene=21)哎呀AIYA 哎呀AIYA

我们在之前的系列文章介绍了文本切分的一些方法[RAG文本切分的第四个层次，基于向量模型的语义切分](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484106&idx=1&sn=e731d2e0cf52ccdd685eab32dfeaa131&chksm=c310483cf467c12a5d5c85ce3c66ec4d1379bff786ed802fd6c954a8972458021998a4367d8a&scene=21#wechat_redirect)，我们如何能将片段有效召回呢？优化的方案较多，后续将逐步介绍。

我们将在本文中介绍一种文本增强技术，该技术利用额外的问题生成来改进矢量数据库中的文档检索。通过生成和合并与每个文本片段相关的问题，增强系统标准检索过程，从而增加了找到相关文档的可能性，这些文档可以用作生成式问答的上下文。

实现步骤

通过用相关问题丰富文本片段，我们的目标是显著提高识别文档中包含用户查询答案的最相关部分的准确性。具体的方案实现一般包含以下步骤：

*
  **文档解析和文本分块:** 处理PDF文档并将其划分为可管理的文本片段。
*
  **问题增强:**使用语言模型在文档和片段级别生成相关问题。
*
  **矢量存储创建:** 使用[向量模型](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483894&idx=1&sn=be66697008c0b2de60819ccb4beab659&chksm=c3104b00f467c216e934a5d24cc7130efe06c8b1e04055c22c5a38184fbbb0e8bf8e2e67f0e3&scene=21#wechat_redirect)计算文档的嵌入，并创建FAISS矢量存储。
*
  **检索和答案生成:**使用FAISS查找最相关的文档，并根据提供的上下文生成答案。


我们可以通过设置，指定在文档级或片段级进行问题增强。

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

    class QuestionGeneration(Enum):    """    Enum class to specify the level of question generation for document processing.
        Attributes:        DOCUMENT_LEVEL (int): Represents question generation at the entire document level.        FRAGMENT_LEVEL (int): Represents question generation at the individual text fragment level.    """    DOCUMENT_LEVEL = 1    FRAGMENT_LEVEL = 2


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2Fr8c4hf2wliaag2s7dTxI1rIMdvXNibNoATIWDD2bJHSG0WniamaeQUmVZ6oUHicPMuEPu3siaYpIwnoTpl7VS5TX3gA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)


方案实现  

**问题生成**

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
* 
* 
* 
* 
* 
* 
* 
* 
* 

    def generate_questions(text: str) -> List[str]:    """    Generates a list of questions based on the provided text using OpenAI.
        Args:        text (str): The context data from which questions are generated.
        Returns:        List[str]: A list of unique, filtered questions.    """    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)    prompt = PromptTemplate(        input_variables=["context", "num_questions"],        template="Using the context data: {context}\n\nGenerate a list of at least {num_questions} "                 "possible questions that can be asked about this context. Ensure the questions are "                 "directly answerable within the context and do not include any answers or headers. "                 "Separate the questions with a new line character."    )    chain = prompt | llm.with_structured_output(QuestionList)    input_data = {"context": text, "num_questions": QUESTIONS_PER_DOCUMENT}    result = chain.invoke(input_data)        # Extract the list of questions from the QuestionList object    questions = result.question_list        filtered_questions = clean_and_filter_questions(questions)    return list(set(filtered_questions))


**处理主流程**

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
* 

    def process_documents(content: str, embedding_model: OpenAIEmbeddings):    """    Process the document content, split it into fragments, generate questions,    create a FAISS vector store, and return a retriever.
        Args:        content (str): The content of the document to process.        embedding_model (OpenAIEmbeddings): The embedding model to use for vectorization.
        Returns:        VectorStoreRetriever: A retriever for the most relevant FAISS document.    """    # Split the whole text content into text documents    text_documents = split_document(content, DOCUMENT_MAX_TOKENS, DOCUMENT_OVERLAP_TOKENS)    print(f'Text content split into: {len(text_documents)} documents')
        documents = []    counter = 0    for i, text_document in enumerate(text_documents):        text_fragments = split_document(text_document, FRAGMENT_MAX_TOKENS, FRAGMENT_OVERLAP_TOKENS)        print(f'Text document {i} - split into: {len(text_fragments)} fragments')                for j, text_fragment in enumerate(text_fragments):            documents.append(Document(                page_content=text_fragment,                metadata={"type": "ORIGINAL", "index": counter, "text": text_document}            ))            counter += 1                        if QUESTION_GENERATION == QuestionGeneration.FRAGMENT_LEVEL:                questions = generate_questions(text_fragment)                documents.extend([                    Document(page_content=question, metadata={"type": "AUGMENTED", "index": counter + idx, "text": text_document})                    for idx, question in enumerate(questions)                ])                counter += len(questions)                print(f'Text document {i} Text fragment {j} - generated: {len(questions)} questions')                if QUESTION_GENERATION == QuestionGeneration.DOCUMENT_LEVEL:            questions = generate_questions(text_document)            documents.extend([                Document(page_content=question, metadata={"type": "AUGMENTED", "index": counter + idx, "text": text_document})                for idx, question in enumerate(questions)            ])            counter += len(questions)            print(f'Text document {i} - generated: {len(questions)} questions')
        for document in documents:        print_document("Dataset", document)
        print(f'Creating store, calculating embeddings for {len(documents)} FAISS documents')    vectorstore = FAISS.from_documents(documents, embedding_model)
        print("Creating retriever returning the most relevant FAISS document")    return vectorstore.as_retriever(search_kwargs={"k": 1})


该技术为提高基于向量的文档检索系统的信息检索质量提供了一种方法。此实现使用了大模型的API，这可能会根据使用情况产生成本。

如果对内容有什么疑问和建议可以私信和留言，也可以添加我加入大模型交流群，一起讨论大模型在创作、RAG和agent中的应用。

好了，这就是我今天想分享的内容。如果你对大模型应用感兴趣，别忘了点赞、关注噢\~


往期推荐


[RAG文本切分LV3：轻松定制Markdown切分](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484120&idx=1&sn=51fdd215151fe9be2d0ab8290eed6a1e&chksm=c310482ef467c13880ca7633fafbac9bedb57c318a7629ce08d27ea7609baa3e42c7ab70992a&scene=21#wechat_redirect)  


[支持大模型流式输出的JSON提取工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247483821&idx=1&sn=6f34d91291fbcab03a79142eaa3ed56f&chksm=c3104b5bf467c24d7c4184784831d2cab8ce97f47cfc86d40da172650e67dba9a0860a7411b0&scene=21#wechat_redirect)  


[高级 RAG实战：召回更好的片段Query扩展](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484014&idx=1&sn=c50328bcf4e970150d36a0435ba8c72d&chksm=c3104898f467c18e5effdbc5b82ddc12f6bdb3848871a353605f1702c1639c8a7a2327da923e&scene=21#wechat_redirect)

[颠覆传统OCR轻松搞定复杂PDF的工具](http://mp.weixin.qq.com/s?__biz=Mzk0NTcyNTMzNw==&mid=2247484116&idx=1&sn=bcc36c86009e0f4811d6b1e0ed5f6de7&chksm=c3104822f467c13463c036ebdda23b93eb68fc7ed1b6679f2c22297582bd5c7453e230566716&scene=21#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7249427872513786838)

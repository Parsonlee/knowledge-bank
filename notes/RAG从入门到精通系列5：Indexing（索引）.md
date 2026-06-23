# RAG从入门到精通系列5：Indexing（索引）

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495567&idx=1&sn=3c2f6d114a792093f28e8a2b95851de6&chksm=eaecf530dd9b7c26842e80ac68098094bc0f39f911cb8861f32727cea4e858e83bb472189a50&cur_album_id=3689450339863740420&scene=190)南七无名式 PyTorch研习社


LLM（Large Language Model，大型语言模型）是一个功能强大的新平台，但它们并不总是使用与我们的任务相关的数据或者是最新的数据进行训练。

RAG（Retrieval Augmented Generation，检索增强生成）是一种将 LLM 与外部数据源（例如私有数据或最新数据）连接的通用方法。它允许 LLM 使用外部数据来生成其输出。

要想真正掌握 RAG，我们需要学习下图所示的技术（技巧）：

![](https://image.cubox.pro/cardImg/2tofsitxtpibxotyebymmk7f8wvbv1v3xteqnpeld4am58om51?imageMogr2/quality/90/format/gif/ignore-error/1)

我们已经学习了 **Query Translation**《[RAG从入门到精通系列2：Query Translation（查询翻译）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495307&idx=1&sn=fed449f41e11c4ef2fe033b38d3d8dc8&scene=21#wechat_redirect)》、**Routing** 《[RAG从入门到精通系列3：Routing（路由）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495394&idx=1&sn=fe6c0e48aa97c9eded45d996041a88b1&scene=21#wechat_redirect)》和 **Query Construction**《[RAG从入门到精通系列4：Query Construction（查询构造）](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495560&idx=1&sn=7762f8e5842b5cc997875a756365e744&scene=21#wechat_redirect)》。

现在我们又要按照上图的节点顺序回到《[RAG从入门到精通系列1：基础RAG](https://mp.weixin.qq.com/s?__biz=MzI2ODUyMTQyNA==&mid=2247495255&idx=1&sn=562e184d49d101f7be545b412a236e46&scene=21#wechat_redirect)》中介绍过的 **Indexing**（索引）。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu96UsJibpEOeaSTVJGESVOhnzgHHQrTX19HcCBy8SHuwZFm2HeESPaF7lcYsvfEib3lo6dI55agDuVg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

许多 RAG 方法侧重于将文档拆分成多个块，并在检索时返回一定数量的块给 LLM。但块大小和块数量是容易出错的参数，许多用户发现这些参数很难设置，如果它们没有包含足够的上下文来回答问题，都会显著影响结果。


**Multi-representation**


通过结合多种表示（例如，文档的摘要、块或完整内容），来在检索和生成过程中取得最佳效果。它通过使用不同层次和粒度的表示（简洁的摘要与详细的文档）来弥补单一表示可能存在的不足。

**Proposition Indexing** 是 Multi-representation 的一种实现方法：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7Bu96UsJibpEOeaSTVJGESVOhnEsTuIvug7Dul8u2EP9TiaLsGqicIAsxSibcnJ3Cg5WPnhDK4ficficGNdRQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

1. 我们使用 LLM 对原始文本进行总结形成摘要（Summary）；

2. 对摘要进行嵌入处理，保存到 Vector Store 中；同时也将原始文本保存到 Doc Store 中；

3. 检索时，根据用户的 Question 嵌入去 Vector Store 中检索对应的摘要，然后返回原始的文本；

不过这种方法对长上下文的 LLM 来说更加友好。  

首先我们加载两篇博客文章并利用 LLM 进行总结：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicksdGicFRiaZECq0rs7JK5gTAaer3VcIWGFJvtTTUwsjCTPuok4TWiaZwW88fxWdhYpDDswhA35xqOg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

然后我们：

1. 将原始文档存在内存数据中（借助于 InMemoryByteStore）；

2. 将摘要的嵌入向量存储到 vectorstore 中；

3. 原始文档和对应的摘要嵌入向量通过 doc_id 关联。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicksdGicFRiaZECq0rs7JK5gT76A6DHLnU9r1WedG06FVdfhAu9tEiaQzI4tDWkTnJ0XMdAvbicib1dZ6w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

如果我们通过 retriever 执行查询，那我们可以获得摘要及原始文档：  

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicksdGicFRiaZECq0rs7JK5gTU5F1q7iaR2Sgb4PwgqfInqwA6ZdPvicZVibjON0y4qt0HeO7rtTGOsAqw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicksdGicFRiaZECq0rs7JK5gThQWyQcOjaBBaz4ibQhGIIY6RNNic3WPUeYbUtro5exRtZtaN4ORbiaMnA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)


**RAPTOR**


RAPTOR（Recursive Abstractive Processing for Tree-Organized Retrieval）是一种将文档组织成分层结构的索引技术，它能够有效地实现递归式的信息抽象和检索。这种方法以"树"的形式组织文档数据，叶节点代表原始文档或者文档块，树的高层节点则代表这些文档经过抽象后的总结。RAPTOR 的目标是通过分层的方式，提升信息检索的效率，同时能够适应不同粒度的查询需求。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FSaeK9tW7BuicCkF5byH5GDibdC9BYwf0tWDhUgY9UdZCxJBdx9y3ZPzYfK5naqvAIvRsNYib8OeFn993VNE1FaHVg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%26wx_co%3D1&valid=false)

1. **叶节点初始化**

2. 最底层（叶节点）的输入可以是：
   * 文本块（一个文档中的小段落或章节）

   * 完整的文档

   * 甚至是更细粒度的数据单元，如句子或短语。

3. **嵌入与聚类**

   * 生成每个叶节点内容的嵌入向量。

   * 根据文档内容的相似性，将嵌入的结果聚类，例如使用 K-means 或层次聚类算法。

4. **聚类摘要**

   * 对每个聚类中的文档或文本块进行信息整合和总结，生成一个高层的摘要。这一步可以使用 LLM 进行总结。

5. **递归构建树状结构**

   * 将上述生成的高层摘要作为新的输入，重复嵌入、聚类和摘要的步骤。

   * 不断重复这一过程，直到生成顶层的全局摘要。

### **RAPTOR的优点**

* **高效的层次化信息检索**：通过分层组织，用户可以快速定位到感兴趣的层级（从概览到细节）。

* **灵活的扩展性**：可以处理不同粒度的数据（从段落到文档再到更大的集合）。

* **适配 LLM**：尤其是上下文窗口更大的模型（如 GPT-4 或 Claude）可以进一步增强其性能。

假设我们有一组关于"机器学习"领域的论文，目标是帮助用户快速检索相关信息并获取概要。

1. **叶节点：初始论文集合**

   * 数据输入为 100 篇机器学习相关论文。

   * 每篇论文被分成多个块（例如，按标题、摘要、方法、实验和结论划分）。

2. **嵌入与聚类**

   * 使用一个嵌入模型，将论文的各个部分转化为向量。

   * 使用聚类算法（如 K-means）将这些块分为主题类别，例如"神经网络优化"、"强化学习应用"和"机器学习模型解释性"。

3. **摘要生成**

   * 对每个聚类生成一个摘要。例如，对于"神经网络优化"类别，摘要可能是：

     > "该类文档主要探讨了神经网络的超参数优化方法，包括梯度下降的改进、优化器选择和自动化调参工具。"
4. **递归摘要**

   * 将上述摘要作为新的输入，进一步分层聚类并总结，例如，将"神经网络优化"和"强化学习应用"等主题进一步整合为更抽象的总结：

     > "该集合的研究重点是机器学习模型的优化和应用，其中涵盖了神经网络技术、强化学习框架及其在实际问题中的应用探索。"
5. **最终树状结构**

   * 顶层总结可以帮助用户快速了解整个论文集合的主题框架，而底层叶节点保留详细信息供深度查询。

### **实际应用场景**

1. **文档搜索引擎**  
   构建分层索引，帮助用户从概览快速定位到具体内容。

2. **学术研究平台**  
   提供主题概览，同时允许深入阅读相关的论文章节。

3. **企业知识管理系统**  
   在公司内部知识库中，通过 RAPTOR 整理文档，帮助员工快速获取有用的总结和细节。

4. **法律文档处理**  
   针对长篇法律文件或案例库，通过 RAPTOR 分层构建法律条文及其解释的索引。

**建立索引树**

建立索引树的过程利用了**高斯混合模型（GMM）**、**UMAP**降维以及多尺度聚类方法。这些技术协同工作，可以高效地组织和抽象数据，形成树状结构。下面逐步讲解它们在索引树构建中的具体作用：

### **1. 高斯混合模型（Gaussian Mixture Model）**

GMM 是一种基于概率的聚类算法，可以通过拟合多维数据的高斯分布来发现不同类别的聚类中心。

* **建模数据分布**：假设数据点的分布由若干个高斯分布组成，每个高斯分布对应一个聚类。

* **确定最优聚类数**：通过计算模型的**贝叶斯信息准则（Bayesian Information Criterion，BIC）**，可以自动选择适合数据的最佳聚类数量（即高斯分布的数量）。

**在索引树中的应用**：

* 用于将数据（如文档嵌入向量）划分为多个簇，每个簇表示一组相似的文档。

* 簇的中心可以进一步抽象为一个高层节点的摘要。

**例子** ：  
假设输入是 1000 篇技术论文，每篇通过嵌入模型生成向量。

* 使用 GMM 对这些向量进行聚类后，可能分成 5 个主题簇，如"计算机视觉"、"自然语言处理"、"强化学习"等。

* 这些主题作为树的第一层节点。

### **2. UMAP降维**

UMAP（Uniform Manifold Approximation and Projection）是一种流行的降维技术，可以将高维数据嵌入到低维空间，同时保留数据的局部和全局结构。

* **支持聚类**：UMAP 将相似的数据点投影到更接近的位置，从而有利于后续的聚类任务。

* **自然分组**：在低维空间中，数据的自然分组更加明显，便于识别不同的类别或主题。

**在索引树中的应用**：

* 在处理高维嵌入向量时，UMAP 可以先将数据降到低维空间（例如，从 768 维降到 10 维），提高聚类算法的效率和效果。

* 它也可以用来直观地展示数据的分布，帮助理解数据的整体结构。

**例子** ：  
在 1000 篇技术论文的嵌入向量（原始 768 维）上应用 UMAP 降维后，你可能会发现低维空间中的数据点聚集成若干组，这些组在语义上可能分别代表不同的研究领域。

### **3. 多尺度聚类（Local and Global Clustering）**

为了捕获数据的细粒度（局部模式）和粗粒度（全局模式）特性，索引树的构建会结合多尺度聚类方法：

* **局部聚类**：关注更小的聚类单元，捕获细节或精确模式。

* **全局聚类**：关注更大的聚类单元，形成高层的抽象和总结。

**在索引树中的应用**：

* 在树的底层进行局部聚类，对细节（如论文中的章节或段落）进行划分。

* 在高层节点使用全局聚类，整合细节为更广义的主题或总结。

**例子** ：  
论文集合可能首先被分为领域（如"机器学习"与"计算机视觉"），这是全局聚类的结果；然后"机器学习"类别中的内容可以细分为更具体的主题（如"强化学习"与"模型优化"）。

### **4. 阈值处理（Thresholding）**

在使用 GMM 聚类时，数据点的归属是基于概率的，而非确定的。

* **阈值的设置**：通过设定一个概率阈值，判断某个数据点是否属于某个簇。

* **多重归属**：对于某些边界点，可以允许其同时归属到多个簇，以确保信息不丢失。

**在索引树中的应用**：

* 确保模糊或多主题的数据点不会被过早剔除，而是允许它们在不同的主题中共享信息。

* 增强了索引树的灵活性，使其可以适应更复杂的数据分布。

**例子** ：  
某篇论文同时探讨了"自然语言处理"和"计算机视觉"，在 GMM 的聚类概率中，这篇论文可能被分配到这两个主题中，并在索引树中出现在两个分支下。

我加载了三篇 LangChain 文档，每篇文档中的 token 计数如下：

然后我们利用 RAPTOR 方法，将这 3 篇文档组织成一个索引树，由于我们的文档比较少且主题都比较集中，所以我最终只有一个簇群：

我们将这唯一一个簇群对应的摘要和这 3 篇文档一起存到 vector store 中：

然后就可以执行 RAG 管道了：  

我这里因为每篇文档的长度都在 LLM 的上下文窗口长度上限内，所以我的叶子节点就是原始的文档，我也直接对原始文档进行嵌入并存入了 vector store。如果原始文档长度非常大，那么我们可以将原始文档切块，将文档块当作叶子节点：


**ColBERT**


到目前为止，我们所学的各种 RAG 技巧都是基于匹配文档（块）和问题的语义相似度来实现的，更具体地说：我们直接对整篇文档或者文档块与用户问题进行嵌入处理，比较处理之后的嵌入向量之间的相似程度。

但是有人说用户提出的问题可能是各种各样的，如果仅仅将整篇文档或者文档块压缩成一个向量表示，那么这未免太过于笼统了。  

于是便有了有**基于细粒度的 token 级嵌入相似性计算**，即 ColBERT（Contextualized Late Interaction over BERT），看名字就知道它基于 BERT。

以下是具体的步骤和原理：

### 1. **Token 级别相似度计算**

### 2. **最大池化（MaxSim）操作**

### 3. **选择最相关的文档**

### 为什么这种方式有效？

1. **关注细粒度匹配**

   * 通过 token 级别的最大相似度，确保了即使查询中只有部分 token 能与文档匹配，这些匹配也能显著影响最终得分。

2. **兼顾上下文信息**

   * ColBERT 的 token 嵌入是基于上下文生成的，能够捕捉到更丰富的语义信息。

3. **鲁棒性**

   * 不依赖于查询和文档的严格字面匹配，能够处理词法变体、同义词或句子结构的变化。

ColBERT 的开源实现：  

https://github.com/stanford-futuredata/ColBERT

关于具体的代码案例，可以参考：

https://python.langchain.com/docs/integrations/retrievers/ragatouille


**GitHub 链接：**

https://github.com/realyinchen/RAG/blob/main/05_Indexing.ipynb  


[Read in Cubox](https://cubox.pro/web/card/7286698454040970358)

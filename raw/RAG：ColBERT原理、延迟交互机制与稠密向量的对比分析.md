---
id: "7371088986099419215"
cubox_url: https://cubox.pro/web/card/7371088986099419215
url: https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485657&idx=1&sn=30bc94da15598a7373aedf9fc33a02a9&scene=21&poc_token=HJoD1mijgUYBup2PQ7CK-tfueFdYxEMkDLGaRe1_
tags:
  - RAG/embedding
  - RAG
---
# RAG：ColBERT原理、延迟交互机制与稠密向量的对比分析

不知道RAG延迟交互的你，已经落伍了，快快跟上步伐！！

[Read in Cubox](https://cubox.pro/web/card/7371088986099419215)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485657&idx=1&sn=30bc94da15598a7373aedf9fc33a02a9&scene=21&poc_token=HJoD1mijgUYBup2PQ7CK-tfueFdYxEMkDLGaRe1_)  

---


---

\## 📖 正文全文

# RAG：ColBERT原理、延迟交互机制与稠密向量的对比分析

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485657&idx=1&sn=30bc94da15598a7373aedf9fc33a02a9&scene=21&poc_token=HJoD1mijgUYBup2PQ7CK-tfueFdYxEMkDLGaRe1_)筱可 筱可AI


\## 🎯 文章目标

本文面向 **AI 开发者与RAG技术爱好者** ，旨在帮助大家：

*
  理解 ColBERT 的核心原理及其延迟交互机制。
*
  掌握 ColBERT 与稠密向量的差异及其在语义匹配中的优势。
*
  通过实验验证 ColBERT 的计算过程并启发实践应用。

> **💡 小提示**   
> 如果你对 RAG 或语义搜索感兴趣，不妨动手试试文中代码，体验 ColBERT 的细粒度匹配能力！
>
> 本次代码开源地址：https://github.com/li-xiu-qi/XiaokeAILabs/blob/main/datas/colbert/test_colbertv1.py

\## 📄 主题

**本次主题** ：RAG：ColBERT 原理、延迟交互机制与稠密向量的对比分析

\## 📚 摘要

*
  传统稠密向量方法虽简单高效，但在高精度任务中易丢失细节。
*
  ColBERT 通过多向量表示和延迟交互机制提升匹配精度，同时保持实用性。
*
  本文将从原理到实验，剖析 ColBERT 的技术优势及其应用潜力。

*** ** * ** ***

**📋 目录**   

* 🎯 文章目标
* 📄 主题
* 📚 摘要
* 🚁 前言
* 🐱 一、向量表示方法的基础
* 🐶 二、ColBERT 的核心原理
* 🐷 三、延迟交互机制的运作
* 🐻 四、与稠密向量的对比
* 🐼 五、相似性计算的细节
* 🦁 六、实验验证
* 🐯 七、技术优势与应用价值
* 🐰 八、实践建议
* 📒 总结与展望
  * 🚀 技术全景图
  * 📓 学习汇总
  * 🔥 动手挑战
  * ♻️ 互动问题
  * 💗 立即行动
  * 🚗 行动召唤
* 📒 附录

*** ** * ** ***

\## 🚁 前言

传统的文本嵌入方法倾向于将句子压缩为单一向量，这种方式简单高效，但在需要高精度语义匹配时，往往会丢失关键细节。ColBERT（Contextualized Late Interaction over BERT）提出了一种不同的思路：通过多向量表示和延迟交互机制，既保证了精度，又兼顾了实用性。让我们一起探讨它的核心原理、运作方式，以及与稠密向量的差异，最后通过实验验证它的表现。

*** ** * ** ***

✨ 你好，我是筱可，欢迎来到「筱可 AI 研习社」！

🚀 **标签关键词** ：\| AI 实战派开发者 \| 技术成长陪伴者 \| RAG 前沿探索者 \| 文档处理先锋 \|

\## 🐱 一、向量表示方法的基础

在进入 ColBERT 的细节之前，我们先梳理三种常见的向量表示方法：稠密向量、稀疏向量和多向量表示。这将为后续分析奠定基础。

*
  **稠密向量（Dense Vector）** ：

  *
    **定义** ：维度较低（通常几百到上千维）且大多数元素都有非零值的向量。
  *
    **特点** ：信息密集，捕捉语义关系，维度相对较小。
  *
    **生成方式** ：通过神经网络如BERT、RoBERTa等模型，对文本进行编码后获得。典型方法如Sentence-BERT，将整个句子编码为一个固定长度的向量。
  *
    **应用** ：语义搜索、文本分类、聚类等。
*
  **稀疏向量（Sparse Vector）** ：

  *
    **定义** ：维度很高（可达百万级）但绝大多数元素为零的向量。
  *
    **特点** ：明确表示特定词汇的存在，计算高效但维度巨大。
  *
    **生成方式** ：传统方法如TF-IDF、BM25，基于词频和文档频率统计。每个非零元素通常对应一个词的权重。
  *
    **应用** ：关键词搜索、传统信息检索。
*
  **多向量表示（Multi-Vector Representation）** ：

  *
    **定义** ：用一组向量集合（而非单一向量）来表示一段文本。
  *
    **特点** ：保留了文本的细粒度语义信息，能捕捉局部特征。
  *
    **生成方式** ：将文本分解为token，每个token通过上下文感知模型单独编码生成向量。ColBERT就是这类方法的代表。
  *
    **应用** ：高精度信息检索、复杂问答系统。

这三种表示各有优缺点：稠密向量计算效率高但可能丢失细节；稀疏向量直观但不擅长语义匹配；多向量表示精度高但计算复杂度增加。ColBERT的创新之处，就在于它采用了多向量表示并配合延迟交互机制，在保持高精度的同时提供了实用的检索效率。

\## 🐶 二、ColBERT 的核心原理

ColBERT 建立在 BERT 模型之上，但它的设计与众不同。传统方法将句子编码为单一向量，而 ColBERT 为每个 token 生成独立的上下文嵌入向量。为什么要这样做呢？让我们看看它的实现。

*
  **表示形式** ：  
  对于查询 ，我们得到向量集合 （ 是 token 数量）；对于文档 ，则是 （ 是 token 数量）。每个向量的维度通常为 1024，由 BERT 输出经线性变换获得。
*
  **生成过程** ：  
  输入文本通过 BERT 编码，提取每个 token 的上下文表示，再通过线性层调整维度，形成多向量集合。
*
  **实际意义** ：  
  考虑查询"What is BGE?"，单一向量可能因句子整体平均而削弱"BGE"的特征。而 ColBERT 赋予"BGE"独立向量，保留了细粒度信息，非常适合需要局部匹配的任务，如信息检索。

\## 🐷 三、延迟交互机制的运作

ColBERT 的独到之处在于"延迟交互"（Late Interaction）。与其在编码阶段融合所有 token 信息，它选择将交互推迟到相似性计算时。这种设计有何特别之处？我们一步步拆解。

*
  **机制流程** ：
  1.
     分别生成查询 和文档 的 token 向量集合，保持独立性。
  2.
     对每个查询向量 ，在文档向量中寻找最匹配的 ，通过点积 计算相似性。
  3.
     将所有查询 token 的最大匹配得分求和，得到最终得分。
*
  **为何延迟** ：  
  提前融合可能导致语义损失，尤其在长句子中。延迟交互则保留了每个 token 的独立性，直到需要匹配时才进行计算。
*
  **简单示例** ：  
  查询"What is BGE?"与文档"BGE is a model"对比。ColBERT 能直接匹配"BGE"与"BGE"，避免整体平均带来的模糊。换句话说，可以理解成他是匹配局部与局部之间的相关性。

\## 🐻 四、与稠密向量的对比

ColBERT 与稠密向量（如 **Sentence-BERT** ）在表示方式和计算逻辑上有显著差异。我们从三个方面进行比较。

*
  **表示方式** ：
  *
    稠密向量：将句子编码为单一向量 或 ，全局概括语义。
  *
    ColBERT：使用向量集合 和 ，保留 token 级细节。
*
  **相似性计算** ：
  *
    稠密向量：直接计算点积或余弦相似性，时间复杂度为 ，高效简洁。
  *
    ColBERT：采用延迟交互，其中 为归一化向量，复杂度 ，但可通过优化（如矩阵运算）提升效率。
*
  **性能表现** ：  
  稠密向量计算快，但对长句或复杂语义的捕捉能力有限。ColBERT 更精准，尤其在局部匹配上优势明显。

\## 🐼 五、相似性计算的细节

ColBERT 的相似性得分公式为：

*
  **计算步骤** ：
  1.
     对向量进行归一化，，确保点积等价于余弦相似性。
  2.
     构建 的相似性矩阵 。
  3.
     对每行取最大值，求和后除以 ，标准化得分。
*
  **设计意义** ：  
  这种方法既强调最佳匹配，又通过标准化确保得分在不同长度文本间具有可比性。

\## 🦁 六、实验验证

我们使用 **BGEM3FlagModel** 实现 ColBERT，验证其延迟交互机制的效果。

\#\#\## 实验设计

*
  **目标** ：测试相似性计算的正确性及归一化影响，同时比较稠密向量与多向量表示的差异。
*
  **输入** ：查询"What is BGE M3?"（8 个 token），文档"Definition of BM25"（7 个 token）。
*
  **方法** ：计算原始得分、归一化得分，并与官方结果对比，同时计算稠密向量的余弦相似度。

\#\#\## 代码实现

    # 作者: 筱可
    # 日期: 2025 年 3 月 30 日
    # 版权所有 (c) 2025 筱可 & 筱可AI研习社. 保留所有权利.
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.

    from FlagEmbedding import BGEM3FlagModel
    import numpy as np

    model_path = r"C:\Users\k\Desktop\BaiduSyncdisk\baidu_sync_documents\hf_models\bge-m3"

    # 初始化模型
    model = BGEM3FlagModel(model_path, use_fp16=True)

    # 输入数据
    sentences = ["What is BGE M3?", "Defination of BM25"]
    output = model.encode(sentences, return_colbert_vecs=True)

    # 提取向量
    dense_vecs = output['dense_vecs'] 
    print(f"Dense vectors shape: {dense_vecs.shape}") # 形状: (2, 1024)

    dense_vecs1 = output['dense_vecs'][0]  # 第一个句子的向量
    print(f"Dense vectors 1: {dense_vecs1.shape}")

    dense_vecs2 = output['dense_vecs'][1]  # 修正为第二个句子的向量
    print(f"Dense vectors 2: {dense_vecs2.shape}")

    query_vecs = output['colbert_vecs'][0]  # 形状: (8, 1024)
    doc_vecs = output['colbert_vecs'][1]    # 形状: (7, 1024)
    print(f"Query vectors: {query_vecs.shape}")
    print(f"Document vectors: {doc_vecs.shape}")

    # 原始计算
    sim_matrix = np.dot(query_vecs, doc_vecs.T)  # 形状: (8, 7)
    score_raw = sim_matrix.max(axis=1).sum()
    print(f"Similarity score (raw): {score_raw}")

    # 归一化

    # 归一化
    query_vecs_norm = query_vecs / np.linalg.norm(query_vecs, axis=1, keepdims=True)
    doc_vecs_norm = doc_vecs / np.linalg.norm(doc_vecs, axis=1, keepdims=True)
    sim_matrix_correct = np.dot(query_vecs_norm, doc_vecs_norm.T)
    score_correct = sim_matrix_correct.max(axis=1).sum() / len(query_vecs)
    print(f"Similarity score (normalized vectors): {score_correct}")

    # 官方方法
    score_colbert = model.colbert_score(query_vecs, doc_vecs)
    print(f"Similarity score (colbert_score): {score_colbert}")

    # 计算dense_vecs1和dense_vecs2之间的余弦相似度
    cosine_similarity = np.dot(dense_vecs1, dense_vecs2) / (np.linalg.norm(dense_vecs1) * np.linalg.norm(dense_vecs2))

    print(f"Cosine similarity between dense_vecs1 and dense_vecs2: {cosine_similarity}")

输出：

     Dense vectors shape: (2, 1024) 
     Dense vectors 1: (1024,)
     Dense vectors 2: (1024,) 
     Query vectors: (8, 1024) 
     Document vectors: (7, 1024) 
     Similarity score (raw): 3.814497232437134 
     Similarity score (normalized vectors): 0.4768121540546417 
     Similarity score (colbert_score): 0.47681212425231934 
     Cosine similarity between dense_vecs1 and dense_vecs2: 0.41029053926467896

\#\#\## 结果分析

*
  **输出示例** ：

  *
    稠密向量形状: (2, 1024)
  *
    查询多向量形状: (8, 1024)
  *
    文档多向量形状: (7, 1024)
  *
    原始得分: 3.8145
  *
    归一化得分: 0.4768
  *
    官方得分: 0.4768
  *
    稠密向量余弦相似度: 0.4103
*
  **解读** ：

  *
    归一化后得分与官方结果完全一致（0.4768），证实了计算流程的准确性
  *
    原始得分未标准化（3.8145），数值较大且不具可比性
  *
    稠密向量的相似度（0.4103）与 ColBERT 得分存在差异，表明两种表示方法捕捉了不同的语义关系，但我们可以明显看出 ColBERT 的对比稠密向量而言相似度会更高，就是由于它选取的是多个向量里面相似度最大的。
*
  **结论** ：

  1.
     ColBERT 的归一化步骤是关键，确保了得分的可解释性和一致性
  2.
     多向量表示与稠密向量比较，体现了细粒度匹配的特性，能够更准确的匹配相关文档。
  3.
     我们的实验验证了 ColBERT 公式的实际计算过程，符合理论预期

\## 🐯 七、技术优势与应用价值

*
  **精度提升** ：多向量表示和延迟交互机制增强了匹配的细粒度。
*
  **计算优化** ：结合矩阵运算和索引技术（如 Faiss），在大规模数据上仍具高效性。
*
  **应用场景** ：适用于语义搜索、问答系统等需要高精度匹配的任务。

\## 🐰 八、实践建议

*
  在计算相似性时，始终对向量归一化并标准化得分，即 和 。
*
  对于大规模场景，建议使用 GPU 加速或向量数据库进一步提升效率。

> 🙋♂️ 入群交流
>
> *
>   公众号菜单点击「社群」，扫码直接入群
> *
>   回复关键词「入群」，添加作者微信人工邀请

\## 📒 总结与展望

\#\## 🚀 技术全景图

*
  ColBERT 通过多向量表示突破了稠密向量的局限。
*
  延迟交互机制在语义匹配中展现了细粒度优势。
*
  与稠密向量的对比凸显了精度与效率的权衡。

\#\## 📓 学习汇总

*
  掌握了 ColBERT 的核心原理及其数学公式。
*
  通过实验验证了延迟交互的计算流程。
*
  理解了多向量表示在 RAG 等场景中的应用潜力。

*** ** * ** ***

\#\## 🔥 动手挑战

1.
   使用 **BGEM3FlagModel** 对自己的数据集运行 ColBERT，计算相似性得分。
2.
   尝试修改代码，比较原始得分与归一化得分的差异。
3.
   在一个小型语义搜索任务中对比 ColBERT 与稠密向量的效果。

*** ** * ** ***

\#\## ♻️ 互动问题

1.
   你认为 ColBERT 的延迟交互机制在哪些场景下最有优势？
2.
   如果计算资源有限，你会如何优化 ColBERT 的效率？
3.
   在你的项目中，ColBERT 能解决什么具体问题？

> **名言** ：  
> "技术的价值不在于复杂，而在于解决问题的优雅。"  
> ------筱可

**欢迎在留言区分享你的想法，每条留言我都会认真阅读！你的反馈是我创作的最大动力 ❤️**

*** ** * ** ***

\#\## 💗 立即行动

1.
   **点赞、收藏、关注** ，顺手分享给可能感兴趣的朋友。
2.
   为账号加个星标或特别关注，获取更多精彩内容。
3.
   以本文为灵感，整理一份属于自己的笔记。

*** ** * ** ***

\#\## 🚗 行动召唤

📢 "与其等着 AI 改变世界，不如自己参与变革！在这里，让 AI 成为你弯道超车的秘密武器。"

\## 📒 附录

（往期文章）

*
  [RAG系统召回率低？ BGE-M3 多语言多功能重塑文本检索](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485540&idx=1&sn=802c474ae5d3235d93e06c16853adcb5&scene=21\#wechat_redirect)

*
  [RAG系统召回率低？ BGE-M3 多语言多功能重塑文本检索](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485447&idx=1&sn=9f9ffbcc724144b33bbf4153bde8faac&scene=21\#wechat_redirect)

*
  [RAG去重小助手SimHash算法：轻松解决文本相似度检测与查重难题](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485200&idx=1&sn=e60772b90260d137b6153f1f8dba4242&scene=21\#wechat_redirect)

*
  [从模式匹配到语义理解：文本嵌入技术的演变与 RAG 系统优化](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485175&idx=1&sn=c6ef3969ee0fbd31e596a9eaec81c012&scene=21\#wechat_redirect)

*
  [别再瞎猜了！用 RAGAS 精准定位 RAG 系统短板](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247484810&idx=1&sn=8a4180ab552ce9305ab5bbaead771396&scene=21\#wechat_redirect)

*
  [PDF提取神器！将双栏学术论文转换为单栏Markdown实战（上）](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247484676&idx=1&sn=c26acbe2949b7ac70c831db43a5eaf15&scene=21\#wechat_redirect)

*
  [从零打造RAG检索系统：BM25让检索快到飞起](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247484623&idx=1&sn=c99bb87fd834ef7c13c756b4718e60c8&scene=21\#wechat_redirect)

*
  [打造RAG应用必知：BM25算法实战解析，让你不落人后](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247484482&idx=1&sn=3de37212e46f59e473ef9802a5e1c652&scene=21\#wechat_redirect)

*
  [手把手教程：用MinerU构建自动化文档转换流水线](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247484303&idx=1&sn=c4fd5adbbf5b0d82f8e83f1d317ca5d6&scene=21\#wechat_redirect)

*
  [飞桨版面检测分析的命令看不懂？恭喜！您已获得 argparse 入门手册一本，快快学起来吧！](http://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247484108&idx=1&sn=ce17f6fb43254f9746810cfcf626d17d&token=1077873472&lang=zh_CN&scene=21\#wechat_redirect)

*
  [pdf提取逆天神器，基于飞浆平台的版面检测与版面识别(1)](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247484011&idx=1&sn=b2c8bd4c02411c81fa5bc15b8980cb8f&poc_token=HLjbyWejZodqLYpboHlbZrRA4CHGuHDINUv1IA4Z&scene=21\#wechat_redirect)

*
  [大模型应用极简开发快速入门](http://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247483971&idx=1&sn=23077b31b2dc82e790e71f2e1f6458f2&scene=21\#wechat_redirect)

*
  [基于 Streamlit 和 DeepSeek 的智能文档助手开发实战指南](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247483959&idx=1&sn=d673f17e3e14ad7ce53fff238ff42cf9&scene=21\#wechat_redirect)

*
  [告别低效沟通：提示词框架助你玩转deepseek](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247483671&idx=1&sn=356e7fc1eb8b160404b66d9948ba01ff&scene=21\#wechat_redirect)


[Read in Cubox](https://cubox.pro/web/card/7371088986099419215)

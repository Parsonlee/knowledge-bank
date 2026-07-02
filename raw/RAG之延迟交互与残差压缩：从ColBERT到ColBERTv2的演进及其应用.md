---
id: "7371088814812430418"
cubox_url: https://cubox.pro/web/card/7371088814812430418
url: https://mp.weixin.qq.com/s/2-9FqIFxgWM10X9lnora4A
tags:
  - RAG/embedding
  - RAG
---
# RAG之延迟交互与残差压缩：从ColBERT到ColBERTv2的演进及其应用

向量存储空间不够了？残差压缩来了，几乎无损直接压缩至1/4

[Read in Cubox](https://cubox.pro/web/card/7371088814812430418)  
[Read Original](https://mp.weixin.qq.com/s/2-9FqIFxgWM10X9lnora4A)  

---


---

## 📖 正文全文

# RAG之延迟交互与残差压缩：从ColBERT到ColBERTv2的演进及其应用

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/2-9FqIFxgWM10X9lnora4A)筱可 筱可AI


## 🎯 文章目标

本文面向**信息检索领域的开发者与研究者以及RAG爱好者** ，旨在帮助大家：

*
  理解早期交互与延迟交互的区别及其在文本检索中的应用。
*
  掌握ColBERT及其改进版本ColBERTv2的工作机制与优化技术。
*
  学习如何将残差压缩技术（特别是聚类的作用）应用于实际模型（如BGE-M3），实现高效存储与检索。

> **💡 小提示**   
> 本文包含详细代码示例，建议结合实践操作以加深理解！  
> 本次代码开源地址：https://github.com/li-xiu-qi/XiaokeAILabs/blob/main/datas/colbert/test_colbertv2.py  
> 配套Notebook学习地址：https://github.com/li-xiu-qi/XiaokeAILabs/blob/main/datas/colbert/test_colbertv2.ipynb

## 📄 主题

**本次主题** ：RAG之延迟交互与残差压缩：从ColBERT到ColBERTv2的演进及其应用

## 📚 摘要

*
  探讨了早期交互与延迟交互的优劣，以及表示模型与交互模型的典型实现。
*
  详细分析了ColBERT的延迟交互机制及其在检索任务中的高效性。
*
  介绍了ColBERTv2通过残差压缩实现的优化，重点解释聚类在其中的关键作用，并结合BGE-M3模型展示具体应用。

*** ** * ** ***

**📋 目录**   

* 🎯 文章目标
* 📄 主题
* 📚 摘要
* 🚁 前言
* 🐱 一、早期交互与延迟交互的对比
  * 🐷 1.1 早期交互与延迟交互的对比
  * 🐰 1.2 表示模型与交互模型的典型实现
* 🐶 二、ColBERT与ColBERTv2的演进
  * 🐷 2.1 ColBERT：延迟交互的实现机制
  * 🐰 2.2 ColBERTv2：残差压缩的优化
  * 🐱 2.3 BGE-M3模型结合残差压缩的实现
* 📒 总结与展望
  * 🚀 技术全景图
  * 📓 学习汇总
  * 🔥 动手挑战
  * ♻️ 互动问题
* 📒 附录
* 🚀参考资料

*** ** * ** ***

## 🚁 前言

在信息检索和文本匹配领域，效率与准确性的权衡一直是核心研究课题。传统的早期交互方法精度高但计算成本大，表示模型效率高但语义表达有限。近年来，延迟交互技术以ColBERT（Contextualized Late Interaction over BERT）及其改进版本ColBERTv2为代表，提供了一种兼顾两者的解决方案。本文将分析早期交互与延迟交互的区别，表示模型与交互模型的典型实现，ColBERT的工作机制，以及ColBERTv2通过残差压缩（特别是聚类技术）实现的优化。

*** ** * ** ***

## 🐱 一、早期交互与延迟交互的对比

### 🐷 1.1 早期交互与延迟交互的对比

早期交互（Early Interaction）是指在编码阶段即对查询（query）和文档（document）进行深度融合的建模方式。通常，查询和文档的词序列被拼接后输入到Transformer等模型中，通过多层自注意力机制捕捉两者间的语义依赖关系。这种方法生成的表示高度相关，适用于需要高精度的场景。然而，由于每次查询都需要与文档重新计算，计算复杂度为 （其中 和 分别为查询和文档长度），且无法预存文档表示，其效率受限。

延迟交互（Late Interaction）则将交互推迟到编码后的阶段。首先，查询和文档独立通过编码器生成上下文相关的向量表示，随后通过轻量级机制计算相关性。相比早期交互，延迟交互降低了在线计算成本，同时保留了词级语义的细粒度，使其在大规模检索任务中更具实用性。

### 🐰 1.2 表示模型与交互模型的典型实现

表示模型（Representation Models）通过将查询和文档独立编码为固定向量表示，利用简单相似度（如余弦相似度）评估相关性。其优势在于文档表示可预计算并存储于索引中，查询时仅需编码查询部分，时间复杂度为 。一个典型实现是**Sentence-BERT** (SBERT)，基于BERT微调生成句子级别嵌入，广泛应用于语义相似性任务。然而，单一向量表示难以捕捉复杂的词间交互，限制了其精度。

交互模型（Interaction Models）则在编码时对查询和文档进行逐词交互，通常通过拼接输入到模型中，利用深度网络生成相关性得分。其代表性实现是**BERT Cross-Encoder** ，将查询和文档组成单一序列（如"\[CLS\] query \[SEP\] document \[SEP\]"），通过BERT输出分类得分。由于自注意力机制允许全面的词间交互，其精度通常高于表示模型，但计算复杂度高（），且无法预存表示，限制了扩展性。

延迟交互结合了两者的优点，通过独立编码和后期轻量交互实现高效与精准的平衡。

延迟交互结合了两者的优点，通过独立编码和后期轻量交互实现高效与精准的平衡。

## 🐶 二、ColBERT与ColBERTv2的演进

### 🐷 2.1 ColBERT：延迟交互的实现机制

ColBERT由斯坦福大学提出，基于BERT构建，通过延迟交互机制优化文本检索。其工作流程如下：

1.
   **独立编码** ：查询和文档分别通过BERT编码器处理，生成多向量表示 和 ，其中 和 为词数， 为向量维度。每个向量捕捉对应词的上下文信息，文档表示可离线预计算。
2.
   **延迟交互（MaxSim）** ：相关性通过最大相似度操作计算。对于查询的每个向量 ，计算其与文档所有向量 的最大点积，然后求和：
3.
   **高效检索** ：文档向量存储于FAISS索引中，在线检索仅需编码查询并执行MaxSim操作，时间复杂度为 ，远低于交互模型。

ColBERT在精度上接近交叉编码器，也就是大家说熟知的rerank模型，同时将查询延迟从数秒降至几十毫秒，支持大规模文档检索。

### 🐰 2.2 ColBERTv2：残差压缩的优化

ColBERT的多向量表示虽有效，但存储需求较高，尤其在大规模应用中成为瓶颈。ColBERTv2（SIGIR 2021）通过残差压缩技术和训练优化解决了这一问题。

#### 改进动机

ColBERT的多向量表示为每个文档生成数百至数千个向量（依文档长度而定），每个向量通常是高维浮点数（例如，128维的float32类型）。这意味着存储一个文档的表示需要 文档长度 * 维度 * 字节数/浮点数 的空间。例如，一个1000个token的文档，使用128维float32向量，存储空间约为 字节，即0.5MB。对于包含数百万甚至数十亿文档的大规模数据集，存储压力巨大，因此需要改进。

#### 主要改进

1.
   **存储压缩** ：通过残差压缩，存储需求减少6-10倍（例如，从每个文档平均24MB降至2-4MB），性能损失仅1-2%。
2.
   **训练优化** ：引入知识蒸馏和改进的损失函数，提升模型对相关性的建模能力。

> 不过我们这次的实验主要是设计残差压缩的复现，其他的改进我们不会提及太多。

#### 残差压缩的实现

##### 具体步骤

1.
   **向量聚类（找到"地标" - 质心）**

   *
     **利用相似性** ：语言模型生成的向量（比如"cat"在不同上下文中的表示）通常会聚集成簇。聚类找到这些簇，用一个质心代表一群向量，避免逐个存储完整数据。
   *
     **压缩基础** ：残差是向量与质心的差值，没有质心就无法计算残差，压缩无从谈起。
   *
     **检索效率** ：聚类将向量分组，检索时只需检查与查询向量靠近的质心组，而不是扫描所有向量，大幅降低计算量。
   <!-- -->

   *
     比如，一个128维向量集合可能生成256个质心，每个质心代表一组语义相近的向量。
   <!-- -->

   *
     **目的** ：找出向量空间中的代表性点（质心），让每个向量都能找到一个相近的"地标"，减少冗余存储。
   *
     **方法** ：对整个文档库中所有的token向量 （）应用k-means聚类算法，生成 个质心 。
   *
     **为什么需要聚类** ：
   *
     **输出** ：每个向量 被分配到最近的质心 ，索引 用少量字节存储（比如2字节支持65,536个质心）。
2.
   **残差计算（计算与"地标"的偏差）**

   *
     因为聚类确保 和 很接近， 的值通常很小，适合进一步压缩。
   <!-- -->

   *
     **目的** ：记录每个向量与质心的具体差别，作为"精细修正"。
   *
     **方法** ：对于每个向量 ，计算残差 。
   *
     **聚类的作用** ：如果没有聚类，就没有质心作为基准，残差无法定义。聚类让残差保持在一个小范围内，为后续量化奠定基础。
3.
   **残差量化（压缩偏差信息）**

   *
     确定所有残差的范围 和 。
   *
     将每个维度 映射到整数范围（比如8位，0-255）：这里 ，每个维度从4字节float32变成1字节uint8。
   <!-- -->

   *
     **目的** ：将残差压缩成低位数整数，进一步减少存储。
   *
     **方法** ：
   *
     **聚类的意义** ：聚类让残差值集中在小范围内，量化误差可控。如果向量分布太散，残差范围大，8位量化会损失过多精度。
4.
   **存储与重建（存储压缩信息并恢复）**

   *
     反量化残差：。
   *
     重建向量：。
   *
     是原始向量的近似，精度取决于聚类质量和量化位数。
   <!-- -->

   *
     每个向量存储两部分：
   *
     全局存储质心集合 和范围 ，分摊到每个向量成本很低。
   <!-- -->

   *
     质心索引 （2字节）。
   *
     量化残差 （128维×1字节 = 128字节）。
   *
     总共130字节，对比原始512字节（128维×4字节）大幅减少。
   <!-- -->

   *
     **存储** ：
   *
     **重建** ：
   *
     **聚类的关键性** ：没有聚类，就没有质心索引，存储和检索都无法高效进行。

##### 聚类为什么不可或缺？

*
  **通俗比喻** ：想象你在整理一堆照片，每张照片都略有不同。没有聚类，你得存每张完整照片（512字节）。有了聚类，你挑几张"代表照"（质心），每张照片只记"跟哪张代表照接近，差别在哪儿"（索引+残差），再把差别简化成"模糊版"（量化）。聚类就像"分类归档"，没有它，你没法挑代表照，也没法只记差别，压缩和检索都无从下手。
*
  **技术角度** ：
  1.
     **存储节省** ：聚类用质心代替相似向量，残差再量化，整体存储减少6-10倍。
  2.
     **检索效率** ：聚类分组向量，检索时只查相关质心组，计算量从 降到 。
  3.
     **质量保证** ：聚类让残差变小，量化损失可控，重建向量接近原始。

##### 实验示例

以下伪代码展示残差压缩的核心逻辑：

    import numpy as np
    from sklearn.cluster import KMeans

    # 输入：文档向量集合 V，质心数 k，量化位数 b
    def residual_compress(V_all_tokens, k, b):
        # 1. 聚类生成质心
        kmeans_model = KMeans(n_clusters=k, random_state=42).fit(V_all_tokens)
        centroids = kmeans_model.cluster_centers_

        compressed_data_per_doc = []
        all_residuals_for_range_calc = []

        # 第一次遍历：分配质心并计算残差
        for doc_vectors in V:
            assignments = kmeans_model.predict(doc_vectors)
            residuals = doc_vectors - centroids[assignments]
            all_residuals_for_range_calc.append(residuals)
            compressed_data_per_doc.append({'assignments': assignments, 'original_shape': doc_vectors.shape})

        # 确定全局残差范围
        all_residuals_flat = np.vstack(all_residuals_for_range_calc)
        r_min, r_max = np.min(all_residuals_flat), np.max(all_residuals_flat)

        # 第二次遍历：量化残差
        final_compressed_docs = []
        for i, doc_data in enumerate(compressed_data_per_doc):
            doc_vectors = V[i]
            assignments = doc_data['assignments']
            residuals = doc_vectors - centroids[assignments]
            quantized = np.round(
                (residuals - r_min) / (r_max - r_min) * (2**b - 1)
            ).astype(np.uint8 if b == 8 else f'uint{b}')
            final_compressed_docs.append({
                'centroids_idx': assignments.astype(np.uint16 if k > 255 else np.uint8),
                'quantized': quantized
            })

        return centroids, r_min, r_max, final_compressed_docs

    # 重建向量
    def reconstruct(centroids, r_min, r_max, b, compressed_doc_data):
        centroids_idx = compressed_doc_data['centroids_idx']
        quantized = compressed_doc_data['quantized']
        residuals_approx = r_min + (quantized / (2**b - 1)) * (r_max - r_min)
        reconstructed_vectors = centroids[centroids_idx] + residuals_approx
        return reconstructed_vectors

论文里面的实验表明，这种方法将存储需要减少6-10倍，意思是从24MB/文档降到2-4MB，性能损失仅1-2%，非常适合应用落地，所以我们下面也会进行实际的实验测试是否能够达到论文所说的效果。如果能达到这种效果，我觉得也是非常优秀的节省资源的手段了。

### 🐱 2.3 BGE-M3模型结合残差压缩的实现

以下是一个完整实现示例，展示如何将ColBERTv2的残差压缩技术应用于BGE-M3生成的ColBERT向量：


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
    from sklearn.cluster import KMeans
    import pickle
    import os

    # 初始化BGE-M3模型
    # 请确保模型路径正确，如果模型未下载，FlagEmbedding库会自动下载

    model_path = r"C:\Users\k\Desktop\BaiduSyncdisk\baidu_sync_documents\hf_models\bge-m3" # 使用你的本地路径

    # model_path = 'BAAI/bge-m3' # 直接使用Hugging Face模型ID
    try:
        model = BGEM3FlagModel(model_path, use_fp16=True) # 尝试使用FP16以节省内存和加速
    except Exception as e:
        print(f"无法加载模型 {model_path}，请检查路径或网络连接: {e}")
        # 在无法加载模型时退出或采取备用措施
        exit()

    # 示例文档集
    documents = [
        "BGE-M3是一个多语言嵌入模型，支持多种语言的文本检索。",
        "ColBERT是一种延迟交互检索模型，通过最大相似度匹配计算相关性。",
        "BM25是一种经典的词袋模型，基于词频和逆文档频率计算相关性。",
        "向量检索在大规模信息检索任务中越来越受欢迎，替代了传统的倒排索引方法。",
        "残差压缩是一种有效的向量压缩技术，可以大幅减少存储需求。",
        "机器学习模型需要大量数据进行训练，以达到良好的泛化能力。",
        "自然语言处理是人工智能的一个重要分支，专注于计算机与人类语言的交互。",
        "深度学习利用深度神经网络学习数据的复杂模式。"
    ] # 增加了文档数量以更好地模拟聚类

    # 生成ColBERT向量
    def generate_colbert_vectors(docs):
        print("正在生成ColBERT向量...")
        all_vectors = []
        for doc in docs:
            # BGE-M3的encode方法可以直接处理列表，但这里为了清晰，逐个处理
            try:
                output = model.encode([doc], return_colbert_vecs=True, batch_size=1) # 指定batch_size=1
                # 注意：BGE-M3 返回的 colbert_vecs 可能已经是 list of list of floats，需要转np.array
                doc_vectors_list = output['colbert_vecs'][0] # 提取token级别向量表示 (可能是list)
                doc_vectors_np = np.array(doc_vectors_list, dtype=np.float32) # 转换为numpy数组
                if doc_vectors_np.ndim == 2 and doc_vectors_np.shape[0] > 0: # 确保不是空或维度错误
                     all_vectors.append(doc_vectors_np)
                else:
                     print(f"警告: 文档 '{doc[:30]}...' 生成的向量为空或格式不正确，已跳过。Shape: {doc_vectors_np.shape}")
            except Exception as e:
                print(f"处理文档 '{doc[:30]}...' 时出错: {e}")
                continue # 跳过出错的文档
        print(f"向量生成完毕，共处理 {len(all_vectors)} 个有效文档。")
        return all_vectors

    # 残差压缩实现类
    class ResidualCompressor:
        def __init__(self, n_centroids=256, quantization_bits=8):
            self.n_centroids = n_centroids
            self.bits = quantization_bits
            self.kmeans = None
            self.r_min = None
            self.r_max = None
            # BGE-M3的维度是1024
            self.dimension = 1024 # 显式指定维度或从数据推断

        def fit(self, vectors_list):
            # 将所有文档的token向量合并为训练集
            # 过滤掉空向量列表
            non_empty_vectors_list = [v for v in vectors_list if v.shape[0] > 0]
            if not non_empty_vectors_list:
                 print("错误：没有有效的向量用于训练KMeans。")
                 return self

            try:
                all_vectors = np.vstack(non_empty_vectors_list)
                if all_vectors.shape[0] == 0:
                    print("错误：合并后的向量集为空。")
                    return self
                self.dimension = all_vectors.shape[1] # 更新维度信息
                print(f"训练聚类模型，向量总数: {all_vectors.shape[0]}, 维度: {self.dimension}")

                # 自适应调整聚类中心数量，避免过拟合
                actual_n_centroids = min(self.n_centroids, all_vectors.shape[0])
                if actual_n_centroids < self.n_centroids:
                    print(f"警告: 样本数({all_vectors.shape[0]})小于指定的聚类中心数({self.n_centroids})。")
                    print(f"已将聚类中心数调整为: {actual_n_centroids}")
                    self.n_centroids = actual_n_centroids
                elif actual_n_centroids == 0:
                    print("错误: 没有可用的聚类中心。")
                    return self

                # 执行K-means聚类，学习向量空间的质心分布
                # 增加 n_init 和 max_iter 以提高聚类质量
                self.kmeans = KMeans(n_clusters=self.n_centroids, random_state=42, n_init=10, max_iter=300)
                self.kmeans.fit(all_vectors)

                # 计算所有残差以确定全局范围
                print("计算残差范围...")
                all_residuals = []
                for doc_vectors in non_empty_vectors_list:
                    if doc_vectors.shape[0] > 0:
                        centroids_idx = self.kmeans.predict(doc_vectors)
                        residuals = doc_vectors - self.kmeans.cluster_centers_[centroids_idx]
                        all_residuals.append(residuals)

                if not all_residuals:
                     print("错误：无法计算残差。")
                     return self

                all_residuals_np = np.vstack(all_residuals)
                self.r_min = np.min(all_residuals_np)
                self.r_max = np.max(all_residuals_np)
                print(f"残差范围确定: min={self.r_min:.4f}, max={self.r_max:.4f}")

            except ValueError as ve:
                 print(f"KMeans训练或残差计算中发生数值错误: {ve}")
                 # 可能需要检查输入数据是否有NaN或无穷大值
            except Exception as e:
                 print(f"拟合过程中发生未知错误: {e}")
            return self

        def compress(self, vectors_list):
            if self.kmeans is None or self.r_min is None or self.r_max is None:
                print("错误: 压缩器未训练或训练不完整。请先调用 fit 方法。")
                return None

            compressed_docs = []
            total_original_size = 0
            total_compressed_size = 0

            # 确定索引和量化值的numpy类型以精确计算大小
            index_dtype = np.uint16 if self.n_centroids > 255 else np.uint8
            quantized_dtype = np.uint8 # 假设 b=8

            for doc_vectors in vectors_list:
                 if doc_vectors.shape[0] == 0: # 跳过空向量
                      compressed_docs.append(None) # 用None占位或跳过
                      continue

                 # 步骤1: 为每个向量分配最近的质心
                 centroids_idx = self.kmeans.predict(doc_vectors).astype(index_dtype)

                 # 步骤2: 计算向量与质心之间的残差
                 residuals = doc_vectors - self.kmeans.cluster_centers_[centroids_idx]

                 # 步骤3: (范围已在fit中确定)

                 # 步骤4: 将残差量化为指定位数的整数
                 # 防止除零错误
                 if self.r_max == self.r_min:
                     print("警告: 残差范围为零，无法进行量化。")
                     # 可以选择将所有量化值设为0或中间值
                     quantized = np.zeros_like(residuals, dtype=quantized_dtype)
                 else:
                     quantized_float = (residuals - self.r_min) / (self.r_max - self.r_min) * (2**self.bits - 1)
                     # 将值裁剪到[0, 2^b-1]范围内，然后取整
                     quantized = np.round(np.clip(quantized_float, 0, 2**self.bits - 1)).astype(quantized_dtype)

                 # 计算压缩效果
                 original_size = doc_vectors.nbytes
                 # 压缩大小 = 索引大小 + 量化残差大小
                 compressed_size = centroids_idx.nbytes + quantized.nbytes

                 total_original_size += original_size
                 total_compressed_size += compressed_size

                 # 存储压缩结果：质心索引和量化残差
                 compressed_docs.append({
                     'centroids_idx': centroids_idx,
                     'quantized': quantized
                 })

            # 输出压缩统计信息
            if total_compressed_size > 0:
                 compression_ratio = total_original_size / total_compressed_size
                 print(f"原始向量总大小: {total_original_size / 1024:.2f} KB")
                 print(f"压缩后总大小: {total_compressed_size / 1024:.2f} KB")
                 print(f"压缩比: {compression_ratio:.2f}x")
            else:
                 print("没有可压缩的数据。")

            return compressed_docs

        def decompress(self, compressed_docs):
            if self.kmeans is None or self.r_min is None or self.r_max is None:
                print("错误: 压缩器未训练或训练不完整。")
                return None

            decompressed_docs = []
            for doc_data in compressed_docs:
                if doc_data is None: # 处理之前跳过的空文档
                    # 可以返回空数组或特定标记
                    decompressed_docs.append(np.empty((0, self.dimension), dtype=np.float32))
                    continue

                centroids_idx = doc_data['centroids_idx']
                quantized = doc_data['quantized']

                # 步骤1: 反量化残差
                if self.r_max == self.r_min:
                     residuals = np.zeros_like(quantized, dtype=np.float32) # 如果范围为0，则残差为0
                else:
                     residuals = self.r_min + (quantized.astype(np.float32) / (2**self.bits - 1)) * (self.r_max - self.r_min)

                # 步骤2: 重建原始向量 = 质心 + 残差
                # 确保使用正确的质心和类型
                reconstructed = self.kmeans.cluster_centers_[centroids_idx].astype(np.float32) + residuals.astype(np.float32)
                decompressed_docs.append(reconstructed)

            return decompressed_docs

        def save(self, path):
            if self.kmeans is None:
                print("错误: 模型未训练，无法保存。")
                return
            with open(path, 'wb') as f:
                pickle.dump({
                    'kmeans_centers': self.kmeans.cluster_centers_,
                    'r_min': self.r_min,
                    'r_max': self.r_max,
                    'n_centroids': self.n_centroids,
                    'bits': self.bits,
                    'dimension': self.dimension # 保存维度信息
                }, f)
            print(f"压缩器状态已保存到 {path}")

        def load(self, path):
            with open(path, 'rb') as f:
                data = pickle.load(f)
                # 重新构建一个KMeans对象，只设置centers，因为我们不需要再用它来predict或fit
                self.kmeans = KMeans(n_clusters=data['n_centroids'])
                self.kmeans.cluster_centers_ = data['kmeans_centers']
                # 初始化一个虚拟的 _n_threads 属性 (部分sklearn版本需要)
                # setattr(self.kmeans, '_n_threads', 1) # 或者根据需要设置
                self.r_min = data['r_min']
                self.r_max = data['r_max']
                self.n_centroids = data['n_centroids']
                self.bits = data['bits']
                self.dimension = data.get('dimension', 1024) # 向后兼容，如果旧模型没存维度，则默认1024
            print(f"压缩器状态已从 {path} 加载")
            return self

    # --- 主流程 ---
    colbert_vectors = generate_colbert_vectors(documents)

    if not colbert_vectors:
        print("未能生成任何有效的ColBERT向量，程序终止。")
        exit()

    # 计算原始向量占用空间
    original_size = sum([doc_vecs.nbytes for doc_vecs in colbert_vectors if doc_vecs.shape[0]>0])
    print(f"原始未压缩向量总大小: {original_size / 1024:.2f} KB")

    # 应用残差压缩 (使用更多质心以获得更好的效果，但受限于样本数量)
    # n_centroids 设为 64 或 128 可能是个更实际的起点
    compressor = ResidualCompressor(n_centroids=64, quantization_bits=8)
    compressor.fit(colbert_vectors)

    # 检查压缩器是否成功训练
    if compressor.kmeans is not None:
        compressed_vectors_data = compressor.compress(colbert_vectors)

        if compressed_vectors_data:
            # 重建向量并评估压缩质量
            decompressed_vectors = compressor.decompress(compressed_vectors_data)

            # 计算均方误差评估重建质量 (只对非空向量计算)
            mse_list = []
            valid_indices = [i for i, v in enumerate(colbert_vectors) if v.shape[0] > 0]
            for i in valid_indices:
                orig = colbert_vectors[i]
                recon = decompressed_vectors[i]
                if orig.shape == recon.shape and orig.shape[0] > 0: # 确保形状匹配且非空
                    mse = np.mean((orig - recon) ** 2)
                    mse_list.append(mse)
                else:
                     print(f"警告: 文档 {i} 的原始和重建向量形状不匹配或为空，跳过MSE计算。")

            if mse_list:
                avg_mse = np.mean(mse_list)
                print(f"平均重建均方误差 (MSE): {avg_mse:.6f}")
            else:
                print("无法计算平均重建均方误差。")

            # 评估重建前后的相似度排序一致性 (只对有效向量操作)
            def compute_similarity(query_vec, doc_vec):
                """计算标准化后的ColBERT相似度得分 (MaxSim)"""
                if query_vec.shape[0] == 0 or doc_vec.shape[0] == 0: return 0.0 # 处理空向量
                # 归一化每个token向量
                query_vec_norm = query_vec / (np.linalg.norm(query_vec, axis=1, keepdims=True) + 1e-8) # 加epsilon防除零
                doc_vec_norm = doc_vec / (np.linalg.norm(doc_vec, axis=1, keepdims=True) + 1e-8)
                # 计算每个查询token与所有文档token的最大相似度
                sim_matrix = np.dot(query_vec_norm, doc_vec_norm.T)
                max_sim_per_query_token = sim_matrix.max(axis=1)
                # 求和并平均 (ColBERT原始得分)
                return max_sim_per_query_token.sum()

            # 以第一个有效文档作为查询示例
            query_index = valid_indices[0] if valid_indices else -1
            if query_index != -1:
                 query_vec_orig = colbert_vectors[query_index]
                 query_vec_recon = decompressed_vectors[query_index] # 重建后的查询向量

                 print("\n比较查询与各文档的相似度得分 (使用原始查询向量):")
                 original_scores = []
                 reconstructed_scores = []
                 for i in valid_indices: # 只和有效文档比较
                     orig_score = compute_similarity(query_vec_orig, colbert_vectors[i])
                     recon_score = compute_similarity(query_vec_orig, decompressed_vectors[i]) # 查询是原始的，文档是重建的
                     original_scores.append(orig_score)
                     reconstructed_scores.append(recon_score)

                     rel_diff = abs(orig_score - recon_score) / (abs(orig_score) + 1e-9) * 100 # 加epsilon防除零
                     print(f"文档 {i+1} - 原始得分: {orig_score:.4f}, 重建文档得分: {recon_score:.4f}, 相对差异: {rel_diff:.2f}%")

                 # 还可以比较使用重建查询向量的情况，但这通常不是典型用法
                 # recon_query_scores = [compute_similarity(query_vec_recon, dv) for dv in decompressed_vectors]

                 # 序列化压缩模型以便在推理阶段使用
                 compressor.save('colbert_compressor_bge_m3.pkl')
                 print("\n压缩模型已保存，可用于生产环境")
            else:
                print("没有有效的查询向量用于相似度评估。")
        else:
            print("压缩过程未能生成有效数据。")
    else:
        print("压缩器训练失败，后续步骤已跳过。")

#### 执行结果分析

    向量生成完毕，共处理 8 个有效文档。
    原始未压缩向量总大小: 636.00 KB
    训练聚类模型，向量总数: 159, 维度: 1024
    计算残差范围...
    残差范围确定: min=-0.0556, max=0.0574
    原始向量总大小: 636.00 KB
    压缩后总大小: 159.16 KB
    压缩比: 4.00x
    平均重建均方误差 (MSE): 0.000000

    比较查询与各文档的相似度得分 (使用原始查询向量):
    文档 1 - 原始得分: 21.0000, 重建文档得分: 20.9998, 相对差异: 0.00%
    文档 2 - 原始得分: 10.2095, 重建文档得分: 10.2084, 相对差异: 0.01%
    文档 3 - 原始得分: 11.5252, 重建文档得分: 11.5264, 相对差异: 0.01%
    文档 4 - 原始得分: 9.4877, 重建文档得分: 9.4883, 相对差异: 0.01%
    文档 5 - 原始得分: 8.4318, 重建文档得分: 8.4333, 相对差异: 0.02%
    文档 6 - 原始得分: 9.4252, 重建文档得分: 9.4252, 相对差异: 0.00%
    文档 7 - 原始得分: 8.8020, 重建文档得分: 8.8011, 相对差异: 0.01%
    文档 8 - 原始得分: 8.1582, 重建文档得分: 8.1580, 相对差异: 0.00%
    压缩器状态已保存到 colbert_compressor_bge_m3.pkl
    压缩模型已保存，可用于生产环境

#### 关键结果解读

1.
   **压缩效率** ：对于1024维的BGE-M3向量，实现约4倍压缩比（636KB降到159.16KB）。但是我自己尝试调整b还有聚类的数量，始终都是4倍压缩比，我不太清楚具体原因，感兴趣的同学可以看看如何修复这个问题，让实验结果能够达到论文提到的6-10压缩水平。

2.
   **重建精度** ：平均MSE极小（约0），表明重建向量与原始向量几乎一致。

3.
   **检索质量** ：相似度得分相对差异在0.02%以内，说明压缩对检索排序影响微乎其微,当然了，对于大规模数据的情况下，可能会出现不同的情况，具体的大家可以自己试试，很期待大家的测试反馈哦，感谢🙏。

最后呢，我们通过上面这次实验验证了残差压缩（尤其是聚类）的实用性，显著降低存储成本，同时保持检索性能。

## 📒 总结与展望

### 🚀 技术全景图

*
  **早期交互** ：高精度，计算成本高，适用于小规模高精度任务。
*
  **表示模型** ：高效但语义表达有限，适合快速检索场景。
*
  **延迟交互** ：ColBERTv2通过残差压缩兼顾效率与精度。

### 📓 学习汇总

*
  ColBERT通过MaxSim实现延迟交互，显著提升检索效率。
*
  ColBERTv2引入残差压缩（核心是k-means聚类+残差量化），存储需求降低6-10倍，性能损失仅1-2%。
*
  BGE-M3结合残差压缩的应用展示了技术的可行性。

*** ** * ** ***

### 🔥 动手挑战

1.
   使用更大的文档集（如MS MARCO）测试压缩比和检索性能（Recall@k）。
2.
   调整聚类中心数（n_centroids）和量化位数（quantization_bits），观察对压缩比和MSE的影响。
3.
   将压缩技术集成到你的RAG项目，评估端到端性能。

### ♻️ 互动问题

1.
   你认为ColBERTv2在哪些RAG场景下更有优势？
2.
   残差压缩中的量化位数b的作用是什么？
3.
   残差压缩的额外计算开销与存储节省相比是否值得？

## 📒 附录

（往期文章）

*
  [RAG：ColBERT原理、延迟交互机制与稠密向量的对比分析](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485657&idx=1&sn=30bc94da15598a7373aedf9fc33a02a9&scene=21#wechat_redirect)
*
  [RAG背后的数学：向量点积与余弦的秘密](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485540&idx=1&sn=802c474ae5d3235d93e06c16853adcb5&scene=21#wechat_redirect)
*
  [RAG系统召回率低？ BGE-M3 多语言多功能重塑文本检索](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485447&idx=1&sn=9f9ffbcc724144b33bbf4153bde8faac&scene=21#wechat_redirect)
*
  [RAG去重小助手SimHash算法：轻松解决文本相似度检测与查重难题](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485200&idx=1&sn=e60772b90260d137b6153f1f8dba4242&scene=21#wechat_redirect)
*
  [从模式匹配到语义理解：文本嵌入技术的演变与 RAG 系统优化](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485175&idx=1&sn=c6ef3969ee0fbd31e596a9eaec81c012&scene=21#wechat_redirect)
*
  [别再瞎猜了！用 RAGAS 精准定位 RAG 系统短板](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247484810&idx=1&sn=8a4180ab552ce9305ab5bbaead771396&scene=21#wechat_redirect)

## 🚀参考资料

*
  [RAG：ColBERT原理、延迟交互机制与稠密向量的对比分析](https://mp.weixin.qq.com/s?__biz=MzkwNjcxNTc2Ng==&mid=2247485657&idx=1&sn=30bc94da15598a7373aedf9fc33a02a9&scene=21#wechat_redirect)
*
  论文地址：https://arxiv.org/abs/2112.01488
*
  官方代码地址：https://github.com/stanford-futuredata/ColBERT

[Read in Cubox](https://cubox.pro/web/card/7371088814812430418)

---
tags: [vector-database, vector-search, indexing, approximate-nearest-neighbor]
confidence: high
type: concept
summary: 倒排文件索引 (Inverted File Index, IVF) 是一种常用的高维向量近似最近邻搜索 (ANNS) 索引方法。它通过聚类将空间划分为若干分区，使得检索时只需搜索最近质心所在的局部胞腔，从而极大降低计算复杂度并提高检索速度。
created: '2026-08-03'
updated: '2026-08-03'
sources:
- wiki/sources/2025-10-27_ANN-search-using-inverted-file-index_19a274.md
---

# 概念_倒排文件索引_IVF

## 定义
**倒排文件索引（Inverted File Index, IVF）**是一种高维向量的近似最近邻搜索（ANNS）索引技术。其核心思想源于传统信息检索中的“倒排索引”（将文档映射到词项），在向量空间中，它通过聚类算法（如 k-means）将向量数据集划分到不同的空间胞腔（Partitions/Cells）中，并建立“质心 $\to$ 胞腔内向量列表”的倒排映射。

在检索时，它只需计算查询向量与各个胞腔质心的距离，找出最邻近的一个或几个胞腔，然后仅在这些胞腔的倒排列表中进行最近邻搜索，从而避免了全库暴力检索。

## 核心机制与索引构建
IVF 的构建过程主要分为以下几个步骤：
1. **空间划分（Partitioning）**：使用聚类算法（通常是 k-means）将给定的 $N$ 个 $D$ 维向量聚类为 $K$ 个簇（Partitions）。
2. **确定质心（Centroids）**：聚类产生 $K$ 个中心点向量（Centroids），每个数据点基于最近邻原则被归入且仅归入一个中心点所对应的胞腔。
3. **倒排列表映射（Inverted Map）**：构建一个倒排哈希映射表（Map/Inverted List），键（Key）为质心标识，值（Value）为属于该簇的所有向量的 ID 或原始向量。

## 检索算法与复杂度推导
在传统的暴力最近邻搜索（kNN）中，查询向量必须与所有 $N$ 个数据点计算距离。若向量维度为 $D$，则其时间复杂度为：
$$\text{Complexity}_{\text{kNN}} = O(ND)$$

IVF 检索是一个**两阶段**的过程：
1. **粗粒度过滤（Coarse Filtering）**：计算查询向量与 $K$ 个质心的距离，找出距离最近的一个（或前 $n_{\text{probe}}$ 个）质心。时间复杂度为：
   $$\text{Complexity}_{\text{Centroids}} = O(KD)$$
2. **细粒度精搜（Fine Search）**：进入最近的质心所指向的胞腔，仅与该胞腔内的向量点计算距离以找出最近邻。假设每个胞腔内的向量分布是均匀的，则每个胞腔平均包含 $N/K$ 个向量。这一阶段的时间复杂度为：
   $$\text{Complexity}_{\text{Partition}} = O\left(\frac{ND}{K}\right)$$

因此，IVF 检索的总时间复杂度为：
$$\text{Complexity}_{\text{IVF}} = O\left(KD + \frac{ND}{K}\right)$$

### 加速性能示例
假设数据集规模 $N = 10\text{M}$（10,000,000 条数据），划分的聚类簇数 $K = 100$：
- **暴力 kNN**：计算量与 **10,000,000** 成正比。
- **IVF 搜索**：计算量与 $100 + \frac{10,000,000}{100} = 100,100$ 成正比。
- **对比结果**：在均布假设下，IVF 相比暴力 kNN 实现了接近 **100 倍**的检索加速（计算量缩减为原来的 $\sim 1\%$）。

## 精度与性能的折中 (Accuracy-Latency Trade-off)
作为近似最近邻搜索（ANN）算法，IVF 在大幅度降低查询延迟的同时，也存在召回精度（Recall）的折中：
- **边界向量遗漏问题**：如果某些最近邻的向量点位于胞腔的边缘，而查询向量落在相邻胞腔中，即使物理上它们非常接近，查询向量也可能被引导至其最近质心的胞腔，从而完全遗漏那些分布在相邻胞腔边缘的真实最近邻向量。
- **权衡参数 ($n_{\text{probe}}$)**：为了缓解上述精度折中，通常会引入检索参数 $n_{\text{probe}}$（即在第一阶段粗筛时检索前 $n_{\text{probe}}$ 个最近的质心胞腔，并在这些胞腔的并集中进行第二阶段精搜）。增大 $n_{\text{probe}}$ 会提高召回率，但也会线性增加计算开销，降低检索速度。

## 关联
- 相关概念：[[概念_向量索引方法]]、[[概念_近似最近邻搜索]]、[[概念_向量数据库]]
- 来源：[[2025-10-27_ANN-search-using-inverted-file-index_19a274]]

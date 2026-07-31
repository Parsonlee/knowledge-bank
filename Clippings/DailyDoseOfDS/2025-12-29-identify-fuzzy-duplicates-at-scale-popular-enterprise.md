---
title: "Identify fuzzy duplicates at scale (popular enterprise problem)"
source: "https://mail.google.com/mail/u/0/#inbox/19b6bfe2074ca987"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-12-29
created: 2026-07-30
description: "探讨在大规模数据集中高效识别模糊重复记录的技术方案，分析朴素两两比较的二次方复杂度瓶颈，并介绍基于规则分桶（Bucketing）减少 98-99% 无效计算的优化策略。"
tags:
  - clippings
---

# 大规模识别模糊重复项（Identify fuzzy duplicates at scale (popular enterprise problem)）

数据重复是许多企业面临的重大难题。

当存在完全相同的重复记录时，Pandas 中的 `df.drop_duplicates()` 方法效果非常好。

![使用 Pandas 删除重复记录](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffae0a6b7-9dfe-48ea-b15a-86ab1fc652b7_1010x308.png)

但如果数据中包含模糊重复项（Fuzzy duplicates）呢？

模糊重复记录并不是彼此的精确副本，但看起来指代同一个实体：

![模糊重复记录示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f6a7d0e-4386-48d4-9247-eab026fecc8d_649x398.png)

例如，记录包含相同的名字、相似的地址以及几乎相同的电话号码。由于 Pandas 的常规方法只能删除完全匹配的记录，因此在此场景下将彻底失效。

那么，我们该如何解决这个问题？

---

### 朴素解决方案（A naive solution）

假设你的数据集有 100 万条记录。一种最直接的方法是对每两条记录进行两两比较（pairwise comparison）：

![比较每对记录](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2b3ed0f-710c-4328-ab10-29a544266d6e_644x492.png)

我们可以为每个字段制定距离度量指标（Distance metric），并生成每对记录的相似度得分。

但这种方法在大规模数据上是完全不可行的。

例如，在一个仅有 100 万条记录的数据集中，两两比较将产生 $10^{12}$ 次比较（$O(n^2)$ 复杂度）。

即使假设计算速度高达每秒 10,000 次比较，这种朴素方法也需要约 3 年时间才能运行完毕。

我们能做得更好吗？

---

### 重复项的技术特性（A special property of duplicates）

如果两条记录是重复项，它们必然具备某种词汇（Lexical）或文本上的重叠。

例如，参考以下数据集：

![数据集示例](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24cd453f-7733-469c-8d22-40b0f69db7cf_1863x847.png)

在这里，将名字“Daniel”与“Philip”或将“Shannon”与“Julia”进行比较毫无意义，因为它们之间不存在任何文本重叠，必然是不同的记录。

然而，朴素两两比较方法依然会尝试对它们进行比较。

我们可以利用重复项的这一特性，聪明地大幅减少总比较次数。

---

### 对重复项进行分桶（Bucketing duplicates）

应用一些规则将数据分割到更小的桶（Buckets）中会大有帮助。

例如，再次考虑上述数据集。规则之一可以是根据名字的前三个字母创建桶。

![基于规则分割数据](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F477867f9-0cdd-4d0a-91cb-29fd452cce7e_792x287.png)

这样，我们仅需比较处于同一桶内的两条记录。如果前三个字母不同，记录将落入不同的桶中，从而完全避免比较。

![基于规则对记录分组](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cdc671d-efea-4898-a2c0-e62b1f80b97b_887x335.png)

对记录进行隔离分桶可以消除约 98% - 99% 本会发生的无效比较。

最后，我们可以在每个桶内部使用朴素比较算法。

![在桶内进行比较](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4779a838-5502-4bb9-aa73-de84fda569da_848x441.png)

事实上，一旦数据完成分桶，你甚至可以结合 LLM 构建驱动的技术方案。

经过优化的方案可以在短短几个小时内运行完毕，而不是花费数年时间。这种方式不仅大幅缩短了运行时间，同时依然保持了出色的去重准确率。

---

### 总结与思考

当然，我们需要对数据进行透彻分析才能得出上述数据切分规则。

成对文本相似度打分（Pairwise context similarity scoring）是许多 NLP 应用（不仅是重复检测，也包括 RAG 等）的核心构建块。许多社区驱动的平台（如 Stack Overflow、Medium、Quora 等）都依赖此类引擎实现相关内容的推荐与去重。

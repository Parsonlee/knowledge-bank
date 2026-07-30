---
title: "How to actually use train, validation, and test sets in ML."
source: "https://mail.google.com/mail/u/0/#inbox/19ce93b00b8a14f0"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-03-13
created: 2026-07-30
description: "详细梳理机器学习中训练集、验证集与测试集的划分准则与防踩坑指南，涵盖 Cross-Validation、Nested CV、时间序列切分及 Group-based 切分。"
tags:
  - clippings
---

# 机器学习中训练集、验证集与测试集的正确使用指南（How to actually use train, validation, and test sets in ML.）

“模型训练集准确率 99%，部署上线却大幅下滑。” 这是无数数据科学家与机器学习工程师踩过的坑。

造成模型高估的核心原因，在于没有正确理解和使用**训练集（Train Set）、验证集（Validation Set）与测试集（Test Set）**，从而引入了隐蔽的数据泄漏（Data Leakage）。

本文将提供一份工业级的完整数据切分与验证实践指南。

![训练集、验证集与测试集的三分法基础示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c3ccca4-7898-4230-98ca-d179cbab203d_1480x688.png)
*图 1：训练集、验证集与测试集的三分法基础示意图*

---

### 一、 验证集泄漏（Validation Leakage）与交叉验证

如果反复根据单一次验证集的表现调整超参数，验证集的信息就会逐渐“泄漏”到模型选择过程中。

![单次验证集划分过拟合风险图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc0b6c54-6721-4b2c-b962-e28d81075176_1480x639.png)
*图 2：单次验证集划分过拟合风险图解*

**解法：K-Fold 交叉验证（Cross-Validation）**
将训练数据平均分为 K 份，轮流选择 1 份作为验证集，其余 K-1 份作为训练集，最后计算平均得分。

![K-Fold 交叉验证工作流程图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd867fc1-4a0c-4266-bef1-90d9d20c4345_1368x700.png)
*图 3：K-Fold 交叉验证工作流程图*

![K-Fold 交叉验证的四大核心优势分析](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7e12644-7a78-4d70-8c5e-d341b894c4a1_1287x662.png)
*图 4：K-Fold 交叉验证的四大核心优势分析*

![嵌套交叉验证（Nested Cross-Validation）双重循环原理](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc7da89f-453b-45cf-a2a1-7eff6431d0cc_1252x654.png)
*图 5：嵌套交叉验证（Nested Cross-Validation）双重循环原理*

对于严谨的超参数搜索，推荐使用**嵌套交叉验证（Nested Cross-Validation）**：外层循环估计泛化误差，内层循环选择最佳超参数。

---

### 二、 测试集的纪律与终极评估

测试集是最终评测模型泛化能力的盲测资产。

![在训练+验证全量数据上重新训练模型示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fac60ac-0392-4686-ba70-30ed3b5c188e_1252x617.png)
*图 6：在训练+验证全量数据上重新训练模型示意图*

黄金法则：
1. **先选最佳超参数，再用全量训练集（Train + Val）重新训练模型**，最后在测试集上评估单次。
2. **绝对不能根据测试集结果回头调整超参数**。

![测试集使用规则的课堂考试类比图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3b83084-7e2e-4a2d-bf17-6af49c2895bb_1024x529.png)
*图 7：测试集使用规则的课堂考试类比图解*

---

### 三、 复杂场景下的特殊切分策略

针对特定结构的数据，随机切分会导致严重的数据泄漏：

1. **时间序列数据（Time-Series Data）**：
   - 随机切分会导致未来信息泄漏给过去。
   - **解法**：采用时序前向展开验证（Walk-forward validation）。

![时序数据随机切分导致信息泄漏 vs 按时间切分对比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F881d826e-9bed-4388-b4fb-e8bead1e3d99_1024x526.png)
*图 8：时序数据随机切分导致信息泄漏 vs 按时间切分对比*

2. **类别不平衡数据**：
   - 随机切分可能导致测试集中极少或没有正样本。
   - **解法**：使用分层切分（Stratified Splits），保证各子集中类别比例一致。

![分层切分（Stratified Split）保持类别比例一致示意图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd529e17d-b0d1-450f-92d3-89971fb3bf28_2160x912.png)
*图 9：分层切分（Stratified Split）保持类别比例一致示意图*

3. **数据预处理与特征工程泄漏**：
   - **错误做法**：在切分数据前对全量数据执行 `StandardScaler.fit()` 或缺失值填充。

![预处理特征工程在全量数据上 fit 导致严重数据泄漏图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b2ccc8d-d9ba-4cbe-8902-0c770ba765bc_2336x832.png)
*图 10：预处理特征工程在全量数据上 fit 导致严重数据泄漏图解*

   - **正确做法**：仅在训练集上 `fit()`，然后在验证集和测试集上执行 `transform()`。

![特征预处理仅在训练集 fit，对验证测试集 transform 正确流程](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F840ce966-ef05-488d-b3a8-f73b13a25311_3000x928.png)
*图 11：特征预处理仅在训练集 fit，对验证测试集 transform 正确流程*

4. **分组数据（Group-based Splits）**：
   - 若来自同一患者或同一用户的多条数据分布在训练和测试集中，模型会记忆特征而非学习通用规律。
   - **解法**：使用 `GroupKFold` 确保组别不跨界。

![基于 GroupKFold 防止同一实体数据跨界泄漏图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61487dcb-ffd9-4d2c-94e9-0ff43cdf021f_1022x507.png)
*图 12：基于 GroupKFold 防止同一实体数据跨界泄漏图解*

严守上述数据集划分纪律，是保证机器学习模型在生产落地中维持稳定预测表现的关键保障。

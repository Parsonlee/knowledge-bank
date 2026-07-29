title: 数据科学与机器学习必须掌握的 11 种核心图表 source: https://mail.google.com/mail/u/0/#inbox/19f29f70428b228f author:


* "[[DailyDoseOfDS]]" published: 2026-07-03 created: 2026-07-28 description: 总结数据科学与机器学习实践中最关键的 11 种评估与可视化图表（KS Plot、SHAP Plot、ROC、PR Curve、QQ Plot、Elbow Curve 等）及其应用场景。 tags:
* clippings


________________


数据科学与机器学习必须掌握的 11 种核心图表
在数据探索、模型评估与可解释性分析中，以下 11 种图表是数据科学家与 ML 工程师的必备工具：


1. KS Plot（柯尔莫哥洛夫-斯米尔诺夫图）：评估两组分布的累积分布函数（CDF）最大距离，常用于风控与分布检验。
2. SHAP Plot：基于博弈论归因总结特征对模型预测的贡献度与依赖关系。
3. ROC Curve：在不同分类阈值下评估 True Positive Rate 与 False Positive Rate 的权衡。
4. Precision-Recall Curve：在不平衡数据集下评估精确率与召回率的 Tradeoff。
5. QQ Plot（分位数图）：对比观测数据与理论分布的分位数，检验正态性假设。
6. Cumulative Explained Variance Plot：在 PCA 降维时决定保留多少主成分以维持最大方差。
7. Elbow Curve（肘部图）：通过 畸变程度/SSE 拐点寻找 K-Means 最佳聚类数 $K$。
8. Silhouette Curve（轮廓图）：聚类簇较多时比 Elbow 曲线更精准地评估聚类分离度。
9. Gini-Impurity & Entropy Plot：评估决策树节点分裂时的不纯度下降。
10. Bias-Variance Tradeoff：寻找模型复杂度与偏差-方差之间的最佳平衡点。
11. Partial Dependency Plots (PDP)：展示一维或二维特征对模型预测目标的边缘效应。
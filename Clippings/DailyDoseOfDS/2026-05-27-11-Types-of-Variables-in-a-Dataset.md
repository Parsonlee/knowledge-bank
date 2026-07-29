title: 数据集中的 11 种变量类型详解 source: https://mail.google.com/mail/u/0/#inbox/19e6b1b1a122a14a author:


* "[[DailyDoseOfDS]]" published: 2026-05-27 created: 2026-07-28 description: 系统梳理表格数据集中除特征与目标之外的 11 种重要变量类型（如混淆变量、控制变量、隐变量、滞后变量与信息泄漏变量等）。 tags:
* clippings


________________


数据集中的 11 种变量类型详解
在机器学习与统计建模中，简单将列分为“特征”与“目标”远远不够。以下是 11 种关键变量类型：


1. 自变量与因变量（Independent & Dependent）：输入与预测目标。
2. 混淆变量与相关变量（Confounding & Correlated）：同时影响自变量与因变量的第三方因素（如温度同时影响冰淇淋与空调销量）。
3. 控制变量（Control Variables）：在因果推断中被显式固定或调整以消除偏置的变量。
4. 隐变量（Latent Variables）：无法直接观测但可从其他特征推断的内在状态（如聚类类别）。
5. 交互变量（Interaction Variables）：两个或多个特征组合相乘产生的交叉效应。
6. 平稳与非平稳变量（Stationary & Non-stationary）：统计特性（均值、方差）随时间变化（如股票价格）的变量，通常需转为相对变化率使用。
7. 滞后变量（Lagged Variables）：过去时间点的值（如上周销量）。
8. 信息泄漏变量（Leaky Variables）：包含了预测时无法获取的未来信息，会导致训练表现虚高。
---
type: "concept"
tags: ["Skill/data-analysis", "Skill/python"]
summary: "基于 Shapley Additive exPlanations 理论的模型解释方法，通过计算各特征对单个样本及全样本预测结果的归因贡献度（SHAP Value），打通复杂机器学习模型的可视化分析。"
sources: ["wiki/sources/XGBoost_SHAP一键生成10张出版级模型解释图.md"]
updated: "2026-07-22"
---

# 概念：SHAP 模型可解释性

## 定义与背景
SHAP（SHapley Additive exPlanations）是一种基于合作博弈论中 Shapley 值的后置模型解释框架。针对如 [[entities/实体_XGBoost]]、随机森林等高精度但强“黑盒”的复杂模型，SHAP 能够将模型的预测输出分解为各个输入特征的加性贡献值之和。

## 核心计算公式
对于每个样本 $x$ 与预测模型 $f$，SHAP 将预测值 $f(x)$ 表示为基准期望值 $E[f(x)]$ 与各特征归因值（SHAP Value） $\phi_i$ 的和：
$$f(x) = E[f(x)] + \sum_{i=1}^{M} \phi_i$$

## 主要可视化图表类型
在实际分析与科研报告中，基于 SHAP 可自动生成以下多维度图形：
1. **小提琴图 (Violin Plot)**：展示特征值的相对高低及其对应 SHAP 值的全样本分布密度。
2. **瀑布图 (Waterfall Plot)**：拆解单一特定样本从基准期望值 $E[f(x)]$ 逐步累加/减各特征贡献最终推导得到预测值 $f(x)$ 的全路径。
3. **热力图 (Heatmap)**：横轴按全样本或随机样本排列，纵轴按特征重要性降序，使用红蓝渐变直观对比特征的正负贡献分布。
4. **依赖图 (Dependence Plot)**：绘制特定特征取值与对应 SHAP 值的散点关系，展现非线性交互效应。
5. **蜂群图 (Beeswarm)** 与 **条形图 (Bar Plot)**：以全样本平均绝对 SHAP 值（$\operatorname{Mean}(|\text{SHAP}|)$）对特征重要性进行整体降序评估。

## 关联实体
- [[entities/实体_SHAP]]
- [[entities/实体_XGBoost]]
- [[entities/实体_Matplotlib]]

## 来源
- [[XGBoost_SHAP一键生成10张出版级模型解释图]]

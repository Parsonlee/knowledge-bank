---
type: "entity"
tags: ["Skill/python", "Skill/data-analysis"]
summary: "基于梯度提升决策树（GBDT）的高性能开源算法框架，在数据科学竞赛和工业界建模中广泛应用。"
sources: ["wiki/sources/XGBoost_SHAP一键生成10张出版级模型解释图.md"]
updated: "2026-07-22"
---

# 实体：XGBoost

## 基本信息
- **类别**：开源机器学习框架 / 梯度提升树
- **主要用途**：表格数据分类、回归、排序任务

## 核心特征与应用
1. **高性能与正则化**：相比传统 GBDT，XGBoost 在目标函数中显式加入 L1/L2 正则项控制模型复杂度，兼顾拟合精度与防止过拟合。
2. **黑盒可解释性需求**：在实际业务与学术论文中，XGBoost 模型常配合 [[entities/实体_SHAP]] 解释库计算特征贡献度（SHAP Value），生成可视化图表以打通模型归因。

## 来源
- [[XGBoost_SHAP一键生成10张出版级模型解释图]]

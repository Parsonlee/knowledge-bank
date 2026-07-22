---
type: "entity"
tags: ["Skill/python", "Skill/data-analysis"]
summary: "基于博弈论 Shapley Additive exPlanations 的 Python 可解释性分析库，为黑盒机器学习模型提供统一的特征归因解释。"
sources: ["wiki/sources/XGBoost_SHAP一键生成10张出版级模型解释图.md"]
updated: "2026-07-22"
---

# 实体：SHAP

## 基本信息
- **全称**：SHapley Additive exPlanations
- **类别**：Python 模型可解释性分析工具包
- **核心理论**：合作博弈论中的 Shapley 值

## 核心功能与可视化
1. **统一归因框架**：计算每个样本中每个特征对预测值与基准值偏差的贡献度（SHAP Value），兼顾全局重要性与局部解释。
2. **丰富图表展现**：包含小提琴图 (Violin Plot)、蜂群图 (Beeswarm)、瀑布图 (Waterfall)、热力图 (Heatmap)、依赖图 (Dependence Plot) 等，用于无缝配合 [[entities/实体_XGBoost]] 等复杂模型输出出版级可视化成果。

## 来源
- [[XGBoost_SHAP一键生成10张出版级模型解释图]]

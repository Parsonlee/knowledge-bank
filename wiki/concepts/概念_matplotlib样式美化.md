---
title: matplotlib 样式美化
type: concept
confidence: high
tags:
  - Skill/data-analysis
---

# 概念：matplotlib 样式美化

## 定义

通过第三方主题库或自定义样式配置，以极少代码量改造 matplotlib 默认的简陋图表外观，使其具备简洁商务风格。

## 核心方法

### 1. 主题设置方式
- **全局设置**：`plt.style.use(主题)` — 一般不建议，影响所有后续绘图
- **局部设置**（推荐）：`with plt.style.context(主题):` 在 `with` 块内局部使用

### 2. dufte 库的设计哲学
- 去除多余的轴线，只保留必要的参考线
- 适用于日常工作中的通用出图需求
- 三个核心 API：
  - `dufte.style` — 主题风格对象
  - `dufte.legend()` — 替代 `plt.legend()`，自动在折线末端标注图例
  - `dufte.show_bar_values()` — 柱状图自动标注 y 值

### 3. 其他美化途径
- matplotlib 内置样式：`plt.style.available` 列出所有内置主题（如 `ggplot`、`seaborn` 等）
- [[概念_Pandas可视化]]：DataFrame.plot 的 kind 参数直接出图
- 中文显示：注册本地字体 `font_manager.FontProperties(fname=...)` + `fontproperties=` 参数

## 来源
- [[一行代码让matplotlib图表变高大上]] — dufte 库介绍及三个 API 用法演示

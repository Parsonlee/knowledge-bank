---
type: source
tags:
  - Skill/data-analysis
summary: 使用 Pandas 的 DataFrame.plot 和 Series.plot 两个核心函数，一行代码实现 25 种可视化，涵盖折线图、条形图、直方图、箱图、面积图、散点图、饼图、hexbin、核密度、andrews_curves、parallel_coordinates、radviz、bootstrap_plot、子图布局及图中嵌入数据表格等，支持 kind 参数 area/bar/barh/box/density/hexbin/hist/kde/line/pie/scatter。
sources:
  - "Cubox/Pandas一行代码绘制25种美图-2023-11-26.md"
created: "2026-06-30"
updated: "2026-06-30"
confidence: high
---

# Pandas 一行代码绘制 25 种美图

## 来源信息

- 标题：Pandas一行代码绘制25种美图
- 作者：pythonic生物人（凹凸数据）
- URL：https://mp.weixin.qq.com/s/By_zRjBhjD07A9S-_pNOow
- 基于全文 ingest（Cubox stub，无高亮）

## 核心内容

Pandas 内置绘图能力，借助两个核心函数 [[概念_Pandas可视化]]——`pandas.DataFrame.plot` 与 `pandas.Series.plot`——大多数图表一行代码即可完成。`kind` 参数支持：`area`/`bar`/`barh`/`box`/`density`/`hexbin`/`hist`/`kde`/`line`/`pie`/`scatter`。

### 25 种图

1. 单组折线图
2. 多组折线图
3. 单组条形图
4. 多组条形图
5. 堆积条形图
6. 水平堆积条形图
7. 直方图
8. 分面直方图
9. 箱图
10. 面积图
11. 堆积面积图
12. 散点图
13. 单组饼图
14. 多组饼图
15. 分面图
16. hexbin 图
17. andrews_curves 图
18. 核密度图（kde）
19. parallel_coordinates 图
20. autocorrelation_plot 图
21. radviz 图
22. bootstrap_plot 图
23. 子图（subplot）
24. 子图任意排列
25. 图中绘制数据表格

### 依赖

- 主要依赖 `pandas.DataFrame.plot` 和 `pandas.Series.plot`
- 部分高级图（andrews_curves、parallel_coordinates、autocorrelation_plot、radviz、bootstrap_plot）来自 `pandas.plotting` 模块

## 关联概念

- [[概念_Pandas可视化]]
- [[概念_Pandas核心操作图解]]

## 关联实体

- [[实体_Pandas]]

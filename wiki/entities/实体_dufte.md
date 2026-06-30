---
title: dufte
type: entity
confidence: high
tags:
  - Skill/data-analysis
---

# 实体：dufte

## 简介

dufte 是一个 Python 库，通过简短代码自动改造 matplotlib 图表的默认样式，使其具备简洁商务风格。名称来自德语"dufte"（意为"很棒的/酷的"）。

## 核心特性

- **设计哲学**：去除多余的轴线，只保留必要的参考线
- **安装方式**：`pip install dufte`
- **三个关键 API**：
  - `dufte.style` — 主题风格对象，配合 `plt.style.context()` 使用
  - `dufte.legend()` — 替代 `plt.legend()`，将图例标注在折线末端
  - `dufte.show_bar_values()` — 自动在柱体上标注 y 值

## 适用场景

- 日常工作中的通用出图需求
- 需要快速出具简洁商务风格图表的场景
- 处于开发初期的库，功能在持续扩展中

## 来源
- [[一行代码让matplotlib图表变高大上]] — 完整功能介绍与代码示例

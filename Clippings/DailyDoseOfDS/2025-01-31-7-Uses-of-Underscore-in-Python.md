---
title: "Python 中下划线的 7 种用法"
source: "https://mail.google.com/mail/u/0/#inbox/194be07e12ab82bc"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-01-31
created: 2026-07-30
description: "介绍 Python 下划线的七种常见用途：获取最近计算结果、忽略循环变量、分隔数字，以及四类命名约定。"
tags:
  - clippings
---

# Python 中下划线的 7 种用法

下划线（`_`）在 Python 中有许多用途。本文介绍其中七种。

## 1. 获取最近一次计算结果

可以用单个下划线 `_` 取得最近一次计算得到的值。邮件指出，这一用法既适用于 `.py` 脚本，也适用于 Jupyter Notebook 等交互式环境。

## 2. 作为循环变量占位符

当循环变量本身不需要使用时，无需特意为它命名，可以用 `_` 作为占位符。

## 3. 作为数字分隔符

声明较大的数字时，数字的位数不易辨认；下划线可以提高可读性。

## 4–7. 在名称声明中使用下划线

下划线也可用于为对象命名，并通过约定或语言机制表达不同含义。

### 4. 单个前导下划线：内部使用

名称前的单个下划线（如 `_internal_value`）通常表示该变量供内部使用。邮件特别说明：在通配符导入（`from file import *`）时，这类名称不会被导入。

### 5. 单个尾随下划线：避开保留关键字

名称末尾的单个下划线（如 `class_`）可用于避免与 Python 保留关键字冲突。

### 6. 双前导下划线：名称改写

双前导下划线会触发名称改写（name mangling），从而避免在类外部直接访问私有变量。

### 7. 双前导和双尾随下划线：魔术方法

双前导、双尾随下划线（如 `__init__`）用于定义魔术方法（magic methods）。邮件提到，这类方法是 Python 对象模型中的特殊方法，并链接了“20 个最常见魔术方法”的指南。

![Python 下划线用法配图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a19924b-1c57-4b50-843c-542ef3fa6816_1456x585.png)

![Python 下划线用法配图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3d2b997-2c28-4fc4-ad39-40c9851a3fd3_1456x571.png)

![Python 下划线用法配图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fc0d05a-7ba9-4dba-b69a-20365950545f_1456x1395.png)

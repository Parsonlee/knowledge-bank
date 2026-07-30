---
title: "20 most common magic methods in Python OOP"
source: "https://mail.google.com/mail/u/0/#inbox/19d838888f466ecf"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-04-12
created: 2026-07-30
description: "全面整理 Python 面向对象编程（OOP）中最常用的 20 个魔法方法（Dunder Methods），按对象初始化、字符串表达、运算符重载、容器操作与上下文管理分类速查。"
tags:
  - clippings
---
# Python OOP 中最常用的 20 个魔法方法速查（20 most common magic methods in Python OOP）

在 Python 面向对象编程（OOP）中，双下划线方法（Double Underscore Methods，常简称为 **Dunder Methods** 或 **Magic Methods**）是实现 Pythonic 代码风味的关键要素。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F331aa904-7b56-4390-bfe1-e7dd337225c2_1084x1186.jpeg)

在绝大多数日常 Python 工程项目中，掌握以下 20 个魔法方法就足以应对绝大部分面向对象设计需求：

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F923b2d47-b894-4f7e-afcc-9be699c2d96d_992x916.gif)

### 20 个常用魔法方法分类汇总

#### 1. 对象初始化与销毁
- `__init__(self, ...)`：示例初始化的常用构造器。
- `__new__(cls, ...)`：对象创建真正的构造器，常用于单例模式或继承不可变类型。
- `__del__(self)`：析构函数，在对象被垃圾回收时触发。

#### 2. 字符串与对象表达
- `__str__(self)`：提供对用户友好的非正式字符串表达（`str(obj)` / `print(obj)`）。
- `__repr__(self)`：提供无歧义、对开发者友好的正式字符串表达（`repr(obj)`）。
- `__format__(self, format_spec)`：自定义对象的格式化输出（如 `f"{obj:...}"`）。

#### 3. 比较运算符重载
- `__eq__(self, other)`：定义 `==` 行为。
- `__lt__(self, other)`：定义 `<` 行为（结合 `@total_ordering` 装饰器）。
- `__hash__(self)`：定义对象的哈希值，使对象可以作为字典的 Key 或 Set 的元素。

#### 4. 算术运算符重载
- `__add__(self, other)`：定义加法 `+`。
- `__sub__(self, other)`：定义减法 `-`。
- `__mul__(self, other)`：定义乘法 `*`。

#### 5. 容器与序列操作
- `__len__(self)`：返回容器长度（`len(obj)`）。
- `__getitem__(self, key)`：支持按索引或 Key 读取（`obj[key]`）。
- `__setitem__(self, key, value)`：支持按索引或 Key 赋值（`obj[key] = val`）。
- `__contains__(self, item)`：支持成员检测运算符（`item in obj`）。
- `__iter__(self)` 与 `__next__(self)`：使对象支持可迭代与迭代器协议（用于 `for` 循环）。

#### 6. 可调用对象与上下文管理
- `__call__(self, ...)`：允许像调用函数一样直接调用对象实例（`obj()`）。
- `__enter__(self)` 与 `__exit__(self, ...)`：定义上下文管理器，支持 `with` 语法。

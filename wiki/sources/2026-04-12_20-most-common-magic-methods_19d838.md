---
type: source
tags:
  - python
  - oop
summary: 本文列举并简要介绍了 Python 面向对象编程（OOP）中 20 个最常用的魔术方法（Dunder 方法），包括对象创建与初始化、表示转换、容器操作、算术与逻辑运算、逻辑比较等。
sources:
  - raw/articles/2026-04-12_20-most-common-magic-methods_19d838.md
updated: '2026-08-04'
---

# Source: 20 most common magic methods

## 来源信息
- **标题**: 20 most common magic methods
- **来源**: Daily Dose of DS (avi@dailydoseofds.com)
- **日期**: 2026-04-12
- **原始物理文件**: [[raw/articles/2026-04-12_20-most-common-magic-methods_19d838.md]]

## 核心要点
- **Dunder 定义**：因首尾带有双下划线（Double Under Score）而被称为 Dunder 方法，用于重载或代理 Python 内置的 OOP 行为。
- **生命周期分配（Lifetime Allocation）**：
  - `__new__`：在对象创建前调用，负责分配内存并返回对象实例。可用于自定义校验或实现单例模式。
  - `__init__`：在内存分配后调用，负责初始化对象实例的属性。
- **对象类型表示与转换**：
  - `__str__`：控制 `print(obj)` 输出的可读格式，解决默认只打印内存地址的不可读问题。
  - `__int__`：定义 `int(obj)` 的整数转换行为。
  - `__len__`：定义 `len(obj)` 返回长度的行为。
  - `__bool__`：定义对象在 `bool(obj)` 或 `if obj:` 布尔上下文中的真值。
- **可调用与容器操作**：
  - `__call__`：使类实例能像函数一样通过 `obj()` 直接调用。
  - `__getitem__` / `__setitem__` / `__delitem__`：代理 `obj[key]` 获取、`obj[key] = value` 赋值及 `del obj[key]` 行为。
  - `__contains__`：用于重载 `item in obj` 成员关系检查。
  - `__iter__`：在 `for x in obj` 迭代时触发。
- **逻辑比较与运算**：
  - 比较方法：`__eq__` (==)、`__ne__` (!=)、`__gt__` (>)、`__lt__` (<)、`__ge__` (>=)、`__le__` (<=)。
  - 算术运算：`__add__` (加法)、`__mul__` (乘法)。
  - 一元与按位运算：`__abs__` (绝对值)、`__neg__` (一元负号 -obj)、`__invert__` (按位取反 ~obj)。
- **Descriptors 联动**：要想精通 Python OOP，必须掌握 Descriptor（描述符）机制。它能基于魔术方法深度规避代码冗余。

## 关键引文
- > "This method (__new__) is invoked before __init__ to allocate memory to an object... Another common usage is to define singleton classes."
- > "Also, if you want to get really good at Python OOP, learn about Python Descriptors. I find them to be massively helpful in reducing work and code redundancy."

---
> 📎 **物理文献**：[[raw/articles/2026-04-12_20-most-common-magic-methods_19d838.md]]

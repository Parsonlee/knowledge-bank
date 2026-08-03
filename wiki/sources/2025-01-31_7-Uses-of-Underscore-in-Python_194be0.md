---
type: source
tags:
  - python
  - python/syntax
summary: 本文介绍了 Python 中下划线（_）的 7 种主要使用场景，包括获取最后计算值、循环占位符、大数字分隔符以及四种用于命名对象的下划线规范（单前导、单后缀、双前导和双前后导）。
sources:
  - raw/articles/2025-01-31_7-Uses-of-Underscore-in-Python_194be0.md
created: '2026-08-03'
updated: '2026-08-03'
confidence: high
---
# 7 Uses of Underscore in Python

## 核心要点

1. **获取最后计算值**：在交互式环境（如 Jupyter Notebook 或 Python REPL）以及脚本中，单下划线 `_` 可用于获取上一次计算出的结果值。
2. **循环占位符**：当不需要在循环体内使用循环变量时，可以使用 `_` 充当临时占位符，从而避免显式声明无用变量。
3. **数字分隔符**：在声明较大的数字时，可以使用下划线作为千分位或任意位置的分隔符（例如 `1_000_000`），从而提高代码的可读性，且不影响其数值大小。
4. **单前导下划线（`_variable`）**：用于声明仅供内部使用的变量或方法。在执行 `from module import *` 时，这类变量不会被导入。
5. **单后缀下划线（`variable_`）**：为了避免与 Python 内置的保留关键字（如 `class`、`def` 等）发生命名冲突，在变量末尾添加单个下划线。
6. **双前导下划线（`__variable`）**：用于触发名称修饰（Name Mangling）。这可以防止在类外部直接访问所谓的私有变量，避免子类中的命名冲突。
7. **双前导与双后缀下划线（`__variable__`）**：用于定义 Python 的“魔术方法”（Magic Methods 或 Dunder Methods，例如 `__init__`、`__str__` 等）。

## 关键引文

> "A single leading underscore is used to declare variables for internal use. Thus, they cannot be imported during wild imports (from file import *)"
> "Double leading underscores are used to invoke name mangling. This way, one can prevent direct access to private variables outside a class"

## 关联

- **相关概念**：由于本篇内容属于 Python 语言的基础语法与命名惯例，为保持知识库简洁，未创建独立的“Python下划线特殊命名与用法”概念页。
- **来源**：[[raw/articles/2025-01-31_7-Uses-of-Underscore-in-Python_194be0.md]]

---
> 📎 **物理文献**：[[raw/articles/2025-01-31_7-Uses-of-Underscore-in-Python_194be0.md]]

---
type: concept
tags:
- Skill/python
summary: Python 魔术方法（Dunder 方法）是实现 Python 对象协议与重载内置行为的核心机制。本文整理分类了 20 种最常用魔术方法，详细解析了
  __new__ 与 __init__ 的本质差异与调用时序，展示了利用 __new__ 实现单例模式，并关联了描述符机制。
sources:
- wiki/sources/2026-04-12_20-most-common-magic-methods_19d838.md
updated: '2026-08-04'
---

# 概念：Python魔术方法

## 定义

**魔术方法（Magic Methods / Dunder Methods）** 是 Python 中以双下划线（Double Underscore）开头和结尾的特殊方法。它们允许自定义类与 Python 的内置操作（如运算符、类型转换、迭代、容器操作等）进行深度无缝集成。

## 20 种常用魔术方法的分类

在日常 OOP 开发中，最常用的 20 种魔术方法可以归纳为以下几类：

### 1. 生命周期分配
- `__new__`：类级别方法，负责分配内存并返回新创建的实例。
- `__init__`：实例级别方法，负责在实例创建后对其属性进行初始化。

### 2. 对象表示与类型转换
- `__str__`：控制 `print(obj)` 或 `str(obj)` 时返回的对用户友好的字符串表示。
- `__int__`：定义 `int(obj)` 强制转换为整数的行为。
- `__len__`：定义 `len(obj)` 获取对象长度或元素个数的行为。
- `__bool__`：定义对象在布尔上下文（如 `if obj:` 或 `bool(obj)`）下的真假值。

### 3. 可调用对象
- `__call__`：使类实例能像普通函数一样被直接调用，例如执行 `obj()`。

### 4. 容器操作与成员关系
- `__getitem__`：定义使用索引或键获取元素，例如 `obj[key]`。
- `__setitem__`：定义为索引或键赋值，例如 `obj[key] = value`。
- `__delitem__`：定义删除索引或键，例如 `del obj[key]`。
- `__contains__`：重载 `in` 运算符以执行数组成员关系检查。
- `__iter__`：在对对象进行迭代循环（如 `for x in obj`）时触发。

### 5. 逻辑比较
- `__eq__`：重载等于操作符 `==`。
- `__ne__`：重载不等于操作符 `!=`。
- `__gt__`：重载大于操作符 `>`。
- `__lt__` / `__le__` / `__ge__`：分别对应小于（`<`）、小于等于（`<=`）、大于等于（`>=`）。

### 6. 算术与一元运算
- `__add__`：重载加法操作符 `+`。
- `__mul__`：重载乘法操作符 `*`。
- `__abs__`：定义 `abs(obj)` 求绝对值行为。
- `__neg__`：重载一元负号操作符 `-obj`。
- `__invert__`：重载按位取反（波浪号）操作符 `~obj`。

---

## `__new__` 与 `__init__` 的深度对比

在 Python 对象的生命周期中，`__new__` 与 `__init__` 具有本质区别：

| 维度 | `__new__` 方法 | `__init__` 方法 |
| :--- | :--- | :--- |
| **方法类型** | 类方法（隐式传入第一个参数为 `cls`） | 实例方法（传入第一个参数为创建好的 `self`） |
| **核心职责** | **负责内存分配**，即创建对象实例的物理存在。 | **负责属性初始化**，即给创建好的对象实例赋初始状态值。 |
| **返回值** | **必须显式返回**一个实例对象（通常通过调用 `super().__new__(cls)`）。如果未返回，则不会触发 `__init__`。 | **不允许有返回值**（隐式返回 `None`）。 |
| **调用时序** | 在 `__init__` 之前触发。 | 在 `__new__` 返回该类实例后自动触发。 |

### 调用时序演示
当执行 `obj = MyClass(args)` 时，底层的运转流程如下：
1. Python 首先执行 `MyClass.__new__(MyClass, args)`。
2. 该方法在堆区申请内存空间并实例化，返回一个实例。
3. Python 判断返回的值是否是该类（或其子类）的实例。如果是，则将其作为 `self` 传入并调用 `obj.__init__(args)` 进行属性绑定。

---

## 代码示例：利用 `__new__` 实现单例（Singleton）模式

单例模式要求一个类在整个生命周期中只能创建一个实例。我们可以利用 `__new__` 拦截实例创建过程来实现该模式：

```python
class Singleton:
    # 用于存储唯一的类实例
    _instance = None

    def __new__(cls, *args, **kwargs):
        # 如果当前实例不存在，则调用父类 object 的 __new__ 分配内存并创建
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        # 返回已分配好内存的唯一实例
        return cls._instance

    def __init__(self, name):
        # 注意：每次 Singleton("xxx") 仍会触发 __init__。若有必要，需在 __init__ 中加上状态校验防范重复初始化。
        self.name = name


# ==================== 测试验证 ====================
if __name__ == "__main__":
    s1 = Singleton("Instance_A")
    s2 = Singleton("Instance_B")

    # 1. 验证两者是否是同一个实例
    print(s1 is s2)  # 输出: True

    # 2. 验证属性变化
    print(s1.name)   # 输出: Instance_B
    print(s2.name)   # 输出: Instance_B
```

---

## 关联与引申

许多高级 Python OOP 特性都依赖特定的魔术方法。例如，描述符（Descriptor）的核心协议方法 `__get__` 和 `__set__` 等就属于特殊的魔术方法，能代理另一个类中属性的生命周期并解决高冗余的校验逻辑。关于描述符的详细信息，请参阅 [[concepts/概念_Python描述符|Python描述符]]。

## 来源与参考
- Sources: [[sources/2026-04-12_20-most-common-magic-methods_19d838|20 most common magic methods]]

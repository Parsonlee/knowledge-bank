---
title: "概念_Python函数式工具"
tags:
  - Skill/python
confidence: high
---

# 概念_Python函数式工具

## 定义

Python 内置和标准库中的函数式编程工具，用于替代显式 for 循环，通常由 C 实现，性能远优于纯 Python 循环。

## 核心工具

### map()

- `map(func, iterable)` → 惰性迭代器
- C 语言实现的内部循环，可比显式 for 快 ~970x
- 适用：对可迭代对象每个元素应用同一函数

### functools.lru_cache

- `@functools.lru_cache(maxsize=128)` 装饰器
- LRU（Least Recently Used）策略缓存函数调用结果
- 相同输入直接返回缓存，避免重复计算
- `maxsize=None` 无限制（耗内存）
- 递归 Fibonacci 提速 57x

### itertools.filterfalse

- `filterfalse(predicate, iterable)` → 保留 predicate 为 False 的元素
- 避免创建中间列表，降低内存使用
- 与 filter 互补：filter 保留 True，filterfalse 保留 False

### Generator 生成器

- `yield` 实现延迟求值（lazy evaluation）
- 按需产出值，不一次性加载全部到内存
- 大数据集场景显著减少内存使用并提升性能

## 设计哲学

- 这些工具优先使用 C 实现的内部循环替代 Python 解释器层面的 for
- 惰性求值避免不必要的内存分配
- 函数式组合可链式使用（`map` + `filter` + `reduce`）

## 来源

- [[加速Python循环的12种方法]]

## 关联

- [[概念_Python循环优化技巧]]

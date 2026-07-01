---
type: source
tags:
- Skill/python
summary: 12 种优化 Python for 循环的方法，提速 1.3x 到 970x。
sources:
- Cubox/加速Python循环的12种方法,最高可以提速900倍-2024-01-03.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
date: 2024-01-03
---
# 加速 Python 循环的 12 种方法

## 来源信息

- **标题**：加速Python循环的12种方法，最高可以提速900倍
- **作者**：Nirmalya Ghosh（Deephub Imba 译）
- **URL**：https://mp.weixin.qq.com/s/LyZtKIVhVvBP8BCKWEYqYw


> 来源：Deephub Imba / AI算法与图像处理，作者 Nirmalya Ghosh
> 测试方法：timeit 模块，10 次运行各 100K 循环，取每循环平均纳秒

## 核心内容

12 种优化 Python for 循环的方法，提速 1.3x 到 970x。

> [重点/高亮]（Cubox 标注）
> - 如果需要依靠列表的长度进行迭代，请在 for 循环之外进行计算。
> - 在使用 for 循环进行比较的情况下使用 set。

### 12 种方法与提速比

| # | 方法 | 提速 | 说明 |
|---|------|------|------|
| 1 | 列表推导式 | 2.00x | `[n**2.5 for n in numbers]` |
| 2 | 外部计算长度 | 1.64x | 把 `len()` 移出 for 循环 |
| 3 | 使用 Set | 498x | `set.intersection()` 替代嵌套查找 |
| 4 | 跳过不相关迭代 | 1.94x | 避免冗余计算 |
| 5 | 代码合并（内联） | 1.35x | 消除函数调用开销 |
| 6 | 避免重复计算 | 1.51x | 预计算（precompute） |
| 7 | 使用 Generators | 22x | 延迟求值，省内存 |
| 8 | map() 函数 | 970x | C 语言实现，内部循环高效 |
| 9 | Memoization | 57x | `functools.lru_cache` 缓存结果 |
| 10 | 向量化 | 28x | `np.sum(np.arange(n))` |
| 11 | 避免中间列表 | 131x | `itertools.filterfalse` |
| 12 | 高效连接字符串 | 1.54x | `"".join()` 替代 `+=` |

### 关键原理

- **map() 970x**：用 C 编写并高度优化，隐含循环比 Python for 高效
- **set 498x**：集合查找 O(1)，嵌套 for 查找 O(n)
- **lru_cache**：LRU = Least Recently Used，装饰器缓存，maxsize 控制缓存大小，None 表示无限增长（耗内存）
- **join 1.5x**：`+` 连接时间复杂度 O(n²)，`join` 为 O(n)
- **内联权衡**：可读性 vs 函数调用频率需平衡

## 关联概念

- [[概念_Python循环优化技巧]]
- [[概念_Python函数式工具]]

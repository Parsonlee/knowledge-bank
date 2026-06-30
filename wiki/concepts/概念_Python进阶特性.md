---
title: "概念_Python进阶特性"
tags:
  - Skill/python
confidence: high
---

# 概念_Python进阶特性

## 定义

Python 标准库中鲜为人知但实用的进阶特性，教程中很少提及，能干净地解决实际工程问题。

## 五大特性

### 1. contextlib.suppress — 优雅忽略异常

```python
from contextlib import suppress
with suppress(FileNotFoundError, PermissionError):
    os.remove('tempfile.txt')
```

- 替代 try/except/pass，意图清晰
- 适用：删文件、关 socket、清理临时资源

### 2. sys.setrecursionlimit — 突破递归限制

- CPython 默认递归限制 1000
- `sys.setrecursionlimit(10**6)` 提升到 100 万
- 注意：每次调用消耗内存，需了解实际栈深度

### 3. typing.Literal — 编译时字符串验证

```python
from typing import Literal
def connect(mode: Literal['read', 'write']): ...
```

- 静态类型检查器在运行前发出警告
- 与 pydantic/FastAPI 配合天衣无缝
- 可与 Union / None 组合

### 4. __missing__ — dict 子类魔法方法

- 键不存在时触发，比 defaultdict 控制更细
- 可记录、转换、设默认值、自动插入
- 大多数开发者不知道其存在

### 5. __subclasshook__ — 结构化类型（鸭子类型）

- ABC + __subclasshook__ 实现接口式行为
- 不强制继承，只检查方法是否存在
- 检查行为而非血统，适合插件/API/框架设计
- `issubclass` 基于方法存在性返回 True

## 设计哲学

- Python 鸭子类型（Duck Typing）：如果它走起来像鸭子，就是鸭子
- 标准库隐藏了大量精巧工具（contextlib / typing / abc）
- 优雅代码优先考虑意图表达而非模板堆砌

## 来源

- [[五个鲜为人知的Python功能]]

## 关联

- [[概念_Python_async_await并发]]
- [[概念_FastAPI项目结构模式]]

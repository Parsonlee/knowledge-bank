---
type: source
tags:
- Skill/python
summary: 5 个教程很少提及但能干净解决实际问题的 Python 功能。
sources:
- raw/写了十年 Python，我竟然现在才知道这5个功能！.md
created: '2026-06-29'
updated: '2026-07-01'
confidence: high
date: 2025-07-31
---
# 五个鲜为人知的 Python 功能

## 来源信息

- **标题**：写了十年 Python，我竟然现在才知道这5个功能！
- **作者**：PyTorch研习社
- **URL**：https://mp.weixin.qq.com/s/YdKuIzRgmXgrz7MDPqSfig


> 来源：微信公众号 AI研究生 / PyTorch研习社

## 核心内容

5 个教程很少提及但能干净解决实际问题的 Python 功能。

### 1. contextlib.suppress：优雅忽略异常

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('tempfile.txt')
```

- 替代 try/except/pass，意图清晰
- 可同时忽略多个异常：`suppress(FileNotFoundError, PermissionError)`
- 适用：删文件/关 socket/清理临时文件/关闭可能不存在的服务

### 2. sys.setrecursionlimit：突破递归限制

```python
import sys
sys.setrecursionlimit(10**6)
```

- CPython 默认递归限制 1000
- 适用：自定义解析器、递归遍历、回溯算法
- 注意：每次调用吃内存，需了解调用栈深度

### 3. typing.Literal：字符串安全的秘密武器

> [重点/高亮]（Cubox 标注）：typing.Literal：字符串安全的秘密武器

```python
from typing import Literal

def connect(mode: Literal['read', 'write']):
    ...
```

- 把运行时验证提前到静态类型检查（mypy/IDE）
- 自带文档，与 pydantic、FastAPI 配合
- 可与 Union 配合：`Literal['json', 'xml'] | None`

### 4. __missing__：dict 子类的魔法方法

```python
class AutoDict(dict):
    def __missing__(self, key):
        value = self[key] = f"[{key} 未找到]"
        return value
```

- 键不存在时触发，比 defaultdict 控制更细
- 可记录、转换、设默认值、自动插入
- 进阶：跟踪未知访问模式后 raise KeyError

### 5. __subclasshook__：结构化类型（鸭子类型）

```python
from abc import ABC, abstractmethod

class JsonSerializable(ABC):
    @abstractmethod
    def to_json(self): pass

    @classmethod
    def __subclasshook__(cls, C):
        if any("to_json" in B.__dict__ for B in C.__mro__):
            return True
        return NotImplemented
```

- 不强制继承，只要实现了指定方法就视为子类
- 检查行为而非血统，适合插件/API/框架
- `issubclass(MyClass, JsonSerializable)` 返回 True（只要有 to_json）

## 关联概念

- [[概念_Python进阶特性]]

---
> 📎 **物理文献**：[[raw/写了十年 Python，我竟然现在才知道这5个功能！.md]]

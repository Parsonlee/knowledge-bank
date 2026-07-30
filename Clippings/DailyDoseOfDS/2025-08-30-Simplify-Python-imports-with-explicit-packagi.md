---
title: "使用显式打包简化 Python 导入"
source: "https://mail.google.com/mail/u/0/#inbox/198fc6ca70584770"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-30
created: 2026-07-30
description: "解释 Python 项目中显式创建 __init__.py 的价值：集中导出公共接口、避免重复导入，并让包的可用内容更加清晰。"
tags:
  - clippings
---

# 使用显式打包简化 Python 导入

Python 可以通过在目录中添加 `__init__.py` 文件将项目打包。尽管 Python 3.3 及更高版本支持隐式命名空间包——包含模块的目录默认可视为包——邮件仍建议显式创建 `__init__.py`。

这样做有两个主要好处：

- 明确指定允许从包导入哪些类或函数；
- 避免重复导入。

## 基本术语

- **模块（module）**：一个 Python 文件。
- **包（package）**：目录中的一组 Python 文件。
- **库（library）**：一组包。

假设一个目录中有 `train.py` 和 `test.py`，其中分别定义 `Training` 和 `Testing`。在 Python 3.3+ 中，`pipeline.py` 可以直接从这两个模块分别导入相应的类；这能工作，但必须逐一写出模块和类，导入会变得重复。

可在该目录创建 `__init__.py`，并把希望暴露的导入集中写入其中：

```python
# model/__init__.py
from .train import Training
from .test import Testing
```

于是调用方可以从 `model` 包直接导入目标类：

```python
from model import Training, Testing
```

换言之，指定 `__init__.py` 后，可以像对待模块一样使用包；同时它也为项目的其他使用者明确了公共导入接口。

## 广告 / 推广

邮件推广 Daily Dose of Data Science 的会员学习资源和广告投放服务；这些内容与 Python 打包主题无直接技术关系。

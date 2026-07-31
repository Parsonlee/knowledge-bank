---
title: "Python 开发者的 uv 速查表与实战指南"
source: "https://mail.google.com/mail/u/0/#inbox/197c7ace7fc9ab0e"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-07-01
created: 2026-07-30
description: "uv 是 Rust 构建的 Python 包管理器，可用单个二进制替代 pip、pip-tools、virtualenv、pipx、Poetry 和 pyenv，并通过锁文件提供可复现环境。"
tags:
  - clippings
---

# Python 开发者的 uv 速查表与实战指南

`uv` 的速度很快：创建虚拟环境约比 `python -m venv` 快 **80 倍**；安装包在无缓存时快 **4–12 倍**，有缓存时约快 **100 倍**。

`uv` 是用 Rust 构建、侧重速度与可靠性的现代 Python 包管理器。它以单个独立二进制替代的不只是 `pip`，还有 `pip-tools`、`virtualenv`、`pipx`、Poetry 和 `pyenv`。

## 快速演示

先安装 `uv`（邮件说明也可用 `wget` 安装）。创建新项目：

```bash
uv init project-name
```

该命令会创建目录结构、`pyproject.toml`、示例脚本和 README。随后进入项目目录：

```bash
cd project-name
```

虽然 `uv` 会在项目中自动初始化虚拟环境，也可以显式创建一个。激活方式为：

- macOS/Linux：`source .venv/bin/activate`
- Windows：`.venv\Scripts\activate`

接着可用 `uv add` 添加依赖。添加包时，`uv` 会更新 `pyproject.toml`、解析完整依赖树并生成 lockfile。

运行脚本时，可以使用 `uv run`。若脚本使用了当前环境中没有的包，但依赖已在 `pyproject.toml` 中声明，`uv` 会在运行时自动安装该包。

对于使用 `uv` 的克隆项目，执行：

```bash
uv sync
```

即可创建与项目精确匹配的本地环境。无论 Windows、macOS 还是 Linux，`uv sync` 都会保证环境一致；若项目需要不同版本的 Python，`uv` 也能自动获取并使用它。

作者团队已将项目全面迁移至 `uv`，原因是它解决了依赖管理问题且具有速度优势；尽管采用率仍较低，但它正在迅速成熟，并建议 Python 开发者尝试迁移。可在[这份 Colab Notebook](https://colab.research.google.com/drive/1o0FJVhYaXPATe6ctgV2cfINhTC_JwxXL?usp=sharing)中跟随分步说明练习。

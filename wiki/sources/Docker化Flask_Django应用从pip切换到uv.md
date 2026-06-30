---
title: "Switching pip to uv in a Dockerized Flask / Django App"
source_url: "https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app"
author: "Nick Janetakis"
date: 2025-06-25
tags:
  - Skill/python
confidence: high
---

# Docker 化 Flask/Django 应用从 pip 切换到 uv

> 来源：Nick Janetakis 博客，2025-06-17 更新

## 核心内容

作者分享了将 Docker 化 Python 项目从 pip 切换到 uv 的完整实践，实测约 10x 速度提升。

### pyproject.toml 替代 requirements.txt

- 只需添加顶层依赖，uv 自动生成 lock 文件
- lock 文件有完整依赖树，远优于 `pip freeze` 输出

### Dockerfile 关键改动

| 步骤 | 配置 |
|------|------|
| 安装 uv | `COPY --from=ghcr.io/astral-sh/uv:0.7.13 /uv /uvx /usr/local/bin/` （静态编译 Rust 二进制） |
| 依赖文件 | `COPY pyproject.toml uv.lock* ./`（`*` 使 lock 文件可选） |
| 环境变量 | `UV_COMPILE_BYTECODE=1`（构建时编译字节码）；`UV_PROJECT_ENVIRONMENT="/home/python/.local"`（跳过 venv） |
| 安装命令 | `uv lock --check` 或 `uv lock` + `uv sync --frozen --no-install-project` |

### 关键 uv 命令

- `uv lock`：生成/更新 lock 文件
- `uv lock --check`：校验 lock 文件是否最新
- `uv sync --frozen`：严格按 lock 文件安装，不更新
- `--no-install-project`：跳过将项目本身安装为包
- `uv add mypackage --no-sync`：添加/更新依赖（不立即安装）
- `uv remove mypackage --no-sync`：移除依赖
- `uv tree --outdated --depth 1`：查看过时依赖

### 最佳实践

- 非 root 用户运行（python 用户）
- 不使用 venv（通过 UV_PROJECT_ENVIRONMENT 指定安装路径）
- 用 shell 脚本封装安装逻辑（bin/uv-install）
- Volume mount 将容器内 lock 文件同步回宿主机

## 关联概念

- [[概念_uv包管理器]]
- [[概念_FastAPI项目结构模式]]

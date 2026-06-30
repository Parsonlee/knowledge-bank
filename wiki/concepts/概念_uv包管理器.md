---
title: "概念_uv包管理器"
tags:
  - Skill/python
confidence: high
---

# 概念_uv包管理器

## 定义

uv 是 Astral 开发的 Rust 编写的 Python 包管理器，作为 pip 的替代品，实测在多个项目中带来约 10x 速度提升。

## 核心特性

- **静态编译 Rust 二进制**：Docker 中直接 `COPY --from=ghcr.io/astral-sh/uv:<ver> /uv /uvx /usr/local/bin/`
- **pyproject.toml + uv.lock**：只声明顶层依赖，自动生成带完整依赖树的 lock 文件（优于 pip freeze）
- **uv sync**：uv 推荐方式（也提供 pip 子命令做心智模型过渡）

## 常用命令

| 命令 | 作用 |
|------|------|
| `uv lock` | 生成/更新 lock 文件 |
| `uv lock --check` | 校验 lock 是否最新 |
| `uv sync --frozen` | 严格按 lock 安装，不更新 |
| `--no-install-project` | 跳过将项目本身装为包（典型 web app 用） |
| `uv add pkg --no-sync` | 添加/更新依赖（不立即安装） |
| `uv remove pkg --no-sync` | 移除依赖 |
| `uv tree --outdated --depth 1` | 查看过时依赖 |

## Docker 实践要点

- `UV_COMPILE_BYTECODE=1`：构建时编译字节码，运行时不再编译
- `UV_PROJECT_ENVIRONMENT`：指定安装路径，跳过 venv
- 非 root 用户运行
- Volume mount 同步 lock 文件回宿主机

## 来源

- [[Docker化Flask_Django应用从pip切换到uv]]

## 关联

- [[概念_FastAPI项目结构模式]]

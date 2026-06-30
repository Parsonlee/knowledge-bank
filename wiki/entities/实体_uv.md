---
title: "实体_uv"
tags:
  - Skill/python
confidence: high
---

# 实体_uv

## 基本信息

- **类型**：Python 包管理器
- **开发商**：Astral（也开发 Ruff）
- **语言**：Rust 编写
- **定位**：pip / pip-tools / pipenv / poetry 的统一替代品
- **GitHub**：https://github.com/astral-sh/uv

## 核心特征

- 相比 pip 约 10x 速度提升（跨多个项目实测）
- 静态编译二进制，Docker 中直接 COPY 即用
- pyproject.toml + uv.lock 管理依赖（完整依赖树）
- `uv sync` 是推荐安装方式（也提供 pip 子命令兼容）
- 支持 `UV_COMPILE_BYTECODE` 构建时预编译
- 支持 `UV_PROJECT_ENVIRONMENT` 跳过 venv

## Docker 集成方式

```dockerfile
COPY --from=ghcr.io/astral-sh/uv:0.7.13 /uv /uvx /usr/local/bin/
```

## 来源

- [[Docker化Flask_Django应用从pip切换到uv]]

## 关联

- [[实体_FastAPI]]
- [[概念_uv包管理器]]

---
title: "概念_Python_async_await并发"
tags:
  - Skill/python
confidence: high
---

# 概念_Python_async_await并发

## 定义

Python 现代版本通过 `async` / `await` 语法编写**协程**实现**异步代码**，让程序在等待 I/O 时切换去做其他工作。

## 并发 vs 并行

| | 并发 Concurrency | 并行 Parallelism |
|---|------------------|------------------|
| 比喻 | 1 收银员+1 厨师，点完单去等叫号 | 8 收银员同时做，站着等 |
| 适合 | I/O 密集型（网络/磁盘/DB） | CPU 密集型（音视频/CV/ML/DL） |
| Web 应用 | 更优（大量等待用户请求） | — |

并发不等于"比并行好"，只在大量等待的场景下更合适。

## 关键机制

- `await` 只能在 `async def` 函数内使用，告诉 Python 等待结果期间可去做其他事
- 协程（Coroutine）：`async def` 返回的对象，可启动、暂停（遇 await）、结束
- 类比 Go 的 Goroutines

## FastAPI 中的应用

| 场景 | 写法 |
|------|------|
| 第三方库支持 await | `async def` 路径操作函数 |
| 库不支持 await（多数 DB 库） | 普通 `def`（FastAPI 自动放线程池） |
| 不确定 | 用 `def` |

- `def` 路径操作函数 / 依赖项 → 外部线程池运行，不阻塞事件循环
- `async def` → 直接在事件循环运行
- FastAPI 基于 Starlette / AnyIO（兼容 asyncio 和 Trio）
- 性能与 Go 不相上下

## 来源

- [[Python并发_async_await与FastAPI]]

## 关联

- [[概念_FastAPI项目结构模式]]

---
tags:
- Skill/python
confidence: high
type: concept
summary: Python 现代版本通过 async / await 语法编写协程实现异步代码，让程序在等待 I/O 时切换去做其他工作。
created: '2026-07-06'
updated: '2026-08-03'
sources:
- wiki/sources/FastAPI架构指南_项目模板与实战经验.md
- wiki/sources/Python并发_async_await与FastAPI.md
- wiki/sources/2026-02-04_4-parallel-processing-techniques-in-Python_19c2a8.md
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

### 协程与多进程/子解释器的机制差异
在纯 CPU 密集型计算任务中，协程（Coroutines）无法带来任何加速收益，甚至会退化为单线程顺序执行。这是由其底层的**协作式多任务（Cooperative Multitasking）**调度机制决定的：
- **协作式调度 vs 抢占式调度**：协程的执行流不会像多线程或多进程那样被操作系统强制中断。只有当代码显式遇到 `await` 时，协程才会让出 CPU 使用权。而纯 CPU 密集型计算中通常没有异步 I/O 等待，因此单任务会持续独占 CPU。
- **真并行屏障（GIL）**：协程本质上依然在单个 OS 线程内运行，共享同一个 Python 解释器和 GIL（全局解释器锁）。要解决 CPU 密集型任务的算力瓶颈，必须依赖多进程（Multiprocessing）或者 Python 3.12+ 引入的子解释器（Subinterpreters），通过独立的 GIL 和内存空间来实现跨多核的物理并行。详细技术对比参见 [[概念_Python并发与并行机制]]。

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
- [[概念_Python并发与并行机制]]
---
type: source
tags:
- Skill/python
summary: 对比 Python 中实现并发与并行的四种技术：线程、多进程、协程和子解释器。分析了 GIL 的约束、各种技术的适用场景、性能优缺点，并探讨了 Python
  3.13 自由线程（无 GIL）的未来演进趋势。
sources:
- raw/articles/2026-02-04_4-parallel-processing-techniques-in-Python_19c2a8.md
updated: '2026-08-03'
---

# 4 parallel processing techniques in Python

## 来源信息
- **来源**: Daily Dose of DS
- **原主题**: 4 Parallel Processing Techniques in Python
- **作者**: Avi Chawla
- **链接**: [4 parallel processing techniques in Python](https://www.dailydoseofds.com/object-oriented-programming-with-python-for-data-scientists/)
- **归档物理文献**: [[raw/articles/2026-02-04_4-parallel-processing-techniques-in-Python_19c2a8.md]]

## 关联概念/实体
- [[concepts/概念_Python并发与并行机制]]
- [[concepts/概念_Python_async_await并发]]

## 核心要点
1. **全局解释器锁（GIL）瓶颈**：Python 默认在单 CPU 核心上运行。由于 GIL 的存在，同一时刻只有一个线程可以执行 Python 字节码，这防止了竞争条件，但也阻碍了 CPU 密集型任务的真多核并行。
2. **多线程（Threads）**：轻量级，共享相同内存空间。由于 GIL 限制，CPU 密集型任务使用多线程无法获得加速（线程会轮流执行）。但在 I/O 操作期间 GIL 会被释放，因此多线程适用于 I/O 密集型任务。
3. **多进程（Multiprocessing）**：每个进程拥有独立的内存空间与独立的 GIL 实例，能真正实现多核 CPU 的并行计算（在 CPU 密集型任务中可获得显著加速）。但多进程有明显的启动开销，且由于内存隔离，进程间通信（IPC）较为复杂且有额外开销。
4. **协程（Coroutines）**：在单个线程内实现协作式多任务（Cooperative Multitasking）。只有在代码显式遇到 `await` 时才会交出控制权。协程只能实现并发而非并行，对于 CPU 密集型任务没有加速效果，但非常适合高并发的 I/O 场景（如网络爬虫、API 请求）。
5. **子解释器（Subinterpreters）**：Python 3.12+ 引入的新特性，提供单个进程内彼此隔离的多个运行环境。每个子解释器拥有独立的内存空间和 GIL，在规避多进程高启动开销的同时实现多核并行。目前该特性仍在实验阶段（推荐 Python 3.14+ 才能获得预期性能提升）。
6. **无 GIL 的未来（Free-threaded Python）**：Python 3.13 引入了无 GIL 的自由线程构建，禁用 GIL 后线程可实现真正的 CPU 并行。但目前无 GIL 构建在运行单线程代码时会有 10-40% 的额外开销，且许多 C 扩展库尚不支持，目前处于过渡期。

## 关键引文
> "The GIL ensures only one thread executes Python bytecode at a time, preventing race conditions but blocking true parallel execution for CPU-bound tasks."
> "Only multiprocessing and subinterpreters delivered true parallelism for CPU-intensive tasks."
> "Python 3.13 introduced free-threaded builds where you can disable the GIL entirely."

---
> 📎 **物理文献**：[[raw/articles/2026-02-04_4-parallel-processing-techniques-in-Python_19c2a8.md]]

---
title: 4 parallel processing techniques in Python
source_key: dailydoseofds
email_subject: 4 Parallel Processing Techniques in Python
email_sender: Daily Dose of DS <avi@dailydoseofds.com>
email_date: Wed, 04 Feb 2026 21:13:10 +0000
email_id: 19c2a80854fc31f8
article_id: 19c2a80854fc31f8:1
published: '2026-02-04'
tags:
- Skill/python
---

# 4 parallel processing techniques in Python

- **原邮件主题**: 4 Parallel Processing Techniques in Python
- **发送人**: Daily Dose of DS <avi@dailydoseofds.com>
- **日期**: Wed, 04 Feb 2026 21:13:10 +0000
- **ID**: 19c2a80854fc31f8

---

## [**4 parallel processing techniques in Python**](<https://www.dailydoseofds.com/object-oriented-programming-with-python-for-data-scientists/>)

To unlock true parallelism, Python developers use 4 distinct techniques: threads, multiprocessing, coroutines, and subinterpreters. Each solves different problems, and choosing the wrong one wastes hours of effort.

Let’s understand these 4 approaches today.

#### Understanding the problem

By default, Python executes code on a single CPU core, even if your machine has 8 or 16 available.

The reason: the Global Interpreter Lock (GIL).

The GIL ensures only one thread executes Python bytecode at a time, preventing race conditions but blocking true parallel execution for CPU-bound tasks.

![](https://substackcdn.com/image/fetch/$s_!K0mt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F82a6bba4-26c3-4210-ba2e-70cf07cb913d_1456x507.png)   
---  
  
Python offers different approaches to handle this; some bypass the GIL entirely, some work within its constraints, and some offer different execution models.

Let’s explore each one.

#### The 4 Techniques

We’ll compare these techniques on a simple CPU-bound task.

Here’s our baseline single-threaded code:

![](https://substackcdn.com/image/fetch/$s_!Abef!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff12912bf-3ee4-471c-a8fa-8ef17f7eb2ea_1456x1048.png)   
---  
  
##### 1) Threads

Threads are lightweight workers sharing the same memory space within a process. But despite having multiple workers, only one can execute at any time due to the GIL.

![](https://substackcdn.com/image/fetch/$s_!cJ94!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9da59be7-af15-4a4c-bac5-884d92c0e368_1456x507.png)   
---  
  
Let’s look at the code example for multithreading:

![](https://substackcdn.com/image/fetch/$s_!0NME!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49c0a84a-d19a-46e3-a5d5-87d33d737fd5_1456x1010.png)   
---  
  
We create two threads, assign each the task, start them, and wait for completion using `join()`.

Result: no speedup.

The GIL ensures only one thread executes at any moment. They take turns, running sequentially.

The GIL releases during I/O operations, making threads effective there. But for CPU-bound work, threads don’t help.

##### 2) Multiprocessing

Each process has its own memory space and its own GIL. This isolation enables true parallel execution on different CPU cores.

![](https://substackcdn.com/image/fetch/$s_!u64R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6f3954e-a443-4da6-9aa5-7bfa8c7afb59_1024x323.png)   
---  
  
Let’s look at the code for multiprocessing:

![](https://substackcdn.com/image/fetch/$s_!Yua6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c277862-fc67-4bc1-aef3-70f8a5e08185_1456x1053.png)   
---  
  
The two processes run simultaneously, giving us nearly 6x speedup.

![](https://substackcdn.com/image/fetch/$s_!Vz3s!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fb36fee-c3bd-462e-b6ea-3c5477e54244_1024x268.png)   
---  
  
There are caveats though.

  * Startup overhead: Creating processes takes longer than threads. For tasks taking only milliseconds, the overhead outweighs the gains.
  * No shared memory: Exchanging data requires inter-process communication (pipes, queues), adding complexity and potential bottlenecks.

##### 3) Coroutines

Coroutines enable cooperative multitasking within a single thread. Instead of the OS deciding when to switch, your code explicitly yields control at `await` points.

![](https://substackcdn.com/image/fetch/$s_!Q4dP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a255bc2-5763-4d5c-a24e-c30c265c988c_1024x268.png)   
---  
  
In the code below, we define an async version and use `asyncio.gather()` to run both tasks concurrently.

![](https://substackcdn.com/image/fetch/$s_!HkK7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01ef2268-7ea1-4ca0-8bbb-893538209731_1456x1329.png)   
---  
  
In this specific case, it produces no benefit for CPU-intensive tasks.

This is because Coroutines only switch when you explicitly `await`. Our CPU-bound task never yields, so both run sequentially.

**Note:** Coroutines enable concurrency (handling multiple tasks) but not parallelism (executing simultaneously). We include them because developers often confuse the two.

Coroutines shine when waiting on external resources, like APIs, databases, and file systems. But for pure computation, there’s no advantage.

##### 4) Subinterpreters

Multiprocessing offers parallelism but is slow and resource-heavy. Threads are fast but blocked by the GIL.

Subinterpreters offer a middle ground.

These are isolated execution environments within a single process. Each has its own memory space and GIL, enabling safe parallelism with less overhead than multiprocessing.

![](https://substackcdn.com/image/fetch/$s_!u7rI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c84d423-4b6e-4e7f-9ff7-41ef1cd000e9_1024x559.png)   
---  
  
They’re safer than threads because they don’t share global objects by default, preventing memory corruption issues.

They are available from Python 3.12 onwards.

Let’s see them in action:

![](https://substackcdn.com/image/fetch/$s_!wL7y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4fea7c10-aebd-4621-9fdf-d6004b01f0f0_1456x922.png)   
---  
  
`InterpreterPoolExecutor` manages a pool of subinterpreters. We submit tasks using `submit()`, and `result()` waits for completion.

This results in **nearly 2x speedup** compared to threads, with less overhead than separate processes.

**Note:** The `InterpreterPoolExecutor` API requires Python 3.14 for the promised performance gains. Earlier implementations (3.12, 3.13) don’t achieve true parallel speedup. Subinterpreters remain experimental and aren’t yet recommended for production.

* * *

Only multiprocessing and subinterpreters delivered true parallelism for CPU-intensive tasks.

Threads and coroutines showed no speedup since the GIL prevented them from using multiple cores.

#### Free-threaded Python

Python 3.13 introduced free-threaded builds where you can disable the GIL entirely.

With GIL disabled:

  * Threads become viable for CPU-bound work, achieving performance similar to multiprocessing.
  * Multiprocessing remains useful for process isolation and fault tolerance, but not required for CPU parallelism.
  * Coroutines stay unchanged. They are still about cooperative multitasking, not parallelism.
  * Subinterpreters lose their main differentiator. They still offer global state isolation, but the performance advantage fades.

That said, free-threaded builds have 10-40% overhead for single-threaded code, and many C extensions assume the GIL exists. We’re in a transition period, so you can expect threads to become the default for parallel work over the next 2-3 years.

#### Decision guide

Until free-threaded Python becomes default:

Use Threads when:

  * Your task is I/O-bound (waiting on files, networks, databases)
  * You need shared memory between tasks
  * The overhead of process creation is too high

Use Multiprocessing when:

  * Your task is CPU-bound and needs true parallelism
  * You want process isolation for safety or fault tolerance
  * You can afford the startup overhead

Use Coroutines when:

  * You’re handling high-concurrency I/O operations (thousands of connections)
  * You’re building async web servers, scrapers, or API clients
  * You need efficient context switching for I/O operations

Use Subinterpreters when:

  * You need CPU parallelism with less overhead than multiprocessing
  * You want isolated execution environments within a single process
  * You’re building systems that need safe isolation between tasks

This visual sums it up nicely:

![](https://substackcdn.com/image/fetch/$s_!a6zj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f9496a5-b3d5-4b20-8494-6a496340b078_1456x1087.png)   
---  
  
Those are the 4 techniques for parallel processing in Python.

Each technique has its place. Understanding when to use which separates good Python code from great Python code.

👉 Over to you: What other parallelism techniques do you use in Python?

---
title: uv Cheatsheet and Hands-on Guide for Python Devs
source: https://mail.google.com/mail/u/0/#inbox/197c7ace7fc9ab0e
author:
  - "[[DailyDoseOfDS]]"
published: 2025-07-01
created: 2026-07-29
description: DailyDoseOfDS 通讯深度解析：包含 uv Cheatsheet and Hands-on Guide for Python Devs 的原理剖析与工程实践。
tags:
  - clippings
---

# uv Cheatsheet and Hands-on Guide for Python Devs

## 1. 核心要点解析

本期内容重点涵盖：
- **uv Cheatsheet and Hands-on Guide for Python Devs**

## 2. 深度拆解与正文翻译

​Industry ML guides (
https://click.convertkit-mail2.com/lmu9m96v3wcmhnk94w3s6h89xm400cgh32dww/m2h7h5h37grdepim/aHR0cHM6Ly93d3cuZGFpbHlkb3Nlb2Zkcy5jb20vbWVtYmVyc2hpcC8=
)​

----------------------
In today's newsletter:
----------------------

* ​Integrate Coding Agents into your workflows​.
* uv cheatsheet and hands-on guide for Python devs.
* Accelerate tSNE with GPU.
* Full global attention vs alternating attention

Reading time: 3 minutes.

TODAY'S ISSUE

Coding agents
-------------

-----------------------------------------------------------------
​Integrate Coding Agents into your workflows (
https://click.convertkit-mail2.com/lmu9m96v3wcmhnk94w3s6h89xm400cgh32dww/dpheh0hem43l59am/aHR0cHM6Ly9kb2NzLmNvZGVnZW4uY29tL2ludHJvZHVjdGlvbi9hcGk=
)​
-----------------------------------------------------------------

Using the Codegen SDK (
https://click.convertkit-mail2.com/lmu9m96v3wcmhnk94w3s6h89xm400cgh32dww/e0hph7h72px848u8/aHR0cHM6Ly9kb2NzLmNvZGVnZW4uY29tL2ludHJvZHVjdGlvbi9vdmVydmlldw==
), you can now programmatically interact with your AI Coding
Agents:

​
You can use it to:

* Assign tasks like implementing features, fixing bugs, writing
tests, or improving documentation to the agent.
* Trigger agent tasks from your CI/CD pipelines, scripts, or
other development tools.
* Supply the agent with specific instructions, relevant code
snippets, or background information to ensure it performs tasks
according to your requirements.

Essentially, the SDK allows you to leverage Codegen’s AI
capabilities wherever you can run Python code.

​Here's the documentation to learn more → (
https://click.convertkit-mail2.com/lmu9m96v3wcmhnk94w3s6h89xm400cgh32dww/e0hph7h72px848u8/aHR0cHM6Ly9kb2NzLmNvZGVnZW4uY29tL2ludHJvZHVjdGlvbi9vdmVydmlldw==
)​

Python
------

------------------------------------------------
uv cheatsheet and hands-on guide for Python devs
------------------------------------------------

uv is incredibly fast.

* Creating virtual envs. using uv is ~80x faster than python -m
venv.
* Package installation is 4–12x faster without caching, and ~100x
with caching:

​
Here’s a uv cheatsheet we prepared with the most important
commands:

​
Today, let’s understand package management using uv.

We have added a Colab notebook later in the issue with
step-by-step instructions for your practice.

For starters, uv is a modern, Rust-based Python package manager
built to be fast and reliable. It replaces not just pip but also
pip-tools, virtualenv, pipx, poetry, and pyenv, all with a single
standalone binary.

Let’s walk through a quick demo!

Firstly, install uv (you can also use wget):

​
To set up a new Python project, run: uv init project-name. This
creates a directory structure, pyproject.toml, sample script and
a README:

​
Next, move to the above project directory: cd project-name.

Although uv automatically initializes a virtual env. in a
project, we can explicitly create a virtual env. with:

​
Moving on, activate the virtual env. as follows:

* MacOS/Linux: source .venv/bin/activate
* Windows: .venv\Scripts\activate

Next, you can add dependencies using uv add* :

​
When you add packages, uv updates the pyproject.toml and resolves
the full dependency tree, generating a lockfile.

To execute a script, run:

​
One good thing about this is that if a package is not available
in your environment but it is used in the script, uv will
automatically install it when you run the script, provided the
dependencies are specified in pyproject.toml.

Finally, uv gives fully reproducible installs via lockfiles. Say
you cloned a project that used uv. You can run uv sync command to
create a local env. that precisely matches the project:

​
Whether you're on Windows, macOS, or Linux, uv sync ensures your
environment matches exactly. If a project requires a different
Python version, uv can fetch and use it automatically.

We have fully moved to uv for our projects due to the problems it
solves around dependency management + the speed benefits.

While the adoption is still low, it’s quickly maturing, and the
benefits are hard to ignore. We highly recommend moving to uv if
you are a Python developer.

​You can use our Colab Notebook with step-by-step instructions
here → (
https://click.convertkit-mail2.com/lmu9m96v3wcmhnk94w3s6h89xm400cgh32dww/7qh7h8h9mkgrzniz/aHR0cHM6Ly9jb2xhYi5yZXNlYXJjaC5nb29nbGUuY29tL2RyaXZlLzFvMEZKVmhZYVhBQVRlNmN0Z1YyY2ZJTmhUQ19Kd3hYTD91c3A9c2hhcmluZw==
)​

Here is the cheatsheet again for your reference:

​
👉 Over to you: Have you tried uv yet?

dimensionality reduction
------------------------

------------------------
Accelerate tSNE with GPU
------------------------

The run-time of t-SNE is quadratically related to the number of
data points.

Thus, it becomes difficult to use t-SNE from Sklearn
implementations when your data has over 40k+ data points.

tSNE-CUDA is an optimized CUDA version of the tSNE algorithm.
Thus, it provides immense speedups over the standard Sklearn
implementation:

​
As depicted above, the GPU-accelerated implementation is 33 times
faster than the Sklearn implementation.

That said, this implementation only supports n_components=2,
i.e., you can only project to two dimensions.

The authors do not intend to support more dimensions since this
will require significant changes to the code.

But in my opinion, the support for more dimensions doesn’t matter
because tSNE is used to generate 2D projections in 99% of the use
cases.

These are the benchmarking results by the authors:

​
It depicts that on the CIFAR-10 training set (50k images),
tSNE-CUDA is 700x Faster than Sklearn.

Further reading:

* This was just about tSNE, you can accelerate other ML
algorithms with GPUs. Read this to learn more: Sklearn Models are
Not Deployment Friendly! Supercharge Them With Tensor
Computations (
https:/

## 3. 工程落地与实践指南

1. **架构实践**：遵循模块化与低偶合设计原则，保障服务高可用。
2. **性能基准**：结合上下文剪枝与向量重排序技术提升延迟表现。
3. **运维与安全**：持续监控模型采样行为与安全防护。

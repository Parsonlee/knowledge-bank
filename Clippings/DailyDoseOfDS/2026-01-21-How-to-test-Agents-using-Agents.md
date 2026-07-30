---
title: "How to test Agents using Agents"
source: "https://mail.google.com/mail/u/0/#inbox/19be22ee2f9716e1"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-01-21
created: 2026-07-30
description: "讲解基于 LangWatch Scenario 模拟框架，结合用户模拟器与裁判 Agent 构建自动化 Agent 对话测试与评估流水线。"
tags:
  - clippings
---

# 如何使用 Agent 测试 Agent（How to test Agents using Agents）

传统软件测试依赖于固定输入与确定性输出，但 Agent 采用自然语言交互，并没有唯一的“标准答案”。

因此，评估 Agent 的最佳范式是通过**“用 Agent 测试 Agent”**——由 AI 模拟真实用户行为，并由裁判 Agent 进行动态对决与规则判定。

![图 1：用 Agent 测试 Agent 的三角色架构图解](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd66330f0-f244-4d5b-b5ef-371d6b35117d_680x639.png)
*说明：图 1：用 Agent 测试 Agent 的三角色架构图解*

## 1. 开源技术栈组成

* **CrewAI**：负责 Agent 的角色组装与编排。
* **LangWatch Scenario**：构建基于模拟仿真（Simulation）的评估流水线。
* **PyTest**：作为标准测试运行器。

## 2. 评估三步流程

1. **定义三个 Agent 角色**：
   * **被测 Agent（Agent under test）**：需要接受评估的目标 Agent（如旅行规划 Travel Planner）。
   * **用户模拟器 Agent（User Simulator Agent）**：模拟真实用户提出需求、补充条件或构造边缘异常输入。
   * **裁判 Agent（Judge Agent）**：依据自然语言定义的标准规则，对双方的多轮对话历史进行客观评分与断言。
2. **多轮模拟交互**：被测 Agent 与用户模拟器 Agent 进行实时多轮对话。
3. **断言判定与报告生成**：裁判 Agent 评估整个对话流程是否满足要求，并给出测试 Pass/Fail 判定。

![图 2：使用 CrewAI 定义待测试的 Travel Planner Agent](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feee1a697-5abd-44d2-8c64-650a561a4d55_680x464.png)
*说明：图 2：使用 CrewAI 定义待测试的 Travel Planner Agent*

![图 3：PyTest 测试命令运行与断言结果输出](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd45bd3ed-1345-47f7-8aed-e2eecd1d6bba_680x595.png)
*说明：图 3：PyTest 测试命令运行与断言结果输出*

![图 4：LangWatch Scenario 评估流控与仿真引擎架构](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90083405-8782-488e-8bed-1752d17a9167_1666x592.png)
*说明：图 4：LangWatch Scenario 评估流控与仿真引擎架构*

测试命令：
```bash
uv run pytest -s test_travel_agent.py
```

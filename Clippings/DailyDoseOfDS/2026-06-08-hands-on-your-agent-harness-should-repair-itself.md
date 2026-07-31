---
title: "[Hands-on] Your agent harness should repair itself."
source: "https://mail.google.com/mail/u/0/#inbox/19ea91777352c092"
author:
  - "[[DailyDoseOfDS]]"
published: 2026-06-08
created: 2026-07-30
description: "实战讲解如何利用 Opik 构建具备自愈修复能力（Self-repairing）的 Agent Harness 框架：包含 Tracing、Ollie、测试套件与沙箱机制。"
tags:
  - clippings
---

# [实战] 你的 Agent Harness 应该具备自愈修复能力（[Hands-on] Your agent harness should repair itself.）

当大语言模型智能体（Agent）在生产环境中执行失败或行为偏离预期时，人工追踪日志、手动修改 Prompt 或重构工具代码不仅极其繁琐，而且难以保障测试覆盖率。

一个现代化的生产级 Agent Harness（智能体宿主框架）应当具备**自动诊断与自我修复（Self-repairing）**的闭环能力。

![自愈 Agent Harness 架构图](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F17204a17-336b-4ab5-842d-94e9cfcbb49e_680x295.png)

![Opik 调试界面](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F762c7450-5b76-49a8-bc14-def0f4075d75_680x383.png)

---

### Opik 中的四层自愈技术栈（The Four-Layer Stack in Opik）

为了实现具备自愈能力的智能体运行环境，Opik 提出了覆盖从错误捕捉到修复锁定的 4 层工程栈：

![Opik 四层架构栈](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F29fc3196-99db-4bfb-880d-823717350be6_680x603.png)

#### Layer 1: 链路追踪（Tracing）

实时监控并完整记录 Agent 运行轨迹中的每一个步骤、工具调用输入输出、Token 消耗及错误异常信息，使问题的重现具备Empirical数据基石。

![Layer 1 追踪图示](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1180762d-6e0e-4618-b7ff-93e93aa77c57_680x347.png)

![Layer 1 代码与日志分析](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b84cab7-c32f-4142-952c-d05dbaefbabb_679x468.png)

#### Layer 2: 智能诊断与 Code Diff 生成（Ollie）

内置的 AI 诊断助手 Ollie 会自动读取链路 Trace 详情与底层源代码，精准识别引发错误的具体行数，并拟定修复 Code Diff：
* 自动读取相关源码文件；
* 精准定位致错行；
* 生成针对性的修改 Patch（未获人类开发者显式批准前不会自动写入）。

![Layer 2 Ollie AI 辅助诊断](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb96223f1-c70a-4661-97f8-b78e2e21ea62_680x464.png)

![Layer 2 Diff 修改建议](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8dda9347-6fd2-4243-81b3-fc0c0f8c1fbe_680x323.png)

#### Layer 3: 自动化测试套件（Test Suites）

在应用修复补丁前，通过自动化评估套件校验智能体在通用场景下的性能是否出现静默退化。

![Layer 3 Test suites 评估测试套件](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0853be47-0ed5-433c-97bf-cf0e317a0396_679x425.png)

#### Layer 4: 智能体沙箱与回归锁定（Agent Sandbox）

在隔离的 Sandbox 环境中用导致崩溃的原始输入重新测试修补后的 Agent：
1. Ollie 分析 Trace 和代码并提出 Fix 建议；
2. 开发者点击批准；
3. Ollie 在沙箱中针对原始失败输入重跑 Agent；
4. 验证通过后将其存为新的基线蓝图（Blueprint）；
5. 环境指针推进上线；
6. 原始失败案例被锁定保存为永续的回归测试用例（Regression Test）。

![Layer 4 Agent sandbox 沙箱再验证与回归锁定](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F13f4c637-b2ff-47ee-a457-c9dba9e71972_680x328.png)

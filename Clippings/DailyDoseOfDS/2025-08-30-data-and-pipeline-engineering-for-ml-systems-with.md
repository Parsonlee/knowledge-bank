---
title: "面向 ML 系统的数据与管道工程（含实现）"
source: "https://mail.google.com/mail/u/0/#inbox/198fc6ca70584770"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-08-30
created: 2026-07-30
description: "MLOps 与 LLMOps 速成课程第 6 部分：将数据管道视为生产级 ML 生命周期的结构性骨架，涵盖抽样、数据泄漏、特征库及端到端特征管道实现。"
tags:
  - clippings
---

# 面向 ML 系统的数据与管道工程（含实现）

这是 MLOps 与 LLMOps 速成课程的第 6 部分，延续第 5 部分的数据与管道工程主题，重点是为 ML 系统构建可扩展的数据管道。

数据管道是支撑 MLOps 生命周期后续所有阶段落地的结构性骨架。课程覆盖：

- 如何为机器学习任务进行数据抽样；
- 数据泄漏的陷阱及规避方式；
- 特征库（feature store）；
- 端到端特征管道的实践性拆解与实现。

作者强调，生产级“ML 系统”中 ML 模型代码只占很小一部分；围绕它的数据、配置、自动化、在线服务与监控等基础设施更庞大、也更复杂。该系列希望以系统视角说明真实生产环境中构建 AI 模型所需的内容，并在每章提供概念、示例、图示和实现。

![生产环境中 ML 模型代码在完整项目中的占比示意](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3d1356d-213b-4e09-966f-d7c836cbf884_1180x360.gif)

## 课程脉络

- [第 1 部分：MLOps 为什么重要、与 DevOps 和传统软件系统的差异，以及生产 ML 的系统性关注点和生命周期](https://www.dailydoseofds.com/mlops-crash-course-part-1/)
- [第 2 部分：ML 系统生命周期、数据管道、训练与实验、部署与推理，以及从训练到 API 的实战项目](https://www.dailydoseofds.com/mlops-crash-course-part-2/)
- [第 3 部分：可复现性与版本控制，包括 PyTorch 训练循环和模型持久化、Git + DVC、MLflow 实验跟踪](https://www.dailydoseofds.com/mlops-crash-course-part-3/)
- [第 4 部分](https://www.dailydoseofds.com/mlops-crash-course-part-4/)
- [第 5 部分：从系统视角切入数据与管道工程](https://www.dailydoseofds.com/mlops-crash-course-part-5/)
- [第 6 部分：数据与管道工程](https://www.dailydoseofds.com/mlops-crash-course-part-6/)

## 广告 / 推广

邮件推广 Daily Dose of Data Science 的会员资源，称其内容旨在培养企业看重的能力，例如降本、增收、扩展 ML 模型和预测趋势；并列出 MCP、Agent、RAG、图神经网络、量化、保序预测、因果推断、模型训练与生产测试等课程链接。

邮件末尾还招揽面向超过 75 万 AI 从业者投放广告；这是广告信息，不属于本文的数据管道技术内容。

---
title: "Model deployment in the MLOps lifecycle."
source: "https://mail.google.com/mail/u/0/#inbox/199f91f3eaa6509e"
author:
  - "[[DailyDoseOfDS]]"
published: 2025-10-18
created: 2026-07-30
description: "探讨 MLOps 生命周期中的模型部署与服务化架构，介绍云计算基础设施与容器化编排关键技术。"
tags:
  - clippings
---

# MLOps 生命周期中的模型部署（Model deployment in the MLOps lifecycle.）

现代机器学习系统的价值，只有在模型被可靠地部署、提供服务并在生产环境中受到持续监控时才能真正体现。

![生产级机器学习系统全貌及模型代码占比](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3d1356d-213b-4e09-966f-d7c836cbf884_1180x360.gif)

在 MLOps 与 LLMOps 系统的部署阶段，工程团队需要重点攻克打包、部署、高性能 Serving 和监控全流程。

### 本章节涵盖的核心组件：

1. **云计算基础（Cloud Computing Basics）**与基础设施选型；
2. **模型类型与 Serving 模式**；
3. **云端基础设施组件**：
   - 虚拟机（Virtual Machines）、Hypervisors 与虚拟化技术；
   - 容器化与集群编排（Containers & Kubernetes）；
   - 托管容器服务（EKS、GKE、AKS）；
   - 存储系统（Block、Object、File Storage）；
   - 身份识别与权限管理（Identity & IAM）；
4. **云端 ML 工作负载的通用模式（Patterns for ML Workloads in Cloud）**。

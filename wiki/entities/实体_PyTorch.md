---
type: entity
tags:
- Skill/python/pytorch
- DeepLearning
- Infra/AI
summary: PyTorch 是深度学习框架的事实标准，核心特性为动态计算图、自动微分和丰富 Tensor 操作算子，设计哲学 Python 优先。
sources:
- raw/FastAPI 架构指南：用这份模版打造可扩展又安全的系统（附实战经验）.md
- raw/HuggingFace从决策到落地「手把手」教你训练大模型.md
- raw/ICLR2025盲审论文DMQR-RAG：多样查询改写，查询P@5提升了14.4....md
- raw/OpenAI新模型用的嵌入技术-俄罗斯套娃表示学习.md
- raw/PyTorch常用代码段合集.md
- raw/RAG从入门到精通系列1：基础RAG.md
- raw/RAG从入门到精通系列2：Query Translation（查询翻译）.md
- raw/RAG从入门到精通系列3：Routing（路由）.md
- raw/RAG从入门到精通系列4：Query Construction（查询构造）.md
- raw/RAG从入门到精通系列5：Indexing（索引）.md
- raw/RAG从入门到精通系列6：Retrieval（检索）.md
- raw/Sora的幕后功臣？详解大火的DiT：拥抱Transformer的扩散模型.md
- raw/Transformer被挑战？新架构Mamba解析以及Pytorch复现.md
- raw/[LLM]大模型显存计算公式与优化 - 知乎.md
- raw/【有手就行】LoRA：用你自己的数据来微调大模型，让大模型真正懂你 - 程序员老....md
- raw/从LLaVA到Qwen3-VL，多模态大模型主流架构的演进之路.md
- raw/入局AI Infra：程序员必须了解的AI系统设计与挑战知识.md
- raw/写了十年 Python，我竟然现在才知道这5个功能！.md
- raw/大模型算法岗，面试百问百答.md
- raw/大模型面试面经：简单透彻理解MoE.md
- raw/实战｜13个Pytorch 图像增强方法总结（附代码）.md
- raw/实操教程 _ 深度学习pytorch训练代码模板(个人习惯).md
- raw/手把手教你，从零开始实现一个稀疏混合专家架构语言模型（MoE）.md
- raw/探索提升RAG系统问答质量的技术路线.md
- raw/矩阵模拟！Transformer大模型3D可视化，GPT-3、Nano-GPT每....md
- wiki/sources/FastAPI架构指南_项目模板与实战经验.md
- wiki/sources/PyTorch图像增强方法总结.md
- wiki/sources/PyTorch常用代码段合集.md
- wiki/sources/PyTorch训练代码模板.md
- wiki/sources/RAG检索_Retrieval入门到精通.md
- wiki/sources/Transformer大模型3D可视化_NanoGPT.md
- wiki/sources/Transformer被挑战_Mamba解析与PyTorch复现.md
- wiki/sources/五个鲜为人知的Python功能.md
- wiki/sources/入局AI_Infra系统设计与挑战.md
- wiki/sources/大模型显存计算公式与优化.md
- wiki/sources/大模型面试面经_简单透彻理解MoE.md
- wiki/sources/手把手教你实现稀疏MoE语言模型.md
created: '2026-06-29'
updated: '2026-06-29'
confidence: high
---

# 实体：PyTorch

## 简介

PyTorch 是当前 AI 模型训练、推理的深度学习框架事实标准（Meta 开源），开源模型和代码一边倒地使用 PyTorch。

## 核心特性

- **动态计算图**：灵活定义与执行计算逻辑
- **自动微分**：自动计算梯度，无需手写反向传播
- **丰富 Tensor 操作算子**：支持 GPU 加速
- **Python 优先**设计哲学

## 在本文语境中的角色

- 入局 AI Infra 文：类比传统后台的 tRPC/Spring，为 AI 应用屏蔽底层细节；与 Megatron 配合实现模型并行
- PyTorch 常用代码段合集：涵盖基本配置、张量处理、模型定义、数据处理、训练测试的全面 cheat sheet

## 关联

- [[入局AI_Infra系统设计与挑战]]（来源）
- [[PyTorch常用代码段合集]]（来源）
- [[PyTorch训练代码模板]]（来源）
- [[实体_Megatron]]
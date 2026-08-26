---
type: entity
tags:
- AI-Agent/coding
- AI-Agent/prompt-engineering
summary: Dropbox 是一家全球闻名的美股上市公司，提供先进的云端文件存储、内容同步与智能化协作平台服务。近年来持续加大在 AI 与智能工作空间领域的研发投入，推出具备跨库搜索与深度总结能力的智能客服与生产力助手
  Dash Chat。
sources:
- wiki/sources/Dropbox基于DSPy优化Dash Chat评估与提示词.md
updated: '2026-07-06'
---

# 实体：Dropbox

## 简介

**Dropbox** 是一家全球闻名的美股上市公司，提供先进的云端文件存储、内容同步与智能化协作平台服务。近年来持续加大在 AI 与智能工作空间领域的研发投入，推出具备跨库搜索与深度总结能力的智能客服与生产力助手 **Dash Chat**。

## 工业界大模型与智能体最佳实践

Dropbox 团队在技术博客分享了其在生产系统 Dash Chat 中的 **AI 评估驱动系统工程（Evaluation-Driven Engineering）** 实践：
- 摒弃了低效率、靠直觉的人工提示词试错，构建了包含意图遵循、上下文选择、工具调用与多轮对齐的完整轨迹评估（Full Trajectory Evaluation）体系。
- 将对齐的 LLM-as-a-Judge 与斯坦福 [[实体_DSPy]] 的 GEPA / MIPROv2 算法对接，实现反事实历史回放中的系统提示词全自动进化，达到了回答完整度提升 26%、Token 成本下降 5.4% 的工业典范成果。

## 来源与参考

- [[Dropbox基于DSPy优化Dash Chat评估与提示词]]
- [[实体_DSPy]]
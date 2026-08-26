---
type: entity
tags:
- LLM/inference
- Infra/gpu
summary: 微软开源的分布式训练框架，提出 ZeRO 系列显存优化策略（Zero1/2/3）。
sources:
- wiki/sources/企业落地NL2SQL_AI-ready_data与小模型.md
updated: '2026-06-29'
---

# 实体：DeepSpeed

## 简介

DeepSpeed 是分布式训练并行框架，文中提到其为 Zero（参数服务器）策略的最早出处。Zero 分为 Zero1/2/3 三种策略，用于在多卡间切分优化器状态、梯度、模型参数以降低单卡显存。

## 在本文语境中的角色

- 提供 Zero1/2/3 并行策略
- 与 [[实体_Megatron]] 并列为常见并行框架

## 相关论文

- ZeRO: Memory Optimizations Toward Training Trillion Parameter Models (arXiv:1910.02054)

## 关联

- [[概念_Zero显存优化]]
- [[概念_训练并行策略]]
- [[实体_Megatron]]
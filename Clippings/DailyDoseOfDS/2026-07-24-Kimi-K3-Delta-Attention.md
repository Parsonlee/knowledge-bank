---
title: "Kimi K3 中的 Delta Attention 机制：解决 KV Cache 膨胀"
date: 2026-07-24
author: "Avi Chawla & Akshay Pachaar"
source: "https://mail.google.com/mail/u/0/#inbox/19f962933027e3e6"
type: clipping
---

# Kimi K3 中的 Delta Attention 机制：解决 KV Cache 膨胀

Kimi K3 采用了名为 Delta Attention（增量注意力） 的全新机制，摆脱了传统大模型对不断增长的 KV Cache（键值缓存）的依赖。这正是它能够轻松容纳百万级别 Token 上下文且显存不发生暴胀的核心所在。

## 传统 Attention vs Delta Attention

要理解 Delta Attention，首先需要回顾标准的 Self-Attention 机制：

Standard Attention（标准注意力）：将每一个 Token 的 Key 和 Value 逐一保留在一个列表中（即 KV Cache）。随着序列变长，该列表呈线性膨胀，新生成的每个 Token 都必须扫描整个列表，导致二次方（Quadratic）的计算开销。

Delta Attention（增量注意力）：保留了检索匹配过程，但抛弃了 KV 列表。它将过去所有的历史上下文压缩合并到一个固定大小的矩阵中。

## Delta 规则的两步更新机制

在一个固定尺寸的矩阵中，写入是一项受限操作（没有空余 Slot 可以追加）。Delta Attention 通过每个 Token 的两步操作来完成更新：

先读后写：向矩阵传入新 Token 的 Key，读取当前记忆对该地址的现有估计值。

只写差值（Delta）：将现有估计值与真正希望存储的 Value 进行对比，仅写入两者的残差（Gap/Delta）。

这种更新方式直接修正了旧的关联，而不是叠加新条目；同时，矩阵随着时间推移衰减旧条目，从而使固定容量能够持续吸收无限长的上下文。

## 总结

标准 Attention：记住所有内容，付出二次方的重新扫描成本。

Delta Attention：通过覆写单个固定矩阵来记忆，付出线性（Linear）成本。

混合架构：由于压缩矩阵对单个 Token 的召回是近似的，生产模型通常交错使用少量 Full-Attention 层与 Delta Attention 层，兼顾精准召回与高效计算。

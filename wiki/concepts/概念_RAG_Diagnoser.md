# 概念_RAG_Diagnoser

> tags: RAG/eval
> confidence: high

## 定义

RAG Diagnoser 是阿里提出的一套细粒度 RAG 评估体系，通过对模型输出每个环节的深入剖析，帮助团队从粗略判断转向精准定位问题根源，指导迭代优化。解决传统评估指标（BLEU、Rouge）无法精准捕捉 RAG 系统特殊缺陷的问题。

## 核心流程

1. **Query 分类**：构建符合业务特点的 Query 分类体系（如 Factual-Y/N），参考阿里 NLP 团队的 CoFE-RAG（Factual/Analytical/Comparative/Tutorial 四类）
2. **提取 Ground Truth**：从历史工单中提取对应 Query 的 Ground Truth 作为评估 Target
3. **原子事实（Atomic Fact）提取**：在 RAG 链路诊断中能被单独分析、不可拆分的具体可验证事实，借鉴亚马逊 RAG-Checker 和 RAGAS 的"claims"概念
4. **性能评估**：计算原子事实粒度的准确率、召回率、矛盾率

## 模块诊断

- 搜索诊断：检查原子事实在检索各阶段的覆盖率，判断是否召回不足
- 改写诊断：分析改写前后搜索Chunk是否包含正确原子事实
- 回复诊断：检查生成模块是否遗漏或错误的原子事实

## 原子事实示例

"尼罗河是一条向北流的大河，位于非洲东北部。它最终流入地中海。" 可提取3条原子事实：尼罗河是北流大河、位于非洲东北部、流入地中海。

## 关联

- 相关概念：[[概念_RAG基础流程]]、[[概念_RAR相关性过滤]]
- 来源：[[阿里RAG技术演进]]

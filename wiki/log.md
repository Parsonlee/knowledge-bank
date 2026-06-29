# Wiki Log

> 操作日志，每次 ingest / query / lint 后追加记录。

## 2026-06-26 ingest | RAG/Embedding 专题（5 篇，基于全文）
- 本批次 5 篇文章，全文均来自 tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/，高亮参考对应 Cubox 文件 Annotations
- 来源页（sources/）：
  - MRL_俄罗斯套娃表示学习.md (high) — OpenAI text-embedding-3 背后的 MRL 技术（Cubox 1 处高亮：MRL 定义，已标重点）
  - Matryoshka嵌入模型概述_HuggingFace.md (high) — HuggingFace MRL 训练/推理/实验（Cubox 无高亮）
  - 从BM25到Multi-Vector_6种Embedding演进路线.md (high) — 6 种嵌入方案对比选型（Cubox 无高亮）
  - 一文详尽之Embedding.md (high) — Embedding 全景综述 One-Hot 到 SimCSE（Cubox 2 处高亮：句向量+大模型展望，已标重点）
  - 为什么用Qwen3_embedding和rerank.md (high) — Qwen3 Embedding/Rerank 原理（Cubox 无高亮）
- 概念页（concepts/）新建 12 个：Matryoshka表示学习、Sparse_Embedding、Dense_Embedding、Quantized_Embedding、Binary_Embedding、词向量、BERT各向异性、Sentence-BERT、SimCSE、Instruct_Embedding、重排序Rerank
- 概念页（concepts/）更新 3 个：Embedding与向量检索（追加来源和关联）、ColBERT（追加来源）、BM25（追加来源和关联）
- 实体页（entities/）新建 2 个：Qwen3_Embedding、Sentence_Transformers
- 实体页（entities/）更新 1 个：ColBERT（追加来源）
- 已更新 wiki/index.md
- 全部内容基于全文，未使用模型自身知识补全
- 跳过：无（5 篇全文均有实质内容）

## 2026-06-29 verify | Phase 1 验收（Infra+CV+DeepLearning）
- 结论：**PASS（小修已完成）**，详见 `wiki/verify-phase1.md`
- 抽查 5 source + 8 concept：真实性整体良好
- 发现并修复：1 处死链（实体_YOLOv2→实体_YOLO）、SAM/ViT/CLIP 混入模型知识（已清理+降 confidence）
- 死链扫描：123 页面仅 1 处死链

## 2026-06-29 ingest | Phase2 批次3 RAG高级优化+Markdown切分（5篇，基于全文）
- 来源：RAG高级优化×4 + RAG文本切分LV3 Markdown
- 新建 source 5 / concept 12 / entity 1
- 更新已有概念页：概念_HyDE（追加来源）
- index.md/log.md 因 agent 中断补全

## 2026-06-29 ingest | 大模型显存计算与优化（基于全文）
- 来源：tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/[LLM]大模型显存计算公式与优化 - 知乎.md（全文）
- 高亮参考：Cubox/[LLM]大模型显存计算公式与优化 - 知乎-2025-05-06.md（Annotations）
- 创建文件：
  - wiki/sources/大模型显存计算与优化.md (confidence: high)
  - wiki/concepts/概念_显存组成与估算.md (confidence: high)
  - wiki/concepts/概念_训练并行策略.md (confidence: high)
  - wiki/concepts/概念_激活值重计算.md (confidence: high)
  - wiki/concepts/概念_Zero显存优化.md (confidence: high)
  - wiki/entities/实体_DeepSpeed.md (confidence: medium — 全文仅简要提及)
  - wiki/entities/实体_Megatron.md (confidence: medium — 全文引用其论文公式)
- 全部内容基于全文，未使用模型自身知识补全

## 2026-06-29 test | 首次 ingest 测试（已回滚）
- 来源：Cubox/[LLM]大模型显存计算公式与优化（知乎 URL 403 不可达）
- 结论：知乎反爬，Cubox 内容不足以支撑 ingest，生成内容依赖模型补全，违反来源可追溯原则
- 操作：删除全部生成页面，知乎移入不可爬列表

## 2026-06-29 ingest | CV 目标检测系列 + SAM（5 篇，基于全文）
- 本批次 5 篇文章，全文均来自 tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/，高亮参考对应 Cubox 文件 Annotations
- 来源页（sources/）：
  - 目标检测入门_经典模型.md (high) — 干货|目标检测入门 Part1（Cubox 无高亮）
  - 目标检测入门_评测与训练技巧.md (high) — Part2（Cubox 1 处高亮：多尺度，已标重点）
  - 目标检测入门_基础网络与分类定位权衡.md (high) — Part3（Cubox stub 无高亮，全文充实）
  - 目标检测入门_特征复用与实时性.md (high) — Part4（Cubox stub 无高亮，全文充实）
  - SAM_Segment_Anything模型.md (high) — SAM（Cubox 1 处高亮：架构，已标重点）
- 概念页（concepts/）新建 15 个：两阶段检测、单阶段检测、Anchor机制、RoI_Pooling、检测评测指标、多尺度检测、NMS与Soft_NMS、数据增强_检测(medium)、Backbone设计范式、深度可分离卷积、通道注意力、位置敏感检测、特征金字塔网络、图像分割、Prompt驱动分割、Vision_Transformer、Focal_Loss
- 实体页（entities/）新建 13 个：R-CNN、YOLO、SSD、ResNet、SENet、R-FCN、FPN、MobileNet、COCO数据集、Mask_R-CNN(medium)、SAM、ViT(medium)、CLIP(medium)
- 已更新 wiki/index.md
- 全部内容基于全文，未使用模型自身知识补全
- 跳过：无（5 篇全文均有实质内容）

## 2026-06-29 ingest | DPP + SVD + 生成式AI + 优化器 + PyTorch模板（5 篇，基于全文）
- 本批次 5 篇文章，全文均来自 tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/，Cubox 文件均为 stub 无 Annotations 高亮
- 来源页（sources/）：
  - DPP行列式点过程.md (high) — DPP 多样性采样/L-Ensemble/Cholesky 贪婪算法（Cubox 无高亮）
  - 机器学习中SVD总结.md (high) — EVD/SVD 原理推导应用，面试向（Cubox 无高亮）
  - 浅入浅出_生成式AI.md (high) — 李宏毅生成式AI导论笔记（Cubox 无高亮）
  - 梯度下降优化器可视化解释.md (high) — 5 种优化器对比（Cubox 无高亮）
  - PyTorch训练代码模板.md (high) — 9 步训练模板（Cubox 无高亮）
- 概念页（concepts/）新建 11 个：Cholesky分解与DPP、行列式与多样性采样、特征值分解、奇异值分解SVD、矩阵分解方法(medium)、Transformer架构、大模型训练三阶段、Prompt工程方法、梯度下降优化器、早停EarlyStopping、PyTorch训练循环
- 实体页（entities/）新建 1 个：Adam优化器
- 已更新 wiki/index.md
- 全部内容基于全文，未使用模型自身知识补全；矩阵分解方法标 medium（全文仅列举多数未展开）
- 跳过：无（5 篇全文均有实质内容）

## 2026-06-26 ingest | DiT + OCR增强 + PyTorch增强 + Attention复杂度 + Normalization（5 篇，基于全文）
- 本批次 5 篇文章，全文均来自 tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/，高亮参考对应 Cubox 文件 Annotations
- 来源页（sources/）：
  - DiT_扩散模型与Transformer.md (high) — DiT 详解（Cubox 无高亮）
  - OCR的有效数据增强.md (high) — OCR 增强实战（Cubox 3 处高亮：工具库、形态学、噪声，已标重点）
  - PyTorch图像增强方法总结.md (high) — 13 个 torchvision 增强（Cubox 无高亮）
  - Attention复杂度解析与改进方向.md (high) — 注意力复杂度与 FlashAttention（Cubox 无高亮）
  - Normalization方法总结_BN_LN_IN_GN.md (high) — BN/LN/IN/GN 对比（Cubox 无高亮）
- 概念页（concepts/）新建 11 个：扩散模型、Latent_Diffusion、Patchify、adaLN_Zero、OCR数据增强、torchvision图像增强、自注意力复杂度、FlashAttention、Normalization方法对比、Batch_Normalization
- 实体页（entities/）新建 3 个：DiT、Albumentations、FlashAttention
- 已更新 wiki/index.md
- 全部内容基于全文，未使用模型自身知识补全
- 跳过：无（5 篇全文均有实质内容）

## 2026-06-26 ingest | RAG从入门到精通系列1-5（5 篇，基于全文）
- 本批次 5 篇文章，全文均来自 tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/，高亮参考对应 Cubox 文件 Annotations
- 来源页（sources/）：
  - RAG基础_索引检索生成.md (high) — 系列1：Indexing/Retrieval/Generation 基础（Cubox 无高亮）
  - RAG查询翻译_Query_Translation.md (high) — 系列2：Multi-Query/RAG Fusion/Decomposition/Step-back/HyDE（Cubox 无高亮）
  - RAG路由_Routing.md (high) — 系列3：Logical/Semantic Routing（Cubox 无高亮）
  - RAG查询构造_Query_Construction.md (high) — 系列4：自然语言转结构化查询（Cubox 无高亮）
  - RAG索引进阶_Indexing.md (high) — 系列5：Multi-representation/RAPTOR/ColBERT（Cubox 3 处高亮，已标重点）
- 概念页（concepts/）新建 11 个：RAG基础流程、Embedding与向量检索、向量数据库(medium)、Query_Translation、RAG_Fusion、HyDE、RAG_Routing、Query_Construction、Multi-representation_Indexing、RAPTOR索引、ColBERT
- 实体页（entities/）新建 3 个：LangChain(medium)、Qdrant(medium)、ColBERT
- 已更新 wiki/index.md
- 全部内容基于全文，未使用模型自身知识补全
- 跳过：无（5 篇全文均有实质内容）

## 2026-06-29 ingest | AI-Native Infra + AI Infra 系统设计 + PyTorch代码段 + RL Infra全景 + 智能体能力金字塔（5 篇，基于全文）
- 本批次 5 篇文章，全文均来自 tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/，高亮参考对应 Cubox 文件 Annotations
- 来源页（sources/）：
  - AI-Native的Infra演化路线L0到L5.md (high) — L0-L5 能力成熟度模型（Cubox 无高亮）
  - 入局AI_Infra系统设计与挑战.md (high) — AI Infra vs 传统 Infra 全拆解（Cubox 无高亮）
  - PyTorch常用代码段合集.md (high) — 5 大类代码段 + Tips（Cubox 无高亮）
  - RL_Infra行业全景.md (high) — RL 环境/RLaaS/数据（Cubox 高亮 1 处：Mechanize 复制训练，已标重点）
  - RL环境与智能体能力金字塔.md (high) — 智能体能力金字塔（Cubox 无高亮）
- 概念页（concepts/）新建 17 个：AI-Native_Infra、L0-L5能力成熟度模型、Result-as-a-Service、模型并行、CUDA_Graph、KV_Cache、连续批处理、通信计算重叠、Label_Smoothing(medium)、Mixup训练(medium)、学习率调度、RL环境、RLaaS、复制训练、RLVR、智能体能力金字塔、接地气Groundedness
- 实体页（entities/）新建 5 个：PyTorch、vLLM、Mechanize、Fireworks_AI、Surge_AI；更新 1 个：Megatron（追加来源）
- 已更新 wiki/index.md
- 全部内容基于全文，未使用模型自身知识补全
- 跳过：无（5 篇全文均有实质内容）

## 2026-06-26 ingest | RAG文本切分系列 Level 1-4（5 篇，基于全文）
- 本批次 5 篇文章，全文均来自 tmp/Cubox-批量导出文章-所有收藏-205 收藏-全文/，高亮参考对应 Cubox 文件 Annotations
- 来源页（sources/）：
  - RAG文本切分_字符切分.md (high) — Level 1 字符切分基础 + 五层级框架（Cubox 无高亮）
  - RAG文本切分_递归字符切分.md (high) — Level 2 递归字符分割（Cubox 无高亮）
  - RAG文本切分_token优化.md (high) — Level 2 token 优化（Cubox 无高亮）
  - RAG文本切分_JSON文档切分.md (high) — Level 3 JSON 文档切分（Cubox 无高亮）
  - RAG文本切分_语义切分.md (high) — Level 4 基于向量模型的语义切分（Cubox 高亮 2 处：语义切分原理、梯度方法，已标重点）
- 概念页（concepts/）新建 7 个：文本切分五层级、字符切分、Chunk_Size与Overlap、递归字符切分、Token切分优化、文档结构切分、语义切分
- 实体页（entities/）新建 1 个：LlamaIndex(medium)；更新 1 个：LangChain（追加文本切分能力与来源）
- 已更新 wiki/index.md
- 全部内容基于全文，未使用模型自身知识补全
- 跳过：无（5 篇全文均有实质内容）

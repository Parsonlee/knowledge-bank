# Wiki Index

> 内容索引，每次 ingest 后更新。按类型分组。

## Sources

- [[大模型显存计算与优化]] — Transformer 大模型训练/推理显存计算公式与优化（LLM/inference, Infra/gpu）
- [[目标检测入门_经典模型]] — R-CNN/Fast/Faster R-CNN、YOLO、SSD 经典检测模型综述（CV/detection）
- [[目标检测入门_评测与训练技巧]] — mAP/IoU 评测指标、VOC/COCO 数据集、训练 tricks（CV/detection）
- [[目标检测入门_基础网络与分类定位权衡]] — ResNet/Xception/ResNeXt/SENet/NASNet backbone 演进与 R-FCN/DCN（CV/detection）
- [[目标检测入门_特征复用与实时性]] — FPN/TDM/DSSD/RefineDet 特征金字塔与 YOLOv2/Light-Head/SSDLite 实时检测（CV/detection）
- [[SAM_Segment_Anything模型]] — Meta AI SAM 架构/训练/Prompt 驱动分割（CV）
- [[DiT_扩散模型与Transformer]] — 用 Transformer 替换扩散模型 U-Net，缩放性与 adaLN-Zero（CV/arch）
- [[OCR的有效数据增强]] — OCR 手写识别数据增强：形态学/噪声/变换 + albumentations（CV/data-augmentation）
- [[PyTorch图像增强方法总结]] — 13 个 torchvision.transforms 增强方法附代码（CV/data-augmentation）
- [[Attention复杂度解析与改进方向]] — 自注意力复杂度、FlashAttention 1/2/3、高效注意力（LLM/arch/attention）
- [[Normalization方法总结_BN_LN_IN_GN]] — BN/LN/IN/GN 归一化方法对比（DeepLearning, 面试）

## Concepts

- [[概念_显存组成与估算]] — 显存消耗组成、各组件估算公式、估算误差
- [[概念_训练并行策略]] — TP/SP/PP/DP/Zero、3D 并行对显存的影响
- [[概念_激活值重计算]] — 重计算原理及不同并行组合的激活值公式
- [[概念_Zero显存优化]] — Zero1/2/3 三种策略与计算公式
- [[概念_两阶段检测]] — Region-based 两阶段范式：Proposal → 分类回归
- [[概念_单阶段检测]] — Region-free 单阶段范式：YOLO/SSD 直接回归
- [[概念_Anchor机制]] — 多尺度多宽高比参考框，检测回归基准
- [[概念_RoI_Pooling]] — 候选区域映射为等长特征向量；RoIAlign 消除量化误差
- [[概念_检测评测指标]] — IoU/mAP(VOC/COCO)/FPS
- [[概念_多尺度检测]] — 多尺度输入/特征图提升检测鲁棒性
- [[概念_NMS与Soft_NMS]] — 非极大抑制与软化版本
- [[概念_数据增强_检测]] — 检测任务数据增强需同步变换标注框
- [[概念_Backbone设计范式]] — Repeat/Multi-path/Skip-connection 三范式
- [[概念_通道注意力]] — SENet Squeeze-Excitation 通道注意力
- [[概念_深度可分离卷积]] — Depthwise + Pointwise 分解，大幅减少计算量
- [[概念_位置敏感检测]] — R-FCN Position Sensitive Score Maps / DCN 可变形卷积
- [[概念_特征金字塔网络]] — FPN 自顶向下多尺度融合及变体
- [[概念_图像分割]] — 语义/实例/交互式分割，SAM 统一为 Prompt 驱动
- [[概念_Prompt驱动分割]] — SAM 多种 Prompt 类型驱动分割
- [[概念_Vision_Transformer]] — ViT 将图像 patch 化输入 Transformer
- [[概念_Focal_Loss]] — 下调简单样本权重解决类别不平衡
- [[概念_扩散模型]] — 前向加噪 + 反向去噪生成；DDPM 开创
- [[概念_Latent_Diffusion]] — 先 AutoEncoder 压缩到 latent 再训扩散模型
- [[概念_Patchify]] — 图像/latent 切 patch 经线性嵌入为 token
- [[概念_adaLN_Zero]] — DiT 最优条件注入，初始化为恒等映射
- [[概念_OCR数据增强]] — OCR 形态学/噪声/变换 + OneOf 组合
- [[概念_torchvision图像增强]] — torchvision.transforms 增强 API 清单
- [[概念_自注意力复杂度]] — 自注意力 O(N²d)/O(N²)，瓶颈在内存 I/O
- [[概念_FlashAttention]] — I/O 感知精确注意力，分块 + 在线 Softmax
- [[概念_Normalization方法对比]] — BN/LN/IN/GN 维度与用途对比
- [[概念_Batch_Normalization]] — BN 动机/算法/作用/问题

## Entities

- [[实体_DeepSpeed]] — 分布式训练框架，ZeRO 系列策略来源
- [[实体_Megatron]] — NVIDIA 并行框架，激活值/重计算公式来源
- [[实体_R-CNN]] — R-CNN 系列，开创两阶段检测范式
- [[实体_YOLO]] — 首个单阶段检测器，YOLOv2 全面升级
- [[实体_SSD]] — 多尺度特征图单阶段检测基线
- [[实体_ResNet]] — 残差学习，检测标准 Backbone
- [[实体_SENet]] — 通道注意力，ILSVRC 最后一届冠军
- [[实体_R-FCN]] — 全卷积位置敏感检测
- [[实体_FPN]] — 特征金字塔网络，检测标配组件
- [[实体_MobileNet]] — 深度可分离卷积轻量网络，移动端部署
- [[实体_COCO数据集]] — 80 类像素级实例标注，检测/分割主流基准
- [[实体_Mask_R-CNN]] — 实例分割，提出 RoIAlign
- [[实体_SAM]] — Meta AI 图像分割基础模型
- [[实体_ViT]] — Vision Transformer，SAM 图像编码器
- [[实体_CLIP]] — 视觉-语言对齐模型，为 SAM 提供文本 Prompt
- [[实体_DiT]] — Diffusion Transformer，扩散模型 SOTA 架构
- [[实体_Albumentations]] — Python 图像增强库，OneOf/Compose 组合
- [[实体_FlashAttention]] — I/O 感知精确注意力，长上下文行业标准

## Comparisons

## Overview

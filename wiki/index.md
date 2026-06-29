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
- [[DPP行列式点过程]] — DPP 多样性采样、L-Ensemble、Cholesky 贪婪算法（DeepLearning）
- [[机器学习中SVD总结]] — 特征值分解/SVD 原理、推导与应用（DeepLearning, 面试）
- [[浅入浅出_生成式AI]] — 生成式 AI 入门：Transformer/Prompt/训练三阶段/Agent（DeepLearning）
- [[梯度下降优化器可视化解释]] — Vanilla GD/Momentum/AdaGrad/RMSProp/Adam 对比（DeepLearning）
- [[PyTorch训练代码模板]] — PyTorch 训练 9 步模板：超参/模型/数据/训练/早停/绘图/预测（DeepLearning, Skill/python/pytorch）
- [[AI-Native的Infra演化路线L0到L5]] — AI-Native Infra 的 L0-L5 能力成熟度模型与 Result-as-a-Service（Infra/AI）
- [[入局AI_Infra系统设计与挑战]] — AI Infra vs 传统 Infra：硬件/软件/训练/推理挑战全拆解（Infra/AI）
- [[PyTorch常用代码段合集]] — PyTorch 5 大类常用代码段 + 实用 Tips（Skill/python/pytorch, DeepLearning）
- [[RL_Infra行业全景]] — RL 环境/RLaaS/数据三大模块，RL 的 GPT-3 时刻（LLM/training/RL, Infra/AI）
- [[RL环境与智能体能力金字塔]] — Surge AI 智能体能力金字塔：工具/规划/适应/接地气/常识推理（LLM/training/RL, Infra/AI）
- [[RAG基础_索引检索生成]] — RAG 基础流程：Indexing/Retrieval/Generation + LangChain/Qdrant 实现（RAG）
- [[RAG查询翻译_Query_Translation]] — Query Translation：Multi-Query/RAG Fusion/Decomposition/Step-back/HyDE（RAG, RAG/query）
- [[RAG路由_Routing]] — Routing：Logical/Semantic 路由智能选择检索路径（RAG）
- [[RAG查询构造_Query_Construction]] — Query Construction：自然语言转元数据结构化查询（RAG, RAG/query）
- [[RAG索引进阶_Indexing]] — 进阶索引：Multi-representation/RAPTOR/ColBERT（RAG, RAG/chunking）
- [[RAG文本切分_字符切分]] — 文本切分系列1：Level 1 字符切分基础 + 五层级框架（RAG, RAG/chunking）
- [[RAG文本切分_递归字符切分]] — 文本切分系列2：Level 2 递归字符分割（RAG, RAG/chunking）
- [[RAG文本切分_token优化]] — 文本切分系列2.5：递归切分的 token 优化（RAG, RAG/chunking）
- [[RAG文本切分_JSON文档切分]] — 文本切分系列3：Level 3 JSON 文档结构切分（RAG, RAG/chunking）
- [[RAG文本切分_语义切分]] — 文本切分系列4：Level 4 基于向量模型的语义切分（RAG, RAG/chunking）

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
- [[概念_Cholesky分解与DPP]] — Cholesky 分解加速 DPP 贪婪 MAP 推断，O(N·k²)
- [[概念_行列式与多样性采样]] — 行列式=超平行体体积=多样性度量，DPP 数学基础
- [[概念_特征值分解]] — EVD 方阵分解，特征值/特征向量/几何意义
- [[概念_奇异值分解SVD]] — 任意矩阵分解 A=UΣV^T，降维/压缩基础工具
- [[概念_矩阵分解方法]] — PCA/SVD/NMF/LDA/PMF 等方法清单与作用
- [[概念_Transformer架构]] — Transformer 5 步流程：Tokenization/Embedding/Attention/FFN/Output
- [[概念_大模型训练三阶段]] — Pre-train/Instruction FT/RLHF 训练流程
- [[概念_Prompt工程方法]] — 有效 Prompt 方法：补充前提/范例/拆解/自我反省/Self-Consistency
- [[概念_梯度下降优化器]] — Vanilla GD/Momentum/AdaGrad/RMSProp/Adam 原理对比
- [[概念_早停EarlyStopping]] — 监控 val_loss 提前停止训练避免过拟合
- [[概念_PyTorch训练循环]] — PyTorch 标准训练 9 步流程模板
- [[概念_AI-Native_Infra]] — 专为 AI 设计、去掉人类兜底层的基础设施范式
- [[概念_L0-L5能力成熟度模型]] — AI 从模仿人类到掌控 OS 的 L0-L5 演进
- [[概念_Result-as-a-Service]] — 人类只表达需求验收结果、AI 负责全实现的终极形态
- [[概念_KV_Cache]] — 缓存 K/V 已计算结果，空间换时间避免重复计算
- [[概念_CUDA_Graph]] — 多 GPU 操作转 DAG 一次性提交，减少 CPU-GPU 交互
- [[概念_模型并行]] — 拆分大模型到多 GPU，解决单机存不下
- [[概念_连续批处理]] — 动态批处理，短请求完成即释放、新请求随时加入
- [[概念_通信计算重叠]] — 用 GPU stream 令计算与通信时间上重叠
- [[概念_Label_Smoothing]] — 软化硬标签缓解过度自信（medium）
- [[概念_Mixup训练]] — Beta 分布插值混合样本图像与标签（medium）
- [[概念_学习率调度]] — ReduceLROnPlateau/Cosine/MultiStep/Warmup 调度器
- [[概念_RL环境]] — Agent 学习的虚拟世界：状态/任务/奖励三要素
- [[概念_RLaaS]] — 强化学习即服务，Palantir 式企业深度定制
- [[概念_复制训练]] — 复现现有软件作为 RL 任务，单元测试验证奖励
- [[概念_RLVR]] — 可自动验证奖励的强化学习
- [[概念_智能体能力金字塔]] — 工具/规划/适应/接地气/常识推理五层能力
- [[概念_接地气Groundedness]] — 智能体紧贴上下文、不幻觉不捏造的能力

### RAG
- [[概念_RAG基础流程]] — RAG 三步：Indexing/Retrieval/Generation
- [[概念_Embedding与向量检索]] — 文本转嵌入向量，按相似度检索 top-k
- [[概念_向量数据库]] — Vector Store 存储嵌入向量并计算相似度（medium）
- [[概念_Query_Translation]] — 查询翻译：改写/分解/退一步提升检索
- [[概念_RAG_Fusion]] — 多查询 + RRF 排序融合检索结果
- [[概念_HyDE]] — 生成假设文档作为检索输入
- [[概念_RAG_Routing]] — 逻辑路由/语义路由智能选择检索路径
- [[概念_Query_Construction]] — 自然语言转元数据结构化查询
- [[概念_Multi-representation_Indexing]] — 摘要+原文多表示索引（Proposition Indexing）
- [[概念_RAPTOR索引]] — 树状分层索引：GMM/UMAP/多尺度聚类递归摘要
- [[概念_ColBERT]] — token 级嵌入 late interaction 细粒度检索
- [[概念_文本切分五层级]] — 文本切分 Level 1-5 框架：字符/递归/文档/语义/Agentic
- [[概念_字符切分]] — Level 1 简单字符长度切分
- [[概念_Chunk_Size与Overlap]] — 块大小与块重叠两个基础参数
- [[概念_递归字符切分]] — Level 2 分隔符递归合并，实践首选
- [[概念_Token切分优化]] — 按 token 而非字符计长度，对齐模型处理
- [[概念_文档结构切分]] — Level 3 适配 JSON/Markdown/代码等格式
- [[概念_语义切分]] — Level 4 向量差异超阈值切分，四种阈值方法

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
- [[实体_Adam优化器]] — 一阶矩+二阶矩自适应优化器，深度学习常用选择
- [[实体_PyTorch]] — 深度学习框架事实标准，动态计算图/自动微分/Python 优先
- [[实体_vLLM]] — 开源 LLM 推理框架，KV Cache/连续批处理/PagedAttention
- [[实体_Mechanize]] — RL 环境平台，复制训练（Replication Training）范式
- [[实体_Fireworks_AI]] — AI Inference Infra 公司，RFT 产品化
- [[实体_Surge_AI]] — RL 环境/数据公司，智能体能力金字塔框架
- [[实体_LangChain]] — LLM/RAG 应用框架，链式串联检索与生成（medium）
- [[实体_Qdrant]] — Rust 编写的开源向量数据库/向量搜索引擎（medium）
- [[实体_ColBERT]] — 斯坦福 token 级细粒度检索模型，MaxSim late interaction
- [[实体_LlamaIndex]] — LLM/RAG 应用框架，文档加载与切分（medium）

## Comparisons

## Overview

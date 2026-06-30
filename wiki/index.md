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
- [[RAG高级优化_问题生成检索增强]] — 基于问题生成丰富文本片段提高检索准确性（RAG, RAG/query）
- [[RAG高级优化_检索策略Fusion_HyDE]] — Fusion/HyDE 多路检索策略实战（RAG, RAG/retrieval）
- [[RAG高级优化_检索后处理]] — 检索后处理：压缩/重排/Long-text Reorder（RAG, RAG/retrieval）
- [[RAG高级优化_query转换之路]] — query 转换全景：重写/HyDE/子查询/Step-back（RAG, RAG/query）
- [[RAG文本切分_Markdown切分]] — Markdown 标题切分定制化方案（RAG, RAG/chunking）
- [[MRL_俄罗斯套娃表示学习]] — MRL 俄罗斯套娃嵌入技术，截断嵌入维度保留语义（RAG/embedding）
- [[Matryoshka嵌入模型概述_HuggingFace]] — HuggingFace MRL 训练原理、Sentence Transformers 实现与性能实验（RAG/embedding）
- [[从BM25到Multi-Vector_6种Embedding演进路线]] — Sparse/Dense/Quantized/Binary/Matryoshka/Multi-Vector 六种嵌入方案对比选型（RAG/embedding, RAG）
- [[一文详尽之Embedding]] — Embedding 全景综述：One-Hot 到 SimCSE，BERT 各向异性问题与优化（RAG/embedding）
- [[为什么用Qwen3_embedding和rerank]] — Qwen3 Embedding/Rerank 原理：[EOS] 池化、Instruct 机制、LLM 化重排（RAG/embedding, RAG）
- [[ColBERT原理与延迟交互机制]] — ColBERT 多向量表示、延迟交互(MaxSim)与稠密向量对比，BGE-M3 实验（RAG/embedding, RAG）
- [[ColBERTv2残差压缩演进]] — 早期/延迟交互、ColBERT→ColBERTv2 残差压缩(聚类+量化)，BGE-M3 4x 压缩实验（RAG/embedding, RAG）
- [[RAG综述_中科院2025]] — RAG 万字综述：核心组件/八步流程/高级 RAG(训练/多模态/记忆/Agentic)（RAG）
- [[ES企业AI搜索实践]] — Elasticsearch 向量搜索/混合检索/RRF/量化/Serverless 构建企业 RAG（RAG）
- [[向量数据库原理与应用全解析]] — 向量化演进、索引方法、相似度度量、主流向量数据库对比（RAG/embedding）
- [[RAG_12痛点与解决方案]] — 12 个 RAG 痛点及解决方案：重排序/Prompt压缩/查询转换/PDF提取/安全（RAG）
- [[斯坦福RAG新基线_DOS_RAG]] — DOS RAG：检索后按原文顺序排列，持平或超越 RAPTOR/ReadAgent（RAG）
- [[DMQR-RAG_多样查询改写]] — DMQR-RAG 四种改写策略 + 自适应选择，P@5 提升 14.46%（RAG, RAG/query）
- [[RAG挑战赛冠军方案]] — 企业年报 RAG 冠军：Docling 解析/FAISS/LLM重排序/多路由器/CoT+SO（RAG）
- [[提升RAG问答质量的技术路线]] — RAG 技术路线总览：Query Translation/Routing/Construction/Indexing/CRAG/Self-RAG（RAG）
- [[阿里RAG技术演进]] — 阿里云服务 RAG 四大命题：数据价值/异构检索/生成控制/评估体系（RAG）
- [[美团搜索查询改写实践]] — 美团查询改写全栈：离线挖掘/BERT判别/SMT/NMT强化学习/向量化召回（RAG/query）
- [[优图RAG技术详解]] — 腾讯优图RAG全栈：2B Embedding/Reranker蒸馏/Text2SQL/GraphRAG知识树（RAG）
- [[RAG检索_Retrieval入门到精通]] — RAG系列6：Re-Rank/CRAG/Self-RAG 检索优化（RAG, RAG/retrieval）
- [[RAG系统设计_语义搜索与KG驱动选型]] — 语义搜索本质/Loss/距离/Embedding/向量库选型 + KG-RAG/Lazy Graph RAG（RAG/embedding, RAG）
- [[TableRAG_文本表格异构问答]] — 华为云 TableRAG：文本检索+SQL 混合推理，HeteQA 评测集（RAG）
- [[跨模态知识联邦与统一语义推理RAG]] — 枫清科技融合知识库+统一知识图谱处理异构知识（RAG）
- [[RAGAS评估RAG系统]] — RAGAS 框架五大核心指标科学评估 RAG 系统（RAG/eval）
- [[腾讯查询优化四大类综述]] — 腾讯 QO 综述：查询扩展/分解/消歧/抽象四大类（RAG, RAG/query）
- [[RAG综述_北大AIGC2024]] — 北大 PKU-DAIR RAG 综述：四大基础范式+五类提升方法+多模态应用+评估（RAG）
- [[OpenAI_LLM应用最佳实践]] — OpenAI DevDay 2023：Prompt Engineering/RAG/Fine-tuning 两轴优化路线图（LLM）
- [[A_Visual_Guide_to_Mamba_and_SSM]] — 50+ 可视化图解 Mamba/SSM 全流程：数学基础/离散化/选择扫描/硬件感知（LLM/arch/Mamba）
- [[Mamba_Explained_Kola_Ayonrinde]] — Mamba 直觉讲解：效率/有效性权衡、选择机制类比、State Swapping 范式（LLM/arch/Mamba）
- [[一文读懂Mamba_知乎]] — 中文解析 Mamba 论文：选择机制动机、作者背景（Albert Gu / Tri Dao）（LLM/arch/Mamba）
- [[Transformer被挑战_Mamba解析与PyTorch复现]] — Mamba 架构解析 + 完整 PyTorch 复现：S6/MambaBlock/RMSNorm/enwiki8 训练（LLM/arch/Mamba）
- [[Mamba2_SSD_大一统]] — Mamba2 SSD 框架：SSM 与 Attention 等价、半可分离矩阵、8倍推理加速（LLM/arch/Mamba）
- [[腾讯混元TurboS技术报告]] — 560B Hybrid Transformer-Mamba MoE 模型，业界首个大规模部署 Mamba 架构，自适应长短 CoT（LLM/arch/Mamba, LLM/arch/MoE）
- [[大模型面试面经_简单透彻理解MoE]] — MoE 结构原理、Router 机制、优缺点、PyTorch 示例代码（LLM/arch/MoE）
- [[手把手教你实现稀疏MoE语言模型]] — 从零 PyTorch 实现稀疏 MoE：Top-k/噪声 Top-k 门控、SparseMoE、完整训练循环（LLM/arch/MoE）
- [[从DeepSeek-V3到Kimi_K2_八种现代LLM架构大比较]] — Sebastian Raschka 对比 8 种 2025 LLM 架构：MLA/MoE/滑动窗口/Post-Norm/NoPE/Muon（LLM/arch）
- [[2025年七大顶流大模型架构]] — 7 大旗舰开源 LLM 架构创新点综述（LLM/arch, LLM/arch/MoE）
- [[Florence-2_微软视觉基础模型]] — 微软 Azure AI Florence-2：FLD-5B 数据集 + Seq2Seq 统一视觉任务（LLM/arch/VLM, CV/arch）
- [[从LLaVA到Qwen3-VL_多模态架构演进]] — LLaVA AnyRes vs Qwen3-VL DeepStack，MLLM 两大演进路线全景（LLM/arch/VLM）
- [[MiniMax_vs_Kimi_注意力路线之争]] — MiniMax M2 回归 Full Attention，Kimi Linear KDA+MLA 3:1，路线对比（LLM/arch/attention）
- [[DeepSeek_MLA矩阵吸收原理]] — MLA 矩阵吸收图解：K/V 升维矩阵吸收进 Q，三处广播优化（LLM/arch/attention）
- [[KV_Cache原理图解]] — KV Cache 图解：自回归推理缓存 K/V，显存估算，仅适用 Decoder（LLM/inference/kv-cache）
- [[推测解码Speculative_Decoding综述]] — Draft-then-Verify 无损推理加速：Independent/Self Drafting + 验证策略（LLM/inference）
- [[大模型显存占用单卡分析]] — 混合精度训练/KV Cache/LoRA/QLoRA 四场景单卡显存估算公式（LLM/inference, Infra/gpu, 面试）
- [[语义缓存_constraint_cache]] — constraint-cache：语义规范化缓存键，99.9% 命中率，毫秒响应（LLM/inference）
- [[思维链CoT高级提示技术]] — CoT/CoT-SC/Decoding CoT/ToT+MCTS 推理技术综述与成本权衡（LLM/reasoning）
- [[自适应快慢思考推理模型]] — Qwen3 SFT混合思考、字节AdaCoT Pareto-PPO、清华AdaThinking约束优化三路方案（LLM/reasoning）
- [[DeepSeek-R1工作原理]] — DeepSeek-R1 GRPO+多阶段训练管道，达到 o1-1217 水平（LLM/reasoning, LLM/training/RL）
- [[DeepSeek-R1复现浪潮]] — UC伯克利/港科大/HuggingFace 以极低成本复现 R1-Zero，验证纯 RL 涌现推理（LLM/reasoning, LLM/training/RL）
- [[R1复现认知与误区]] — 一线视角：复现 R1 四大关键（基模/数据/infra/超参）与四大误区（LLM/reasoning, LLM/training/RL）
- [[从CoT到Agent综述_上交]] — 上交综述：CoT 三条路径（Prompt/结构/应用）及 CoT 赋能 Agent 感知/记忆/推理（LLM/reasoning, AI-Agent）
- [[强化学习入门指南_RLHF到GRPO]] — Unsloth：RLHF→PPO→GRPO→RLVR 原理+奖励函数设计+实战技巧（LLM/training/RL）
- [[LoRA微调实战_Qwen2.5全流程]] — LoRA 低成本微调 Qwen2.5-0.5B 实战：数据/代码/超参/CPU 跑通全流程（LLM/training/post-train）
- [[三大Scaling_Law_预训练后训练推理]] — 预训练/后训练/推理阶段三大 Scaling Law 定义与技术手段（LLM/training）
- [[大规模神经网络优化_超参实践与规模律]] — GPT→LLaMA2 超参演进 + Kaplan/Chinchilla 规模律推导与拾遗（LLM/training）
- [[翁荔_LLM外在幻觉_原因检测抵抗]] — 翁荔 Blog：外在幻觉定义、产幻原因、FActScore/SAFE/CoVe/FLAME 检测与抵抗（LLM/hallucination）
- [[LLM_32种消除幻觉技术综述]] — 32 种幻觉消除技术：提示工程（RAG/反馈/提示微调）与模型开发（解码/KG/损失/SFT）（LLM/hallucination）
- [[大模型幻觉陷阱_AGI之路04期]] — 技术/传播/治理三维解构幻觉本质：长尾压缩→编造、专家之死、对齐税与责任归属（LLM/hallucination）
- [[Discrete_Tokenization多模态综述]] — 首个多模态LLM离散化综述：8类VQ方法（VQ/RVQ/FSQ/LFQ等）、码本坍塌与跨模态全景（LLM/tokenization）
- [[Transformer大模型3D可视化_NanoGPT]] — Brendan Bycroft 3D可视化逐层拆解 GPT-3/NanoGPT：Embedding/LN/Attention/MLP/Softmax（LLM/arch）
- [[LLM两年发展万字综述_2023-2025]] — 2023-2025年LLM三大支柱：MoE/MLA效率革命、Thinking推理模型、Agent工具使用（LLM/arch, LLM/reasoning）
- [[Andrej_Karpathy_LLM教学笔记]] — Karpathy教学视频总结：预训练数据管线/BPE/分布式训练/SFT/奖励建模/GRPO/Aha moment（LLM/arch, LLM/training）
- [[LLM面试50题_MIT_CSAIL]] — MIT CSAIL 工程师 Hao Hoang 整理的 50 个 LLM 核心面试题（LLM, 面试）
- [[大模型算法岗面试百问百答]] — 大模型算法岗面试知识点：RAG 体系/LLaMA 架构/SFT 方法/幻觉复读机（LLM, 面试）
- [[北大LLMs数据管理全流程综述]] — 北大综述：预训练+SFT 两阶段数据规模/质量/组合/管理系统（LLM/training）
- [[Jina_AI创业复盘]] — Jina AI 创始人肖涵六年复盘：两次 Pivot、AI 团队 Scaling Law 困惑、被 Elastic 收购（创业）
- [[GPT5通用验证器_Universal_Verifier]] — 通用验证器（Universal Verifier）技术全景：RLVR 局限→两大路线→OaK 终局（LLM/training/RL）
- [[蚂蚁集团大模型推荐算法与应用]] — 蚂蚁集团三条路径将LLM融入推荐：KG生产/教师蒸馏/种子用户池（LLM, Recommendation）
- [[从GPT-2到gpt-oss_OpenAI开放模型进化之路]] — Sebastian Raschka 深度解析 gpt-oss 架构 7 项进化与 Qwen3 对比、MXFP4 量化（LLM/arch/MoE）
- [[淘宝直播数字人_LLM文案生成技术]] — 淘宝直播数字人口语化改写(DPO 97%)、多源信息单步蒸馏、素材图文一致（LLM, LLM/arch/VLM）
- [[别再误会MCP了辟谣指南]] — 阿里云工程师以 SDK 源码法证 MCP CHS 三组件，Host 是 AI 智能唯一承载者（AI-Agent/tools）
- [[MCP加数据库]] — MCP+MongoDB Text-to-SQL 实战，结构化检索优于传统 RAG，含 Function Call 痛点与演进（AI-Agent/tools）
- [[MCP遇上代码执行]] — Anthropic：CodeAgent 模式调用 MCP，Token 减少 98.7%，隐私保护与 Skills 沉淀（AI-Agent/tools）
- [[MCP五大原语与Web化]] — MCP 联合创建者 David 解构五大原语，Web 化方向 OAuth 2.1 + Streamable HTTP（AI-Agent/tools）
- [[基于MCP的AI_Agent应用开发实践]] — 字节跳动 Agent TARS：MCP 前后端分离类比、工程实践与 Roadmap（AI-Agent/tools）
- [[HumanInTheLoop用MCP实现]] — 阿里云 OpenLM：send_inquiry+MCP Notification 实现服务端 HITL，含 Proxy 代理和 YOLO 模式（AI-Agent/tools）
- [[如何让Agent规划调用工具]] — 蚂蚁集团：「思考和规划」工具强制结构化规划，航空客服提升 54%，选 DeepSeek V3 而非 R1（AI-Agent/tools）
- [[Qwen3混合部署与MCP]] — 阿里云：Qwen3-0.6b 本地做工具选择节省 token，Qwen3-235b-a22b 生成结果（AI-Agent/tools）
- [[Anthropic多智能体研究系统构建]] — Anthropic：orchestrator-worker 研究系统，多智能体比单智能体提升 90.2%，8条提示词原则（AI-Agent/multi-agent）
- [[Context_Engineering_LangChain_Manus_NotebookLM]] — LangChain × Manus 对话提炼：4条反直觉原则——战略边界/可逆压缩/工具分层卸载/简化优先（AI-Agent/context-engineering）
- [[AI应用实战_搞定复杂指令和工具膨胀]] — 阿里云联调造数：单Agent→多Agent，意图识别+工具引擎+逆向推导，工具100+→5个（AI-Agent/context-engineering）
- [[Manus创始人手把手拆解上下文工程]] — Peak 亲写：KV缓存/工具掩码/文件系统记忆/注意力复述/错误保留/Few-Shot多样性六大原则（AI-Agent/context-engineering）
- [[浅谈上下文工程_Claude_Code_Manus_Kiro]] — 提示工程→上下文工程→环境工程演进，Claude Code/Manus/Kiro三产品实践对比（AI-Agent/context-engineering）
- [[也许当前最好的上下文工程讲解_LangChain联合Manus]] — Lance Martin × Peak Ji 对话实录：压缩/总结两模式、隔离两模式、三层行动空间、避免过度工程化（AI-Agent/context-engineering）
- [[Agent工程能力思考记录]] — 大淘宝：LLM 时代核心业务资产重定义、多 Agent 协作机制、MCP 工程补充（权限/接入/长列表优化）（AI-Agent/coding）
- [[Anthropic再发Agent神文_像人类工程师一样思考解决长程任务难题]] — Anthropic 双 Agent 架构解决长程 Coding 任务：初始化 Agent + 编码 Agent + 功能列表/增量进展/端到端测试三支柱（AI-Agent/coding）
- [[万字长文深入浅出教你优雅开发复杂AI_Agent]] — 腾讯：Agent 三级进化/MCP+A2A 协议对比/CoT+ReAct+Plan-and-Execute 框架/Golang Eino+tRPC-A2A-Go 生产实践（AI-Agent/coding）
- [[从Copilot到通用Agent_阿里在AI_Coding上的应用和挑战]] — 阿里代码平台负责人：Copilot 两年演进瓶颈、IDE Agent + Aone Agent 双产品架构、通用 Agent 工程与模型挑战（AI-Agent/coding）
- [[从代码生成到自主决策_Coding驱动的自我编程Agent]] — 阿里云：Coding 驱动（Py4j 泛化调用）+ 仿脑区五功能区架构 + Segment 上下文工程 + 三层记忆体系（AI-Agent/coding）
- [[六位一线AI工程师总结_大模型应用一年心得]] — 六位工程师一年实战：Prompt/RAG/微调/Agent/评估全链路经验，实习生测试+LLM裁判+古德哈特定律（AI-Agent/coding）
- [[私域知识工程实战_让AI一次性写出高质量代码]] — 阿里云：三板斧（入职培训/知识驱动编程/自动维护）解决 AI 编程信息不对称，一次性输出符合项目规范代码（AI-Agent/coding）
- [[Claude_Agent_Skills_从第一性原理深入剖析]] — PaperAgent：Skills 元工具架构速览，SKILL.md 结构、四种模式、纯 LLM 推理技能选择（AI-Agent/skill）
- [[Agentic_Design_Patterns_中文翻译版]] — Antonio Gulli 著作中文翻译：21种 Agent 设计模式，核心/高级/集成/生产四类全景（AI-Agent/skill）
- [[从第一性原理深度拆解_Claude_Agent_Skill_宝玉]] — Han Lee/宝玉：源码级解构 Skills 双消息注入、isMeta 机制、contextModifier 执行上下文修改全生命周期（AI-Agent/skill）
- [[DeepResearch的概念、核心挑战与进化路径]] — 华为/利物浦/牛津综述：DR Agent 定义、四大核心挑战与未来进化路径（AI-Agent/deep-research）
- [[Tongyi DeepResearch的技术报告探秘]] — 魔搭社区解读：通义 DeepResearch 三阶段训练、IterResearch 范式、WebFrontier 数据合成与六大研发问题（AI-Agent/deep-research）
- [[一篇95页最新80种Deep Research系统全面综述]] — 浙大综述 80+ 系统，4 维分类法与单体/流水线/多智能体/混合四种架构（AI-Agent/deep-research）
- [[通义 DeepResearch：开源 AI 智能体的新纪元]] — 通义官方博客：全开源 Web Agent 完整技术全貌，Agentic CPT+SFT+RL 端到端训练与 Research-Synthesis 框架（AI-Agent/deep-research）
- [[AI智能体8种Memory策略与技术实现]] — 8 种记忆策略原理+模拟代码：全量/滑动窗口/相关性过滤/摘要/向量DB/知识图谱/分层/类OS内存管理（AI-Agent/memory）
- [[Agent记忆模块前沿研究简述]] — 机器之心综述：记忆分类体系+MemGPT/MemOS/MIRIX/G-Memory/M3-Agent前沿系统+五大挑战（AI-Agent/memory）
- [[OpenAI_构建AI智能体实用指南]] — OpenAI 官方指南（宝玉译）：Agent 三大基石/单一+主管+去中心化编排/分层安全护栏/HITL（AI-Agent/multi-agent）
- [[阿里云服务领域Agent构建方法论]] — 阿里云一年实战：广义/狭义定义之争/四大挑战/Workflow三代演化/Multi-Agent权衡/调优路径图（AI-Agent/prompt-engineering）
- [[程序员的提示工程实战手册]] — 10种提示技巧速查+调试/重构/功能实现三场景好坏提示对比+常见反模式修复（AI-Agent/prompt-engineering）
- [[用系统架构思维告别意大利面条式系统提示词]] — 系统提示词四层架构（核心定义/交互接口/内部处理/全局约束）替代扁平规则堆砌（AI-Agent/prompt-engineering）
- [[腾讯OlaChat_LLM智能数据分析平台实践]] — 腾讯 OlaChat：FlattenedRAG/StructuredRAG 元数据检索 + Text2SQL 微调+Agent + 多任务对话编排（AI-Agent/AI-BI）
- [[腾讯ABI工程架构探索与实践]] — OlaChat 工程架构：原子 Agent + DAG 编排 + 统一协议 + Text2DSL 中间层方案（AI-Agent/AI-BI）
- [[腾讯欧拉数据自治系统]] — 腾讯欧拉：生产即治理（耗散结构）+ 资产工场/tMetric/数据发现三产品 + Headless BI（AI-Agent/AI-BI）
- [[AI_Agent与AI_Workflow的区别和深度解析]] — AI Agent 自主决策 vs AI Workflow 预定义流程：四类 Agent + 五大 Workflow 优势（AI-Agent）
- [[Agent系统开发经验]] — 三种复杂性幻觉+三层复杂度（可运行/可复现/可进化）+LLM放大效应+系统化工程原则（AI-Agent）
- [[人工智能体AI_Agent开发与应用全面调研]] — 2023年全面调研：大脑/感知/行动框架 + 8大开源框架（AutoGPT/LangChain/AutoGen）+ 应用与挑战（AI-Agent）
- [[聊聊AI应用架构演进]] — 七步演进：基础调用→RAG→Guardrails→意图路由→模型网关→缓存→Agent模式，含推理优化（AI-Agent, 创业）
- [[企业落地NL2SQL_AI-ready_data与小模型]] — NL2SQL生产落地：AI-ready data + 小模型（3B/7B LoRA）+ 两级Schema Linking，幻觉率7.9%→1.3%（AI-Agent/AI-BI）
- [[FastAPI架构指南_项目模板与实战经验]] — 生产级 FastAPI 项目结构：Routers/Schemas/Services 三层分离 + 安全中间件 + Makefile（Skill/python）
- [[Python并发_async_await与FastAPI]] — FastAPI 官方文档：async/await 协程、并发 vs 并行、路径函数 def/async def 选择（Skill/python）
- [[Docker化Flask_Django应用从pip切换到uv]] — Nick Janetakis：Docker 项目 pip→uv，约 10x 提速，pyproject.toml/uv.lock/非 root（Skill/python）
- [[加速Python循环的12种方法]] — 12 种 for 循环优化：map 970x/set 498x/filterfalse 131x/lru_cache 57x（Skill/python）
- [[五个鲜为人知的Python功能]] — contextlib.suppress/setrecursionlimit/typing.Literal/__missing__/__subclasshook__（Skill/python）
- [[自动探索性数据分析EDA_10个Python包]] — D-Tale/Pandas-Profiling/Sweetviz/AutoViz/Dataprep 等 10 个自动 EDA 包对比与选型（Skill/python, Skill/data-analysis）
- [[Pandas一行代码绘制25种美图]] — DataFrame.plot/Series.plot 一行代码绘制 25 种图表（Skill/data-analysis）
- [[超强图解Pandas操作大全]] — 图解 Pandas 核心操作：排序/分组/连接/透视/索引（Skill/data-analysis, 面试）
- [[图解Pandas常用操作_NumPy对比与进阶]] — Pandas Illustrated 翻译：NumPy 对比/Series/DataFrame/MultiIndex 四部分（Skill/data-analysis, Skill/python, 面试）
- [[一行代码让matplotlib图表变高大上]] — dufte 库三个 API 自动美化 matplotlib 图表样式（Skill/data-analysis）
- [[600条Linux命令速查手册]] — 28 大类约 600 条 Linux 命令分场景速查手册（Skill/linux）
- [[现代打工人如何获得幸福]] — 评论尸：时间度量衡/幸福积分模型/天职/逃离职场PUA五种思维（Life）
- [[Gemini的PPT生成技巧与模板提示词]] — Gemini APP PPT 生成能力使用技巧与五套百搭风格提示词（AIGC）
- [[How_to_prompt_Veo3_Replicate]] — Replicate 官方 Veo 3 提示词指南：七要素/角色一致性/音频/风格/自拍（AIGC）
- [[Google_Veo3账号获取与提示技巧全攻略]] — Veo3 免费获取账号方法+Flow平台使用+提示技巧全攻略中文版（AIGC）
- [[九大主流AI_PPT横测]] — 九大 AI PPT 工具横测：AI原生派vs传统革新派，最后一公里难题（AIGC）
- [[一套提示词实现封面自由]] — 模块化封面生成提示词：小红书/公众号封面+十套风格，DeepSeek V3 也能用（AIGC）
- [[Nano-Banana_Pro论文绘图教程]] — 「架构师→渲染器→编辑器」三步工作流，VISUAL SCHEMA 驱动 Gemini 2.5 Flash Image 生成 CVPR/NeurIPS 学术插图（AIGC）
- [[关于Nano_Banana的一些浅思]] — Gemini 2.5 Flash Image 功能/提示词模板全解析+普通人与大模型协作哲学/Vibe Coding 三阶段实践（AIGC）
- [[超详细提示词教程_玩转Wan2.2]] — 通义万相 2.2 文生视频提示词完整词典：基础/进阶/图生视频公式 + 9大维度美学控制（AIGC）
- [[淘宝直播数字人_TTS语音合成技术]] — 淘天直播 AIGC 团队：TTS 数据管线 + V1→V4 四代模型演进（CosyVoice2+vLLM）（TTS）
- [[Foundation_Sprint产品验证完全指南]] — 谷歌 Jake Knapp 的 Foundation Sprint：10 小时奠定战略基础，基础/差异化2x2/Magic Lenses 三阶段 + 创始假设（创业）
- [[RLMRec_港大百度LLM推荐算法]] — 港大联合百度：互信息最大化对齐 CF 表征与 LLM 语义表征，即插即用去噪增强（Recommendation）
- [[阿里云大模型落地RIDE方法论与RaaS实践]] — 阿里云 CIO 蒋林泉：RIDE 四步方法论 + RaaS 结果即服务 + 翻译/Agent 两模式 + 数字人管理（创业）
- [[Superhuman_PMF引擎方法论]] — Superhuman 把 PMF 量化为可优化指标的四步引擎，22%→58%，ARR 3500 万美元（创业）
- [[Bundle_Unbundle视角看AI时代机会]] — 42章经：Grammarly 案例 + Shishir Bundle 理论(MCC/2x2) + 集装箱历史类比 AI（创业）
- [[100家顶尖AI初创公司的7个真相]] — Leonis AI 100：高人效/倒漏斗GTM/多赢家/快速转型/阈值解锁/收入激增/研究型创始人（创业）

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
- [[概念_向量数据库]] — 专用于存储向量化表示的系统，ANN 索引+相似度查询
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
- [[概念_问题生成检索增强]] — LLM 为文本片段生成问题，增强向量检索匹配
- [[概念_Fusion_Retrieval]] — 稀疏(BM25)+稠密(向量)双路检索融合
- [[概念_Reciprocal_Rank_Fusion]] — RRF 排序融合多路检索结果
- [[概念_BM25]] — 经典稀疏检索算法，词频+文档长度惩罚
- [[概念_检索后处理]] — 检索后重排/压缩/Long-text Reorder
- [[概念_Contextual_Compression]] — LLM 提取检索文档中与查询相关的片段
- [[概念_Long-text_Reorder]] — 长文本检索结果重排，重要文档置首尾
- [[概念_查询重写]] — LLM 改写用户查询提升检索效果
- [[概念_子查询分解]] — 复杂查询拆为子查询分别检索再合并
- [[概念_Step-back提示]] — 退一步生成更抽象的查询获取更广泛上下文
- [[概念_Markdown标题切分]] — 按 Markdown 标题层级结构化切分文档
- [[概念_Matryoshka表示学习]] — MRL 嵌套学习多粒度表征，可截断维度保留语义
- [[概念_Sparse_Embedding]] — 关键词式稀疏向量（TF-IDF/BM25/SPLADE）
- [[概念_Dense_Embedding]] — 语义级稠密向量，通用语义搜索首选
- [[概念_Quantized_Embedding]] — float32→int8 压缩，省内存磁盘
- [[概念_Binary_Embedding]] — 0/1 二值化极致压缩，设备端离线快搜
- [[概念_词向量]] — Word2Vec/GloVe/FastText 静态词向量及其局限
- [[概念_BERT各向异性]] — BERT 词向量锥形分布导致相似度失效及优化
- [[概念_Sentence-BERT]] — 孪生/三级网络微调 BERT 优化句向量相似度
- [[概念_SimCSE]] — Dropout mask 增广 + 对比学习优化句向量
- [[概念_Instruct_Embedding]] — 编码查询时附带任务指令引导多维度检索
- [[概念_重排序Rerank]] — 检索后相关性精排，Qwen3 LLM 化 yes/no 打分
- [[概念_ColBERTv2残差压缩]] — k-means 聚类+残差量化，存储减 6-10 倍性能损失 1-2%
- [[概念_混合检索]] — 稀疏+稠密+BM25 多路召回融合(RRF/加权)
- [[概念_近似最近邻搜索]] — ANNS：哈希/树/图/量化四类加速方法
- [[概念_向量索引方法]] — Flat/Tree/LSH/IVF-PQ/HNSW 索引类型对比
- [[概念_向量相似度度量]] — L2/L1/余弦/内积/汉明/杰卡德距离度量
- [[概念_向量量化]] — float32→int8/INT4/BBQ/PQ/残差量化压缩方法
- [[概念_Agentic_RAG]] — 智能体+RAG：查询规划/工具利用/推理优化
- [[概念_Memory_RAG]] — 显式记忆增强 RAG：Memory3/MemoRAG/CAG
- [[概念_知识整合]] — 输入层/中间层/输出层三种外部知识整合方式
- [[概念_DOS_RAG]] — 保留文档原始结构：检索后按原文顺序排列片段
- [[概念_DMQR-RAG]] — 多样化多查询改写：GQR/KWR/PAR/CCE 四策略 + 自适应选择
- [[概念_LLM重排序]] — 让 LLM 给文本相关性打分(0~1)的精排方法
- [[概念_父页面检索]] — 小块检索定位、完整父页面入上下文
- [[概念_表格序列化]] — 大表格转一系列上下文独立字符串
- [[概念_多查询路由]] — 路由到数据库/提示词/复合查询拆解
- [[概念_结构化输出]] — 强制 LLM 按 schema 输出 JSON，与 CoT 结合
- [[概念_Prompt_Compression]] — 检索后压缩上下文，LongLLMLingua（medium）
- [[概念_CRAG]] — 纠正型 RAG：评估文档相关性触发额外检索（medium）
- [[概念_Self-RAG]] — 自我反思 RAG：生成后自检决定是否补检索（medium）
- [[概念_Adaptive-RAG]] — 自适应 RAG：按查询复杂度选择检索生成策略（medium）

#### 阿里/美团/优图实践概念（批次7）
- [[概念_知识图谱RAG]] — 图结构组织知识，多跳推理跨文档关联检索
- [[概念_RAR相关性过滤]] — 检索增强相关性，赋予 LLM 判断"不相关"能力
- [[概念_RAG_Diagnoser]] — 原子事实粒度的细粒度 RAG 评估体系
- [[概念_迭代式检索]] — 首次无效时分层递进查询，避免一次性检索污染
- [[概念_SMT查询改写]] — 统计翻译模型查询改写，噪声信道+BeamSearch+XGBoost
- [[概念_强化学习NMT改写]] — NMT 改写以搜索系统为环境强化学习优化
- [[概念_向量化召回改写]] — 双塔向量从候选池 ANN 召回改写词（模糊改写）
- [[概念_协同训练]] — NMT-BERT 半监督互训提升数据和模型质量
- [[概念_分层知识蒸馏]] — Reranker 多层输出约束，支持层级输出能力
- [[概念_Embedding训练管线]] — 多阶段对比学习+精细数据工程+多任务均衡
- [[概念_Text2SQL]] — 自然语言转 SQL，MAC-SQL 多智能体框架
- [[概念_GraphRAG]] — 图/树结构组织知识的检索增强生成
- [[概念_知识树结构]] — 融合图与树优点的四级知识粒度树型图谱
- [[概念_S2Dual社区检测]] — Structure+Semantics 双感知社区检测，超越 Leiden

#### 语义搜索/系统设计/评估概念（批次8）
- [[概念_Semantic_Search本质]] — metric embedding，document as index，无结构即灵活
- [[概念_Multi-Vector检索]] — 用代理表示（自然语言/总结）索引低资源/长文件
- [[概念_对比损失与三元组损失]] — Contrastive/Triplet Loss 按类内方差选择
- [[概念_距离函数选择]] — 余弦(非度量)/欧氏(度量)距离选型与三角不等式
- [[概念_Lazy_Graph_RAG]] — 语义搜索弥补 KG 不足，索引成本降至 0.1%（medium）
- [[概念_迭代式表格推理]] — TableRAG 在线推理：拆解/检索/SQL/组合四步
- [[概念_融合知识库]] — 多元异构数据统一逻辑存储，物理存储不变
- [[概念_统一知识图谱]] — 多模态元素统一图谱，N度扩展查询提取子图
- [[概念_RAG评估框架RAGAS]] — RAGAS 检索侧/生成侧多维评估指标

#### 腾讯QO/北大综述/OpenAI最佳实践概念（Phase2 收尾）
- [[概念_查询扩展]] — 内部扩展(LLM知识)+外部扩展(知识库)提高检索效果
- [[概念_查询消歧]] — 识别消除查询歧义，确保单一精确解释
- [[概念_查询抽象]] — 提炼核心概念创建高层次表示，Step-back 为具体实现
- [[概念_RAG四大基础范式]] — 基于查询/隐空间/概率/投机四种检索-生成交互方式（RAG）
- [[概念_RAG五类提升方法]] — 输入/检索器/生成器/结果/流程五类 RAG 增强方法（RAG）
- [[概念_自适应检索]] — 基于规则或模型判断是否需要检索，避免过度检索（RAG）
- [[概念_迭代RAG]] — 迭代检索和生成，循环直到输出达标（RAG）
- [[概念_LLM应用优化两轴]] — Context Optimization(RAG) + LLM Optimization(FT) 两轴并行迭代（LLM）
- [[概念_Fine-tuning]] — 微调增强 LLM 特定领域/任务能力，蒸馏降本（LLM）

### LLM/arch/Mamba（批次 Mamba）
- [[概念_状态空间模型SSM]] — SSM 两方程：状态方程/输出方程，A/B/C/D 矩阵（LLM/arch/Mamba）
- [[概念_SSM三种表示]] — 连续/循环/卷积三种等价表示，训练用卷积、推理用循环（LLM/arch/Mamba）
- [[概念_SSM离散化]] — ZOH 离散化 + 步长参数 Δ，连续 SSM 转为离散序列模型（LLM/arch/Mamba）
- [[概念_HiPPO矩阵]] — Legendre 多项式系数构造矩阵 A，压缩并记忆长程历史（LLM/arch/Mamba）
- [[概念_线性时不变LTI]] — LTI 局限：A/B/C 固定导致无内容感知，选择机制的动机（LLM/arch/Mamba）
- [[概念_Mamba选择机制]] — B/C/Δ 输入依赖，实现 content-aware 推理（LLM/arch/Mamba）
- [[概念_Mamba硬件感知算法]] — parallel scan + kernel fusion + recomputation，GPU 高效实现（LLM/arch/Mamba）
- [[概念_MambaBlock架构]] — 投影+1DConv+SelectiveSSM+残差，Mamba1/2 Block 结构（LLM/arch/Mamba）
- [[概念_状态空间对偶SSD]] — Mamba2 核心：SSM 与线性 Attention 数学等价（LLM/arch/Mamba）
- [[概念_半可分离矩阵]] — SSM 变换矩阵的代数结构，SSD 算法分块分解基础（LLM/arch/Mamba）
- [[概念_State_Swapping]] — Mamba 特有推理范式：预生成 state 复用，无需 few-shot（LLM/arch/Mamba）

### LLM/arch/MoE（批次 MoE+arch）
- [[概念_MoE混合专家]] — 稀疏专家层替换 FFN，相同计算预算实现更大模型容量（LLM/arch/MoE）
- [[概念_MoE_Router]] — Top-k 门控网络/路由机制，决定 Token 路由到哪些专家（LLM/arch/MoE）
- [[概念_MoE负载均衡]] — 噪声 Top-k / 辅助损失 / 专家容量限制防止专家坍塌（LLM/arch/MoE）
- [[概念_混合Mamba架构]] — Hybrid Transformer-Mamba：AMF/MF 交错模块，O(n) 长序列处理（LLM/arch/Mamba, LLM/arch/MoE）
- [[概念_自适应长短CoT]] — 根据问题复杂度自动切换快速/深度推理模式（LLM/arch）
- [[概念_MLA多头潜在注意力]] — K/V 压缩进低维潜在空间，KV Cache 最小化（LLM/arch）
- [[概念_滑动窗口注意力]] — 局部注意力机制，大幅降低 KV Cache 内存（LLM/arch）
- [[概念_QK_Norm]] — Q/K 在 RoPE 前各加 RMSNorm，稳定大模型训练（LLM/arch）
- [[概念_NoPE无位置嵌入]] — 不使用位置编码，因果掩码隐式学习序列顺序（LLM/arch）
- [[概念_Muon优化器]] — 替代 AdamW 的新优化器，Kimi K2 首次在 1T 参数规模使用（LLM/training）
- [[概念_GRPO强化学习]] — 组相对策略优化，混元 TurboS 后训练 RL 算法（LLM/training/RL）

### LLM/arch/VLM（批次3）
- [[概念_MLLM三位一体架构]] — 视觉编码器 + 连接器 + LLM 通用框架（LLM/arch/VLM）
- [[概念_视觉基础模型统一范式]] — Prompt 驱动 Seq2Seq，一套权重统一多视觉任务（LLM/arch/VLM）
- [[概念_AnyRes高分辨率处理]] — LLaVA 系列全局+局部双路高分辨率策略（LLM/arch/VLM）
- [[概念_DeepStack深度视觉融合]] — Qwen3-VL ViT 多中间层特征注入 LLM 浅层（LLM/arch/VLM）

### LLM/arch/attention + inference（批次3）
- [[概念_线性注意力与混合注意力]] — Linear Attention O(N)、Hybrid 3:1 路线及行业现状（LLM/arch/attention）
- [[概念_MLA低秩KV压缩]] — DeepSeek MLA：低秩压缩 + 矩阵吸收广播优化（LLM/arch/attention）

### LLM/inference + reasoning（批次4）
- [[概念_推测解码]] — Draft-then-Verify：并行推测+验证实现无损推理加速（LLM/inference）
- [[概念_混合精度训练]] — BF16/FP32混合训练流程，16 bytes/参数显存估算（LLM/inference）
- [[概念_LoRA与QLoRA显存]] — LoRA 2Φ、QLoRA 0.5Φ显存估算原理（LLM/inference, 面试）
- [[概念_语义缓存]] — 确定性规范化缓存键，语义相似查询命中同一缓存（LLM/inference）
- [[概念_思维链CoT高级方法]] — CoT/CoT-SC/Decoding CoT/ToT+MCTS 及成本权衡（LLM/reasoning）
- [[概念_自适应快慢思考]] — 三方案：Qwen3 SFT、AdaCoT Pareto、AdaThinking 约束优化（LLM/reasoning）

### LLM/reasoning + training/RL（批次5）
- [[概念_DeepSeek-R1训练管道]] — 冷启动SFT→推理RL→拒绝采样SFT→全场景RL四阶段，规则奖励无奖励黑客（LLM/training/RL）
- [[概念_PPO近端策略优化]] — 生成策略+参考策略+价值模型三组件，RLHF 核心算法（LLM/training/RL）
- [[概念_RLHF基于人类反馈的强化学习]] — 人类偏好→奖励模型→PPO 对齐流程，RLVR 演进方向（LLM/training/RL）
- [[概念_奖励函数与验证器]] — 验证器判对错、奖励函数给分值，GRPO 奖励设计原则（LLM/training/RL）
- [[概念_推理模型顿悟时刻]] — RL 训练中自发涌现的反思/重评估行为，1.5B 起可观察（LLM/reasoning）
- [[概念_Agent感知记忆推理三能力]] — CoT 赋能 Agent：感知CoT/记忆CoT（树搜索+矢量检索）/推理CoT（AI-Agent, LLM/reasoning）

### LLM/training + hallucination（批次7）
- [[概念_LoRA低秩适应微调]] — LoRA 低秩分解原理、r/alpha/dropout 超参、QLoRA 变体与端侧适用场景（LLM/training/post-train）
- [[概念_Scaling_Law三大规律]] — 预训练/后训练/推理三大 Scaling Law 定义、技术手段与 Kaplan/Chinchilla 关系（LLM/training）
- [[概念_LLM外在幻觉与上下文内幻觉]] — 翁荔框架：两种幻觉类型、预训练/微调新知识两大根因（LLM/hallucination）
- [[概念_幻觉检测方法]] — FActScore/SAFE/SelfCheckGPT/TruthfulQA 检测体系（LLM/hallucination）
- [[概念_LLM幻觉消除技术分类]] — 32 种技术两大分类：提示工程（RAG/反馈/提示微调）vs 模型开发（LLM/hallucination）
- [[概念_抗幻觉方法]] — RARR/FAVA/Self-RAG/CoVe/FLAME/WebGPT 抵抗方法体系（LLM/hallucination）
- [[概念_幻觉的社会传播影响]] — 后真相时代幻觉放大机制：专家之死、衔尾蛇、责任归属与对齐税（LLM/hallucination）
- [[概念_温度参数与幻觉创造力权衡]] — 温度参数控制输出分布平滑度，高温增创意增幻觉，低温保准确减创意（LLM/hallucination, LLM/inference）
- [[概念_Discrete_Tokenization]] — VQ将连续多模态信号压缩为离散token，8类方法，码本坍塌核心挑战（LLM/tokenization）
- [[概念_BPE分词算法]] — 迭代合并高频字节对，平衡词汇表大小与序列长度，GPT系列标准分词（LLM/tokenization）
- [[概念_预训练数据处理管线]] — URL采集→过滤→去重→PII移除9步流程，FineWeb 15T token标准管线（LLM/training）
- [[概念_LLM三大演进支柱_效率推理智能体]] — 2023-2025 LLM演进：效率（MoE/MLA）→推理（Thinking/RL）→智能体（工具调用）三大正交支柱（LLM/arch）

### LLM/面试/训练/RL（批次9）
- [[概念_LLM面试知识体系]] — LLM 面试五大模块清单：架构/微调/推理/数学/扩展（LLM, 面试）
- [[概念_LLM数据管理预训练SFT]] — 预训练+SFT 两阶段数据质量/规模/组合管理框架（LLM/training）
- [[概念_通用验证器]] — 突破 RLVR 限制的两大路线：评分细则 vs 内部自信度，OaK 终局架构（LLM/training/RL）
- [[概念_AI创业Scaling_Law]] — AI 团队规模与产出效率的悖论：小而精 vs 规模扩张（创业）

### LLM/Recommendation + arch（Batch 10）
- [[概念_大模型推荐系统]] — 大模型融入推荐的三条路径：两阶段KG/教师蒸馏/种子用户池（LLM, Recommendation）
- [[概念_LLM知识图谱生产]] — 大模型生成三元组扩充KG：关系过滤+目标实体生成+Utility精排RAG（LLM, Recommendation）
- [[概念_gpt-oss架构特征]] — gpt-oss 7项架构进化、宽vs深对比、MXFP4量化（LLM/arch/MoE）
- [[概念_数字人文案生成]] — 口语化改写/多步蒸馏/图文一致/测评体系完整框架（LLM）

### AI-Agent/tools MCP系列（Phase 4 Batch 1）
- [[概念_MCP协议]] — MCP 定义、CHS 架构、五大原语、传输方式、与 Function Call 关系全景（AI-Agent/tools）
- [[概念_MCP_CHS架构]] — Client-Host-Server 三组件精确界定：Host 是 AI 智能唯一承载者，Server/Client 是模型无关 RPC 管道（AI-Agent/tools）
- [[概念_MCP五大原语]] — Tool/Prompt/Resource/Sampling/Roots 五类原语：触发方、用途、高阶玩法与 Web 化方向（AI-Agent/tools）
- [[概念_MCP传输方式]] — Stdio/SSE/Streamable HTTP 三种传输方式对比与选型（AI-Agent/tools）
- [[概念_MCP与Function_Call对比]] — 协议 vs 模型特性、静态 vs 动态、碎片化痛点与 MCP 解法（AI-Agent/tools）
- [[概念_MCP代码执行模式]] — CodeAgent 模式：按需加载工具定义，Token 消耗减少 98.7%，含隐私保护与 Skills 沉淀（AI-Agent/tools）
- [[概念_MCP数据库集成]] — MCP+数据库 Text-to-SQL 模式，结构化检索优于 RAG，含 MongoDB 实战与局限（AI-Agent/tools）
- [[概念_HITL_MCP]] — send_inquiry 挂起等待人类答复，MCP Notification 传凭条，HTTP 接口收答复，多端协同（AI-Agent/tools）
- [[概念_MCP_Proxy]] — 代理模式在 tool/call 前植入确认逻辑，现有 MCP Server 零改动（AI-Agent/tools）
- [[概念_Agent思考工具]] — think/plan/action 工具强制结构化规划，航空客服提升 54%，优于纯 Prompt（AI-Agent/tools）
- [[概念_MCP混合部署]] — 小模型做工具选择节省 token，大模型负责生成保证质量（AI-Agent/tools）
- [[概念_orchestrator-worker模式]] — 主智能体规划分解，子智能体并行执行，多智能体 vs 单智能体提升 90.2%（AI-Agent/multi-agent）
- [[概念_多智能体协调]] — 多智能体协调挑战、提示词 8 原则、评测策略与生产可靠性（AI-Agent/multi-agent）

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
- [[实体_rank_bm25]] — Python BM25 轻量检索库（medium）
- [[实体_Qwen3_Embedding]] — Qwen3 系列嵌入/重排模型，MTEB 排名第一，Instruct+LLM化Rerank
- [[实体_Sentence_Transformers]] — 嵌入模型训练/推理框架，Matryoshka/Instruct 支持
- [[实体_BGE-M3]] — BAAI 多语言嵌入模型，1024 维，同时支持 dense 和 ColBERT 多向量
- [[实体_Elasticsearch]] — 全文+原生向量搜索引擎，混合检索/RRF/量化/Serverless
- [[实体_Faiss]] — Facebook 开源向量检索库，丰富索引算法+GPU 加速
- [[实体_HNSW]] — 分层可导航小世界图，毫秒级 ANN 业界主流
- [[实体_Docling]] — IBM 开源 PDF 解析库，RAG 挑战赛最佳解析器
- [[实体_Cohere_Rerank]] — Cohere 重排序 API，CohereRerank top-k 精排（medium）
- [[实体_美团搜索]] — 美团App搜索，查询改写全栈实践，覆盖率73%，QPS 6万/秒
- [[实体_优图实验室]] — 腾讯AI实验室，RAG全栈方案，apd-embedding-2b/MAC-SQL/GraphRAG
- [[实体_MAC-SQL]] — 多智能体Text2SQL框架，Selector/Decomposer/Refiner（COLING 2025）
- [[实体_通义千问]] — 阿里大语言模型，RAG生成/判别核心模型（medium）
- [[实体_RAGAS]] — RAG 系统开源评估框架，多维度指标
- [[实体_TableRAG]] — 华为云文本+表格异构问答混合推理框架
- [[实体_Mamba]] — Mamba 选择性状态空间模型，线性时间序列建模（LLM/arch/Mamba）
- [[实体_Mamba2]] — Mamba2 SSD 框架，SSM 与 Attention 大一统，ICML 2024（LLM/arch/Mamba）
- [[实体_S4]] — Structured State Space for Sequences，Mamba 前置架构（LLM/arch/Mamba）
- [[实体_Albert_Gu]] — Mamba/S4/HiPPO 核心作者，CMU 助理教授，Cartesia AI 联创（LLM/arch/Mamba）
- [[实体_Tri_Dao]] — FlashAttention/Mamba 作者，Princeton 助理教授（LLM/arch/Mamba）
- [[实体_腾讯混元TurboS]] — 业界首个大规模部署的 560B Hybrid Transformer-Mamba MoE 模型（LLM/arch/Mamba, LLM/arch/MoE）
- [[实体_DeepSeek-V3]] — DeepSeek 旗舰 MoE 模型，MLA+256专家+共享专家架构（LLM/arch/MoE）
- [[实体_Kimi_K2]] — 月之暗面 1T 参数开源 MoE 模型，Muon 优化器，基于 DeepSeek-V3 架构（LLM/arch/MoE）
- [[实体_Gemma3]] — Google DeepMind 开源 LLM，滑动窗口注意力+双层 Norm，27B 性能优异（LLM/arch）
- [[实体_Florence-2]] — 微软 Azure AI 通用视觉基础模型，FLD-5B + Seq2Seq（LLM/arch/VLM）
- [[实体_FLD-5B数据集]] — Florence-2 配套 1.26亿图像/54亿标注超大规模视觉数据集（LLM/arch/VLM）
- [[实体_LLaVA]] — 大道至简多模态系列：极简连接器 + AnyRes（LLM/arch/VLM）
- [[实体_Qwen3-VL]] — 阿里 DeepStack + MoE 深度融合多模态模型（LLM/arch/VLM）
- [[实体_MiniMax_M2]] — MiniMax 2025 旗舰，回归 Full Attention，Agent/代码定位（LLM/arch/attention）
- [[实体_Kimi_Linear]] — 月之暗面开源 48B 混合注意力：KDA+MLA 3:1，KV Cache 减少 75%（LLM/arch/attention）
- [[实体_Kimi_Delta_Attention]] — KDA：channel-wise gate 线性注意力，vLLM 已收录（LLM/arch/attention）
- [[实体_DeepSeek_V2]] — DeepSeek MLA 首发模型（LLM/arch/attention）
- [[实体_Medusa]] — Medusa 推测解码框架：多 FFN Head Self-Drafting（LLM/inference）
- [[实体_Qwen3]] — 阿里 Qwen3：SFT 混合思考 + Thinking Budget 涌现（LLM/reasoning）
- [[实体_DeepSeek-R1]] — DeepSeek 推理模型，GRPO+四阶段训练，AIME 79.8%，与 o1-1217 相当（LLM/reasoning, LLM/training/RL）
- [[实体_TinyZero]] — UC伯克利 $30 复现 R1-Zero，CountDown 任务验证纯 RL 涌现推理（LLM/reasoning）
- [[实体_SimpleRL]] — 港科大 8K 数据 7B 模型复现 R1，AIME 33.3%，第44步顿悟（LLM/reasoning）
- [[实体_Open_R1]] — HuggingFace 官方完全开源复刻 R1 全套 pipeline（LLM/training/RL）
- [[实体_Unsloth]] — 开源高效 LLM 微调框架，支持 GRPO 训练推理模型，GitHub 4万星（LLM/training/RL, Skill/python）
- [[实体_SmolLM3]] — HuggingFace 3B 开源模型，384×H100 训练 11T tokens，GQA+RNoPE 架构（LLM/training/pre-train）
- [[实体_DEITA]] — SFT 数据筛选方法，复杂性×质量综合评分 + 向量相似度多样性过滤（LLM/training/post-train）
- [[实体_MoDS]] — 三维度 SFT 数据筛选：奖励模型质量+K-Center-Greedy多样性+必要性过滤（LLM/training/post-train）
- [[实体_陈丹琦团队]] — 普林斯顿 NLP 组，后训练遗忘机制研究：on-policy 数据是关键（LLM/training/post-train）

### LLM/面试/创业/RL（批次9）
- [[实体_Jina_AI]] — 专注搜索底座模型 AI 初创，2020-2025，两次 Pivot 后被 Elastic 收购（创业）
- [[实体_RLVR技术]] — 可验证奖励强化学习，o1/R1 推理能力核心，局限于有标准答案领域（LLM/training/RL）

### LLM/Recommendation + arch（Batch 10）
- [[实体_蚂蚁集团NextEvo]] — 蚂蚁集团AI创新研发部门，大模型推荐系统研究与落地（LLM, Recommendation）
- [[实体_DLLM2Rec]] — 蚂蚁 GPT3.5→LLAMA2→序列模型两级蒸馏推荐框架（LLM, Recommendation）
- [[实体_gpt-oss]] — OpenAI 首批开放权重推理模型 gpt-oss-20b/120b，Apache 2.0（LLM/arch/MoE）
- [[实体_Sebastian_Raschka]] — LLM 架构技术博主，《Build a LLM from Scratch》作者（LLM/arch）
- [[实体_淘天AIGC团队]] — 淘天集团直播AIGC团队，数字人直播完整链路（LLM）

### LLM/training + hallucination（批次7）
- [[实体_翁荔_Lilian_Weng]] — OpenAI 华人科学家，Agent 公式 + 幻觉 Blog 作者（LLM/hallucination）
- [[实体_李维_出门问问]] — 出门问问大模型团队前工程副总裁，幻觉技术解析与应对建议（LLM/hallucination）
- [[实体_Brendan_Bycroft]] — 软件工程师，bbycroft.net/llm LLM 3D 可视化作者（LLM/arch）
- [[实体_Minimax_m1]] — Minimax 456B 开源 MoE 模型，Lightning Attention+CISPO，支持100万token上下文（LLM/arch）
- [[实体_PaperWeekly]] — AI/ML 论文解读媒体平台，多篇综述传播渠道（LLM/tokenization）
- [[实体_PEFT库]] — HuggingFace 参数高效微调库，LoRA/QLoRA/Adapter/Prefix 支持（LLM/training/post-train）

### LLM/training/post-train（批次6）
- [[后训练认知_SFT_vs_RL_记忆与遗忘机制]] — 普林斯顿研究：RL 抗遗忘优于 SFT，根源是 on-policy 数据分布（LLM/training/post-train）
- [[HuggingFace手把手训练大模型实战指南]] — SmolLM3 端到端训练实战：Why→What→How + 架构/数据/基础设施全链路（LLM/training/pre-train, post-train）
- [[SFT数据挑选方法_质量多样性必要性]] — SFT 数据三维度筛选：MoDS/DEITA/CaR 方法梳理（LLM/training/post-train）
- [[375篇文献_推理大模型后训练技术综述]] — 后训练三分类综述：微调/RL/测试时扩展（LLM/training/post-train）
- [[LLM后训练技术全景解读]] — 全景解读后训练：PEFT/LoRA/Prompt Tuning/PPO/DPO/GRPO/CoT/ToT（LLM/training/post-train）

### AI-Agent/context-engineering（Phase 4 Batch 3）
- [[概念_上下文工程]] — 动态系统填充恰好合适的信息给LLM，四类操作：Offload/Retrieve/Reduce/Isolate（AI-Agent/context-engineering）
- [[概念_Context_Rot]] — 上下文腐化：长度增长导致性能下降，预腐化阈值128K-200K，触发压缩/总结（AI-Agent/context-engineering）
- [[概念_分层行动空间]] — Manus三层工具架构：函数调用/沙盒工具集/软件包API，稳定接口+无限能力（AI-Agent/context-engineering）
- [[概念_上下文隔离两种模式]] — 通信模式（干净上下文）vs 共享上下文模式，借鉴Go语言哲学（AI-Agent/context-engineering）
- [[概念_Spec_Driven_Development]] — 规范驱动开发：Prompt→Requirements→Design→Tasks→Code，Kiro 实现（AI-Agent/context-engineering）

### AI-Agent/coding（Phase 4 Batch 4）
- [[概念_Agent开发范式三级进化]] — Level 1 LLM/Level 2 AI Agent/Level 3 Multi-Agent 三阶段演进，Human in the Loop 作为特殊 Agent（AI-Agent/coding）
- [[概念_A2A协议]] — Google 2025 年发布的 Agent 间协作开放协议：Agent Card 能力发现/任务管理/消息交换，与 MCP 分层互补（AI-Agent/coding）
- [[概念_长程Agent双Agent架构]] — Anthropic：初始化 Agent + 编码 Agent 解决跨会话长程 Coding 任务，功能列表/增量进展/端到端测试三支柱（AI-Agent/coding）
- [[概念_Coding驱动Agent]] — LLM 直接生成 Python 代码控制 Agent 行为（Py4j 泛化调用），FIM 格式续写，支持分支/循环复杂控制流（AI-Agent/coding）
- [[概念_Agent仿脑区功能分区架构]] — 感知区/认知区/运动区/表达区/自我评估区五功能区，运动区（TaskExecutor）多轮循环执行复杂任务（AI-Agent/coding）
- [[概念_Agent三层记忆体系]] — 感知记忆（标签页级）/短期记忆（Session+ES）/长期记忆（知识点+用户画像+经验图谱）（AI-Agent/coding）

### AI-Agent/coding+skill（Phase 4 Batch 5）
- [[概念_私域知识工程]] — 将项目专属知识系统化文档化，解决 AI 与真实项目信息不对称，三板斧：入职培训/知识驱动编程/自动维护（AI-Agent/coding）
- [[概念_LLM应用评估体系]] — LLM 应用评估方法论：断言式单元测试/LLM 裁判最佳实践/实习生测试/古德哈特定律（AI-Agent/coding）
- [[概念_Agent_Skills元工具架构]] — Skills = 提示词模板+上下文注入+执行上下文修改，纯 LLM 推理选择，双消息 isMeta 机制，渐进式披露（AI-Agent/skill）
- [[概念_Agentic设计模式分类]] — 21种 Agent 设计模式四大类：核心（提示链/路由/并行化/反思/工具/规划/多智能体）/高级/集成/生产（AI-Agent/skill）

### AI-Agent/memory（Phase 4 Batch 7）
- [[概念_AI_Agent记忆策略]] — 8 种主要策略原理（全量/滑动窗口/相关性过滤/摘要/向量DB/知识图谱/分层/类OS），翁荔学术分类框架与前沿系统（AI-Agent/memory）

### AI-Agent/prompt-engineering（Phase 4 Batch 7）
- [[概念_Agent调优路径]] — 阿里云实战四级调优路径：提示词原型→Workflow→Multi-Agent→模型训练，选型原则表（AI-Agent/prompt-engineering）
- [[概念_编程提示工程实战]] — 程序员向 10 种技巧+7 条基础原则+调试/重构/功能三场景策略+常见反模式（AI-Agent/prompt-engineering）
- [[概念_系统提示词四层架构]] — 核心定义/交互接口/内部处理/全局约束四层，解决规则冲突/维护困难/行为不可预测（AI-Agent/prompt-engineering）

### AI-Agent/AI-BI（Phase 4 Batch 8）
- [[概念_生产即治理]] — 耗散结构理念：数据生产过程内置规范和自调节，对抗信息熵增（AI-Agent/AI-BI）
- [[概念_FlattenedRAG与StructuredRAG]] — 元数据检索两种方案：打平为自然语言 vs 保留层次结构分步检索（AI-Agent/AI-BI）
- [[概念_HeadlessBI指标中台]] — 前后端分离指标服务：统一指标库+API，保障多平台口径一致（AI-Agent/AI-BI）
- [[概念_Text2DSL中间层方案]] — NL→SQL→DSL→前端指令，引入中间层解决直接转换困难，关键是无损转换（AI-Agent/AI-BI）
- [[概念_DataOps数据工程化]] — 将 DevOps 应用于数据开发：代码化/版本/CI/CD，实现生产即治理（AI-Agent/AI-BI）

### AI-Agent 综合 + AI-BI（Phase 4 Batch 9）
- [[概念_AI_Workflow与Agent对比]] — AI Workflow 预定义流程 vs AI Agent 自主决策：选型原则与核心区别（AI-Agent）
- [[概念_AI_Agent四种类型]] — 反应型/目标导向型/学习型/协作型四种 Agent 分类与适用场景（AI-Agent）
- [[概念_Agent系统化工程]] — 三层复杂度+LLM放大效应+Level 0-4认知演化+系统化方法论（AI-Agent）
- [[概念_LLM不确定性放大]] — 多步调用的指数级错误放大数学模型及三类放大维度（AI-Agent）
- [[概念_AI应用架构演进]] — 七步演进路线：基础调用→RAG→Guardrails→路由→网关→缓存→Agent，含TTFT/TPOT优化（AI-Agent）
- [[概念_AI-ready_data]] — NL2SQL落地第一性问题：元数据/业务语义/权限/样例SQL的系统化准备（AI-Agent/AI-BI）
- [[概念_M-Schema]] — NL2SQL增强Schema表示：补充类型/中文释义/真实值示例+约束池（AI-Agent/AI-BI）
- [[概念_Schema_Linking]] — BM25粗排+SIC精排两级联接，从全量Schema筛选相关表列，幻觉率-78%（AI-Agent/AI-BI）

### Skill/python（Phase 5 Batch 1）
- [[概念_FastAPI项目结构模式]] — Routers/Schemas/Services 三层分离 + 安全中间件 + pydantic-settings（Skill/python）
- [[概念_Python_async_await并发]] — 协程/并发vs并行（汉堡比喻）/FastAPI def vs async def 选择（Skill/python）
- [[概念_uv包管理器]] — Rust 编写 pip 替代品，pyproject.toml+uv.lock，Docker 集成 10x 提速（Skill/python）
- [[概念_Python循环优化技巧]] — 12 种 for 循环优化方法与提速比，map/set/lru_cache/filterfalse（Skill/python）
- [[概念_Python函数式工具]] — map/lru_cache/filterfalse/Generator，C 实现替代显式循环（Skill/python）
- [[概念_Python进阶特性]] — suppress/setrecursionlimit/Literal/__missing__/__subclasshook__（Skill/python）

### Skill/data-analysis（Phase 5 Batch 2）
- [[概念_自动EDA工具]] — 10 个自动 EDA 包四类分类（报告/可视化/定制/ML 集成）与选型建议（Skill/data-analysis, Skill/python）
- [[概念_Pandas可视化]] — DataFrame.plot/Series.plot 内置绘图 + pandas.plotting 高级可视化（Skill/data-analysis）
- [[概念_Pandas核心操作图解]] — 选择/排序/分组/合并/变形/索引 + NumPy 对比关键差异（Skill/data-analysis, Skill/python, 面试）
- [[概念_matplotlib样式美化]] — dufte 主题/图例/柱标注三 API，一行代码商务风图表（Skill/data-analysis）

### Skill/linux（Phase 5 Batch 3）
- [[概念_Linux命令分类速查]] — 28 大类 600 条 Linux 命令按场景分组速查体系（Skill/linux）

### Life（Phase 5 Batch 3）
- [[概念_幸福积分模型]] — 幸福总量=曲线下面积（积分），时间度量衡，等周不等式类比（Life）
- [[概念_天职Calling]] — 本身能带来快乐的工作，三条筛选标准，天职不是"钱多事少离家近"（Life）
- [[概念_习得性快乐]] — A型（多巴胺驱动）vs B型（社会建构），被动习得→习得性不快乐的风险（Life）

### AIGC（Phase 6 Batch 1）
- [[概念_Veo3视频提示词]] — Veo 3 提示词七要素/角色一致性/音频控制/避免字幕/风格切换/自拍技巧（AIGC）
- [[概念_PPT生成提示词]] — 用结构化提示词控制 AI 生成 PPT/封面的风格/配色/排版，三维度描述法（AIGC）
- [[概念_HTML代码方式生成视觉物料]] — LLM 输出 HTML+CSS 代码渲染视觉物料，可控性强、可复用（AIGC）
- [[概念_AI_PPT工具路径]] — AI 原生派（Gamma 对话生成）vs 传统革新派（WPS AI 润物细无声）（AIGC）
- [[概念_AI产品最后一公里]] — AI PPT 从「能用」到「可交付」的 gap：二次编辑+格式导出兼容（AIGC）

### AIGC（Phase 6 Batch 2）
- [[概念_Nano_Banana_Pro论文绘图工作流]] — 架构师→渲染器→编辑器三步工作流；VISUAL SCHEMA 五种布局原型；禁止用于实验数据图表（AIGC）
- [[概念_Nano_Banana图像生成提示词]] — 描述场景而非关键词；摄影师/设计师思维；六大生成+四大编辑场景完整模板（AIGC）
- [[概念_人与大模型协作]] — Gemini 三大启示：思想催化剂/认知谦逊/Knowing-Why；GPT-5 补充：三颗钉子+错账本（AIGC）
- [[概念_Vibe_Coding三阶段]] — 初级原型/中级重构/高级整体-细节-整体循环；UI/UX 不适合 AI 直接生成（AIGC）
- [[概念_文生视频提示词公式]] — 基础/进阶/图生视频三套公式；主体+场景+运动+美学控制+风格化（AIGC）
- [[概念_视频美学控制词典]] — Wan2.2 九大维度完整词典：光源/光线/时间/景别/构图/焦段/运镜/风格/特效（AIGC）

### TTS（Phase 6 Batch 2）
- [[概念_直播TTS数据处理管线]] — 语音信号处理/语音理解/说话人聚类三环节漏斗；利用直播回放替代录制素材（TTS）
- [[概念_TTS两阶段架构]] — 前端文本归一化+后端语言模型/声学模型/声码器；Encodec偏声学/HuBERT偏语义（TTS）
- [[概念_韵律情感拟人化TTS]] — 显式停顿@/拖音→标签控制韵律；参考音频情感注入高低音变化；个性化韵律表（TTS）

### Recommendation（Phase 6 Batch 2）
- [[概念_互信息最大化去噪表征]] — CF 表征含噪声，引入文本语义模态极大化共存部分；InfoNCE 变分下界优化（Recommendation）
- [[概念_LLM用户商品画像生成]] — Item-to-User 流水线；商品先于用户生成；CoT 风格 Instruction；可并行（Recommendation）

### 创业（Phase 6 Batch 3）
- [[概念_Foundation_Sprint]] — Jake Knapp 超早期项目战略奠基流程：10 小时三阶段，产出创始假设（创业）
- [[概念_Design_Sprint]] — 五天产品验证冲刺：Map/Sketch/Decide/Prototype/Test + Scorecard 计分卡（创业）
- [[概念_差异化2x2分析]] — Foundation Sprint 差异化工具：经典+自定义因素，2x2 独占右上角避开"失败者村"（创业）
- [[概念_Magic_Lenses魔术镜头]] — 五种专家视角（客户/务实/增长/财务/差异化）评估执行路径（创业）
- [[概念_先思考再行动]] — AI 时代先做战略思考再开发：快是陷阱、AI 致平庸、思考不可外包（创业）

### 创业（Phase 6 Batch 4）
- [[概念_RIDE方法论]] — 阿里云 RIDE：Reorganize/Identify/Define/Execute 大模型 E2E 落地四步法（创业）
- [[概念_RaaS结果即服务]] — 红杉 RaaS：只交付工具不够，必须真正上线产生业务结果（创业）
- [[概念_AI企业数字人管理模式]] — 数字人作为正式员工管理：汇报业务部门/AI 工号/效率效果双达标上岗（创业）
- [[概念_PMF引擎]] — Superhuman 四步法：精准细分/分析反馈/规划路线图/重复迭代，量化优化 PMF（创业）
- [[概念_Sean_Ellis_PMF指标]] — "非常失望"比例 40% 门槛：PMF 领先指标（创业）
- [[概念_Bundle理论]] — Shishir Mehrotra：三种用户/MCC 分成/刚需错开非刚需重叠/2x2 矩阵（创业）
- [[概念_Unbundle_Rebundle规律]] — 技术 unbundle 切入市场/商业 rebundle 捕获价值/集装箱类比 AI（创业）
- [[概念_AI初创高人效模式]] — Leonis AI 100：极简扁平团队人均百万美元 ARR，轻人力重算力数据（创业）
- [[概念_倒漏斗GTM模式]] — AI 初创：PLG 先行验证价值，销售后置正式化已存在需求（创业）
- [[概念_AI市场阈值解锁]] — AI 市场按序爆发：模型突破关键阈值才解锁新品类（创业）
- [[概念_研究型创始人崛起]] — 86% 技术创始人/82% 技术 CEO，研究型创始人预判能力突破（创业）

### AI-Agent/deep-research（Phase 4 Batch 6）
- [[概念_Deep-Research-Agent定义与分类]] — DR Agent 定义、与 RAG/Tool Use 的边界、规划策略三模式（Planning-Only/Intent-to-Planning/Unified）（AI-Agent/deep-research）
- [[概念_Deep-Research四大挑战]] — 信息窄门/幻觉不可靠/线性效率瓶颈/评测错位，及对应未来方向（AI-Agent/deep-research）
- [[概念_Deep-Research实现架构四类]] — 单体/流水线/多智能体/混合四种架构对比与代表系统（AI-Agent/deep-research）
- [[概念_IterResearch范式]] — 通义 DeepResearch 创新范式：精简工作空间+核心报告迭代重构，解决上下文认知瓶颈（AI-Agent/deep-research）
- [[概念_WebFrontier数据合成]] — 种子-扩展-评估三步数据合成，知识图谱随机游走+原子操作难度建模（AI-Agent/deep-research）

### AI-Agent/tools MCP系列（Phase 4 Batch 1）
- [[实体_Agent_TARS]] — 字节跳动开源多模态 Agent，内置 Function Call + 用户自定义 MCP Server 双轨设计（AI-Agent/tools）
- [[实体_David_Soria_Parra]] — Anthropic 工程师，MCP 协议联合创建者，五大原语与 Web 化主导者（AI-Agent/tools）
- [[实体_MongoDB]] — 文档型 NoSQL 数据库，mcp-mongo-server 接入 MCP 生态，Text-to-Query 结构化检索（AI-Agent/tools）
- [[实体_CherryStudio]] — 开源 MCP Host 应用，MCPService.ts（Client）+ ApiService.ts（Host）CHS 架构典型案例（AI-Agent/tools）
- [[实体_Cline]] — VS Code AI 编码扩展，原生 MCP Client，npx 配置接入任意 MCP Server（AI-Agent/tools）
- [[实体_OpenLM平台]] — 阿里巴巴智能引擎团队大模型研发平台，HITL MCP 方案落地环境（AI-Agent/tools）
- [[实体_Anthropic_Research系统]] — Anthropic Claude Research 多智能体研究系统，Opus 4 + Sonnet 4 orchestrator-worker（AI-Agent/multi-agent）

### AI-Agent/context-engineering（Phase 4 Batch 3）
- [[实体_Peak_Ji_季逸超]] — Manus 联合创始人，MIT TR35 2025，上下文工程六大原则提出者（AI-Agent/context-engineering）
- [[实体_Manus]] — 通用AI Agent，上下文工程实践标杆，KV缓存/分层行动空间/文件系统记忆（AI-Agent/context-engineering）

### AI-Agent/coding（Phase 4 Batch 4）
- [[实体_Aone_Agent]] — 阿里巴巴通用 Agent 产品，类 Devin，Leader Agent + 子 Agent 容器架构，全研发生命周期提效（AI-Agent/coding）
- [[实体_Eino框架]] — CloudWego 开源 Golang LLM 框架，泛型强类型/有向图编排/Callbacks 切面/Checkpoint HITL（AI-Agent/coding）

### AI-Agent/skill（Phase 4 Batch 5）
- [[实体_Antonio_Gulli]] — 《Agentic Design Patterns》作者，21种 Agent 设计模式实践指南，版税捐赠救助儿童会（AI-Agent/skill）
- [[实体_Han_Lee]] — AI 工程师/技术博主，Claude Agent Skills 源码级深度解析文章作者（AI-Agent/skill）

### AI-Agent/deep-research（Phase 4 Batch 6）
- [[实体_通义DeepResearch]] — 阿里通义实验室开源 Web Agent，30B MoE，HLE 32.9/BrowseComp-EN 43.4，IterResearch+ReAct 双模式（AI-Agent/deep-research）

### AI-Agent/memory（Phase 4 Batch 7）
- [[实体_MemGPT]] — Letta AI，专用记忆 LLM 管理工作 LLM 上下文窗口，受 OS 分页机制启发，函数链多步检索（AI-Agent/memory）

### AI-Agent/AI-BI（Phase 4 Batch 8）
- [[实体_腾讯OlaChat]] — 腾讯 PCG 智能数据分析平台，多任务对话+DAG编排+Text2SQL(70B)+元数据RAG（AI-Agent/AI-BI）
- [[实体_腾讯欧拉平台]] — 腾讯数据治理平台，生产即治理理念，资产工场+tMetric指标中台+数据发现三产品（AI-Agent/AI-BI）

### AI-Agent 综合 + AI-BI（Phase 4 Batch 9）
- [[实体_AutoGPT]] — 2023年早期 Agent 代表，GitHub 最受欢迎项目，典型"能跑但不可靠"案例（AI-Agent）
- [[实体_AutoGen]] — 微软多 Agent 对话框架，可定制/可对话/支持 Human-in-the-loop（AI-Agent）
- [[实体_MetaGPT]] — 模仿软件公司结构的多 Agent 框架：产品经理/PM/工程师角色协作（AI-Agent）
- [[实体_ChatDev]] — 清华/面壁开源虚拟软件公司，CEO/CTO/程序员多角色 Agent 协作（AI-Agent）
- [[实体_LangSmith]] — LangChain 可观测性平台：可视化 Trace/调试/测试评估，Agent 复现性关键工具（AI-Agent）
- [[实体_Qwen2.5-Coder]] — 阿里代码专用模型3B/7B，NL2SQL LoRA 精调基座，实测EX提升+6.4%（AI-Agent/AI-BI）
- [[实体_矩阵起源]] — MatrixOne HTAP数据库 + Matrix Intelligence 平台，AI-ready data 基础设施（AI-Agent/AI-BI）

### Skill/python（Phase 5 Batch 1）
- [[实体_FastAPI]] — Python 高性能 Web 框架，基于 Starlette/Pydantic，原生 async/await，性能与 Go 不相上下（Skill/python）
- [[实体_uv]] — Astral 开发的 Rust 编写 Python 包管理器，pip 替代品，约 10x 速度提升（Skill/python）

### Skill/data-analysis（Phase 5 Batch 2）
- [[实体_Pandas]] — Python 数据分析核心库，基于 NumPy，Series/DataFrame + groupby/merge/pivot/plot（Skill/data-analysis, Skill/python）
- [[实体_Dataprep]] — 开源 Python EDA 包，基于 Pandas+Dask，自动 EDA 中速度最快（Skill/data-analysis, Skill/python）
- [[实体_dufte]] — matplotlib 样式美化库，dufte.style/legend()/show_bar_values() 三 API（Skill/data-analysis）

### Life（Phase 5 Batch 3）
- [[实体_评论尸]] — 中文互联网创作者，博客「虹线」，《幸福的积分》作者（Life）

### AIGC（Phase 6 Batch 1）
- [[实体_Veo_3]] — Google 文本生成带音频视频模型，物理模拟出色，需 Gemini Pro（AIGC）
- [[实体_Gemini]] — Google AI 助手，PPT 生成/深度研究/搜索，Veo 3 使用前提（AIGC）
- [[实体_Gamma]] — AI 原生 PPT 工具先行者，对话生成卡片式演示文稿（AIGC）
- [[实体_Genspark]] — 通用型超级智能体，PPT 为附属功能，图片引用缺失问题（AIGC）

### AIGC（Phase 6 Batch 2）
- [[实体_Nano_Banana_Pro]] — Gemini 2.5 Flash Image 别名，原生多模态/强角色一致性/对话式编辑，学术绘图最佳选择（AIGC）
- [[实体_通义万相Wan2.2]] — 阿里通义文生视频模型，三套提示词公式+九大维度美学控制词典（AIGC）

### TTS（Phase 6 Batch 2）
- [[实体_CosyVoice]] — 阿里通义开源 TTS 模型，V4 融合 CosyVoice2+Qwen2.5-0.5B+vLLM，相似度 0.93（TTS）

### Recommendation（Phase 6 Batch 2）
- [[实体_RLMRec]] — 港大+百度模型无关 LLM 推荐框架；互信息最大化对比/生成双范式；落地搜索业务（Recommendation）
- [[实体_港大数据智能实验室]] — HKU-DS，RLMRec 团队，chaoh 实验室（Recommendation）

### 创业（Phase 6 Batch 3）
- [[实体_Jake_Knapp]] — Design Sprint 创造者，前 Google Ventures 设计合伙人，Character Capital 联创（创业）
- [[实体_Character_Capital]] — Jake Knapp 与 John Zeratsky 创立的风投，专注 0 阶段超早期项目（创业）

### 创业（Phase 6 Batch 4）
- [[实体_蒋林泉]] — 阿里云 CIO & aliyun.com 负责人，RIDE 方法论提出者（创业）
- [[实体_阿里云]] — 阿里巴巴公共云服务商，企业大模型落地实践与技术底座（创业, Infra/AI）
- [[实体_Superhuman]] — AI 邮件客户端，PMF 引擎标杆，ARR 3500 万美元，被 Grammarly 收购（创业）
- [[实体_Rahul_Vohra]] — Superhuman 创始人兼 CEO，PMF 引擎方法论提出者（创业）
- [[实体_Grammarly]] — 嵌入式 AI 写作工具，年收入超 7 亿美金，收购 Coda+Superhuman 后改名（创业）
- [[实体_Shishir_Mehrotra]] — Coda 创始人，新 Superhuman 集团 CEO，Bundle 理论实践者（创业）
- [[实体_Leonis_Capital]] — 华人 2021 年成立早期 AI 风投，发布 The Leonis AI 100 报告（创业）

## Comparisons

## Overview

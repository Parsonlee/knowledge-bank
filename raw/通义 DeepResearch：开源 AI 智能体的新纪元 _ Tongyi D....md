---
id: "7375797183372594179"
cubox_url: https://cubox.pro/web/card/7375797183372594179
url: https://tongyi-agent.github.io/zh/blog/introducing-tongyi-deep-research/
tags:
  - AI-Agent/deep-research
---
# 通义 DeepResearch：开源 AI 智能体的新纪元 | Tongyi DeepResearch

https://github.com/Alibaba-NLP/DeepResearch

[Read in Cubox](https://cubox.pro/web/card/7375797183372594179)  
[Read Original](https://tongyi-agent.github.io/zh/blog/introducing-tongyi-deep-research/)  

---

## Annotations  

> IterResearch 范式的创建是为了解决Agent将所有信息堆积在一个不断扩展的单一上下文窗口中时出现的认知瓶颈和噪音污染。针对多步研究任务，IterResearch 将其解构为一系列研究回合。
>
>
> 在每一轮中，Agent仅使用上一轮中最重要的输出来重建一个精简的工作空间。在这个专注的工作空间中，Agent会分析问题，将关键发现整合成一个不断演变的核心报告，然后决定下一步行动——是收集更多信息还是提供最终答案。这种“综合与重构”的迭代过程使Agent能够在执行长期任务时保持清晰的认知焦点和高质量的推理能力。
>
> 在此基础上，我们提出了Research‑Synthesis框架。并行使用多个IterResearch Agent探索同一个问题。并最终整合它们完善的报告和结论，从而得出更准确的最终答案。这种并行结构使模型能够在有限的上下文窗口内考虑更广泛的研究路径，从而将其性能推向极限。  

[Link️](https://cubox.pro/web/annotations/cards/7375797183372594179?highlight=7380557808028093770)  

> 我们认为，算法固然重要，但并非 Agentic RL 成功的唯一决定因素。 在尝试了多种算法和优化技巧后我们发现，数据质量和训练环境的稳定性，可能是决定强化学习项目成败的更关键一环。一个有趣的现象是，我们曾尝试直接在 BrowseComp 测试集上训练，但其表现远不如使用我们合成数据的结果。我们推测，这种差异源于合成数据提供了一致性更高的分布，使模型能进行更有效的学习和拟合。相比之下，像 BrowseComp 这样的人工标注数据，本身就含有更多噪声，加之其规模有限，导致模型很难从中提炼出一个可供学习的潜在分布，从而影响了其学习和泛化（generalize）能力。这一发现对其他智能体的训练同样具有启发意义，为构建更多样、更复杂的智能体训练方案提供了思路。  

[Link️](https://cubox.pro/web/annotations/cards/7375797183372594179?highlight=7380559795624870017)


---

## 📖 正文全文

# 通义 DeepResearch：开源 AI 智能体的新纪元

[tongyi-agent.github.io](https://tongyi-agent.github.io/zh/blog/introducing-tongyi-deep-research/)DeepResearch Team, Tongyi Lab

[GITHUB](https://github.com/Alibaba-NLP/DeepResearch) [HUGGINGFACE](https://huggingface.co/Alibaba-NLP/Tongyi-DeepResearch-30B-A3B) [MODELSCOPE](https://modelscope.cn/models/iic/Tongyi-DeepResearch-30B-A3B) [SHOWCASE](https://tongyi-agent.github.io/showcase/)
![](https://image.cubox.pro/cardImg/baem1r5gkb3r35pu1rs6xkaoicga1j58hh19gsfefkwa4d8ff.png?imageMogr2/quality/90/ignore-error/1)

## 从 Chatbot 到 Autonomous Agent

我们发布了通义 DeepResearch ------ 首个在性能上可与 OpenAI DeepResearch 相媲美、并在多项权威基准测试中取得领先表现的全开源 Web Agent。

在多个极高难度的信息检索和推理任务中，通义DeepResearch 取得了最先进的（SOTA）成绩：

* Humanity's Last Exam (HLE)：32.9
* BrowseComp‑EN：43.4
* BrowseComp‑ZH：46.7
* xBench‑DeepSearch：75.0

全面超越了目前所有的闭源及开源 Deep Research 智能体（Agent）。

不仅如此，我们还完整分享了一套可落地的高水平Agent构建方法论，详细介绍了从数据合成、Agentic 增量预训练（CPT）、有监督微调（SFT）冷启动，到强化学习（RL）的全套流程。在 RL 环节，我们提供了算法创新、自动化数据构建与高稳定性基础设施的全栈解决方案。

在推理阶段，基础的 ReAct 模式无需任何提示工程即可充分展现模型固有能力，而深度模式（test‑time‑scaling） 则展示了其在复杂推理与规划能力上的上限。

## 基于合成数据的增量预训练和后训练

### 增量预训练数据

我们提出在Agent模型训练中加入智能体增量预训练（Agentic Continual Pre‑training, Agentic CPT）阶段，从而为后训练提供一个强大的Agent基座模型。为此，我们提供了一套支持大规模持续扩展的智能体预训练数据合成方案AgentFounder，并与后训练过程中源源不断生产的数据形成数据飞轮。

**数据重组和问题构建** 基于广泛收集和持续更新的知识文档、公开可用的爬虫数据、知识图谱以及后训练数据生产和训练中产生的轨迹数据和工具调用返回结果（例如，搜索结果和网页访问记录）等，我们构建了一个以实体为锚定的开放世界知识记忆。进一步，我们基于采样的实体和相关知识构造多风格的（问题，答案）对，以尽可能涵盖智能体所面临的真实场景。
![](https://image.cubox.pro/cardImg/5ghfzwy8d3e568y5urri2tbs4mkwj5e1fwzgrm1bz34fxj3clf.png?imageMogr2/quality/90/ignore-error/1)

**动作合成** 基于多风格问题和历史轨迹数据，我们分别构建了三种类型的动作数据，包含单步的规划、推理动作和多步的决策动作合成。我们的方法能够在离线环境下大规模、全面地探索潜在的推理‑动作空间，从而消除了对额外商业工具 API 调用的需求。例如，对于决策动作合成，我们将原始轨迹中的步骤进行扩展，并最终建模成多步骤决策过程数据，以激发模型的探索能力和决策能力。

### 后训练数据

**High‑quality QA**

我们开发了一套端到端的合成数据生成解决方案。这一全自动流程无需人工干预即可构建超越人类质量的数据集，旨在突破智能体的性能极限。经过长期的探索和迭代------从早期的网页点击流逆向工程Benchmark（WebWalker）到更系统的基于图谱的合成方法（WebSailor 和 WebSailor‑V2），再到形式化的任务建模（WebShaper），我们的方法确保了卓越的数据质量和强大的可扩展性，突破了模型能力的上限。

为了解决复杂且高度不确定的问题，我们通过一种新颖的流程合成基于 Web 的问答数据。该流程首先通过在高度互联的知识图谱随机游走和基于表格数据融合同构表构建，将来自真实网站数据整合，并确保信息结构的真实性。然后，我们对子图和子表进行采样，生成初始问题和答案。关键步骤是通过策略性地混淆或模糊问题中的信息来增加问题难度。该方法基于一个组合泛化的理论框架，我们将问答难度正式建模为一系列可控的"原子操作"（例如，合并具有相似属性的实体），这些操作基于实体关系，使我们能够系统地增加复杂性。

为了进一步减少问答系统的信息结构与推理结构之间的不一致性，提高推理难度和结构扩展能力，我们提出了一种基于集合论的信息搜索问题形式化建模。基于这种建模，我们开发了能够以可控方式扩展问题的智能体，并最大限度地减少了推理捷径和结构冗余，从而进一步提升了问题质量。此外，这种形式还能高效地验证问答的正确性，有效解决了信息搜索合成数据难以验证的挑战。

此外，我们还开发了一个自动化学术数据构建流程，以扩大博士级研究问题的规模。该引擎基于多学科知识库，生成需要多源推理的"种子"问答对。然后，每个种子都会进入一个自我引导的"迭代复杂性升级"循环，其中，一个问题构建代理配备了一套强大的工具，包括网络搜索、学术检索和 Python 执行环境。在每次迭代中，代理都会扩展知识边界，深化概念抽象，甚至构建计算任务，从而形成一个演化循环，上一轮的输出成为下一轮更复杂的输入，确保任务难度的可控且系统地升级。

**融合多样推理模式，激发智能体潜能**

为激发模型的初始能力，我们基于 ReAct 和 IterResearch 框架，通过拒绝采样的方式构建了一组轨迹。一方面，ReAct 作为一个经典且基础的多轮推理范式，为模型注入了丰富的推理行为，并加强了其遵循结构化格式的能力。

另一方面，我们引入了一种创新的智能体范式------IterResearch（下文将详细介绍）。它通过在每一轮动态地重构一个精简的工作空间，来释放模型的全部推理潜力，从而确保每一个决策都经过深思熟虑，不受上下文噪声干扰。借助 IterResearch，我们构建了一组融合了推理、规划和工具使用的轨迹，从而加强了模型在面对复杂问题时的持续规划能

## Rollout模式

我们对深度研究型智能体的部署范式进行了广泛的探索。因此，我们的最终模型支持多种部署格式，包括原生的 ReAct 模式和上下文管理的深度模式。

### ReAct 模式

我们的模型使用ReAct推理范式展现出卓越的性能。它严格遵循"思考‑行动‑观察"的循环，通过多次迭代来解决问题。模型上下文长度为 128K，可以处理大量的交互轮次，从而完全实现与环境交互的可扩展性。ReAct 的简单性和通用性为模型的内在能力和我们训练流程的有效性提供了最清晰的基准。

我们选择ReAct很大程度上受到了"The Bitter Lesson"的影响，利用可扩展计算的通用方法最终将优于依赖复杂的人工知识和复杂设计的方法。

### 深度模式

除了 ReAct 模式外，我们还开发了"深度模式"，用于处理极端复杂的多步研究任务。此模式基于我们全新的 IterResearch 范式，旨在将Agent的能力发挥到极致。

IterResearch 范式的创建是为了解决Agent将所有信息堆积在一个不断扩展的单一上下文窗口中时出现的认知瓶颈和噪音污染。针对多步研究任务，IterResearch 将其解构为一系列研究回合。
![](https://image.cubox.pro/cardImg/ct894412vrjhjumt7vn16zmjny0zvykt1dz0ggxlwdujf0oec.png?imageMogr2/quality/90/ignore-error/1)

在每一轮中，Agent仅使用上一轮中最重要的输出来重建一个精简的工作空间。在这个专注的工作空间中，Agent会分析问题，将关键发现整合成一个不断演变的核心报告，然后决定下一步行动------是收集更多信息还是提供最终答案。这种"综合与重构"的迭代过程使Agent能够在执行长期任务时保持清晰的认知焦点和高质量的推理能力。

在此基础上，我们提出了Research‑Synthesis框架。并行使用多个IterResearch Agent探索同一个问题。并最终整合它们完善的报告和结论，从而得出更准确的最终答案。这种并行结构使模型能够在有限的上下文窗口内考虑更广泛的研究路径，从而将其性能推向极限。
![](https://image.cubox.pro/cardImg/5z6v9cdmxu0bh7g338d7kbr3as5hz2wyokc1c8wnfekoejv0cy.png?imageMogr2/quality/90/ignore-error/1)

## 端到端Agent训练流程

![](https://image.cubox.pro/cardImg/2p0t2nf55e0vciaj3i0e93oqbnnjpgk0ms5tdrud5c4sedbp0k.png?imageMogr2/quality/90/ignore-error/1)

训练这样的Agent模型需要**重新思考整个模型训练流程**，从预训练到微调再到强化学习。我们建立了一套完整的智能体模型训练范式，将Agentic CPT → Agentic SFT → Agentic RL 连接起来，为 AI Agent创建了一个无缝的端到端训练循环。以下是我们利用强化学习解决最后阶段的方法，这对于使代理的行为与高阶目标保持一致至关重要：

### 基于On-Policy策略的智能体强化学习 (RL)

通过强化学习构建高质量的Agent是一项复杂的系统工程挑战；如果将整个开发过程视为一个"强化学习"循环，其组件中的任何不稳定或鲁棒性不足都可能导致错误的"奖励"信号。接下来，我们将分享我们在强化学习方面的实践，涵盖算法和基础设施两个方面。

在强化学习（RL）算法方面，我们基于GRPO进行了定制优化。我们严格遵循 on‑policy 的训练范式，确保学习信号始终与模型当前的能力精准匹配。同时，我们采取了一个 token 级别的策略梯度损失函数来优化训练目标。其次，为了进一步降低优势估计（advantage estimation）的方差，我们采用了留一法 (leave‑one‑out) 策略。此外，我们发现未经筛选的负样本会严重影响训练的稳定性，这种不稳定性在长时间训练后可能表现为"格式崩溃"（format collapse）现象。为缓解此问题，我们会选择性地将某些负样本排除在损失计算之外，例如那些因过长而未能生成最终答案的样本。出于效率考虑，我们没有采用动态采样，而是通过增大批次（batch size）和组规模（group size）的方式，来维持较小的方差并提供充足的监督信号。
![](https://image.cubox.pro/cardImg/n1q2senc8ffdazdx4kghv6kghmyrrc99lvdi7tnkz3cn17rzp.png?imageMogr2/quality/90/ignore-error/1)

训练过程的动态指标显示，模型学习效果显著，奖励（reward）呈持续上升趋势。同时，策略熵（policy entropy）始终维持在较高水平，这表明模型在持续进行探索，有效防止了过早收敛。我们将此归因于Web环境天然的非平稳性，该特性促进了稳健自适应策略的形成，也因此无需再进行显式的熵正则化。

我们认为，**算法固然重要，但并非 Agentic RL 成功的唯一决定因素。** 在尝试了多种算法和优化技巧后我们发现，**数据质量和训练环境的稳定性，可能是决定强化学习项目成败的更关键一环** 。一个有趣的现象是，我们曾尝试直接在 BrowseComp 测试集上训练，但**其表现远不如**使用我们合成数据的结果。我们推测，这种差异源于合成数据提供了一致性更高的分布，使模型能进行更有效的学习和拟合。相比之下，像 BrowseComp 这样的人工标注数据，本身就含有更多噪声，加之其规模有限，导致模型很难从中提炼出一个可供学习的潜在分布，从而影响了其学习和泛化（generalize）能力。这一发现对其他智能体的训练同样具有启发意义，为构建更多样、更复杂的智能体训练方案提供了思路。
![](https://image.cubox.pro/cardImg/3ulv318fj8i9qdxjm0mdqnu3bc7bgw8uu5fmknc6knqijo4yyv.png?imageMogr2/quality/90/ignore-error/1)

在基础设施方面，使用工具训练智能体需要一个高度稳定高效的环境：

● 仿真训练环境：依赖实时 Web API 进行开发成本高昂、速度慢且不一致。我们利用离线维基百科数据库和自定义工具套件创建了一个模拟训练环境来解决这一问题。并且通过SailorFog‑QA‑V2的流程，为该环境生成专属的高质量数据，创建了一个经济高效、快速可控的平台，显著加快了我们的研究和迭代速度。

● 稳定高效的工具沙盒：为了确保在智能体训练和评估期间对工具的稳定调用，我们开发了一个统一的沙盒。该沙盒通过缓存结果、重试失败的调用以及饱和式响应等改进来高效地处理并发和故障。这为智能体提供了快速且鲁棒的交互环境，可以有效防止工具的错误响应破坏其学习轨迹。

● 自动数据管理：数据是提升模型能力的核心驱动力，其重要性甚至超过了算法。数据质量直接决定了模型是否能通过自我探索提升分布外泛化能力。因此，我们在训练动态的指导下实时优化数据，通过全自动数据合成和数据漏斗动态调整训练集。通过数据生成和模型训练之间的正向循环，这种方法不仅确保了训练的稳定性，还带来了显著的性能提升。

● On‑Policy策略的异步框架：我们在 rLLM 之上实现了异步强化学习训练推理框架，多个智能体实例并行与（模拟或真实）环境交互，独立生成轨迹。

通过这些措施，我们实现了智能体强化训练的"闭环"。从基座模型开始，我们进行了Agentic持续预训练以初始化工具使用技能，然后使用类似专家的数据进行监督微调以实现冷启动，最后进在on‑policy的强化学习，使模型进行自我进化。这种全栈方法为训练能够在动态环境中稳健地解决复杂任务的 AI 代理提供了一种全新的范例。

（我们的强化学习算法受到 [Agentica](https://agentica-project.com/index.html) 过去研究的启发。我们基于[rLLM](https://github.com/rllm-org/rllm)框架进行开发和扩展，实现高效训练）

## 应用及影响

通义Deep Research不仅仅是一个研究成果的展示，它已经在阿里巴巴内外赋能实际应用，并在实际场景中展现其价值：

**高德地图（地图导航智能体）** 高德 App 作为通义在集团内长期共建的重点客户，其"地图导航+本地生活"的业务场景，以及高德内部丰富的专用工具，具备构建Deep Research 类 Agent 的土壤，高德也将这种能力作为 25 年暑期大版本 V16 的一个亮点功能。通义团队近期在地图+本地生活场景，基于纯agentic + ReAct执行复杂推理的垂类Deep Research技术建设，为高德提供更好效果的模型。因此，双方团队共建合作，"通义团队提供Deep Research模型 + 高德团队提供工具和 Agent 链路"，打造了高德 App 中助手「小高老师」的复杂查询体验，在地图行业内打出影响力。
![](https://image.cubox.pro/cardImg/352epjnevd70gbhg8wqjgafl3woubxmon9splcr5osq39izb3b.png?imageMogr2/quality/90/ignore-error/1)

**通义法睿（法律Deep Research）** 作为大模型原生的"法律智能体"，致力于为大众及法律从业者提供专业、便捷的法律智能服务。集法律问答、案例法条检索、合同审查、文书阅读、文书起草等功能于一体，全面满足法律用户需求。依托创新的Agentic架构与迭代式规划（Iterative Planning）技术，通义法睿全新升级司法DeepResearch能力，可高效执行多步查询与复杂推理，实现权威类案精准检索、法条智能匹配与专业观点深度融合。我们以真实判例、官方法规和权威解读为基础，打造可追溯、高可信的法律分析服务，在法律问答的深度研究三大核心维度------答案要点质量、案例引用质量、法条引用质量上领先行业。
![](https://image.cubox.pro/cardImg/1oifbr6swgbss253z2vb3lsm14nwshpzmbji777qytbgrcsz7u.png?imageMogr2/quality/90/ignore-error/1)

## 未来工作

我们未来的工作将致力于解决以下三个关键局限性：首先，当前 128k 的上下文长度在处理极端复杂的长程推理任务时仍显不足。为此，我们将探索扩展上下文窗口的有效方法，并研究更精细的上下文管理策略。其次，我们训练流程的可扩展性在远超 30B 参数规模的模型上尚未得到充分验证，我们计划在更大规模的模型上测试并验证我们流程的有效性。最后，我们旨在通过引入 partial rollouts 等技术进一步提升强化学习框架的效率，这需要我们攻克离线训练所面临的挑战，尤其是分布偏移问题。

## 系列工作

![](https://image.cubox.pro/cardImg/3o74gz5rp5dubud2ochk9u41ar4072b8b6k9mzay2aw6cylujq.png?imageMogr2/quality/90/ignore-error/1)

通义Deep Research也拥有丰富的Deep Research Agent家族。您可以在以下论文中找到更多信息：

\[1\] [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/pdf/2501.07572)

\[2\] [WebDancer: Towards Autonomous Information Seeking Agency](https://arxiv.org/pdf/2505.22648)

\[3\] [WebSailor: Navigating Super‑human Reasoning for Web Agent](https://arxiv.org/pdf/2507.02592)

\[4\] [WebShaper: Agentically Data Synthesizing via Information‑Seeking Formalization](https://arxiv.org/pdf/2507.15061)

\[5\] [WebWatcher: Breaking New Frontier of Vision‑Language Deep Research Agent](https://arxiv.org/pdf/2508.05748)

\[6\] [WebResearch: Unleashing reasoning capability in Long‑Horizon Agents](https://arxiv.org/abs/2509.13309)

\[7\] [ReSum: Unlocking Long‑Horizon Search Intelligence via Context Summarization](https://arxiv.org/abs/2509.13313)

\[8\] [WebWeaver: Structuring Web‑Scale Evidence with Dynamic Outlines for Open‑Ended Deep Research](https://arxiv.org/abs/2509.13312)

\[9\] [WebSailor‑V2: Bridging the Chasm to Proprietary Agents via Synthetic Data and Scalable Reinforcement Learning](https://arxiv.org/abs/2509.13305)

\[10\] [Scaling Agents via Continual Pre‑training](https://arxiv.org/abs/2509.13310)

\[11\] [Towards General Agentic Intelligence via Environment Scaling](https://arxiv.org/abs/2509.13311)

我们的团队长期致力于Deep Research的研发。过去六个月，我们每月持续发布一篇技术报告，迄今为止已发布五篇。今天，我们非常高兴地同时发布六篇新报告，并与社区分享我们的通义DeepResearch‑30B‑A3B模型。

敬请期待我们下一代Agent模型。

    @misc{tongyidr,
      author={Tongyi DeepResearch Team},
      title={Tongyi DeepResearch: A New Era of Open-Source AI Researchers},
      year={2025},
      howpublished={\url{https://github.com/Alibaba-NLP/DeepResearch}}
    }

[Read in Cubox](https://cubox.pro/web/card/7375797183372594179)

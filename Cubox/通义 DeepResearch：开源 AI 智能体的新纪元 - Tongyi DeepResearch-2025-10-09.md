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


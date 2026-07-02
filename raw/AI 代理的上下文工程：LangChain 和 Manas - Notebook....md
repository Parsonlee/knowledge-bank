---
id: "7383111332934979442"
cubox_url: https://cubox.pro/web/card/7383111332934979442
url: https://notebooklm.google.com/notebook/317f5e39-3a3c-4bb6-a0f2-85f842c2f385
tags:
  - AI-Agent/context-engineering
---
# AI 代理的上下文工程：LangChain 和 Manas - NotebookLM --- Context Engineering for AI Agents: LangChain and Manas - NotebookLM

Use the power of AI for quick summarization and note taking, NotebookLM is your powerful virtual research assistant rooted in information you can trust.

[Read in Cubox](https://cubox.pro/web/card/7383111332934979442)  
[Read Original](https://notebooklm.google.com/notebook/317f5e39-3a3c-4bb6-a0f2-85f842c2f385)  

---


---

## 📖 正文全文

# Context Engineering for AI Agents: LangChain and Manas AI 代理的上下文工程：LangChain 和 Manas

[notebooklm.google.com](https://notebooklm.google.com/notebook/317f5e39-3a3c-4bb6-a0f2-85f842c2f385)

Building Smarter AI Agents: 4 Surprising Truths About Managing Context  
构建更智能的 AI 代理：管理上下文有 4 个惊人的真相

If you've built an AI agent, you've likely experienced this frustrating scenario: your agent excels at simple, self-contained tasks, but as you give it more complex, long-running objectives, it starts to get lost. It forgets previous steps, calls the wrong tools, and becomes inefficient, despite being powered by a state-of-the-art model.  
如果你已经构建了一个 AI 代理，你可能经历过这个令人沮丧的场景：你的代理在简单、自包含的任务上表现出色，但当你给它更复杂、长时间运行的目标时，它开始迷失。它忘记之前的步骤，调用错误的工具，并且效率低下，尽管它是由最先进的模型驱动的。

This is the central paradox of agent development. On one hand, agents need a rich history of their actions and tool outputs to make informed decisions. Production agents can easily span hundreds of turns, accumulating a massive amount of context. On the other hand, a growing body of research and developer experience shows that model performance drops as context grows.  
这是代理开发的核心悖论。一方面，代理需要丰富的行动和工具输出历史来做出明智的决策。生产代理可以轻松跨越数百个回合，积累大量的上下文。另一方面，越来越多的研究和开发者经验表明，随着上下文的增长，模型性能会下降。

The solution to this paradox is a discipline called **Context Engineering** , which experts at LangChain and Manus define as:  
解决这一悖论的方法是一种称为上下文工程的学科，LangChain 和 Manus 的专家将其定义为：

"the delicate art and science of filling the context window with just the right information needed for the next step"  
"一种精妙的艺术和科学，用恰到好处的信息填充上下文窗口，以供下一步使用"

It's about intelligently managing what the model sees, ensuring it has everything it needs and nothing it doesn't. This article distills four of the most impactful and counter-intuitive lessons on context engineering from a recent discussion between experts at LangChain and Manus, providing a practical guide for building more robust and capable AI agents.  
这关乎智能地管理模型所见内容，确保它拥有所需的一切，又不会有多余。本文从 LangChain 和 Manus 专家最近的一次讨论中提炼出关于上下文工程的四条最具影响力和反直觉的教训，为构建更健壮和强大的 AI 代理提供实用指南。

Takeaway 1: Context Engineering is a Strategic Boundary, Not Just a Technical Fix  
要点 1：上下文工程是一种战略边界，而不仅仅是技术修复

When an agent struggles, the common temptation for developers is to reach for fine-tuning. The logic seems sound: "If I train a base model on my specific data and use case, it will surely perform better."  
当代理遇到困难时，开发者的常见诱惑是进行微调。这种逻辑看似合理："如果我针对我的特定数据和用例训练基础模型，它肯定会表现更好。"

However, Peak, co-founder of Manus, argues that for startups and fast-moving product teams, this is a "trap" rooted in his own hard-won experience. At a previous startup, his team trained their own language models from scratch. The result was a painful bottleneck. "Our product's innovation speed was completely capped by the model's iteration speed," he recalls, noting that "a single training plus evaluation cycle could take... one or two weeks."  
然而，Manus 的联合创始人 Peak 认为，对于初创公司和快速发展的产品团队来说，这是一种源于他自身宝贵经验的"陷阱"。在他之前创办的创业公司里，他的团队从零开始训练自己的语言模型。结果是一个痛苦的瓶颈。"我们产品的创新速度完全被模型的迭代速度所限制"，他回忆道，并指出"一次训练加评估周期可能需要...一到两周。"

Relying on context engineering instead of fine-tuning allows a company's innovation speed to remain independent of the model's slow iteration cycle. This choice is about more than just technology; it's a strategic decision to draw a clear line between your application and the underlying model. As Peak puts it:  
依靠上下文工程而不是微调，可以让公司的创新速度独立于模型的缓慢迭代周期。这个选择不仅仅关乎技术；它是一个战略决策，旨在明确区分你的应用和底层模型。正如 Peak 所说：

"be firm about where you draw the line right now context engineering is the clearest and most practical boundary between application and model so trust your choice"  
"现在就要坚定地划定界限。上下文工程是应用和模型之间最清晰、最实际的分界线，所以相信你的选择。"

This insight is crucial. It keeps product development agile and prevents teams from getting bogged down in the complex, expensive work of model training. It allows you to leverage the rapid improvements in foundation models without tying your product's fate to a single, slow-moving training pipeline. Ultimately, it stops you from trying to become an LLM company yourself, because you're "rebuilding the same layer that they have already built and that's a duplication of effort."  
这一见解至关重要。它使产品开发保持敏捷，并防止团队陷入复杂且昂贵的模型训练工作中。它让你能够利用基础模型的快速改进，而无需将产品的命运与单一的、进展缓慢的训练管道绑定。最终，它阻止你试图自己成为一家 LLM 公司，因为你在"重建他们已经构建好的相同层级，这是重复劳动。"

Takeaway 2: Not All Context Reduction is Equal---The Power of Reversibility  
要点 2：并非所有上下文减少都相同------可逆性的力量

To keep the context window lean, you must reduce the information within it. But before you start summarizing, it's critical to understand that most models start degrading long before they hit their hard context limit---a phenomenon Manus calls "context rot." To combat this, they identify a "pre-rot threshold," typically between 128K and 200K tokens, which serves as the trigger for context reduction. When this threshold is crossed, Manus employs two distinct methods: **compaction** and **summarization** . The key difference lies in one critical concept: reversibility.  
为了保持上下文窗口的简洁，你必须减少其中的信息。但在开始总结之前，关键是要理解大多数模型在达到其硬性上下文限制之前就已经开始退化------这种现象被 Manus 称为"上下文腐化"。为了应对这种情况，他们确定了一个"预腐化阈值"，通常在 128K 到 200K 个 token 之间，这作为上下文减少的触发点。当跨越这个阈值时，Manus 采用两种不同的方法：压缩和总结。关键的区别在于一个关键概念：可逆性。

**Compaction** is a *reversible* process. It strips out information that can be reconstructed from an external state, like a file system. For example, consider a tool that writes content to a file. The full tool output includes both the file `path` and the lengthy `content`. The compacted version would drop the `content` field entirely, keeping only the `path`. The full content isn't lost; the agent can simply read the file again if it needs it.  
压缩是一个可逆的过程。它会移除可以从外部状态（如文件系统）重建的信息。例如，考虑一个将内容写入文件的工具。完整的工具输出包括文件 `path` 和冗长的 `content` 。压缩版本会完全删除 `content` 字段，仅保留 `path` 。完整内容并未丢失；如果代理需要，可以再次读取文件。

Crucially, compaction isn't an all-or-nothing affair. As Peak explains, "we might compactate like the oldest 50% of tool calls while keeping the newer ones in full detail so the model still has fresh few-shot examples." This reversibility is vital because, as Peak notes, "you never know like which past action will suddenly become super important like 10 steps later."  
关键在于，压缩并非一刀切的事情。正如 Peak 解释的那样，"我们可能会压缩最老的 50%的工具调用，同时保留较新的调用以完整细节，这样模型仍然有新鲜的少量示例。"这种可逆性至关重要，因为 Peak 指出，"你永远不知道哪个过去的行动会在 10 步后突然变得极其重要。"

**Summarization** , by contrast, is an *irreversible* process used only as a last resort when the context window ceiling is hit, even after compaction. To mitigate information loss, Manus uses it very carefully. Before summarizing, the entire pre-summary context is offloaded to a file, creating a backup log the agent can later search with tools like `glob` or `grep`. They also follow a critical rule: "when summarizing we always use the full version of the data not the compact one." This safeguard prevents compounding information loss from one reduction cycle to the next.  
相比之下，摘要是一个不可逆的过程，仅在达到上下文窗口上限后，即使经过压缩仍作为最后的手段使用。为了减少信息丢失，Manus 非常谨慎地使用它。在摘要之前，整个预摘要上下文会被卸载到一个文件中，创建一个代理稍后可以使用 `glob` 或 `grep` 等工具搜索的备份日志。它们还遵循一个关键规则："在摘要时，我们始终使用完整版数据，而不是压缩版。"这个保护措施防止了信息在一次次压缩循环中累积丢失。

Takeaway 3: Offload Your Tools, Not Just Your Data  
要点 3：卸载你的工具，而不仅仅是数据

As an agent's capabilities grow, so does its list of available tools. This leads to "context confusion," a state where the model has too many tools in its prompt and starts calling the wrong ones or hallucinating invalid parameters.  
随着智能体能力的增长，其可用的工具列表也会随之增加。这会导致"上下文混淆"的状态，即模型在提示中包含太多工具，开始调用错误的工具或产生无效的参数幻觉。

Manus's novel solution is not just to offload data, but to offload the tools themselves through a **layered action space** . This architecture dramatically expands the agent's abilities without cluttering its primary context. It consists of three levels:

• **Level 1: Function Calling:** This is a small, fixed set of atomic functions that are always present in the prompt (e.g., read/write file, execute shell command). Keeping this set minimal ensures the primary interface remains simple and cache-friendly.

• **Level 2: Sandbox Utilities:** These are pre-installed command-line tools running inside a VM sandbox---things like **format converters** , **speech recognition utilities** , or even a custom **MCP CLI** . The agent accesses them through the `execute shell` function from Level 1, adding new capabilities without ever changing the function-calling space. This approach is "super good for large outputs," Peak notes, but has a trade-off: "it's also not that good for low latency back and forth interactions with the front end."

• **Level 3: Packages and APIs:** For the most complex tasks, the agent writes and executes scripts (e.g., in Python) to interact with external APIs or libraries. This is perfect for heavy computations where only the final result matters. For example, "imagine if you're analyzing a stock's entire year of price data," says Peak. "You don't feed the model all the numbers; instead, you should let the script to compute it and only put the summary back into the context."

This layered approach is a powerful paradigm shift. Instead of giving the agent a hundred different tools directly, you give it three very powerful *methods* for getting work done. This keeps the model's immediate job simple and focused while giving it a near-infinite action space to draw upon.

Takeaway 4: The Paradoxical Path to a Smarter Agent Is to Build Less

After exploring these advanced techniques, the final and most surprising lesson is a call for simplicity. Since launching in March, the Manus team has **refactored their system five times** , and they found that their biggest breakthroughs didn't come from adding more complexity.

The core insight is that over-engineering context management can be counterproductive. Every layer of abstraction you add is another potential point of failure and another concept the model has to understand. The most significant performance gains came from removing unnecessary components and placing more trust in the raw capabilities of the underlying model. Peak shared this powerful observation:

"the biggest leap we've ever seen didn't came from like adding more fancy context management layers or clever retrieval hacks they all came from simplifying or from like removing unnecessary tricks and trusting the model a little more"

This philosophy reframes the entire goal of context engineering. The objective isn't to build a complex scaffold *around* the model; it's to create the simplest possible environment that allows the model to do its job effectively.

Conclusion: A Final Thought

The journey of building a sophisticated AI agent is one of continuous learning. We start by understanding *why* context engineering is a strategic necessity, not just a technical one. We then learn specific techniques for managing context, like reversible compaction and layered tool offloading. But the ultimate lesson is perhaps the most profound: the path to a smarter agent often lies in simplification.

As you continue your work, keep Peak's final piece of advice in mind as a guiding principle:

"if you like take one thing from today I think it should be build less and understand more"

As you build your next AI agent, what is one piece of complexity you can remove to trust the model more?

[Read in Cubox](https://cubox.pro/web/card/7383111332934979442)

---
title: 我们如何利用 DSPy 将 AI 评估转化为 Dash Chat 的更优回复
source: https://www.bestblogs.dev/article/c2a3404e
author:
  - "[[Simran Jumani]]"
published: 2026-06-26
description: Dropbox 使用 DSPy 校准 LLM-as-judge 评估体系，进而自动优化 Dash Chat 智能体的系统提示词，实现了不完整回答减少 26%、token 使用量降低 5.4% 的效果。
tags:
  - AI-Agent/eval
---
## How we used DSPy to turn AI evaluations into better responses in Dash Chat

Dropbox 使用 DSPy 校准 LLM-as-judge 评估体系，进而自动优化 Dash Chat 智能体的系统提示词，实现了不完整回答减少 26%、token 使用量降低 5.4% 的效果。

⭐ 推荐理由

Dropbox 分享了 Dash Chat 的 AI 评估闭环工程路径：先用人工标注样本校准 LLM-as-judge 评判器，再由 DSPy 的 GEPA 算法自动优化系统提示词。最终实现不完整回答减少 26%、遗漏关键要点降低 13%、token 用量下降 5.4%。文章强调评估应覆盖完整交互轨迹而非仅看最终回复，为评估驱动的智能体优化提供了完整工程范本。

[Dropbox Tech Blog](https://www.bestblogs.dev/articles?sourceid=2ded56 "查看该来源的更多文章")

06-262091 字 (约 9 分钟)

[查看原文 →](https://dropbox.tech/machine-learning/how-we-turned-ai-evaluations-into-better-responses-in-dash-chat)

### 摘要

本文介绍了 Dropbox 如何为其 Dash Chat 产品构建严谨的智能体评估框架，随后利用 DSPy 配合 GEPA 和 MIPROv2 等优化算法，将 LLM 评判器与人工标注样本进行校准。在获得可靠的评判器后，他们通过回放代表性对话、使用校准后的评判器为输出打分，并迭代筛选候选提示词，实现了聊天智能体系统提示词的自动优化。最终成果包括：不完整回答减少 26%、遗漏关键要点降低 13%、总 token 使用量减少 5.4%——且未牺牲回答质量。文章还涵盖了评估标准、失败编码方法论，以及关于自动提示词优化防护机制的经验教训。

### 主要内容

- 1\. 智能体评估必须考察完整交互轨迹，而非仅看最终回复。
	与传统搜索相关性不同，智能体交互涉及多步推理、工具使用和回合对话；评估中间决策对于识别失败的根本原因至关重要。
- 2\. 人工标注样本用于校准 LLM 评判器，使其与人工判断保持一致。
	Dropbox 收集了一小批标注 dataset，从意图遵循、上下文选择、工具使用等维度进行评分，随后使用 DSPy 优化评判器提示词，以最小化与人工评估的分歧。
- 3\. 基于回放与生产环境对齐评分的自动提示词优化，优于手动迭代。
	通过回放代表性历史对话 对话并运用校准后的评判器为智能体输出打分，GEPA 生成候选提示词并在真实行为中验证，将探索速度提升一倍。
- 4\. 质量提升与效率改进均可量化且效果显著。
	优化后的智能体将不完整回答减少 26%、遗漏关键要点降低 13%、token 使用量减少 5.4%——表明评估驱动的优化能够同时改善质量与成本。

The AI features in Dropbox bring together company knowledge from documents, messages, meetings, and other sources. Users can then ask questions in one place and get answers from the Dash Chat agent. Agent quality—how well our chat agent helps users accomplish their goals—is evaluated using a suite of large language model-as-judge evaluations. These evaluations provide a way to measure how well an agent is performing and identify opportunities to improve. Rather than judging only a final response, they inspect the full trajectory an agent takes to satisfy a user’s goal: how it interprets intent, gathers context, uses tools, handles ambiguity, grounds its answer, and completes the task.  
Dropbox 中的人工智能功能能够整合来自文档、消息、会议以及其他来源的公司知识。用户可以在一个平台上提出问题，然后获得 Dash Chat 智能客服的回复。智能客服的表现质量——即它们帮助用户实现目标的能力——是通过一系列基于大型语言模型的评估来衡量的。这些评估有助于衡量智能客服的绩效，并找出改进的机会。这些评估不仅关注最终回复的质量，还关注智能客服实现用户目标整个过程的表现：包括它们如何理解用户意图、收集上下文信息、使用各种工具、处理模糊性、明确回答要点以及完成任务等。

We built agent evaluations as the foundation for improving the chat agent. These evaluations are the powerhouses behind the judges that measure the chat outcomes, given the context available to the agent, including relevance, reasoning quality, evidence use, robustness, task completion, and alignment with user asks. Once we had that foundation, we used DSPy to turn evaluation into improvement. DSPy is an open-source framework for [optimizing AI systems](https://dropbox.tech/machine-learning/optimizing-dropbox-dash-relevance-judge-with-dspy) using evaluation feedback.  
我们构建了代理评估机制，作为改进聊天机器人的基础。这些评估结果是衡量聊天结果的关键指标，它们考虑了代理所面临的各种情境因素，包括相关性、推理质量、证据使用、系统的鲁棒性、任务完成度以及与用户需求的匹配程度等。一旦有了这个基础，我们就利用 DSPy 将评估结果转化为改进建议。DSPy 是一个开源框架，可用于通过评估反馈来优化人工智能系统。

We applied DSPy and its optimization algorithms in two stages. First, we used it to improve the judges themselves, calibrating them against a small set of human-labeled examples so their scores better matched human judgment. Then, we used those improved judges to optimize the chat agent’s system prompt. This created a feedback loop: human labels improved the judges, the judges produced scalable evaluation signals, and those signals improved the agent. As a result, users saw significantly fewer incomplete answers and we were able to reduce our token usage too, without compromising answer quality.  
我们在两个阶段应用了 DSPy 及其优化算法。首先，我们利用这些算法来改进评分器本身，通过针对一小组人工标注的样本进行校准，使得评分结果更能反映人类的判断。然后，我们利用改进后的评分器来优化聊天机器人的提示方式。这样形成了一个反馈循环：人类的标注数据提升了评分器的性能，评分器则产生了可扩展的评估指标，而这些评估指标又进一步改善了机器人的表现。结果就是，用户看到的不完整答案数量显著减少，同时我们还减少了令牌的使用量，而并未影响答案的质量。

In this story, we’ll explain how we set up the evaluation layer, calibrated judges against human labels, applied DSPy—along with its optimization algorithms such as GEPA and MIPROv2 to improve judge performance—and then used those judges to optimize the chat agent itself.  
在这个故事中，我们将介绍如何设置评估层，如何对评委的评分进行校准，以及如何应用 DSPy 算法——还包括使用 GEPA 和 MIPROv2 等优化算法来提高评委的评分能力。最后，我们利用这些评委的评分数据来优化聊天机器人的性能。

## The hidden complexity of agent evals代理行为的隐藏复杂性

Agent evaluation is significantly more complex than traditional search relevance evaluation because the object being judged is no longer a single, isolated output. Instead, it is the result of a multi-step process. The agent must interpret user intent, gather context, and decide when and how to use tools. It also needs to synthesize information across sources before determining whether to answer directly, search for more information, summarize its findings, or ask for clarification.  
代理评估比传统搜索相关性评估要复杂得多，因为被评估的对象已经不再是一个孤立的单一输出结果。相反，它是一个由多个步骤构成的过程。代理需要理解用户的意图，收集相关上下文信息，并决定何时以及如何使用各种工具。此外，代理还需要整合来自不同来源的信息，然后决定是直接回答用户的问题，还是寻找更多相关信息，或者总结自己的发现，或者寻求进一步的澄清。

This makes evaluation much broader. A good agent response might depend on multiple knowledge sources, including documents, prior messages, meeting notes, or tool calls such as search and read documents. The quality of the final answer depends not only on what information was found, but also on how the agent approached the task.  
这使得评估的范围变得更加广泛。一个优秀的智能体响应可能依赖于多个信息来源，包括文档、先前的消息、会议记录，以及诸如搜索和读取文档之类的工具调用。最终答案的质量不仅取决于找到了哪些信息，还取决于智能体处理任务的方式。

Agent interactions can also unfold across multiple turns. The system may need to clarify an ambiguous request, incorporate user feedback, revise its answer, or continue searching as the task evolves. As a result, evaluation cannot focus only on the final response. It must also assess the decisions that led there.  
代理之间的互动也可能发生在多个回合中。系统可能需要澄清一些模糊的请求，整合用户的反馈，修改自己的回答，或者随着任务的进展继续寻找解决方案。因此，评估不能仅仅关注最终的回应，还必须考量导致该回应产生的决策过程。

Because an agent is made up of multiple interacting components, each part of that process needs its own evaluation. We have to assess not just answer quality, but also intent understanding, tool use, context selection, synthesis, grounding, turn-by-turn adaptation, and overall task completion. Evaluating these dimensions separately helps us identify where failures occur and improve the underlying components more effectively.  
因为智能体是由多个相互协作的组成部分构成的，所以该过程中的每个部分都需要进行独立的评估。我们需要评估的不仅仅是问题的解答质量，还包括意图理解、工具的使用、上下文的选择、合成能力、基础信息的获取、逐步调整以及整体的任务完成情况。分别评估这些方面有助于我们找出问题所在，并更有效地改进相关的组件。

This raised an important challenge: before we could use evaluations to improve the chat experience, we first needed to ensure the judges themselves were reliable.  
这提出了一个重要的问题：在利用评估来改善聊天体验之前，我们首先需要确保评估者本身的可靠性。

To evaluate chat responses, we needed an LLM judge that could assess an answer in the context of the user’s intent. But before we could trust those judges, we needed to know whether their evaluations aligned with human judgment. That meant starting with a small set of human-labeled examples and an evaluation rubric that engineers could apply consistently.  
为了评估聊天机器人的回复，我们需要一个能够根据用户意图来评判答案的 LLM 裁判。但在信任这些裁判之前，我们必须确保他们的评估结果与人类判断一致。这意味着要从一组由人类标记好的样本开始，并制定一套工程师可以一致使用的评估标准。

==We sampled a set of internal chats, including the final responses and trace logs showing how the agent arrived at them, then asked human evaluators to review each example across five dimensions: user intent following, semantic relevance (how well the answer addressed the user's request), tool calling, instruction following, and context selection. Together, these dimensions capture what makes a chat agent valuable. They measure whether the agent understands the user's goal, gathers the right context, uses its tools effectively, follows instructions, and ultimately produces a grounded, useful response.  
我们收集了一系列内部聊天记录，包括最终的回复内容以及显示代理如何得到这些回复的跟踪日志。然后，我们让人类评估者从五个维度来评估每一例聊天内容：用户需求的满足程度、语义相关性（回答在多大程度上满足了用户的请求）、工具调用方式、指令的遵循情况以及上下文的选择。这些维度共同体现了聊天代理的价值所在。它们衡量了代理是否理解用户的意图，是否能够获取正确的上下文信息，是否能够有效使用相关工具，是否遵循指令，最终是否能够产生有实质意义且实用的回复。==

To keep assessments consistent, evaluators followed a structured review process. They first determined whether the agent understood the user’s intent and selected the right context. They then reviewed the searches, retrievals, and other tool actions used to gather that information before checking whether the claims in the final response were supported by the selected evidence. Finally, they scored the response for relevance, grounding, completeness, and instruction following.  
为了保持评估的一致性，评估人员遵循了规范化的审查流程。他们首先确认代理是否理解了用户的意图，并选择了正确的上下文。接着，他们审核了用于收集信息的搜索结果、检索结果以及其他工具操作，然后检查最终回复中的陈述是否得到了所选证据的支持。最后，他们从相关性、基础性、完整性以及遵循指示等方面对回复进行了评分。

Several metrics were scored on a 1–5 scale. Evaluators also recorded reasoning notes explaining their scores and assigned failure codes for issues such as stale evidence, missing context, unsupported claims, incomplete coverage, or failure to personalize. The reasoning notes captured why a response succeeded or failed, while the failure codes provided a structured way to categorize recurring problems.  
在 1 到 5 的评分标准中，对多个指标进行了评估。评估人员还记录了关于评分的理由说明，并为一些问题制定了相应的处理方案，例如证据过时、缺乏背景信息、无依据的断言、覆盖范围不完整，或者未能实现个性化处理等问题。这些理由说明解释了某个回答为何成功或失败，而处理方案则提供了一种结构化方式来分类那些反复出现的问题。

This richer supervision proved especially valuable. A score provides a useful summary, but the reasoning notes and failure codes reveal what went wrong and where. They can show whether the agent misunderstood the user’s intent, selected the wrong context, made a poor tool decision, missed an instruction, or produced an answer that was only partially relevant. That gave us signal not just on response quality, but on the underlying causes of failure.  
这种更严格的监督机制显得尤为重要。评分可以提供一个有用的总结，而推理记录以及错误代码则能揭示出了什么问题以及问题所在。这些信息可以帮助我们了解代理是否误解了用户的意图、选择了错误的上下文、做出了错误的工具决策、遗漏了某个指令，或者给出的答案只是部分相关而已。这样一来，我们不仅能够了解响应的质量，还能发现导致失败的根本原因。

These annotations were useful to optimize the judge’s prompts to minimize disagreements between the LLM judge and the human labelers, but they were also useful beyond judge training. Annotations also helped with debugging, error analysis, roadmap planning, and prioritizing improvements to the agent system. Most importantly, they gave us a reliable benchmark against which we could measure and improve the judges themselves.  
这些注释对于优化裁判员的提示非常重要，这样可以减少大型语言模型裁判员与人类标注员之间的分歧。不过，这些注释在裁判员培训之外也发挥着重要作用。它们还有助于调试、错误分析、规划发展路线以及确定对智能体系统进行改进的重点方向。最重要的是，这些注释为我们提供了一个可靠的基准，让我们能够衡量并改进裁判员的工作方式。

## From evaluating agents to improving them从评估代理程序到改进它们

With the rubrics and labeled data in place, we could begin improving the judges themselves. Our goal was to make the judges agree more closely with human evaluators while preserving the structured evaluation process. Doing so required more than a generic scoring prompt. The judge needed to follow a specific workflow (retrospectively, or reviewing traces after the chats ended): infer the user's intent, inspect the conversation, review the trace and supporting evidence, reason about context selection and tool use, and then assign a score along with failure codes and reasoning notes.  
在各项标准和数据都已确定之后，我们可以开始改进评委的评选方式了。我们的目标是让评委与人类评估者更加一致，同时保留原有的评估流程。要做到这一点，仅仅使用一个通用的评分提示是不够的。评委需要遵循特定的工作流程：首先推断用户的意图，然后检查对话内容，再查看对话记录及相关的证据，接着分析上下文选择以及工具的使用情况，最后给出评分以及相关的失败原因和解释说明。

==To improve judge performance, we used DSPy and optimization algorithms such as GEPA and MIPROv2. Think of DSPy as the toolkit, and GEPA and MIPROv2 as specific algorithms within that toolkit. These algorithms automatically proposed prompt changes and tested them against our human-labeled examples to identify improvements.  
为了提升法官的工作效率，我们采用了 DSPy 以及 GEPA 和 MIPROv2 等优化算法。可以将 DSPy 视为一套工具包，而 GEPA 和 MIPROv2 则是该工具包中的具体算法。这些算法能够自动提出改进建议，并通过与人类标注的示例进行比对，以确定需要优化的地方。==

==We supported several optimization strategies. In some cases, we allowed DSPy to rewrite a judge's instructions from the ground up. In others, we adapted an existing judge to a different underlying model while preserving the same evaluation behavior. We also supported targeted optimization, where the goal was to correct specific failure modes, such as over-scoring outdated information or underweighting missing context, without changing the overall rubric or evaluation process.  
我们支持了多种优化策略。在某些情况下，我们允许 DSPy 重新编写裁判的评分规则。在其他情况下，我们则将现有的裁判系统调整为使用不同的底层模型，同时保留其原有的评估机制。我们还支持有针对性的优化，即针对特定的问题进行调整，比如纠正过度重视过时信息或忽视缺失上下文的情况，而无需改变整体的评分标准或评估流程。==

Regardless of the optimization strategy, we relied on both scores and textual feedback from human evaluators. The scores told us when a judge disagreed with humans, while the feedback helped explain why. For example, if a judge consistently gave high scores to answers that relied on outdated information, we could update its instructions to better recognize and penalize that failure mode. Once we had judges that reliably reflected human judgment, we could use them as the foundation for improving the agent itself.  
无论采用何种优化策略，我们都是结合评分结果和人类评估者的文字反馈来做出决策的。评分结果让我们了解到哪些评委不同意人类的判断，而文字反馈则有助于我们理解原因。例如，如果某个评委总是给那些依赖过时信息的答案高分，我们可以修改指导方针，以更好地识别并惩罚这种错误模式。一旦我们有了能够可靠反映人类判断的评委，我们就可以利用他们作为改进智能体的基础。

![](https://image.jido.dev/20260625212958_4ab799a.webp)

Our chat agent’s prompt optimization used to be a largely manual process. Engineers reviewed failures, proposed prompt edits, tested them, and iterated. While this helped in individual cases, it was difficult to scale and hard to know whether a change would reliably improve production quality. We replaced that workflow with an automated, evaluation-driven loop built on labeled examples, production-aligned scorers, and offline counterfactual replay. For each GEPA round, a candidate prompt is replayed on representative historical Dropbox internal chats, and the resulting agent outputs are scored by the evaluation pipeline. Those scores, along with structured judge reasoning, become the feedback signal GEPA uses to propose the next prompt update.  
我们的聊天机器人提示优化过程过去主要依靠人工操作。工程师们会审查存在的问题，提出修改建议，然后进行测试并不断迭代改进。虽然这种方法在个别情况下效果不错，但很难实现规模化应用，而且很难确定某个修改是否真的能提升系统的性能。因此，我们采用了一种自动化、基于评估的优化流程。在每轮 GEPA 评估中，都会有一个候选提示在代表性的历史 Dropbox 内部聊天记录中进行测试，然后根据评估标准对机器人的输出结果进行评分。这些评分结果，加上评委的评判意见，共同构成了 GEPA 用于提出下一次提示更新的依据。

This grounds prompt optimization in realistic agent behavior rather than abstract examples or ad hoc judgments. The same replay infrastructure used to diagnose production failures is now part of the optimization loop itself, so each candidate is evaluated against representative interactions before being considered for launch. Optimization focused on concrete failure modes, including wrong context selection, incomplete answers, missed ambiguity, incorrect search-tool use, and loss of multi-turn context.  
这种优化方式将重点放在真实的智能体行为上，而不是抽象的例子或临时的判断。用于诊断生产故障的同一套回放机制，现在也被纳入了优化流程中。因此，在考虑某个候选方案投入使用之前，会先对其进行相关的评估，以判断其是否适合实际应用场景。优化的重点在于具体的故障模式，比如错误的上下文选择、不完整的回答、未能处理歧义问题、错误的搜索工具使用，以及多轮对话上下文的丢失等问题。

The result was a tighter feedback loop. We replayed representative examples, scored them with production-aligned evaluators, used those scores to guide the next GEPA proposal, and repeated the process until the data supported a launch candidate.  
结果就是形成了一个更紧密的反馈循环。我们重新评估了代表性案例，用与生产要求相一致的评分标准对它们进行打分，然后利用这些评分来指导下一个 GEPA 提案的制定。这个过程不断重复，直到找到一个可行的启动方案。

## Faster iteration and better quality更快的迭代过程与更高的质量

To measure the impact of this prompt optimization work, we focused on failure modes tied to semantic relevance and answer quality. (As mentioned earlier, semantic relevance measures whether the agent understood the user's request and addressed the right parts of it.) Answer quality measures whether the response was complete, useful, grounded, and well-formed. In practice, this meant tracking issues like incomplete answers and missed key aspects of a user's request.  
为了衡量这种针对性优化工作所带来的效果，我们重点关注了与语义相关性和回答质量相关的失败情况。如前所述，语义相关性指的是智能体是否能够理解用户的请求，并且能够准确回应其中的关键部分。而回答质量则体现在回答是否完整、有用、切题且结构清晰。实际上，这意味着需要关注诸如回答不完整、遗漏了用户请求的关键方面等问题。

For each new prompt, we compared its performance against the existing production prompt using the same set of examples. This gave us a cleaner apples-to-apples comparison and made it easier to determine whether a prompt change actually improved performance. We also tested whether the gains were statistically meaningful.  
对于每一个新的提示，我们都使用相同的示例集来比较其性能与现有的生产提示。这样就能进行更清晰的对比，从而更容易判断是否真的有性能提升。同时，我们还测试了这些提升是否具有统计学上的意义。

We used statistical tests to check whether the observed improvements were likely to reflect a real change, rather than random variation in the evaluation results. The optimization loop increased experimentation velocity. In the first two weeks, we generated six prompt candidates automatically, compared with five manual prompt changes in the prior month, nearly doubling the pace of exploration.  
我们使用统计测试来确认所观察到的改进是否确实属于真实的变化，而非评估结果中的随机波动。优化流程提升了实验的效率。在最初的两周内，我们自动生成了六个提示方案，而去年同期则需要手动调整五次提示方案，因此现在的探索速度几乎翻了一番。

The launch results were measurable: a 26% reduction in incomplete answers and a 13% reduction in missed key aspects, with improvements appearing within the first 24 hours. The optimized agent also became more efficient. Total token usage dropped by 5.4%, while average completion length decreased by 9.8%. Importantly, these efficiency gains did not come at the expense of answer quality.  
该系统的实施效果是显而易见的：不完整答案的比例减少了 26%，遗漏的关键信息比例减少了 13%。这些改进在 24 小时内就显现出来了。此外，优化后的智能助手也变得更加高效。整体代币使用量减少了 5.4%，平均完成时间则缩短了 9.8%。重要的是，这些效率的提升并没有影响答案的质量。

Together, these results show how agent evaluations and DSPy can create a practical feedback loop for improving agent behavior: identifying failure modes, generating candidate prompts, validating quality gains, and reducing serving costs.  
总的来说，这些结果表明，智能体评估与 DSPy 技术可以构建一个实用的反馈机制，以改进智能体的行为：识别故障模式、生成合适的提示语、验证性能提升的效果，以及降低服务成本。

## What’s next 接下来是什么？

==One of the biggest lessons from this work is that automated prompt optimization needs strong guardrails. We intentionally constrained most agent prompt edits to small, targeted instruction updates and added automated review checks for prompt structure, completeness, caching behavior, and size limits. These safeguards helped ensure that candidate prompts remained maintainable and production-safe as the optimization process became more automated.  
从这项工作中我们得到的一个重要启示是：自动化的提示优化需要严格的约束机制。我们故意将大多数智能体提示的修改限制在较小的、有针对性的指令更新上，并引入了自动化的审查机制，以检查提示的结构、完整性、缓存行为以及大小限制等方面是否符合要求。这些保护措施有助于确保在优化过程变得更加自动化的情况下，候选提示仍然易于维护且能够在生产环境中安全使用。==

More broadly, this experiment showed that prompt optimization brings traditional machine learning discipline to prompt engineering. By combining human-labeled evals, representative replay data, and GEPA-based optimization in DSPy, we treated prompts as measurable, optimizable artifacts rather than static instructions. This framework gave us a systematic way to search over the instructions, constraints, examples, and policies that shape model behavior, helping us move beyond intuition and manual iteration to identify failure modes, compare improvements, and validate impact before launch.  
更广泛地说，这个实验表明，快速优化能够将传统的机器学习领域引入提示工程领域。通过结合人类标记的评估数据、代表性的重放数据，以及基于 GEPA 优化的 DSPy 算法，我们将提示视为可测量、可优化的产物，而非静态的指令。这一框架为我们提供了一种系统化的方法，来探索那些影响模型行为的指令、约束条件、示例和政策因素，从而帮助我们超越直觉和手动迭代的方式，识别出潜在的失败模式，比较各种改进方案，并在产品发布之前验证其效果。

Longer term, agent optimization may look less like manual prompt iteration and more like a continuous machine learning workflow: replay representative data, run optimization jobs, compare candidates against evaluation datasets, review evidence, and ship validated improvements. As with traditional ML systems, weak evaluation signals can lead to brittle improvements, while strong evaluations, representative data, and expert review help changes generalize and keep regressions under control.  
从长远来看，代理优化工作可能不再需要反复的手动调整，而是更像是一个持续性的机器学习工作流程：重新处理代表性数据，执行优化任务，将候选方案与评估数据集进行比较，审查相关证据，然后推出经过验证的改进方案。就像传统的机器学习系统一样，即使评估效果不佳，也能产生有效的改进成果；而可靠的评估数据以及专家审核则有助于确保这些改进方案能够泛化应用，同时控制可能出现的回归问题。

The broader takeaway is that agent optimization works best when automation is paired with rigorous evaluation. Reliable judges, representative replay data, and clear success metrics create the feedback loop needed to improve agent behavior while keeping quality measurable and regressions under control.  
总的来说，当自动化与严格的评估相结合时，代理优化才能达到最佳效果。可靠的评判标准、具有代表性的回放数据以及明确的成功指标，能够形成必要的反馈机制，从而改进代理的行为，同时确保质量的可衡量性，并控制系统的偏差。

*Acknowledgments: Jongmin Baek, Josh Wilson, Akshay Bapat, Gonzalo Garcia, April Liu, Eric Wang, Hans Sayyadi, Prasang Upadhyaya, and Emeka Okafor Jr. We’re also grateful to the DSPy community for their engagement and support. Our DSPy collaborators offered guidance, discussions, and responsiveness as we applied DSPy to real production systems at Dropbox.  
感谢：Jongmin Baek、Josh Wilson、Akshay Bapat、Gonzalo Garcia、April Liu、Eric Wang、Hans Sayyadi、Prasang Upadhyaya 以及 Emeka Okafor Jr. 我们也感谢 DSPy 社区的成员们提供的支持与帮助。在将 DSPy 应用于 Dropbox 的实际生产系统过程中，我们的合作者们给予了指导、讨论以及及时的响应。*

*If building innovative products, experiences, and infrastructure excites you, come build the future with us! Visit* [*jobs.dropbox.com*](https://jobs.dropbox.com/) *to see our open roles.*  
如果你对打造创新的产品、体验以及基础设施充满热情，那么请加入我们，共同创造未来吧！请访问 jobs.dropbox.com，查看我们现有的职位信息。
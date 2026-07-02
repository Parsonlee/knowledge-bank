---
id: "7398619984923987075"
cubox_url: https://cubox.pro/web/card/7398619984923987075
url: https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/
tags:
  - AI-Agent/coding
  - AI-Agent/UI
---
# Generative UI: A rich, custom, visual interactive user experience for any prompt



[Read in Cubox](https://cubox.pro/web/card/7398619984923987075)  
[Read Original](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)  

---


---

\## 📖 正文全文

# Generative UI: A rich, custom, visual interactive user experience for any prompt

[research.google](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)

Generative UI is a powerful capability in which an AI model generates not only content but an entire user experience. Today we introduce a novel implementation of generative UI, which dynamically creates immersive visual experiences and interactive interfaces --- such as web pages, games, tools, and applications --- that are automatically designed and fully customized in response to any question, instruction, or prompt. These prompts can be as simple as a single word, or as long as needed for detailed instructions. These new types of interfaces are markedly different from the static, predefined interfaces in which AI models typically render content.

In our new paper, "[Generative UI: LLMs are Effective UI Generators](https://generativeui.github.io/static/pdfs/paper.pdf)", we describe the core principles that enabled our implementation of generative UI and demonstrate the effective viability of this new paradigm. Our evaluations indicate that, when ignoring generation speed, the interfaces from our generative UI implementations are strongly preferred by human raters compared to standard LLM outputs. This work represents a first step toward fully AI-generated user experiences, where users automatically get dynamic interfaces tailored to their needs, rather than having to select from an existing catalog of applications.

Our research on generative UI, also referred to as generative interfaces, comes to life today in the [Gemini app](https://blog.google/products/gemini/gemini-3-gemini-app) through an experiment called dynamic view and in AI Mode in [Google Search](http://blog.google/products/search/gemini-3-search-ai-mode).

![](https://image.cubox.pro/cardImg/sdsf6vyaet0yh069uhg3pn1qdtc2ux63obutpi6qq46kz2zr6.png?imageMogr2/quality/90/ignore-error/1)

*Generative UI is useful for a range of applications. For any user question, need, or prompt, as simple as a single word or as complex as elaborate instructions, the model creates a fully custom interface.* ***Left:*** [*Getting tailored fashion advice*](https://generativeui.github.io/static/demos/carousel.html?result=fashion-advisor)*.* ***Middle:*** [*Learning about fractals*](https://generativeui.github.io/static/demos/carousel.html?result=fractal-explorer)*.* ***Right:*** [*Teaching mathematics*](https://generativeui.github.io/static/demos/carousel.html?result=basketball-math)*.*

*For more examples see the* [*project page*](https://generativeui.github.io/)*.*

<br />

\## Bringing generative UI to Google products

<br />

Generative UI capabilities will be rolled out as two experiments in the [Gemini app](https://blog.google/products/gemini/gemini-3-gemini-app): dynamic view and visual layout. When using dynamic view, an experience built upon our generative UI implementation, Gemini designs and codes a fully customized interactive response for each prompt, using Gemini's agentic coding capabilities. It customizes the experience with an understanding that explaining the microbiome to a 5 year old requires different content and a different set of features than explaining it to an adult, just as creating a gallery of social media posts for a business requires a completely different interface to generating a plan for an upcoming trip.

Dynamic view can be used for a wide range of scenarios, from learning about [probability](https://generativeui.github.io/static/demos/carousel.html?result=rolling-an-8) to helping in practical tasks like [event planning](https://generativeui.github.io/static/demos/carousel.html?result=thanksgiving) and getting [fashion advice](https://generativeui.github.io/static/demos/carousel.html?result=fashion-advisor). The interfaces allow users to learn, play or explore interactively. Dynamic view, along with visual layout, are rolling out today. To help us learn about these experiments, users may initially see only one of them.

play silent looping video pause silent looping video

unmute video mute video

Example of generative UI in dynamic view based on the prompt, "Create a Van Gogh gallery with life context for each piece".

Generative UI experiences are also integrated into [Google Search](http://blog.google/products/search/gemini-3-search-ai-mode) starting with AI Mode, unlocking dynamic visual experiences with interactive tools and simulations that are generated specifically for a user's question. Now, thanks to Gemini 3's unparalleled multimodal understanding and powerful agentic coding capabilities, Gemini 3 in AI Mode can interpret the intent behind any prompt to instantly build bespoke generative user interfaces. By generating interactive tools and simulations on the fly, it creates a dynamic environment optimized for deep comprehension and task completion. Generative UI capabilities in AI Mode are available for Google AI Pro and Ultra subscribers in the U.S. starting today. Select "Thinking" from the model drop-down menu in AI Mode to try it out.

play silent looping video pause silent looping video

unmute video mute video

Example of AI Mode in Google Search with the prompt, "show me how rna polymerase works. what are the stages of transcription and how is it different in prokaryotic and eukaryotic cells".

<br />

\## How the generative UI implementation works

<br />

Our generative UI implementation, described in the [paper](https://generativeui.github.io/static/pdfs/paper.pdf), uses Google's Gemini 3 Pro model with three important additions:

1. *Tool access*: A server provides access to several key tools, like image generation and web search. This allows the results to be made accessible to the model to increase quality or sent directly to the user's browser to improve efficiency.
2. *Carefully crafted system instructions*: The system is guided by detailed instructions that include the goal, planning, examples and technical specifications, including formatting, tool manuals, and tips for avoiding common errors.
3. *Post-processing*: The model's outputs are passed through a set of post-processors to address potential common issues.

![](https://image.cubox.pro/cardImg/2uw334say64gm32idchmnlxl9vko17fxs556uu0q6tvphw69hv.png?imageMogr2/quality/90/ignore-error/1)

*A high-level system overview of the generative UI implementation.*

For some products, it might be preferable to consistently see results in specific styles. Our implementation could be configured for these products so that all results, including generated assets, are created in a consistent style for all users. Without specific styling instructions, the generative UI will select a style automatically, or the user can influence styling in their prompt, as in the case of dynamic view in the Gemini app.

![](https://image.cubox.pro/cardImg/4pe2sk8acz19w11oihabmctqcc3y3gyyv8q7zs1bm3pwwczk3d.png?imageMogr2/quality/90/ignore-error/1)

*Screenshots of generative UI results with consistent "Wizard Green" styling.*

<br />

\## Generative UI outputs are strongly preferred over standard formats

<br />

To facilitate consistent evaluations and comparisons of generative UI implementations, we created PAGEN, a dataset of human expert--made websites and will soon be releasing it to the research community.

To evaluate user preferences, we compared our new generative UI experience against various different formats: a website designed for a specific prompt by human-experts, the top Google Search result for the query, and baseline LLM outputs in raw text or the standard markdown formats.

The sites designed by human experts had the highest preference rates. These were followed closely by the results from our generative UI implementation, with a substantial gap from all other output methods. This evaluation did not take into account generation speed. We also show that the performance of generative UI strongly depends on the performance of the underlying model, and that our newest models perform substantially better. See more details in the [paper](https://generativeui.github.io/static/pdfs/paper.pdf).

<br />

\## Opportunities ahead

<br />

We are still in the early days of generative UI, and important opportunities for improvement remain. For example, our current implementation can sometimes take a minute or more to generate results, and there are occasional inaccuracies in the outputs; these are areas of ongoing research. Generative UI is an example of the [magic cycle of research](https://blog.google/technology/research/google-research-team-tackles-big-challenges-with-science/), where research breakthroughs lead to product innovation that opens up new opportunities for addressing user needs and in turn fuel further research. We see potential in extending generative UI to access a wider set of services, adapt to additional context and human feedback, and deliver increasingly more helpful visual and interactive interfaces. We are excited about the further opportunities ahead for generative UI.

[Read in Cubox](https://cubox.pro/web/card/7398619984923987075)

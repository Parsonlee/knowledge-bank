---
id: "7398058308050881507"
cubox_url: https://cubox.pro/web/card/7398058308050881507
url: https://mp.weixin.qq.com/s/V5cb4HAufxvbNackr8aLVg
tags:
  - AI-Agent/tools
---
# Human In the Loop竟然可以是个MCP?



[Read in Cubox](https://cubox.pro/web/card/7398058308050881507)  
[Read Original](https://mp.weixin.qq.com/s/V5cb4HAufxvbNackr8aLVg)  

---

## Annotations  

> 在普适化的Prompt作用下，当Agent发现需要澄清问题时，虽然会产生“疑问”，但是它会将疑问直接“打在公屏”上：在输出中阐述这个疑问。即使出现在“深度思考”的正文中，大模型也会试图通过既有知识尝试自主回答这个问题。
>
> 通过在提示词中加入一些轻微的引导，就可以将Agent的“疑问”——如“您想查询哪个地方的天气呢”——交给MCP做工具调用。此处给出了OpenLM大模型研发平台“AI搜索助手”中的提示词片段。  

[Link️](https://cubox.pro/web/annotations/cards/7398058308050881507?highlight=7398058521570316283)  

> 1）“人机回路”工具本身的Description
>
> 与Senquential-Thinking工具一样，“人机回路”工具的Description需要事无巨细，且具有极强的普适性描述。这是通用工具的一个无法回避的选择。此类描述虽然可以覆盖大部分场景，但是一旦出现和Agent的主提示词冲突的描述，那么将无法调和：大模型将无法判断哪一个描述更加重要。
>
> 如果是私有的“人机回路”工具服务，那么只需要通过修改Description后发布既可以完美解决上述冲突；大部分场景下——无论是公共的“人机回路”工具服务还是私有的服务——都或多或少带有一些“复用”的使命在身。另外，从迭代效率和部署成本考虑，也极少选择专门用于某一个Agent的独立部署MCP。  

[Link️](https://cubox.pro/web/annotations/cards/7398058308050881507?highlight=7398059751206031305)  


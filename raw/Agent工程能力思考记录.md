---
id: "7334547807375720989"
cubox_url: https://cubox.pro/web/card/7334547807375720989
url: https://mp.weixin.qq.com/s?__biz=MzAxNDEwNjk5OQ==&mid=2650540423&idx=1&sn=abe0ca23e1f40fa95408ac62449ba310
tags:
  - AI-Agent/coding
---
# Agent工程能力思考记录

本文探讨了在大模型（LLM）时代下，如何重新定义业务核心资产以及Agent的演进与协作机制。

[Read in Cubox](https://cubox.pro/web/card/7334547807375720989)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzAxNDEwNjk5OQ==&mid=2650540423&idx=1&sn=abe0ca23e1f40fa95408ac62449ba310)  

---


---

## 📖 正文全文

# Agent工程能力思考记录

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzAxNDEwNjk5OQ==&mid=2650540423&idx=1&sn=abe0ca23e1f40fa95408ac62449ba310)营销交易技术团队 大淘宝技术


![](https://image.cubox.pro/cardImg/6cj4sddjgejgwsve4c1dkjyxe75em4ihvkhw4t430gp7i7nl39?imageMogr2/quality/90/ignore-error/1)


本文探讨了在大模型（LLM）时代下，如何重新定义业务核心资产以及Agent的演进与协作机制。文章从技术分层、Agent定义、协作模式、任务分配、冲突解决到工具调用标准（如MCP协议）等多个维度展开分析，并结合工程实践视角，提出了对Agent平台能力建设的思考，旨在为构建高效、灵活、可扩展的Agent系统提供参考。


![](https://image.cubox.pro/cardImg/uvu68x9xpv5b7niv7qaj2fah9d2m13ce1t3f01iyqgqmjopfv?imageMogr2/quality/90/format/gif/ignore-error/1)

业务核心资产定义

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F33P2FdAnju95BibBb7OEibjtejJtUoda5Yh0exUFA4hV46pnPEXhX3mV00ia8ibLbD5kwG3pTrmK2oYGia2nOAgChmg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

上面这张图是LLM时代技术分层 与 Java时代技术分层的一个简单映射，用来标识领域层和基础设施层的设计范围。

大模型时代的核心业务资产应该是Agent的抽象、Tool的抽象，业务Prompt的设计，业务数据的供给，微调后的模型，完整评测集。

定义核心业务资产的目的是，让业务产品的建设和接入更多围绕这部分进行，Agent平台提供相配套的服务能力，与之对应的是Agent注册与构建能力、Tool接入能力、prompt调试能力、模型微调能力和测评能力；当然这里每一个点都是一个庞大的命题，可以做得很深入。

```
      
       ![](https://image.cubox.pro/cardImg/1yy2tqxnc9xp6dby7k6lypn831zbhsjnmib5bys3vxua994rbr?imageMogr2/quality/90/format/gif/ignore-error/1)
      Agent定义
```


我在之前的文章里面画过下面这张图：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F33P2FdAnju95BibBb7OEibjtejJtUoda5YHlZZLsYDPzCVibp6Ech76icGy8Pf4ZtkYV9oM7AnKIWg4EYuxeYAUrzg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

当时我认为从任务规划的视角出发，Agent的定义是随着大模型的发展而变化的；从人类编排任务流程到人类描述详细任务细节到人类发出简单指令，AI在其中扮演的规划、执行角色从少到多，Agent也在不同阶段有不同的定义。

但是上述不同阶段会长久地并存，就像Python的出世，并不会影响到C/C++/Java的消亡，因为物理世界是复杂的，大家可以在不同领域发光发热；所以本文中对Agent的定义是一个能够完成一定范围内人类任务的系统，在这个范围内，万物皆Agent，即使某个领域系统中并没有AI的参与，它在这个广义的定义下，也能作为Agent参与互联。

![](https://image.cubox.pro/cardImg/73wase4r58d8rw0j4hi3759nlx1x7cknh9665x41h9fc51msz?imageMogr2/quality/90/format/gif/ignore-error/1)

Agent协作机制

过去的互联网架构经历了从单体服务 到 微服务/ServerLess的演化：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F33P2FdAnju95BibBb7OEibjtejJtUoda5Y396ib8uFvHLfV3YNySK9VNUAxQVuPRBB9184BMwq5FV1jia7CJ6LPNDg%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

------图摘自《从单体架构到微服务的演进之路》

这本质上是对业务系统高内聚低耦合的实践；譬如一次优惠的创建，在营销、库存、限购、商品等多个领域，都有或多或少的参与；单领域的业务知识膨胀，行业的诉求迭代，都会推动我们做系统和服务的拆分。

在Agent系统的发展上，应该也会有类似的演进路径，从最开始一个Agent做大做强，到领域知识逐渐厚重，催生出更多Agent来帮助共同实现某个任务：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F33P2FdAnju95BibBb7OEibjtejJtUoda5YviaZs1SKBx5b6uNho4PjibrO72vZFXiaQ8KEI9HEGvINtFiaMcdqfPZnvA%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

过去在微服务的实践上，我们在统一的一套系统框架（HSF）下进行交互，领域的互联以服务接口交互的方式进行，因此在AI时代，未来的系统交付物可能不再是现在的某个服务，而是某个Agent；它与接口最大的差别在于不是一轮input-output，而可能是多轮的，因此协议上的设计需要考虑多轮input-output完成某项任务；而像服务注册与发现等这类能力，依然有较高的参考性：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F33P2FdAnju95BibBb7OEibjtejJtUoda5Y3BP9WMddjaaljco0DG9Y8LNYRsvFQR572wYOElUzpF2duX8v2oBdQA%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

------图转自《服务架构的演进：从单体到微服务的探索之旅》

即然单体Agent到多Agent协作是必然的客观演进规律，那么就有必要看一下多Agent协作模式：

|----------------------------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| 任务分配机制                                                               | 协作方式                                                                                 | 冲突解决                                                                 |
| * 集中式任务分配 <!-- --> * 分布式任务协商 <!-- --> * 基于角色的任务划分 <!-- --> * 动态任务重分配 | * 平行协作：多Agent并行解决问题 <!-- --> * 层级协作：管理Agent统筹下级Agent <!-- --> * 专家协作：不同领域Agent联合解决问题 | * 基于优先级的决策 <!-- --> * 投票机制 <!-- --> * 仲裁Agent介入 <!-- --> * 基于规则的冲突处理 |
| * 集中式任务分配 <!-- --> * 分布式任务协商 <!-- --> * 基于角色的任务划分 <!-- --> * 动态任务重分配 | * 平行协作：多Agent并行解决问题 <!-- --> * 层级协作：管理Agent统筹下级Agent <!-- --> * 专家协作：不同领域Agent联合解决问题 | * 基于优先级的决策 <!-- --> * 投票机制 <!-- --> * 仲裁Agent介入 <!-- --> * 基于规则的冲突处理 |
| * 集中式任务分配 <!-- --> * 分布式任务协商 <!-- --> * 基于角色的任务划分 <!-- --> * 动态任务重分配 | * 平行协作：多Agent并行解决问题 <!-- --> * 层级协作：管理Agent统筹下级Agent <!-- --> * 专家协作：不同领域Agent联合解决问题 | * 基于优先级的决策 <!-- --> * 投票机制 <!-- --> * 仲裁Agent介入 <!-- --> * 基于规则的冲突处理 |
| * 集中式任务分配 <!-- --> * 分布式任务协商 <!-- --> * 基于角色的任务划分 <!-- --> * 动态任务重分配 | * 平行协作：多Agent并行解决问题 <!-- --> * 层级协作：管理Agent统筹下级Agent <!-- --> * 专家协作：不同领域Agent联合解决问题 | * 基于优先级的决策 <!-- --> * 投票机制 <!-- --> * 仲裁Agent介入 <!-- --> * 基于规则的冲突处理 |

可以看到当前市面上关于多Agent协作的讨论，核心是围绕着任务的解决展开的：任务分发、任务处理、任务结果回收；这也是A2A协议引入任务这个概念的原因。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F33P2FdAnju95BibBb7OEibjtejJtUoda5YysXNFXeB0SXBdnYevqAvLqw2hibNz09xE6JGz3Gr4SfL2r9t7Zg33jA%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

上图是我对多Agent协作模块理解的一个简图，从业务主Agent出发，需要基于任务中心恢复当前任务上下文，继续本次任务的处理；接着通过Agent仓库找到需要协同的Agent；我们通过多Agent交互协议与其他协作Agent交互，并在主Agent业务流程中完成结果决策或子Agent的状态透传。

这套模型也呼应了前面说的，Agent可以是任意一个能够完成一定范围内人类任务的系统，只要它能在我们的业务流程中参与协同并解决一类问题：是 "一行Hello World代码" 到 "复杂交互系统" 中的任意一个坐标点。同样的，基于万物皆Agent的思路，MCP工具服务也可以抽象成一个Agent，并且可以在这一层做一些额外的比如鉴权/参数校验等的事情。

![](https://image.cubox.pro/cardImg/2x9bdcqofisbed60dd1qzgs1s8hfd87cv4sn75zmvisfkx8is3?imageMogr2/quality/90/format/gif/ignore-error/1)

MCP协议的优与劣

我们在业务核心资产定义中，除了Agent的抽象，还有Tool的抽象；这也是现在大家讨论得最多的，通过工具扩展大模型的边界，尤其当下MCP已经成为既定的行业标准，这个讨论很有价值。

这样一个行业标准出来后的好处是大家不用再为自己的工具或工具平台编写调试提示词，模型厂商在工具结构标准化的前提下也能够做一些特定的优化，提升工具调用的准确性。

但MCP协议当前整体偏薄，在集团视角需要工程侧做一些能力上的丰富；另外不仅是MCP的服务能力供给，上一章讲到的Agent能力供给，也同样需要下述的工程补充：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F33P2FdAnju95BibBb7OEibjtejJtUoda5YvKx8PsCicmGKiaaLfjMuVob92yNZldKiaouR3troicDHMqcxD0AbsrhRyQ%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

* 公网/内网级的权限控制

前面我们讲到，单体服务向微服务转变后，会抽象出许多只在集团内部供给能力的领域，因此工具/Agent需要在公网和内网的维度进行隔离；现在的MCP服务是基于公网的协议，这意味着内网的MCP服务需要有统一的网关层收口，基于请求类型给出相应的工具集。

* 用户态的权限控制

当前MCP协议并没有用户态信息，这会导致有些只对指定用户开放使用的工具无法做用户级的鉴权，所以在用户态信息层面，需要对MCP进行补充，对于集团来说，用户态信息应该可以是多类型的，譬如淘宝用户、飞猪用户、集团员工等。有了这层信息后，业务工具可以在自己的服务内部进行鉴权行为；但不同于传统应用，面向大模型的服务最好在工具供给这一层就做好权限控制，用户没有权限的工具直接对大模型不可见，以防陷入请求后却无法获取数据的错误。

* 工具快速接入能力

从零开发一个MCP Server，现在对于业务团队来说是有一定工作量的，HSF支持0代码一键转MCP Server，这就是一种工具快速接入的能力；除了HSF，其实还有很多业务团队常用的接入诉求，比如SLS日志查询的接入，ODPS表读取的接入，IDEAs服务的接入等，这些能力可以快速支撑起一个简单的应用场景，譬如我之前文章里面的FlowLink原子能力接入后台、多啦a梦平台，本质上都是做的工具接入提效；对于集团的MCP中心，如果能够支持收敛这种工具接入，是可以提高业务应用建设效率的。

* 长工具列表优化

随着业务系统的复杂性提升，一个Agent系统依赖的工具可能会有显著的膨胀；对于业务侧来说，需要让工具更加内聚，简单；对于MCP中心来说，也可以通过一些更通用的工程化手段来处理，比如在服务发现的末端，基于用户的请求前置过滤一些与本次无关的工具，可以是通过向量相似性或是LLM来处理，这种二阶段工具匹配的做法不仅可以减少长任务下的上下文长度，还能提高工具匹配的准确性。

![](https://image.cubox.pro/cardImg/22tu7ur91ctyu7ycofq4kqc1gxj0zhufnc731ltrvayoywmkdp?imageMogr2/quality/90/format/gif/ignore-error/1)

Agent框架配套

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F33P2FdAnju95BibBb7OEibjtejJtUoda5YSpVxZkiasAria9PhUSlxwuqpoCSOOjnYfprEDFRdpBSgeeRshJ8DtMhA%2F640%3Fwx_fmt%3Dother%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

------图摘自《《PUA指南》Agent开发框架：OpenAI Agents \& Google ADK》

上面这张图对于Agent框架的分层总结得很好，可以看到除了前面的Agent协作构建模式和既定的工具调用标准MCP，常见的Agent还需要引入问题理解、关键记忆召回、知识库增强、评测等能力：

如上图，由此衍生出的Agent平台模块，还有知识库的管理与干预、模型市场中心、记忆管理、链路追踪、评测管理与微调能力；这里每一个点都是一个可以深入的垂直领域，这里不再过细展开。

写在最后

Manus的出现以及类Manus产品的层出不穷，都标志着AI已经进入了一个新的阶段，在这个节点如何将已有业务深入融入到Agent体系中，值得每一个人思考。


参考文献

*
  《从单体架构到微服务的演进之路》：https://baijiahao.baidu.com/s?id=1827853965130757323\&wfr=spider\&for=pc
* 《服务架构的演进：从单体到微服务的探索之旅》：https://developer.aliyun.com/article/1638314


**¤****拓展阅读****¤**

[3DXR技术](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxNDEwNjk5OQ==&action=getalbum&album_id=2565944923443904512#wechat_redirect) \| [终端技术](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxNDEwNjk5OQ==&action=getalbum&album_id=1533906991218294785#wechat_redirect) \| [音视频技术](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxNDEwNjk5OQ==&action=getalbum&album_id=1592015847500414978#wechat_redirect)

[服务端技术](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxNDEwNjk5OQ==&action=getalbum&album_id=1539610690070642689#wechat_redirect) \| [技术质量](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxNDEwNjk5OQ==&action=getalbum&album_id=2565883875634397185#wechat_redirect) \| [数据算法](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxNDEwNjk5OQ==&action=getalbum&album_id=1522425612282494977#wechat_redirect)

[Read in Cubox](https://cubox.pro/web/card/7334547807375720989)

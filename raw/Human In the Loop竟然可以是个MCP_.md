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


---

## 📖 正文全文

# Human In the Loop竟然可以是个MCP?

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/V5cb4HAufxvbNackr8aLVg)阿里巴巴智能引擎 阿里云开发者


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FZ6bicxIx5naLnL1xVFZ2yiba3wcYXgibx5WMcWCdwGrsm6F3Gh6CGVZcmB67UrzcAM6Kj3YGFSYN6knwjwibbGF4rA%2F640%3Fwx_fmt%3Djpeg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0&valid=false)


阿里妹导读


本文基于我们的实践，阐述了如何使用统一的工程方案在阿里的大模型研发平台（OpenLM）上，以及其他Agent平台上针对"Human In The Loop"场景进行大模型产品设计和研发工作。


作者：彭世昕、亚男、闫科忠


一、背景


**1.1 什么是Human In The Loop？**


Human In The Loop又称为人机回路，是人类监督、参与Agent活动的一种交互方式。在常规场景下，人类参与的Agent活动只有输入和中断。"输入"可以是人类向Agent下发任务、提供上下文信息的动作；而"中断"则是在人类暂停Agent活动的一个行为。在"中断"动作后，人类也可以选择让Agent"继续"活动，或者提供更多信息让Agent取消之前的动作，进行新的活动；也可以什么都不做，完全停止Agent的活动。

还有另一种场景就是人类在Agent的活动过程中为其答疑解惑，或者授权批准其下一步的动作。当Agent对"输入"部分的上下文有歧义或者模糊感时，Agent可以通过向人类提交"疑问"并寻求"答复"来明确一些根据"输入"产生的上下文的不清晰之处。这实际上可以算作对于"输入"的进一步补充；而在Agent需要做出一些动作，如操作文件系统，或者访问某些文档时，也可以通过"获取授权"的行为征得人类同意，继续完成后续的动作。

下面以阿里内部大模型研发平台OpenLM为例，展示了用户如何在"AI搜索助手"Agent上使用天气问询触发人机回路：

您的浏览器不支持 video 标签


**1.2 在客户端/服务端模式下的困难**


Cline、Cursor、Claude Code以及iFlow CLI\[3\]等工具能够率先以终端产品的方式呈现Human In The Loop的原因，主要是其LLM虽然使用外部的MaaS服务，但是Agent却是在使用者的PC上执行。Agent在需要解惑的时候调用UI，无论是桌面UI还是移动UI，其实现架构都相对容易，也无需特别的设计。然而，在"Agent的执行环境不在使用者PC（或其他端侧设备）而是在远端（服务端）"的场景下，如果没有特殊的工程设计，那么面对并发、分布式及多端等组合拳的围攻下，Human In The Loop的使用体验将会大打折扣。

MCP（Model Context Protocol）Server在设计之初引入的stdio Transport之所以能够被广泛采纳，也是因为其对应的"单进程单客"模式实现起来十分简单，不需要考虑复杂的服务端模型。然而在将其以微服务方式部署之后，即使引入了支持远端访问的HTTP+SSE Transport，依旧无法解决很多微服务工程问题。直到出现了Streamable Transport才让微服务部署MCP Server的问题得到了一定的缓解，但是仍然挑战重重。

当前多数Agent框架基于React框架开发，缺乏类似LangGraph的HITL（Human-in-the-Loop，下同）节点能力\[1\]。另外，流式场景常用的SSE（Server-Sent Events）响应机制返回的结果若要适配HITL模式，需要引入图状态的持久化存储与恢复机制。下面是一段HITL存储与恢复的FastAPI示例：

    from fastapi import FastAPIfrom chatagent import graph_with_menufrom langgraph.types import Commandfrom fastapi.middleware.cors import CORSMiddleware
    app = FastAPI()app.add_middleware(    CORSMiddleware,    allow_origins=["*"],    allow_credentials=True,    allow_methods=["*"],    allow_headers=["*"],)@app.get("/")def read_root():    return {"message": "Welcome to your FastAPI backend!"}
    @app.get("/chat_initiate")def read_item(thread_id: str, response: str = None):    thread_config = {"configurable": {"thread_id": thread_id}}        state = graph_with_menu.invoke(        {"messages": [],         "order": [],         "finished": False},         config=thread_config)
        return {        "AIMessage": state["messages"][-1].content,        "state": state,        "thread_id": thread_id    }
    @app.get("/chat-continue")def continue_chat(thread_id: str, response: str):    thread_config = {"configurable": {"thread_id": thread_id}}    state = graph_with_menu.invoke(        Command(resume = response),         config=thread_config)
        return {        "AIMessage": state["messages"][-1].content,        "state": state,        "thread_id": thread_id    }


这不仅涉及API架构的重构，还需支持多阶段执行流程。并且在分布式计算场景下，图状态的跨节点同步与恢复会显著增加系统复杂度，Agent框架需要进行深度改造，其技术成本和开发难度较高。考虑到目前大多数Agent框架都比较好的支持了MCP协议，使用MCP实现"人机回路"这个想法就自然浮现了出来。

二、解决方案


**2.1 用MCP实现人类"确认"能力**


Agent对于MCP Tool的调用tool/call行为可以类比"请求、响应"，也可以类比为人类的"问询、答复"。只不过，这次的问询方是大模型，而回答方是人类。当大模型有问题需要向人类确认时，可以向一个专门的MCP Server的inquiry工具发送tool/call请求；当人类回答后，这个tool/call请求才会将响应反馈给大模型，完成整个问询流程：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4APjMRxT11fs5E6T2SVHxkLia8jFjtW1hG5pHQcEcVxa8xSBMAdsWMAlA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D1&valid=false)

从技术实现上来看，如果借助MCP，那么我们需要提供一个类似名为send_inquiry的MCP工具。这个工具函数接受一个名为prompt的字符串类型参数，给大模型提供一个提出问询的场所。send_inquiry收到请求后就必须将tool/call行为挂起，直到收到人类的答复后才可以结束挂起，并将人类的答复作为函数响应交还给大模型。

那么，在这个循环中，人类如何参与进来呢？

1）UI与接口

在计算机历史上，人类参与互动的途径一直是UI。无论这种UI是命令行、Web页面还是APP，人类都必须通过具象化的界面参与到计算机的计算流程中来。而在互联网借助各种纯文本协议大行其道之时，HTTP协议作为承载主要交互任务的媒介，自然是人类参与的首选。

通过在与上述MCP Server同一个微服务中提供一个HTTP协议接口，我们几乎可以将现阶段互联网上所有的UI打通，形成一个固定的"人类回答"模式。此HTTP接口仅需提供一个名为response字符串类型参数，既可以实现一个承载前述能力的入口。

按照程序员们的传统做法，这里有一个"关联"问题，即在"多客"的微服务模式下，如何将不同Agent的疑问和不同"人类"的回答关联在一起。好在由于数据类型单一，数据模式简单，只需要用ID和哈希表即可完成关联。但是接下来的坏消息是，在Agent发出tool/call和人类响应之间，似乎还缺少一个有效的信道，以便完成ID（凭条）的传递。

Agent在计算机内执行，其计时单位是毫秒，甚至是微秒；而人类的思考过程及作答的计时单位则是秒。在Agent看来，将疑问丢给人类，实际上就是将一个"异步任务"下发给了人类。在执行异步任务的常见模式下，当异步任务下发之后，异步任务的接受方就需要提供一个"任务ID"，以便调用方后续对"任务状态"进行跟踪。从此模式上来看，上述send_inquiry函数在收到tool/call请求后就应该响应一个ID（凭条），以便Agent进行后续的状态跟踪。然而，MCP Tool被设计为"同步调用"模式，即函数的响应必须在同一个tool/call中响应给调用方。为了保证架构的一致性，我们必须保持这种模式不做改变，否则将会失去使用MCP作为Human In The Loop实现方案的意义。那么，有没有其他办法可以在send_inquiry不做出响应的同时让调用方获得ID（凭条）呢？

2）MCP的Notification

在MCP从服务端向客户端发送数据的协议中，除了有展示服务端能力的Capabilites之外，还有一条专门的通知路径：Notification。服务端可以通过Notification将任务的的处理进度、状态实时同步给调用方。我们借助这个能力，即可在Agent调用send_inquiry后通过Notification帧将ID（凭条）发给调用方。而调用方收到此类Notification帧后，就可以通知他的调用方：这里有一条需要人类确认的消息，请帮忙渲染界面并提醒人类进行响应；而直接调用Agent服务接口（ChatCompletions等）的业务服务甚至可以将此帧进行二次封装，同时通知多个调用方，以实现多端协同。

这是一个典型MCP Notification的响应帧内容的例子（截取自MCP的SSE信道）：

    {  "method": "notifications/progress",  "params": {    "meta": {      "question": "明天北京天气如何？",      "inquiryId": "a4cecc76-2fb3-41bc-97ae-e809059ad68a",      "type": "INQUIRY"    },    "progressToken": 1,    "progress": 0,    "method": "notifications/progress"  },  "jsonrpc": "2.0"}


Notification帧中除了ID（凭条）之外，还可以将大模型的疑问（问题）一并囊括。端侧收到这个帧的同时就可以一次性完成UI渲染工作；Agent将此ID（凭条）转送给调用方（业务服务）的途径也只有一条，就是已经建立的Agent服务接口（如ChatCompletions）的SSE帧响应。

这是一个OpenAI ChatCompletions兼容协议的响应SSE帧结构示例，用于将问询的Notification原样转发给Agent调用方：

    {    "id": "chatcmpl-202d02d5-68cd-40d1-bd5f-0dc82751ba89",    "created": 1756272472,    "object": "chat.completion.chunk",    "choices": [        {            "index": 0,            "delta": {                "chatos_additional_data": {                    "mcp_progress_notification_data": "{\"method\":\"notifications/progress\",\"params\":{\"meta\":{\"question\":\"明天北京天气如何？\",\"inquiryId\":\"a4cecc76-2fb3-41bc-97ae-e809059ad68a\",\"type\":\"INQUIRY\"},\"progressToken\":1,\"progress\":0.0,\"total\":null,\"message\":null,\"method\":\"notifications/progress\"},\"jsonrpc\":\"2.0\"}"                }            }        }    ],    "agent_info": {        "name": "Tool Calling Agent",        "run_id": "202d02d5-68cd-40d1-bd5f-0dc82751ba89"    }}


可以看到mcp_progress_notification_data中的结构实际上就是前述的MCP的Notification帧。这就意味着Agent平台可以完全不识别其中的内容，将解析职责完全交由调用方。

完整的（单端）流程如下图：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4A6kcEIYRsFkbHp4ZsftjutdWD4fb573fx2nTPbicTFyt4b4iaUdpvyU5w%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D2&valid=false)

上图用户发送"确认"结果到MCP Server的路径，除了可以是HTTP协议发起的请求外，也可以是直接通过tool/call实现工具调用。


**2.2 代理现有工具以支持"确认"**


当大模型认为回答问题的上下文不足时，可以借助上述方案，以一个专门的"问询"服务的形式让人类进一步提供信息。然而，如果我们需要Agent在做每一步之前都向人类进行"操作确认"，又该如何实现呢？

实际上，参考前面的实现方案，我们可以在每一个MCP Tool调用前都加入一个"确认"流程。而当人类完成确认后，我们要做的不是将人类回答直接反馈给调用方，而是根据人类回答的"是"和"否"来确认这个MCP调用是否要继续进行。

当人类回答"否"时，tool/call直接返回一个TextContent\[4\]，在其中标注"人类拒绝执行"；当人类回答"是"或"继续"时，就可以按照原路径继续完成这个工具原本的执行逻辑，最终返回这个工具的执行结果。

这个流程像极了设计模式中的代理模式：被代理方前面植入了一段"代理逻辑"；当"代理逻辑"认为被代理方可以执行时，调用被代理方的代码；当"代理逻辑"认为被代理方不能执行时，直接"断路"处理。而代理模式的固定流程就给了我们将这个行为模式化的理论支撑。

我们可以提供一个专门用于代理的MCP Server，这个微服务按照如下方式提供服务：

1）透传如tools/list等的全部请求。完整的流程如下图：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4AicbkhevKiaYib1SRa0ymZvlaibpF8gicwhLOnWGabldDjEaj0aGf4ntnUZA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D3&valid=false)

2）代理tool/call请求，并根据需要调用Upstream（后端，被代理方）MCP Server的tool/call。完整的流程如下图：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4ARYS4IIbjOaTIIyJ6EIk1HgHmv2tFIzv2xxhzAQsArYDegPxKFCUmAg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D4&valid=false)

MCP Server方接入MCP Proxy服务后，将代理后的URL交给Agent进行集成。这样既可以实现在现有工具调用前让人类进行确认，又不会对现有的服务、架构进行大幅度调整，一举多得。


**2.3 关于YOLO模式**


YOLO（You Only Look Once）模式是Cursor于2024年末推出的重要功能\[5\]。它允许Agent自动执行每一个原本应该由人类进行确认的操作，如终端命令等。开启此模式的Agent将可以在人类下达命令后，自动完成一系列操作，成为真正的AI助理。

当Agent设计为支持开启YOLO模式后，Agent将面临更多的能力和技术上的挑战。比如：

* 针对大模型提出的疑问，谁来做出决策？

* 如何进行决策？

### 2.3.1 服务端决策

当确定"开启YOLO模式后的决策方是服务端"时，由于"YOLO是否开启"只是一个"开关"，实际上Agent代码在设计、编写时，都已经"连接"了上述HITL MCP Server（即"人机回路"的MCP Server，下同）或者MCP Server Proxy。当"YOLO模式"开启时，Agent只能通过Prompt对大模型进行约束，迫使其绕过HITL MCP Server，不要主动调用；而对于MCP Server Proxy，Agent要么完全无法绕过而被迫执行，要么完全不去执行。无论选用哪种方式，Agent得到的结果都将与原有设计大相径庭。

如果Agent的代码编写较为灵活，那么也可以在"YOLO模式"开启时，去除其与HITL MCP Server的"连接"，减少对Prompt的干预。即使这样，也依旧无法解决MCP Server Proxy代理的工具调用的困境。

### 2.3.2 客户端决策

通常情况下在服务端执行Agent，其客户端一般都设计为"瘦客户端"，即客户端（含桌面端、Web端和App端等）都不具备模型推理和其他计算能力，只是作为"UI渲染器"。那么如果由客户端来代替人类进行决策的话，客户端可选的策略类型就只能是"随机"、"YOLO"或者"请求外援"三种了。

"随机"就意味着"随便替人类选一个"。这样做事实上放弃了决策权，改成了"抛硬币"。"概率"产生的结果很"不智能"。

"YOLO"即主动告知Agent：人类将选择权交给了你，你来决策吧。对于HITL MCP Server而言，虽然这个策略看起来也像是放弃了决策权，但是实际上依旧是服务端决策的一种形式；而对于MCP Server Proxy来说，"YOLO"默认代表"立即执行"。

由客户端主动回复"超时未回答"也是一个类似"YOLO"回答的方案。"超时未回答"设计为人类的第三种选择，即"忽略大模型的疑问"。如果在"YOLO"模式开启时，客户端在收到需要人类确认的请求后不去渲染UI，而是直接回复"超时未回答"，那么Agent也可以据此判定需要他自己决策。

2.3.3 Agent决策方法

事实上，即使不考虑YOLO模式的问题，Agent在收到人类"拒绝回答"或者"超时未回答"时都需要进行一定的决策：接下来怎么办？可以通过在Prompt中加入如下提示词以提醒大模型自主进行决策：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4AVPrF2dv6HHgxbRUaMCGrrnLkYBuK1yCQjKCeLdevicNTOmo5AArX41Q%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D5&valid=false)

而提供另一个Agent专门代替人类决策也是一个比较好的选择。当Agent在收到人类"拒绝回答"或者"超时未回答"的结论时，当前Agent主动将背景、目标等信息连同它的原始问题一起抛给另一个决策使用的Agent，强迫它代替人类进行作答。这样做既可以保持当前Agent架构和Prompt的纯净，又可以让人类回溯、审计"代理"日志，甚至可以逐步形成一个个性化的、专门代表某一个人类个体进行决策的"个人助理"。

从工程架构上来看，当前Agent将决策动作抛给另外一个"决策"Agent的动作，可以由Agent的"执行循环"来触发。当执行循环发现HITL MCP Server的回答不符合预期时，就可以主动请求"决策"Agent，以便获得正式的响应。但是对"执行循环"的入侵将无法避免。

另外，也可以将"决策"Agent暴露为MCP Server的形式，如：Double MCP Server，其Description信息可以描述为"这是对于人类未作答的补充，当人类未作答且信息依旧不充分时，可以交由此工具代为回答"。且需要略微调整Prompt以调教大模型适配这种场景。

最后，"服务端决策"也是可以通过"客户端"来主动触发的，这就是前面提到的客户端主动"请求外援"。当人类"拒绝回答"或"超时未作答"时，客户端可以将全部原本提交给人类的信息一股脑抛给应用提供的"专用代理Agent接口"，并强迫其作答；然后将"答复"通过原链路返回给产生疑问的Agent。对于原Agent而言，它并不知道这个回答实际上是由谁做出的，因此并不需要做适配调整。


**2.4 端侧方案**


### 2.4.1 常规处理

无论是业务侧的Web端、App端还是桌面端，UI渲染的基础都是调用Agent主入口的SSE链路的帧。常见的主入口是OpenAI兼容协议的ChatCompletions，使用HTTP POST方法访问。端侧不断地解析Agent主入口（接口）源源不断的返回的SSE帧，根据帧类型决策立即渲染或者攒批渲染。

当收到代表Agent问询的帧时，端侧根据协议渲染UI，等待人类答复。业务侧服务端需要另外提供一个专门用户答复的API（接口），在接入业务侧的认证、鉴权的同时，对接HITL部分的"答复"接口。端侧在人类作答后调用这个API实现"答复"。

等待人类作答期间，端侧还需要打开计时器，在一定时间内自动触发"超时未作答"机制。而对于网络异常导致的Agent主入口SSE断连，端侧还需要自动关闭已经渲染好的UI界面，以防误作答。

### 2.4.2 多端协同

在使用美国苹果公司的iCloud帐号登录新设备，或者使用新浏览器时，经常会被要求登录人在已经登录这个帐号的机器上确认本次登录的合法性，并获取6位数字；登录人需要在任意设备上确认完成后，将6位数字填入新设备的输入框内，完成新设备的登录授权工作。当"确认合法性"任务下发时，几乎所有的设备都会立即收到这个通知；点击任意设备"确认"后，其他设备的登录通知都会立即消失或者不可用。

在多端场景下，虽然一般只有一个主界面接收到了人类直接下发给Agent的任务，但是其他已登录的"端"是可以通过服务端的"通知"机制同步获取一些服务端下发的消息的。在Agent下发问询帧给主界面（即访问Agent主入口下发任务的端）的同时，服务端也可以通过上述通知机制告知其他端本次问询的详细内容。其他端发放提示通知给人类，人类点击任意端侧后，该端也可以渲染UI，提供答复。

在任意一端完成答复后，无论是正常、拒绝或者是超时，其他端也会收到服务端"撤回"本次问询的通知，以便其他端自动关闭已经渲染好的问询界面。而Agent也会同步下发一个代表已经作答的完成帧，告知主界面关闭问询界面。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4Aaq9YmRqM9vTN8uepT7scZGlTUUMgic9RwtPRqx7qMHWLCMjhdFq6xWA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D6&valid=false)

需要注意的是，除了主界面因保持SSE连接，无论收到的"请求答复"消息还是"ToolCall End"消息，都是通过SSE帧的形式完成的之外，其他端侧都是以各自通知的方式接受到的。其数据结构可以结合自身业务场景、协议栈等条件进行设计。


**2.5 超时配置**


在Agent作为MCP客户端使用MCP Server的过程中，常常需要针对tool/call配置一个工具调用的响应等待时间。一方面是防止过长时间的等待会让Agent使用人（一般是终端用户）放弃对Agent的等待，中止服务；另一方面是加强Agent的鲁棒性，使其可以在服务异常时尽快感知并恢复，避免连锁故障。

OpenLM Agent平台上MCP组件的默认超时时间一般是30秒。这几乎可以满足绝大部分场景下对于工具调用的预期延迟需求。但是这对"人机回路"是不够的。Agent需要针对这种情况，对MCP Client相关对象配置的超时时间适度加长，尽量超过"人机回路"服务自身的超时时间，以便尽可能的等待用户答复；而"超时未作答"行为则由端侧（一般是Agent的调用方）主动发起。最终形成"MCP Client的响应等待时间"大于"人机回路服务超时时间"大于"超时未作答行为超时时间"的这么一整套超时配置。

三、人类的回答


**3.1 直接回答**


人类直接回答看起来是最容易的，实际在工程实现上却是最复杂的。从"问询"数量上来看：如果大模型的疑问只有一个，那么只需要让人类直接书写"答复"即可；如果大模型的疑问不止一个，那么除了要考虑"疑问"的传递方式和UI渲染方式之外，还需要顾虑人类的体验。

### 3.1.1 现实问题

有的人使用Agent是期望其产生不一样的创意，比如生成不一样的图片、视频和文字。这类人通常乐于在大模型实际工作之前将任务尽可能的描述清晰，以防止生成的内容偏差较大，甚至有大方向上的背离；有的人使用Agent则是期望其成为一个全能的"助理"，协助完成一定程度的重复工作。如果一个简单的工作交给Agent之后，它还要问东问西，问这问那，那么人类一定会产生"还不如我自己做"的想法，最终弃用这个助理Agent。

而从"答复"质量上来看，人类"答复"的"充分性"也是一个需要关注的要点。如果Agent询问的问题是

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4A2ca9TDtuFjm46k8KfHnMicgiaF8Tz9MDuTU8JM6scVXiagYgv2nN3pTkA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D7&valid=false)

那么人类可以简单的回答"北京"或者"杭州；如果Agent询问的问题是：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4A8NCc87FHNuffictph6DGOSsXCgUiacMh3BiaU7tluQcXIC9Dw1bvWJQQg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D8&valid=false)

那么人类真的会针对每一个问题细致作答吗？

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4AicMhmd3oicl82xGZR2LUGpiaXzhlOdKv7Oq9niaDy20n7N0Iz90Bva0vLQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D9&valid=false)

### 3.1.2 多轮单问题

"通过多轮次问问题，每次一个问题"的模式从功能上看起来更像是人类和AI下属之间的任务交派过程：人类下发一个任务，AI下属通过多次问简单问题澄清一些不清楚点。然后AI下属开始干活儿，交活儿。其技术实现也较为简单：每次发送一个代表"疑问"的字符串，人类也会回答一个代表"答复"的字符串。字符串可长可短，代表着人类和AI之间的思想沟通。

Agent可以利用大模型的执行循环，在不断确认信息是否足够，或者任务是否已达成的过程中，根据需要草拟一个疑问提交给HITL MCP Server，以期从人类处获取到更进一步的描述。

多轮单问题的好处是显而易见的：Agent可以在多轮中逐步对人类任务的模糊之处进行确认，甚至可以对每一次"答复"中的模糊之处再次进行问询，最终达到一个它满意的状态。而缺点也较为明显：带过6岁大小朋友的人都可以理解一个人在耳边不停地问"为什么""为什么""为什么"时候的心情。轮次的数量是一个较为难以把控的难点。轮次太多容易让人类产生厌烦情绪；而人为限制轮次又可能会僵化设计，在某些场景下出现任务描述不清晰就开始干活儿的窘境。

### 3.1.3 单轮多问题

单轮多问题与多轮单问题相对：AI只提出一次（或者限定极少次数的）疑问，但是会一次性提出多个疑问。使用这种模式工作的Agent需要在Prompt上进行特殊的约束。而多个疑问以结构化数据还是以非结构化数据提交给人类面前的UI进行渲染也是一个工程上的选择难题。

1）结构化数据

使用结构化数据（如：JSON）提交疑问是一个较为常见的工程选择，有利于UI渲染部分的代码开发工作，毕竟这是程序员的日常工作。但是让大模型将疑问产出为一个"既定"的结构化数据而不出错------无论是结构性错误还是Schema的错误------显然对于Prompt工程是一个巨大的挑战。但凡有一个微小的错误都会让UI渲染机制罢工。

一个可行的解决办法是将UI渲染的代码开发工作交付给一个专用Agent来完成。当Agent提交的结构化"疑问"端到UI处之时，端侧的调度逻辑可以调用Agent自动完成UI渲染代码的实时编写工作，编写完成后的代码再通过端侧调度机制在端侧直接执行，完成UI渲染；这个Agent甚至都可以直接生成用户"提交"之后构建最终结构化"答复"的处理代码。这样既可以避免预先定制Schema的难题，又可以减少零星的结构化错误对UI渲染的影响。看起来十分具有可行性。然而，Agent真的能定向生成符合界面风格、符合设计要求、符合功能要求的100%无错误的代码吗？如果可以的话，那么为什么生成前述结构化数据的时候会出问题呢？

2）非结构化数据

使用非结构化数据在技术实现上可以与"多轮单问题"完全一致。此时的疑问可以是一个带有Markdown语法结构的字符串。端侧渲染时可以将其放入一个可修改的富文本编辑器中，让人类直接在每一个问题后面"依次作答"。最后，人类的作答连同原始问题一并以一个带有Markdown语法结构的字符串交还给Agent作为"答复"。

这是充分利用了大模型文本处理能力的"低工程"类方案。使用这种方式的优点即是工程实现简单，各类型端侧的实现逻辑可以高度一致。甚至支持人类"作弊"。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4AJ77EVibibdWamzMgpfiawnpoS6a6kRJSmsCwHg0jcaEMHjB1Go5x5gKug%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D10&valid=false)

### 3.1.4 渲染方式

"依次作答"的渲染可以用在"单轮多问题"的问答结构下。无论使用结构化数据还是非结构化数据传递"疑问"和"答复"，都可以一次性渲染多个问题，让人类依次作答。只是渲染出来的界面可以有不同的策略。

使用Markdown格式渲染，将"疑问"和"答复"放在同一个富文本编辑器内是最简单的方式。人类可以直接在"疑问"后面作答。甚至还可以支持Agent自主生成"答复"供人类修改后直接再提交，帮助人类"作弊"。

而渲染成"一个问题"+"一个单行（或者多行）文本编辑器"的方式仅支持结构化数据。人类会将其看做一次针对大模型提问的"调查问卷"，填写问卷内容后再以结构化数据的方式提交。而调查问卷的形式可以多种多样。

更进一步的调查问卷是让Agent针对"疑问"设计多种"答复"供用户选择。UI渲染大量使用"一个问题"+"若干个复选（或者单选）按钮框"。人类操作起来也较为简单。但是缺点也是比较明显的：如果Agent的候选答案与人类的想法完全不一致，那么人类可能无法做出较为灵活的调整。

总之，与人类UI打交道的渲染工作需要千人千面。即使使用同一个Agent，针对不同类型的用户也需要做出不同的UI渲染尝试，以便摸索出符合使用者习惯的、个性化的界面渲染方式。


**3.2 其他回答**


### 3.2.1 拒绝回答

1）答疑解惑

人类拒绝回答本质上就是一种"答复"。人类也许只是在界面上点击一下，无论点击的是"我不想回答"按钮还是界面上的、代表"取消"的小叉子。Agent是无法理解"不答复"行为的，唯一的解决办法是我们的应用在用户明确表达不做答复时，将特定的一段文字回复给Agent。例如：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4AOOkVjNU8CKOR9dz4jkWlXYcXoiauXP66eibnhy2mS5Bk79HUCPGqn7dw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D11&valid=false)

或者：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4A8X1Wiaszb65dG1qcOJWOrBGj6A1FtnTfALvNAXpSZpfHBaIdo4Xl9sA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D12&valid=false)

对于Agent来说，这个答复依旧不会让模糊的"疑问"更加清晰。对于一些不那么"聪明"的模型，其Agent调用工具的行为甚至会表现出"循环"的特征：反复的针对同一类甚至同一个问题进行询问。这时候就需要对提示词进行一定的针对性调整，使之在收到拒绝回答时能够不再调用HITL MCP Server。

2）工具代理

在大量使用大"语言"模型构建Agent的场景下，MCP Server的tool/call主要响应方式为TextContent。这种类型的响应结果可以直接被Agent嵌入到提示词中，以便在执行循环中参与下一次的大模型调用。而当工具被类似MCP Proxy的代理工具代理时，如果人类选择了拒绝执行，那么其tool/call的响应将会直接被MCP Proxy代理，且类型也固定为TextContent。因此，在"工具代理"场景下的"拒绝答复"也是需要Agent开发者考虑的事情。可参考拒绝答复如：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4AFm8cibN7eZS9GFPC7gpZVZqSfGYMhoUEdTKqfwwWqAe6Cz1bM7aHgVg%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D13&valid=false)

而配套的Agent提示词可以做配套调整：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4AUibIBUnFWH2CthJYXJMgnc7QRQvJ1NBtnFWMlAOA2CvqPagOj0koXBA%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D14&valid=false)

### 3.2.2 超时未作答

无论是从工程上来看，还是从"让Agent作为助理干活儿"的需求上来看，Agent对于人类的询问如果在一段时间之内未得到人类的答复，那么Agent还是需要将任务继续做下去的。不然如何体现出"智能"呢？因此"超时未作答"机制也是需要在工程链路中做出考量的一个环节。

与前述"拒绝回答"一样，在超过一段时间后直接答复"超时未作答"对于Agent来说也是较为模糊的。参考的答复可以是：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FZ6bicxIx5naKahRTlpm3GYyaauSblaX4ATSJVQZwibPDXQnzufPNRYB4onhZKMOOIaGWCVnvia86GmIQiaNFsSgvPQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D15&valid=false)

由于已经针对"拒绝回答"的场景优化过提示词，"超时未作答"场景可以复用这些实现，让Agent更好的在人类未对模糊点进行答复的情况下努力工作。

### 3.2.3 默认作答

无论是"拒绝回答"还是"超时未作答"策略，都是利用一个"兜底"的"答复"来试图搪塞Agent，以便让Agent自主决策，或者自由发挥。而"兜底"的答复一般都是内置在Agent中或者端侧UI代码中的，不一定符合上下文，极易造成场景局限性。如果把自己想象成Agent，那么这种搪塞式的统一作答很像是在和心不在焉的人交流，其答复也可能"驴唇不对马嘴"。

当Agent寻找"人类"补全一些上下文缺失时，可以使用另一个助理Agent针对这些"疑问"直接作答。而原Agent的"疑问"和助理Agent的"答复"都可以一并端给人类。Agent同时提供了"疑问"和"回答"时，人类就可以选择直接提交这个默认作答。这实际上规避了前述"拒绝回答"和"超时未作答"策略下的兜底"答复"的场景局限性。

四、提示词倾向性


**4.1 Agent的Prompt**


在普适化的Prompt作用下，当Agent发现需要澄清问题时，虽然会产生"疑问"，但是它会将疑问直接"打在公屏"上：在输出中阐述这个疑问。即使出现在"深度思考"的正文中，大模型也会试图通过既有知识尝试自主回答这个问题。

通过在提示词中加入一些轻微的引导，就可以将Agent的"疑问"------如"您想查询哪个地方的天气呢"------交给MCP做工具调用。此处给出了OpenLM大模型研发平台"AI搜索助手"中的提示词片段。

首先是流程上的改变，增加"澄清"步骤：

        <instruction>      请严格遵循以下思考和操作步骤：      1.  **意图分析 (Intent Analysis):** 首先，深入分析用户的提问，判断其意图是否清晰、具体。      2.  **澄清意图 (Clarification - If Needed):** 如果符合 `clarify_user_intent` 指令的条件，立即停止并严格按照该指令的行动指南调用 `send_inquiry`。      3.  **信息检索 (Information Retrieval):** 一旦意图明确，判断是否需要外部信息。如果需要，则必须调用搜索工具。      4.  **结果验证 (Verification - If Needed):** 在获取搜索结果后，进行审阅。如果对搜索结果的准确性、完整性或存在矛盾之处有疑问，可以进行**补充搜索**（再次调用搜索工具）来交叉验证或获取更多维度的信息。      5.  **综合回答 (Synthesis & Response):** 结合你的内部知识和经过验证的外部信息，形成一个完整、结构化、准确的答案，并按指定格式输出。    </instruction>


然后是解释clarify_user_intent指令的说明：

      <!--  指令的核心部分，定义了最重要的行为准则。    此处的指令拥有最高优先级，必须严格遵守。  -->  <directive id="clarify_user_intent" importance="critical">    <description>在对用户意图不明确时，必须优先澄清，这是所有后续操作的前提。</description>    <condition>      当你对用户的提问感到困惑、或问题包含歧义以至于无法进行下一步操作时。    </condition>    <action>      1.  你必须（MUST）调用 `send_inquiry` 工具，向用户提出具体、有针对性的问题，以澄清其真实意图。      2.  严禁通过直接生成文本内容（即直接回复）的方式向用户提问以澄清意图。所有澄清问题的行为都必须、且只能通过调用 `send_inquiry` 工具来完成。      3.  在澄清意图之前，严禁进行猜测或执行任何其他工具（如搜索）。    </action>    <example name="correct_behavior">      - 用户提问："帮我查一下最新的'泰坦'。"      - 你的判断：意图困惑（是指电影、游戏还是科技产品？）。      - 正确行动：调用工具 send_inquiry with question 如 ("您好，您提到的'泰坦'具体是指什么呢？是电影、游戏还是某个科技产品？")    </example>    <example name="incorrect_behavior_to_avoid">      - 用户提问："帮我查一下最新的'泰坦'。"      - 你的判断：意图困惑。      - **错误行动：** 直接生成并返回文本内容 "您好，您提到的'泰坦'具体是指什么呢？是电影、游戏还是某个科技产品？"      - **此行为是严格禁止的。**    </example>  </directive>


然而，当过分强调HITL MCP Server中的send_inquiry工具的重要性时, Agent的一切行为都将优先使用HITL问询。这让本该通过"检索数据"来获得进一步信息的动作也变成了"问询人类"。通过在提示词中区分"意图识别"和"补充信息"，我们可以进一步引导大模型做出正确的"Next Move"。

增加的提示词在information_gathering中：

      <directive id="information_gathering" importance="high">    <description>在明确用户意图后，主动通过网络搜索来补充和验证信息，以确保回答的准确性和时效性。</description>    <condition>      当你的内部知识不足以回答问题，或问题涉及需要最新、实时信息（如新闻、股价、事件进展、产品发布）时。    </condition>    <action>      在完全理解用户问题后，你必须（MUST）调用搜索工具（如 `GoogleWebSearch` 等）来获取相关信息。不要仅依赖可能过时的内部知识回答此类问题。    </action>    <example>      - 用户提问："请总结一下上周关于人工智能领域的主要新闻。"      - 你的判断：意图明确，但需要最新的外部信息。      - 你的行动：调用 `GoogleWebSearch(query="上周 人工智能领域 主要新闻 总结")`    </example>  </directive>


**4.2 工具的Description**


在MCP协议\[2\]中，tools/list响应中的description是为了让大模型能够充分理解工具的用途，并在适当的时机选用该工具而存在的。工具的Description会与Agent的Prompt融合到大模型的上下文中，因此重要性等同。

下面是一个典型的tools/list响应，其中包含了一个get_weather工具和对应的description描述：

    {  "jsonrpc": "2.0",  "id": 1,  "result": {    "tools": [      {        "name": "get_weather",        "title": "Weather Information Provider",        "description": "Get current weather information for a location",        "inputSchema": {          "type": "object",          "properties": {            "location": {              "type": "string",              "description": "City name or zip code"            }          },          "required": ["location"]        }      }    ],    "nextCursor": "next-page-cursor"  }}


然而对于使用MCP实现的"人机回路"工具来说，send_inquiry也仅仅是与web_search或者xxx_call地位相等的"另一个工具"罢了。如果需要向Agent强调其具体作用，甚至是其重要性，就需要同样在Description中给出具体的示例。

与此类似的MCP工具Sequential-Thinking的工具描述中就详细阐述了其用途：

    何时使用此工具：1. 将复杂问题分解为步骤2. 留有修改空间的规划与设计3. 可能需要调整方向的分析4. 初始阶段范围不明确的问题5. 需要多步骤解决方案的问题6. 需要在多个步骤中保持上下文的任务7. 需要过滤无关信息的情况8. 需要指导使用哪些工具及顺序时


    核心功能：
    1. 可根据进展调整总思维次数2. 可质疑或修改之前的思维3. 即使看似到达终点，也可添加更多思维4. 可表达不确定性并探索替代方案5. 并非每个思维都需要线性推进，可分支或回溯6. 生成解决方案假设7. 基于思维链步骤验证假设8. 为每一步推荐适当工具9. 提供工具推荐的依据10. 建议工具执行顺序及参数11. 跟踪之前的推荐和剩余步骤


    操作建议：
    1. 从所需思维的初始估算开始，但需准备好调整2. 随时可以质疑或修改之前的思维3. 不要犹豫在看似终点时添加更多思维4. 遇到不确定性时明确表达5. 标记修改之前思维或分支到新路径的思维6. 忽略与当前步骤无关的信息7. 在适当的时候生成解决方案假设8. 基于思维链步骤验证假设9. 考虑可用于当前步骤的可用工具10. 为工具推荐提供清晰依据11. 在适当的时候建议具体工具参数12. 为每一步考虑替代工具13. 通过推荐步骤跟踪进度14. 最终输出一个单一且尽可能正确的答案15. 仅在真正完成且达到满意答案时将 next_thought_needed 设为 false


甚至包括参数说明。

1）"人机回路"工具本身的Description

与Senquential-Thinking工具一样，"人机回路"工具的Description需要事无巨细，且具有极强的普适性描述。这是通用工具的一个无法回避的选择。此类描述虽然可以覆盖大部分场景，但是一旦出现和Agent的主提示词冲突的描述，那么将无法调和：大模型将无法判断哪一个描述更加重要。

如果是私有的"人机回路"工具服务，那么只需要通过修改Description后发布既可以完美解决上述冲突；大部分场景下------无论是公共的"人机回路"工具服务还是私有的服务------都或多或少带有一些"复用"的使命在身。另外，从迭代效率和部署成本考虑，也极少选择专门用于某一个Agent的独立部署MCP。

在QueryString的魔盒被MCP开发者打开之后，各类型的、基于QueryString参数设计的动态参数逐步取代了以环境变量为媒介的启动参数。以环境变量为媒介的启动参数仅可以在MCP Server启动时配置；如果需要修改配置，那么只能重启服务。以环境变量为媒介的启动参数较为适合本机部署或者沙箱部署的MCP Server，它们按需启动，不再使用时即可停止。

而基于QueryString的参数可以实现更细粒度的动态参数，参数使用范围从"部署级"缩小到"会话级"，以此实现的多租户共享MCP Server的机制已经广泛的使用在OpenLM MCP市场上公开的各类型一方、三方工具上。

"人机回路"工具也可以使用QueryString参数，通过动态传入的description值来干预tools/list调用的响应结果，以此实现按需、动态调整工具Description的目的。优点是几乎不需要对客户端进行任何调整，且随时可以进行Description干预和调优工作。缺点在于干预粒度。

在MCP协议中，除了工具的Description之外，任意工具中的任意参数都可以配置Description，用于告知大模型"如何填写该参数"。如果在MCP Server设计之初无法考虑到使用者的全部干预场景，那么提供出来的干预手段也只可能遇到"不上不下"的尴尬匹配处境。

2）客户端覆盖Description

另外一个实现动态干预的方式则是由客户端提供工具Description的覆盖机制。当Agent的MCP客户端访问"人机回路"工具的tools/list获取到响应结果后，由Agent根据需要完成任意工具Schema部分的替换工作，然后将替换结果结合提示词一起交给大模型。

这种方式的优点是可以根据需要完全自主的控制MCP Server响应的任意一处细致的配置。个性化程度极高（几乎拉满）。当然缺点也同样在此：这样细致的定制几乎就是一个定制化的客户端适配工作，当MCP Server出现较大调整时，客户端处的实现也需要随之调整。这似乎违背了MCP协议存在的初衷。


**4.3 Agent也是"人"**


在与Agent的沟通中，或者直接与大模型的对话中，Agent并不清楚自己是什么。这听起来很科幻，但是大模型会将自己视为一个和人一样的个体。这也就意味着在设计、描述各类型提示词的过程中，需要把Agent当做另一个面对面的"人类"来沟通、交流。在提示词，甚至是问题中，尽量淡化、避免使用"人"、"工具"、"LLM"（或者"大模型"）这类术语，防止Agent产生理解偏差。

团队介绍：

我们是阿里巴巴智能引擎团队，是阿里集团内AI工程系统的建设者与维护者，主导设计了大数据AI工程体系AI·OS。团队聚焦于大模型全链路工程能力建设，持续优化研发范式，专注大模型训推性能优化、引擎平台、Agent应用平台等关键组件，为阿里集团各业务提供高效稳定的AI工程基础设施。


## 附录参考

\[1\] https://blog.langchain.ac.cn/human-in-the-loop-with-opengpts-and-langgraph/

\[2\] https://modelcontextprotocol.io/specification/2025-06-18/server/tools#listing-tools

\[3\] https://platform.iflow.cn/cli/quickstart

\[4\] https://modelcontextprotocol.io/specification/2025-06-18/server/tools#text-content

\[5\] https://cursor.com/changelog/0-44-x


**主动式智能导购 AI 助手构建**


为助力商家全天候自动化满足顾客的购物需求，可通过百炼构建一个 Multi-Agent 架构的大模型应用实现智能导购助手。该系统能够主动询问顾客所需商品的具体参数，一旦收集齐备，便会自动从商品数据库中检索匹配的商品，并精准推荐给顾客。

点击阅读原文查看详情。


[Read in Cubox](https://cubox.pro/web/card/7398058308050881507)

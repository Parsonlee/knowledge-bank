# 基于 MCP 的 AI Agent 应用开发实践

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247514365&idx=1&sn=dd898cc5dfe8ab4fe7c48442a2d7fc35&subscene=0)金鑫 字节跳动技术团队


最近大家都在聊 MCP，发现有个最重要的点被忽略了： 通过标准化协议，将工具提供方与应用研发者解耦，这一点带来的将是 AI Agent 应用研发范式的转移（类似 Web 应用研发的前后端分离）。

本文以开发 Agent TARS（https://agent-tars.com/） 应用为例，尽可能详细地介绍 MCP 在开发范式、工具生态扩展上起到的作用。

名词解释

AI Agent：在 LLM 语境下，AI Agent 是某种能自主理解意图、规划决策、执行复杂任务的智能体。Agent 并非 ChatGPT 升级版，它不仅告诉你"如何做"，更会帮你去做。如果 Copilot 是副驾驶，那么 Agent 就是主驾驶。类似人类"做事情"的过程，Agent 的核心功能，可以归纳为三个步骤的循环：感知（Perception）、规划（Planning）和行动（Action）。

Copilot：Copilot 是指一种基于人工智能的辅助工具，通常与特定的软件或应用程序集成，旨在帮助用户提高工作效率。Copilot 系统通过分析用户的行为、输入、数据和历史记录，提供实时建议、自动化任务或增强功能，帮助用户做出决策或简化操作。

MCP：Model Context Protocol（模型上下文协议）是一个开放协议，它规范了应用程序如何为 LLMs 提供上下文。可以将 MCP 想象为 AI 应用的 USB-C 端口。就像 USB-C 提供了一种标准方式，让你的设备连接到各种外设和配件，MCP 也提供了一种标准方式，让你的 AI 模型连接到不同的数据源和工具。

Agent TARS：一个开源的多模态人工智能代理，提供与各种真实世界工具的无缝集成。

RESTful API：RESTful 是一种软件架构风格、设计风格，而不是标准，只是提供了一组设计原则和约束条件。它主要用于客户端和服务器交互类的软件。

背景

AI 从最初只能对话的 Chatbot，辅助人类决策的 Copilot，再到能自主感知和行动的 Agent，AI 在任务中的参与度不断提升。这要求 AI 拥有更丰富的任务上下文 （Context），并拥有执行行动所需的工具集 （Tools）。

痛点

缺少标准化的上下文和工具集导致开发者的三大痛点：

1.
   开发耦合度高：工具开发者需要深入了解 Agent 的内部实现细节，并在 Agent 层编写工具代码。这导致在工具的开发与调试困难。
2.
   工具复用性差：因每个工具实现都耦合在 Agent 应用代码内，即使是通过 API 实现适配层在给到 LLM 的出入参上也有区别。从编程语言角度来讲，没办法做到跨编程语言进行复用。
3.
   生态碎片化：工具提供方能提供的只有 OpenAPI，由于缺乏标准使得不同 Agent 生态中的工具 Tool 互不兼容。


![](https://image.cubox.pro/cardImg/3phc9zoce2ygsbm4z0961kjlwc1kink0fqx505fv83cvzwrjpq?imageMogr2/quality/90/format/gif/ignore-error/1)

目标

"All problems in computer science can be solved by another level of indirection" -- Butler Lampson  
在计算机科学中，任何问题都可以通过一个抽象层解决。

将工具从 Agent 层解耦出来，单独变成一层 MCP Server 层，并对开发、调用进行标准化。MCP Server 为上层 Agent 提供上下文、工具的标准化调用方式。

![](https://image.cubox.pro/cardImg/81mdxy75cj0pdxdi9o9awir4liui7ic1yxsg9xwz6ms8411tn?imageMogr2/quality/90/format/gif/ignore-error/1)

演示

从几个例子中看 MCP 在 AI Agent 应用中发挥的作用。

例 1 (不构成投资建议，使用的是券商模拟账户下单)

*
  指令：从技术面分析下股票，然后以市价买入 3 股股票
*
  回放：  


*
  使用的 MCP Servers:
  *
    券商 MCP：https://github.com/longportapp/openapi/tree/main/mcp
  *
    文件系统 MCP：https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem

例 2

*
  指令：我的机器中的 CPU、内存和网络速度分别是多少？
*
  回放：  


*
  使用的 MCP Servers：
  *
    命令行 MCP：https://github.com/g0t4/mcp-server-commands
  *
    代码执行 MCP：https://github.com/formulahendry/mcp-server-code-runner

例 3

*
  指令：在 ProductHunt 上找到点赞数最高的前 5 款产品
*
  回放：  


*
  使用的 MCP Servers：
  *
    浏览器操作 MCP：https://github.com/bytedance/UI-TARS-desktop/tree/fb2932afbdd54da757b9fae61e888fc8804e648f/packages/agent-infra/mcp-servers/browser

例 4

*
  指令：根据[这篇文章](https://mp.weixin.qq.com/s?__biz=MzAxNDEwNjk5OQ==&mid=2650533088&idx=1&sn=74b233244fb1a692fd6397d2312553d4&scene=21#wechat_redirect)，调研下各个 Agent 框架的各维度对比，并生成一个报告 markdown
*
  回放：  

*
  使用的 MCP Servers：Link Reader

已支持自定义 MCP Servers !415（https://github.com/bytedance/UI-TARS-desktop/pull/415） !489（https://github.com/bytedance/UI-TARS-desktop/pull/489），可以添加 Stdio、Streamable HTTP、SSE 类型的 MCP Server。

更多：https://agent-tars.com/showcase

介绍

什么是 MCP？

Model Context Protocol（模型上下文协议）是 Anthropic 在推出的用于 LLM 应用和外部数据源（Resources）或工具（Tools）通信的标准协议，遵循 JSON-RPC 2.0 的基础消息格式。

可以把 MCP 想象成 AI 应用程序的 USB-C 接口，规范了应用程序如何为 LLMs 提供上下文。

架构图如下：

*
  MCP Client：通过 MCP 协议与 Servers 通信，并保持 1:1 连接。
*
  MCP Servers：上下文提供方，暴露外部数据源（Resources）、工具（Tools）、提示词（Prompts）等由 Client 进行调用。
*
  语言支持层面：TypeScript 和 Python、Java、Kotlin、C#。

流程图

一句话解释就是 MCP 提供给 LLM 所需的上下文：Resources 资源、Prompts 提示词、Tools 工具。

MCP 和 Function Call 区别？

|--------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
|        | MCP                                                                                                                       | Function Call                                                               |
| 定义     | 模型和其他设备集成的标准接口，包含： * 工具 Tools：模型可调用的函数防范，与外部系统进行交互，并执行计算 * 资源 Resources：提供给模型的数据、文档、配置、截图等 * 提示词 Prompt：支持用户自定义工具的 Prompt | 将模型连接到外部数据和系统，平铺式的罗列 Tools 工具。 和 MCP Tools 的不同在于：MCP Tools 的函数约定了输入输出的协议规范。 |
| 协议     | JSON-RPC，支持双向通信（但目前使用不多）、可发现性、更新通知能力                                                                                      | JSON-Schema，静态函数调用                                                          |
| 调用方式   | Stdio/SSE/Str/eamable HTTP/同进程调用（见下文）                                                                                     | 同进程调用/编程语言对应的函数                                                             |
| 适用场景   | 更适合动态、复杂的交互场景                                                                                                             | 单一特定工具、静态函数执行调用                                                             |
| 系统集成难度 | 高                                                                                                                         | 简单                                                                          |
| 工程化程度  | 高                                                                                                                         | 低                                                                           |


从前后端分离看 MCP

早期 Web 开发在 JSP、PHP 盛行时，前端交互页面都是耦合在后端逻辑里的，造成开发复杂度高、代码维护困难、前后端协作不便，难以适应现代 Web 应用对用户体验和性能的更高要求。

AJAX、Node.js、RESTful API 推动前后端分离，对应 MCP 也正在实现 AI 开发的"工具分层"：

*
  前后端分离：前端专注界面，后端专注 API 接口；
*
  MCP 分层：让工具开发者和 Agent 开发者各司其职，工具质量和功能的迭代不需要 Agent 开发者感知。这种分层让 AI Agent 开发者能像搭积木一样组合工具，快速构建复杂 AI 应用。


实践

整体设计

以 MCP Browser 浏览器工具（https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-servers/browser）开发和接入为例，逐步解析具体实现。

在设计 Browser MCP Server 时，并没有采用官方的 stdio call 方式（即通过 npx 方式跨进程调用）。原因是为了降低使用门槛，避免用户在首次使用时先安装 Npm、Node.js 或 UV，从而影响 Agent 开箱即用的体验（相关 issue#64：https://github.com/modelcontextprotocol/servers/issues/64）。

因此，Agent 工具的设计分为两类：

*
  内置 MCP Servers：完全遵循 MCP 规范，同时支持 Stdio 和函数调用。（换句话说用 MCP 标准开发 Function Call）
*
  用户自定义 MCP Servers：针对需要扩展功能的用户，默认他们已经具备 Npm 或 UV 环境，因此可以支持更灵活的扩展方式。

两者的区别：

*
  内置 MCP Servers 是完成当前 Agent 功能的必备工具
*
  调用方式：内置方式不需要 Agent 用户安装 Node.js / npm，这对于普通用户比较友好。

MCP Server 开发

以 mcp-server-browser 为例，其实就是一个 npm 包，package.json 配置如下：

    {
      "name": "mcp-server-browser",
    "version": "0.0.1",
    "type": "module",
    "bin": {
        "mcp-server-browser": "dist/index.cjs"
      },
    "main": "dist/server.cjs",
    "module": "dist/server.js",
    "types": "dist/server.d.ts",
    "files": [
        "dist"
      ],
    "scripts": {
        "build": "rm -rf dist && rslib build && shx chmod +x dist/*.{js,cjs}",
        "dev": "npx -y @modelcontextprotocol/inspector tsx src/index.ts"
      }
    }

*
  bin 指定通过 stdio 调用的入口文件。
*
  main、module 执行通过 Function Call 同进程调用的入口文件。

开发（dev）
实践下来，通过 Inspector（https://modelcontextprotocol.io/docs/tools/inspector） 来开发调试 MCP Server 是比较好，Agent 与工具解耦，可以单独调试和开发工具。

直接运行 npm run dev 启动一个 Playground，里面包含 MCP Server 可调试的功能（Prompts、Resources、Tools 等）。

    $ npx -y @modelcontextprotocol/inspector tsx src/index.ts
    Starting MCP inspector...
    New SSE connection

    Spawned stdio transport
    Connected MCP client to backing server transport
    Created web app transport
    Set up MCP proxy

    🔍 MCP Inspector is up and running at http://localhost:5173 🚀

注：用 Inspector 调试开发 Server 时，console.log 是无法显示的，这点 debug 确实有点麻烦。

实现（Implement）

启动入口（Entry）

为了内置 MCP Server 可以当Function call 同进程调用，这里在入口文件 src/server.ts 中导出三个共用方法：

*
  listTools：列举所有函数
*
  callTool：调用具体函数
*
  close：Server 不使用后的清理函数

    // src/server.ts
    export const client: Pick<Client, 'callTool' | 'listTools' | 'close'> = {
      callTool,
      listTools,
      close,
    };

同时 Stdio 调用支持，直接在 src/index.ts 导入模块即可使用。

    #!/usr/bin/env node
    // src/index.ts
    import { client as mcpBrowserClient } from "./server.js";

    const server = new Server(
      {
        name: "example-servers/puppeteer",
        version: "0.1.0",
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );
    // listTools
    server.setRequestHandler(ListToolsRequestSchema, mcpBrowserClient.listTools);
    // callTool
    server.setRequestHandler(CallToolRequestSchema, async (request) =>
    return await mcpBrowserClient.callTool(request.params);
    );

    async functionrunServer() {
      const transport = new StdioServerTransport();
      await server.connect(transport);
    }

    runServer().catch(console.error);

    process.stdin.on("close", () => {
      console.error("Browser MCP Server closed");
      server.close();
    });

工具定义（Definition）

MCP 协议要求用 JSON Schema 约束工具的入参、出参，这里实践下来：推荐用 zod (https://github.com/colinhacks/zod) 来定义一套 Zod Schema，导出到 MCP 时再将 zod 转成 JSON Schema。

    import { z } from 'zod';

    const toolsMap = {
      browser_navigate: {
        description: 'Navigate to a URL',
        inputSchema: z.object({
          url: z.string(),
        }),
        handle: async (args) => {
          // Implements
          const clickableElements = ['...']
          return {
            content: [
              {
                type: 'text',
                text: `Navigated to ${args.url}\nclickable elements: ${clickableElements}`,
              },
            ],
            isError: false,
          }
        }
      },
      browser_scroll: {
        name: 'browser_scroll',
        description: 'Scroll the page',
        inputSchema: z.object({
          amount: z
            .number()
            .describe('Pixels to scroll (positive for down, negative for up)'),
        }),
        handle: async (args) => {
          return {
            content: [
              {
                type: 'text',
                text: `Scrolled ${actualScroll} pixels. ${
                  isAtBottom
                    ? 'Reached the bottom of the page.'
                    : 'Did not reach the bottom of the page.'
                }`,
              },
            ],
            isError: false,
          };
        }
      },
      // more
    };

    const callTool = async ({ name, arguments: toolArgs }) => {
    return handlers[name].handle(toolArgs);
    }

技巧 Tips:

与 OpenAPI 返回结构化数据不同，MCP 的返回值专为 LLM 模型设计。为了更好地连接模型与工具，返回的文本和工具的描述 description 应更具语义化，从而提升模型的理解能力，提高工具调用的成功率。

例如，browser_scroll（浏览器滚动）在每次执行工具后，应返回页面的滚动状态（如距底部剩余像素、是否已到底等）。这样模型在下次调用工具时即可精准提供合适的参数。

Agent 集成

开发完 MCP Server 后，需要在 Agent 应用中进行集成。原则上，Agent 无需关注 MCP Servers 提供的工具、入参和出参的具体细节。

MCP Servers 配置

在 MCP Servers 配置中分为「内置 Server」和「用户扩展 Server」，内置 Server 通过同进程 Function Call 调用，保证 Agent 应用对小白用户开箱即用，扩展 Server 则提供给高级用户扩展 Agent 上限功能。

    {
        // Internal MCP Servers(in-process call)
        fileSystem: {
          name: 'fileSystem',
          localClient: mcpFsClient,
        },
        commands: {
          name: 'commands',
          localClient: mcpCommandClient,
        },
        browser: {
          name: 'browser',
          localClient: mcpBrowserClient,
        },

        // External MCP Servers(remote call)
        fetch: {
          command: 'uvx',
          args: ['mcp-server-fetch'],
        },
        longbridge: {
          command: 'longport-mcp',
          args: [],
          env: {}
        }
    }

MCP Client

MCP Client 的核心任务是集成不同调用方式（Stdio / SSE / Streamable HTTP / Function Call）的 MCP Server。Stdio 和 SSE 方式直接复用了官方示例(https://modelcontextprotocol.io/quickstart/client)，这里主要介绍下我们对 Function Call 调用是怎样在 Client 中支持的。

Function Call 调用

    exporttype MCPServer<ServerNames extends string = string> = {
      name: ServerNames;
      status: 'activate' | 'error';
      description?: string;
      env?: Record<string, string>;
    + /** in-process call, same as function call */
    + localClient?: Pick<Client, 'callTool' | 'listTools' | 'close'>;
      /** Stdio server */
      command?: string;
      args?: string[];
    };

MCP Client 调用方式如下：

    import { MCPClient } from '@agent-infra/mcp-client';
    import { client as mcpBrowserClient } from '@agent-infra/mcp-server-browser';

     const client = new MCPClient([
        {
          name: 'browser',
          description: 'web browser tools',
          localClient: mcpBrowserClient,
        }
    ]);

    const mcpTools = await client.listTools();

    const response = await openai.chat.completions.create({
      model,
      messages,
      // Different model vendors need to convert to the corresponding tools data format.
      tools: convertToTools(tools),
      tool_choice: 'auto',
    });

至此，MCP 的整体流程已全部实现，涵盖了从 Server 配置、Client 集成到与 Agent 的衔接等各个环节。更多 MCP 细节/代码已开源到 Github：

*
  Agent 集成：https://github.com/bytedance/UI-TARS-desktop/blob/fb2932afbdd54da757b9fae61e888fc8804e648f/apps/agent-tars/src/main/llmProvider/index.ts#L89-L91
*
  mcp-client：https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-client
*
  mcp-servers：https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-servers

Remote 远程调用

如果是 Web 应用（无法使用 Stdio MCP Server），可以用 FaaS 将 Stdio 转成 SSE MCP Server，从而在 Function Call 的基础上无缝支持 MCP 类型的 Tools，这个过程换句话讲是「MCP Servers 云化」。

调用代码示例：

    import asyncio
    import openai
    import json
    from agents.mcp import MCPUtil
    from agents.mcp import MCPServerSse

    from agents import set_tracing_disabled

    set_tracing_disabled(True)

    async def chat():
        client = openai.AzureOpenAI(
            azure_endpoint=base_url,
            api_version=api_version,
            api_key=ak,
        )

    +   async with MCPServerSse(
    +       name="fetch", params={"url": "https://{mcp_faas_id}.mcp.bytedance.net/sse"}
    +   ) as mcp_server:
    +       tools = await MCPUtil.get_function_tools(
    +           mcp_server, convert_schemas_to_strict=False
    +       )
            prompt = "请求下 https://agent-tars.com/，主要是做什么的？"
            completion = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
    +           tools=[
    +               {
    +                   "type": "function",
    +                   "function": {
    +                       "name": tool.name,
    +                       "description": tool.description,
    +                       "parameters": tool.params_json_schema,
    +                   },
    +               }
    +               for tool in tools
    +           ],
            )

            for choice in completion.choices:
                if isinstance(choice.message.tool_calls, list):
                    for tool_call in choice.message.tool_calls:
                        if tool_call.function:
    +                       tool_result = await mcp_server.call_tool(
    +                           tool_name=tool_call.function.name,
    +                           arguments=json.loads(
    +                               tool_call.function.arguments
    +                           ), # or jsonrepair
    +                       )
    +                       print("tool_result", tool_result.content)

    if __name__ == '__main__':
        asyncio.run(chat())


思考

生态

MCP 生态不断发展壮大，越来越多的应用支持 MCP，同时开放平台也提供 MCP Server。同时也有像 Cloudflare、Composio、Zapier 使用 SSE 方式将 MCP 进行托管（即接入一个 MCP Endpoint 即接入一批 MCP Servers），通过 Stdio 方式最理想场景是 MCP Servers 和 Agent 系统跑在同一 Docker 容器中（类似 Sidecar 模式）。

MCP 生态图

举个例子：接入地图厂商的 MCP Server 后，Agent 具备生活服务工具能力，远远优于单纯依赖搜索的方式。

未来

*
  目前的 MCP 开发非常初级，在工程化上缺少一套完善的框架来约束和规范。
*
  根据 MCP Roadmap（https://modelcontextprotocol.io/development/roadmap），未来主要三件事：
  *
    Remote MCP Support：鉴权、服务发现、无状态服务，很明显奔着 K8S 架构去的，这样才能构建一个生产级、可扩展的 MCP 服务。根据最近的 RFC Replace HTTP+SSE with new "Streamable HTTP" transport（https://github.com/modelcontextprotocol/modelcontextprotocol/pull/206），支持 Streamable HTTP，可以低延迟、双向传输。
  *
    Agent Support：提升不同领域复杂的 Agent 工作流，并可以处理更好的人机交互。
  *
    Developer Ecosystem：更多的开发者和大厂商参与进来，才能扩展 AI Agent 的能力边界。
*
  实践下来，MCP Server SSE 并不是理想的方案，因为需要保持连接和 session 状态，而云服务（如 FaaS）更倾向于无状态架构（issue#273：https://github.com/modelcontextprotocol/typescript-sdk/issues/273#issuecomment-2789489317），所以最近提出了更适配云场景的 Streamable HTTP Transport。
*
  MCP 模型调用与 RL 强化学习：如果 MCP 成为未来的规范，那么 Agent 应用能否准确调用各个 MCP，将成为模型 RL 未来需要支持的关键功能。与 Function Call 模型不同，MCP 是一个动态的工具库，模型需要具备对新增 MCP 的泛化理解能力。
*
  Agent K8s：虽然目前 LLM 和上下文之间建立了标准化的通信协议，但 Agent 之间的交互协议尚未形成统一标准，Agent 服务发现、恢复、监控等一系列生产级问题等解决。目前 Google 的 A2A（Agent2Agent） 和社区的 ANP（Agent Network Protocol）在做这方面的探索与尝试。

参考：

*
  [详解 MCP：Agentic AI 中间层最优解，AI 应用的标准化革命](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247511799&idx=1&sn=c063b0da3fcbfd309d1d6294f58bbc72&poc_token=HDHfCWijwO4rRDuRm27MHkcjkCAt8UEi2ypH3vS_&scene=21#wechat_redirect)
*
  [a16z详解MCP，以及AI工具的未来](https://mp.weixin.qq.com/s?__biz=MzkxOTU4NzEyOQ==&mid=2247511596&idx=1&sn=19987907b0e8d2db56916fcf8bceeb61&scene=21#wechat_redirect)
*
  How to Build an MCP Server Fast: A Step-by-Step Tutorial：https://medium.com/@eugenesh4work/how-to-build-an-mcp-server-fast-a-step-by-step-tutorial-e09faa5f7e3b
*
  智能体互联网的三大趋势：连接范式正在彻底重构：https://zhuanlan.zhihu.com/p/31870979392
*
  有了 MCP，AI 才完整：https://www.youtube.com/watch?v=ElX5HO0wXyo
*
  硅谷 101：AI Agent爆发前的黎明：Manus 不够好，但天快亮了：https://www.youtube.com/watch?v=2PSCnOFkR3U
*
  MCP 终极指南：https://guangzhengli.com/blog/zh/model-context-protocol
*
  OpenAI 支持 MCP：https://x.com/sama/status/1904957253456941061

[Read in Cubox](https://cubox.pro/web/card/7321436519405718623)

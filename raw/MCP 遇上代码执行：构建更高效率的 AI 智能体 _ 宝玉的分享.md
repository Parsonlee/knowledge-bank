---
id: "7387384365380010539"
cubox_url: https://cubox.pro/web/card/7387384365380010539
url: https://baoyu.io/blog/code-execution-with-mcp
tags:
  - AI-Agent/tools
---
# MCP 遇上代码执行：构建更高效率的 AI 智能体 | 宝玉的分享

简述：以CodeAgent的方式，通过代码来调用tool (MCP tools)

[Read in Cubox](https://cubox.pro/web/card/7387384365380010539)  
[Read Original](https://baoyu.io/blog/code-execution-with-mcp)  

---


---

## 📖 正文全文

# MCP 遇上代码执行：构建更高效率的 AI 智能体

[baoyu.io](https://baoyu.io/blog/code-execution-with-mcp)

[模型上下文协议 (Model Context Protocol, 简称 MCP)](https://modelcontextprotocol.io/) 是一种开放标准，用于将 `AI 智能体 (AI Agent)` 连接到外部系统。在过去，将智能体连接到工具和数据，每一种"配对"都需要定制开发，这导致了严重的碎片化和重复劳动，让真正互联的系统难以规模化。MCP 提供了一种通用协议------开发者只需在他们的智能体中实现一次 MCP，就能解锁一整个集成生态系统。

自 2024 年 11 月推出以来，MCP 的普及速度非常快：社区已经建立了数千个 [MCP 服务器](https://github.com/modelcontextprotocol/servers)，[SDK](https://modelcontextprotocol.io/docs/sdk) 已覆盖所有主流编程语言，业界也已将 MCP 采纳为连接智能体与工具和数据的"事实标准"。

如今，开发者们日常构建的 AI 智能体，动辄就能访问分布在几十个 MCP 服务器上的成百上千个工具。然而，随着连接工具的数量激增，**"在智能体运行之初就加载所有工具的定义"** 以及 **"让所有中间结果都通过上下文窗口"** （**这里的上下文窗口，你可以理解为 AI 用来"思考"和"记忆"的临时白板，它的容量是有限的**）的做法，正严重拖慢智能体的速度并增加成本。

在这篇博客中，我们将探讨"代码执行"如何帮助 AI 智能体更高效地与 MCP 服务器互动，实现在使用更少"**Token** "（**AI 处理信息的基本单位**）的同时，轻松驾驭海量工具。

## 工具带来的过度 **Token**消耗，正让 AI 智能体效率低下

随着 MCP 用量猛增，有两种常见模式会显著增加智能体的成本和延迟：

1. 工具定义撑爆了上下文窗口；

2. 任务的中间结果额外消耗了大量 **Token**。

### 1. 工具定义撑爆了上下文窗口

大多数 MCP 客户端会一股脑地把所有工具的定义，在任务开始前就直接加载到上下文中，通过"直接工具调用"的语法暴露给模型。这些工具定义大概长这个样子：

    gdrive.getDocument
         Description: Retrieves a document from Google Drive
         Parameters:
                    documentId (required, string): The ID of the document to retrieve
                    fields (optional, string): Specific fields to return
         Returns: Document object with title, body content, metadata, permissions, etc.

    salesforce.updateRecord
        Description: Updates a record in Salesforce
        Parameters:
                   objectType (required, string): Type of Salesforce object (Lead, Contact,      Account, etc.)
                   recordId (required, string): The ID of the record to update
                   data (required, object): Fields to update with their new values
         Returns: Updated record object with confirmation

这些工具描述占用了宝贵的上下文窗口空间，增加了响应时间和成本。想象一下，当一个智能体连接了数千个工具时，它可能在"读到用户的请求之前"，就必须先处理掉几十万 **Token**的工具定义。

### 2. 任务的中间结果额外消耗了大量 **Token**

大多数 MCP 客户端允许模型（**即 AI 智能体背后的"大脑"，通常是某个大语言模型**）直接调用 MCP 工具。例如，你给智能体下达一个指令："从我的 Google Drive 下载会议纪要，并把它附加到 Salesforce 的潜在客户记录里。"

模型会像下面这样执行调用：

    TOOL CALL: gdrive.getDocument(documentId: "abc123")
            → returns "Discussed Q4 goals...\n[full transcript text]"
               (loaded into model context)

    TOOL CALL: salesforce.updateRecord(
    			objectType: "SalesMeeting",
    			recordId: "00Q5f000001abcXYZ",
      			data: { "Notes": "Discussed Q4 goals...\n[full transcript text written out]" }
    		)
    		(model needs to write entire transcript into context again)
        (模型需要把完整的会议纪要内容在上下文中*又写了一遍*)

每一个中间结果都必须"过一遍"模型。在这个例子里，完整的会议纪要内容被"来来回回"处理了两次。如果这是一场 2 小时的销售会议，可能就意味着额外处理了 50,000 个 **Token**。如果文档再大一点，甚至可能直接撑爆上下文窗口的限制，导致整个工作流崩溃。

在处理大型文档或复杂数据结构时，模型在工具调用之间"复制粘贴"数据时，也更容易出错。

![](https://image.cubox.pro/cardImg/19ou9pag3ynfnd7ln81slxiossr7jxdb1pjl8xeyroazsneq3d.webp?imageMogr2/quality/90/format/gif/ignore-error/1)

MCP 客户端将工具定义加载到模型的上下文窗口中，并协调一个消息循环，在这个循环里，每一次工具调用和返回的结果都必须在操作之间"过一遍"模型。

## MCP 遇上代码执行：上下文效率的救星

随着代码执行环境在 AI 智能体中变得越来越普遍，一个解决方案浮出水面：**不要把 MCP 服务器当作"直接工具"来调用，而是把它们当作"代码 API"来看待。** 这样，AI 智能体就可以通过*写代码*来与 MCP 服务器互动。这种方法完美解决了前面提到的两个挑战：智能体可以只加载它真正需要的工具，并且可以在执行环境中处理完数据后，再把"净结果"返回给模型。

实现的方式有很多种。一种方法是，根据所有连接的 MCP 服务器，生成一个包含所有可用工具的"文件树"。下面是一个用 TypeScript 实现的例子：

    servers
    ├── google-drive
    │   ├── getDocument.ts
    │   ├── ... (其他工具)
    │   └── index.ts
    ├── salesforce
    │   ├── updateRecord.ts
    │   ├── ... (其他工具)
    │   └── index.ts
    └── ... (其他服务器)

然后，每个工具都对应一个文件，大概是这样：

    // ./servers/google-drive/getDocument.ts
    import { callMCPTool } from "../../../client.js";

    interface GetDocumentInput {
      documentId: string;
    }

    interface GetDocumentResponse {
      content: string;
    }

    /\* 从 Google Drive 读取一个文档 \*/
    export async function getDocument(input: GetDocumentInput): Promise\<GetDocumentResponse\> {
      return callMCPTool\<GetDocumentResponse\>('google\_drive\_\_get\_document', input);
    }

这样一来，我们前面那个"Google Drive 到 Salesforce"的例子，就变成了下面这段代码：

    // 从 Google Docs 读取纪要并添加到 Salesforce 潜在客户记录
    import * as gdrive from './servers/google-drive';
    import * as salesforce from './servers/salesforce';

    const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
    await salesforce.updateRecord({
      objectType: 'SalesMeeting',
      recordId: '00Q5f000001abcXYZ',
      data: { Notes: transcript }
    });

智能体通过"探索文件系统"来发现工具：比如列出 `./servers/` 目录找到可用的服务器（像 `google-drive` 和 `salesforce`），然后读取它需要的特定工具文件（像 `getDocument.ts` 和 `updateRecord.ts`）来理解每个工具的接口。这使得智能体可以只为当前任务加载它需要的定义。**这一改变，将 Token 使用量从 150,000 锐减到 2,000 ------ 节省了 98.7% 的时间和成本。**

Cloudflare 也[发布了类似的发现](https://blog.cloudflare.com/code-mode/)，他们称这种将 MCP 与代码执行相结合的方式为"代码模式 (Code Mode)"。大家的核心洞见是相同的：`大语言模型 (LLM)` 非常擅长写代码，开发者应该充分利用这一优势，来构建能更高效地与 MCP 服务器互动的 AI 智能体。

## "MCP + 代码执行"的几大好处

MCP 结合代码执行，能让智能体"按需加载工具"、"在数据抵达模型前就地筛选"，以及"一步执行复杂逻辑"，从而更高效地利用上下文。此外，这种方法在安全性和状态管理方面也有额外的好处。

模型非常擅长浏览文件系统。将工具以代码文件的形式呈现在文件系统中，允许模型"按需读取"工具定义，而不是在一开始就"全量阅读"。

另一种方法是，在服务器上添加一个 `search_tools`（搜索工具）的工具。例如，在使用我们前面假设的 Salesforce 服务器时，智能体可以先搜索"salesforce"，然后只加载它当前任务真正需要的那些工具。在 `search_tools` 工具里再加一个"详细程度"参数，让智能体可以选择需要的信息级别（比如：仅名称、名称+描述、或包含模式的完整定义），这也能帮助智能体节省上下文并高效地找到工具。

### 更节省上下文的工具结果

在处理大型数据集时，智能体可以在返回结果*之前*，先在代码中对结果进行过滤和转换。想象一下获取一个有 10,000 行数据的电子表格：

    // 没有代码执行时 - 所有行都涌入上下文
    // TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
    //    → 在上下文中返回 10,000 行数据，等待模型手动筛选

    // 有了代码执行 - 在执行环境中就地筛选
    const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
    const pendingOrders = allRows.filter(row =>
      row["Status"] === 'pending'
    );
    console.log(`找到了 ${pendingOrders.length} 个待处理订单`);
    console.log(pendingOrders.slice(0, 5)); // 只打印前 5 个供模型审阅

最终，智能体（模型）只看到了 5 行数据，而不是 10,000 行。类似的模式也适用于数据聚合、跨多个数据源的连接，或者提取特定字段------所有这些操作都不会撑爆上下文窗口。

循环、条件判断和错误处理，现在都可以用我们熟悉的编程模式来完成，而不是靠一长串独立的工具调用链。例如，如果你需要一个 Slack 部署通知，智能体可以这样写：

    let found = false;
    while (!found) {
      const messages = await slack.getChannelHistory({ channel: 'C123456' });
      found = messages.some(m => m.text.includes('deployment complete'));
      if (!found) await new Promise(r => setTimeout(r, 5000));
    }
    console.log('已收到部署通知');

这种方法比在智能体循环中反复交替调用"MCP 工具"和"睡眠命令"要高效得多。

此外，能够写出一个完整的条件树（**比如 if-else 逻辑** ）并让它一次性执行，也节省了"首个 **Token** 响应时间"（**Time to first token, 指 AI 开始生成回复的速度** ）的延迟：智能体不必等待模型慢吞吞地评估一个 `if` 语句，而是直接让代码执行环境搞定这一切。

### 保护隐私的操作

当 AI 智能体使用代码执行时，默认情况下，所有的中间结果都只停留在"执行环境"中。这样一来，智能体（模型）只能看到你明确*打印* 或*返回*给它的东西。这意味着，你不想与模型分享的数据，可以在你的工作流中顺畅流转，而根本无需进入模型的上下文。

对于更敏感的工作负载，智能体的"马甲"（**Agent Harness，指控制智能体的外层程序** ）可以自动对敏感数据进行"**Token** 化"处理（**即数据脱敏或打码**）。例如，假设你需要将电子表格中的客户联系方式导入 Salesforce。智能体写了如下代码：

    const sheet = await gdrive.getSheet({ sheetId: 'abc123' });
    for (const row of sheet.rows) {
      await salesforce.updateRecord({
        objectType: 'Lead',
        recordId: row.salesforceId,
        data: {
          Email: row.email,
          Phone: row.phone,
          Name: row.name
        }
      });
    }
    console.log(`已更新 ${sheet.rows.length} 条潜在客户信息`);

MCP 客户端会在数据到达模型*之前* 拦截这些数据，并对 PII（**Personally Identifiable Information，个人身份信息**）进行脱敏处理：

    // 如果智能体打印了 sheet.rows，它会看到这样的内容：
    [
      { salesforceId: '00Q...', email: '[EMAIL_1]', phone: '[PHONE_1]', name: '[NAME_1]' },
      { salesforceId: '00Q...', email: '[EMAIL_2]', phone: '[PHONE_2]', name: '[NAME_2]' },
      ...
    ]

然后，当这些数据在另一次 MCP 工具调用中被使用时，MCP 客户端会通过查找表将其"反脱敏"。真实的电子邮件、电话号码和姓名，从 Google Sheets 流向了 Salesforce，但*全程没有经过模型本身*。这就防止了智能体（模型）意外记录或处理敏感数据。你还可以用这种方式来定义确定性的安全规则，精确控制数据的流向。

### 状态持久化与"技能"沉淀

能够访问文件系统的代码执行能力，允许智能体跨多个操作"保持状态"。智能体可以将中间结果写入文件，这使得它们能够"断点续作"并跟踪进度：

    const leads = await salesforce.query({
      query: 'SELECT Id, Email FROM Lead LIMIT 1000'
    });
    const csvData = leads.map(l => `${l.Id},${l.Email}`).join('\\n');
    await fs.writeFile('./workspace/leads.csv', csvData);

    // 之后的执行可以从它上次中断的地方继续
    const saved = await fs.readFile('./workspace/leads.csv', 'utf-8');

智能体还可以将*自己的代码*沉淀为可复用的函数。一旦智能体为某个任务开发出一段可用的代码，它就可以将这个实现保存下来以备将来使用：

    // 保存在 ./skills/save-sheet-as-csv.ts
    import * as gdrive from './servers/google-drive';
    export async function saveSheetAsCsv(sheetId: string) {
      const data = await gdrive.getSheet({ sheetId });
      const csv = data.map(row => row.join(',')).join('\\n');
      await fs.writeFile(`./workspace/sheet-${sheetId}.csv`, csv);
      return `./workspace/sheet-${sheetId}.csv`;
    }

    // 之后，在任何一次智能体执行中：
    import { saveSheetAsCsv } from './skills/save-sheet-as-csv';
    const csvPath = await saveSheetAsCsv('abc123');

这与 [Skills（技能）](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) 的概念紧密相关------这些"技能"是包含可复用指令、脚本和资源的文件夹，模型可以利用它们来提高在特定任务上的表现。为这些保存的函数添加一个 `SKILL.md`（技能描述文件），就创造了一个模型可以引用和使用的结构化技能。随着时间的推移，这能让你的 AI 智能体建立起一个"高级能力工具箱"，不断进化出它高效工作所需的"脚手架"。

请注意，代码执行也引入了它自己的复杂性。运行 AI 智能体生成的代码，需要一个安全的执行环境，配备适当的[沙盒 (sandboxing)](https://www.anthropic.com/engineering/claude-code-sandboxing)（**一种安全隔离机制，防止恶意代码破坏系统** ）、资源限制和监控。这些基础设施需求增加了额外的运营开销和安全考量，而"直接工具调用"则没有这些烦恼。因此，我们必须权衡代码执行带来的好处（减少 **Token**成本、降低延迟、改进工具组合）与这些实现成本。

## 总结

MCP 为 AI 智能体连接海量工具和系统提供了基础协议。然而，一旦连接的服务器过多，工具定义和中间结果就会消耗过多的 **Token**，导致智能体效率下降。

尽管这里提到的许多问题感觉很新奇------比如上下文管理、工具组合、状态持久化------但它们在传统的软件工程领域早已有成熟的解决方案。"代码执行"就是将这些行之有效的模式应用到 AI 智能体上，让它们使用熟悉的编程结构，来更高效地与 MCP 服务器互动。如果你也实现了这种方法，我们鼓励你与 [MCP 社区](https://modelcontextprotocol.io/community/communication) 分享你的发现。

### 致谢

*本文由 Adam Jones 和 Conor Kelly 撰写。感谢 Jeremy Fox、Jerome Swannack、Stuart Ritchie、Molly Vorwerck、Matt Samuels 和 Maggie Vo 对本文草稿提供的反馈。*

*** ** * ** ***

来源： <https://www.anthropic.com/engineering/code-execution-with-mcp>

[Read in Cubox](https://cubox.pro/web/card/7387384365380010539)

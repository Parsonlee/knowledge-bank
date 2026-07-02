---
id: "7393599330126398303"
cubox_url: https://cubox.pro/web/card/7393599330126398303
url: https://mp.weixin.qq.com/s/tmXg0tguoZZplDZMaJWlJQ
tags:
  - AI-Agent/coding
---
# Anthropic再发Agent神文：像人类工程师一样思考，解决「长程任务」难题



[Read in Cubox](https://cubox.pro/web/card/7393599330126398303)  
[Read Original](https://mp.weixin.qq.com/s/tmXg0tguoZZplDZMaJWlJQ)  

---

## Annotations  

> 1. 功能列表（Feature List）
> 为了防止Agent一次性蛮干或过早结束，初始化Agent被要求编写一个包含所有功能需求的详细文件。在claude.ai克隆案例中，这包含超过200个功能点。
>
> 这些功能最初都被标记为“failing”（未通过），为后续Agent提供了清晰的工作全景图
>
> JSON文件示例：
>
> {
>     "category": "functional",
>     "description": "New chat button creates a fresh conversation",
>     "steps": [
>       "Navigate to main interface",
>       "Click the 'New Chat' button",
>       "Verify a new conversation is created",
>       "Check that chat area shows welcome state",
>       "Verify conversation appears in sidebar"
>     ],
>     "passes": false
> }
> 实验发现，使用JSON格式优于Markdown，因为模型不太容易错误地更改或覆盖JSON文件。同时，提示词需包含强硬指令，禁止删除或编辑测试，只允许更改passes字段的状态  

[Link️](https://cubox.pro/web/annotations/cards/7393599330126398303?highlight=7393599330327725540)


---

## 📖 正文全文

# Anthropic再发Agent神文：像人类工程师一样思考，解决「长程任务」难题

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/tmXg0tguoZZplDZMaJWlJQ)AI寒武纪


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FICgnAptln0WQWA5T8kibQvGCozW3fB1Ya2qIf8GjES0DyQiaqicFXHY4I4UQ6hIroxT0YGTiawCoZL4mWwNQfA6ufw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0&valid=false)


↑阅读之前记得关注+星标⭐️，😄，每天才能第一时间接收到更新

Anthropic再发Agent工程实践神文：Effective harnesses for long-running agents（适用于长期运行Agents的有效工具），强烈建议大家围观阅读

之前我介绍过Anthropic Agent文章合集这里：

[Agent下半场！比Prompt更重要的是「上下文工程」，Anthropic首次系统阐述](https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA==&mid=2247508202&idx=1&sn=3d589ef9b4cfe42520e9fe67812bc615&scene=21#wechat_redirect)

[万物皆可Agent！Anthropic官方"三步循环法"手把手教你造最强智能体](https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA==&mid=2247508397&idx=1&sn=e4a41eafa3799d060cb01ae19b5b021f&scene=21#wechat_redirect)

[Anthropic又出王炸！一个文件夹，把Claude"调教"成真正可以干活的Agent](https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA==&mid=2247508677&idx=1&sn=c90297804afd4aa3b576748cce036d52&scene=21#wechat_redirect)

[Anthropic又一篇Agent开发神文，新范式让Token消耗暴降98.7%](https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA==&mid=2247509344&idx=1&sn=94d00c1ab9f2d0e9c910d60deb7ee6cd&scene=21#wechat_redirect)

随着AI Agent能力的提升，开发者开始要求它们承担跨越数小时甚至数天的复杂任务。然而，如何让Agent在多个上下文窗口之间保持一致的进度，仍然是一个未解难题

长程Agent面临的核心挑战在于，它们必须分"会话"（Session）工作，而每个新会话开始时都像是一个没有过往记忆的新工程师接班。由于上下文窗口有限，且复杂项目无法在单一窗口内完成，Agent需要一种机制来弥合编码会话之间的鸿沟

Anthropic工程团队通过观察人类工程师的工作方式，为Claude Agent SDK开发了一套包含两个部分的解决方案：**初始化Agent（Initializer Agent）**和** 编码Agent（Coding Agent）**

### 核心挑战：上下文压缩还不够

Claude Agent SDK是一个通用的Agent框架，具备上下文管理功能（如压缩），理论上应能让Agent无限期工作

但在实际测试中（例如要求最新的Opus 4.5构建一个claude.ai的克隆版），仅靠上下文压缩是不够的。Claude主要表现出两种失败模式：

1.试图一次性完成所有工作：Agent倾向于在一次会话中做太多事，导致中途耗尽上下文，留下的功能只完成了一半且缺乏文档。下一个会话的Agent必须猜测之前发生了什么，浪费大量时间修复基础应用

2.过早宣布完工： 在项目后期，新的Agent实例看到已经有一些功能，就误以为整个工作已完成

### 解决方案：双Agent架构

Anthropic将问题分解，提出了双重解决方案：

**初始化Agent：** 第一个会话使用专用提示词，负责搭建环境。包括生成init.sh脚本、记录进度的claude-progress.txt文件，以及展示文件添加情况的初始Git提交

**编码Agent：** 后续的每一个会话都致力于取得增量进展，并留下结构化的更新

这一方案的关键在于让Agent在开启新窗口时能迅速理解工作状态------这主要通过claude-progress.txt文件和Git历史记录来实现

### 环境管理的三大支柱

为了支持这种工作流，环境设置包含以下关键组件：

#### 1. 功能列表（Feature List）

为了防止Agent一次性蛮干或过早结束，初始化Agent被要求编写一个包含所有功能需求的详细文件。在claude.ai克隆案例中，这包含超过200个功能点。

这些功能最初都被标记为"failing"（未通过），为后续Agent提供了清晰的工作全景图

**JSON文件示例：**

    {
        "category": "functional",
        "description": "New chat button creates a fresh conversation",
        "steps": [
          "Navigate to main interface",
          "Click the 'New Chat' button",
          "Verify a new conversation is created",
          "Check that chat area shows welcome state",
          "Verify conversation appears in sidebar"
        ],
        "passes": false
    }

实验发现，使用JSON格式优于Markdown，因为模型不太容易错误地更改或覆盖JSON文件。同时，提示词需包含强硬指令，禁止删除或编辑测试，只允许更改passes字段的状态

#### 2. 增量进展（Incremental Progress）

有了初始脚手架后，编码Agent被要求一次只做一个功能

为了保持环境整洁，Agent需要在每次代码变更后：

通过Git提交代码，并附带描述性信息；

在进度文件中撰写摘要

这使得模型可以利用Git回滚错误代码，恢复到工作状态，避免了后续Agent需要猜测前任做了什么的情况。

#### 3. 端到端测试

Claude的另一个主要失败模式是：在没有适当测试的情况下标记功能为完成。它往往只做单元测试或简单的curl命令，却忽略了端到端的验证。

解决方案是明确提示Claude使用浏览器自动化工具（如Puppeteer MCP server），像人类用户一样进行测试。通过让Claude看到屏幕截图，它能识别并修复代码中不明显的Bug

### 快速上手流程（Getting up to speed）

基于上述架构，每个编码Agent在会话开始时都会被提示执行一系列标准步骤：

1.
   1. 运行 pwd 查看当前工作目录。
2.
   2. 阅读Git日志和进度文件，了解最近完成了什么。
3.
   3. 阅读功能列表文件，选择一个未完成的最高优先级功能。
4.
   4. 运行 init.sh 启动开发服务器。
5.
   5. 在实现新功能前，先运行基本的端到端测试，确保应用未处于损坏状态。

**典型会话流程示例：**
> \[Assistant\] 我先了解一下项目当前状态。  
> \[Tool Use\] <bash - pwd>  
> \[Tool Use\] <read - claude-progress.txt>  
> \[Tool Use\] <read - feature_list.json>  
> \[Assistant\] 检查Git日志...  
> \[Tool Use\] <bash - git log --oneline -20>  
> \[Assistant\] 检查是否有启动脚本并重启服务器...  
> \[Assistant\] 现在验证基本功能是否正常...  
> \[Assistant\] 验证通过。现在我查看 tests.json 决定下一步做什么。

### 常见故障模式与修复方案总结


|        问题        |          初始化Agent行为          |                  编码Agent行为                   |
|------------------|------------------------------|----------------------------------------------|
| Claude过早宣布项目全部完成 | 根据输入规格，建立包含详细功能描述的结构化JSON文件。 | 会话开始时读取功能列表，只选择一个功能开始工作。                     |
| 环境遗留Bug或无文档记录    | 建立初始Git仓库和进度笔记文件。            | 开始时读取进度文件和Git日志；运行基础测试发现潜在Bug；结束时提交Git和进度更新。 |
| 过早标记功能为"完成"      | 建立功能列表文件。                    | 自我验证所有功能。仅在仔细测试后标记功能为"通过"。                   |
| 浪费时间研究如何运行App    | 编写能运行开发服务器的 init.sh 脚本。      | 会话开始时直接读取并运行 init.sh。                        |


### 写在最后

这项研究展示了长程Agent框架的一种可行方案，但仍有未解决的问题：

单Agent vs 多Agent：目前尚不清楚是通用的编码Agent表现最好，还是采用多Agent架构（如专门的测试Agent、QA Agent、代码清理Agent）更优

领域泛化：本演示针对全栈Web开发。未来方向是将这些经验推广到科学研究或金融建模等其他长程任务领域#Agent

参考：

https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

--end--  

最后记得⭐️我，这对我非常重要，每天都在更新：

欢迎点赞转发推荐评论，别忘了关注我


[Read in Cubox](https://cubox.pro/web/card/7393599330126398303)

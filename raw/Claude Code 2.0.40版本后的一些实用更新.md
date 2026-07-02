---
id: "7395715492368878501"
cubox_url: https://cubox.pro/web/card/7395715492368878501
url: https://mp.weixin.qq.com/s/lEWh_QNOwNRFcjYKVjxTEg
tags:
  - Skill/claude-code
---
# Claude Code 2.0.40版本后的一些实用更新

Claude更新支持自定义系统提示词，允许创建输出样式、使用钩子控制代理行为、扩展Git命令权限，并新增子代理生命周期管理和技能自动加载功能，提升AI编程的灵活性和效率。

[Read in Cubox](https://cubox.pro/web/card/7395715492368878501)  
[Read Original](https://mp.weixin.qq.com/s/lEWh_QNOwNRFcjYKVjxTEg)  

---


---

\## 📖 正文全文

# Claude Code 2.0.40版本后的一些实用更新

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/lEWh_QNOwNRFcjYKVjxTEg)node 字节笔记本

2.0.40后允许修改系统提示词了。

创建、共享和安装自定义输出样式,这些样式本质上是 Claude 的系统提示,可以完全改变 Claude Code 的交互方式和行为模式。

CSwitch就是基于这点实现的全局风格提示。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F4HWyricuhgQcFhV9Ciby01Mia67KvH4AkSDS8tMNwp523rtLFocXe8j8Egxa3MFIvWw8atVghbSIRDohFJvhAXcicg%2F640%3Fwx_fmt%3Dpng%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0&valid=false)

包括里面的输出语言还有回答风格等全局的输出风格提示。

我们也可以创建自定义输出样式：

    # 描述你想要的样式
    "我想要一个性能优化专家输出样式:
    - 优先考虑算法复杂度和数据结构选择
    - 每次修改都分析性能影响
    - 提供优化前后的基准测试"


输出样式存储在全局可用：地址 `~/.claude/output-styles`

或者项目级别，在 `.claude/output-styles`。

然后通过 `/output-style` 命令切换。

Claude默认提供了三种内置样式，对比如下：

Default：简洁高效,直接执行任务，适合于经验丰富的开发者快速编码。

Explanatory提供"Insight"块解释设计决策，可用于理解新代码库,生成文档。

Learning会留下 `TODO(human)` 让你实现，对于入门学习特定领域很有效。

**提示钩子的模型参数**

实际案例:

    {
      "hooks": {
        "Stop": [
          {
            "type": "prompt",
            "model": "claude-haiku-4-5-20250929",
            "prompt": "评估 Claude 是否应该停止: $ARGUMENTS。检查所有任务是否完成,如果还有未完成的测试或文档,返回 block。"
          }
        ]
      }
    }


提示钩子将钩子输入和你的提示发送给快速 LLM (Haiku)，最后LLM 以结构化 JSON 返回决策。

**Git 命令优化**

扩展了无需批准即可运行的安全 git 命令范围，也就是说没有危险性操作的git命令就直接放开了，直接提升开发流程效率。

无公害的git安全命令如下：

* `git status`
* `git log`
* `git diff`
* `git branch`

**钩子新增字段SubagentStop**

`SubagentStop` 钩子中新增 `agent_id`和 `agent_transcript_path` 字段。

在此之前,当多个子代理运行时共享同一个 session_id,无法识别是哪个具体的子代理停止了。

这个功能就是专门用于智能体编排时用于快速定位问题用的，可以追踪每个子代理的执行时间，还可以针对特定子代理进行清理操作。

其实这点也可以借鉴到我们的日常AI Coding当中，通过具体的id和日志输出帮助快速定义问题的所在。

**代理系统与技能自动化**

为自定义代理添加 `permissionMode` 字段，实现细粒度权限控制。

案例:

    <!-- .claude/agents/code-reviewer.md -->
    ---
    name: code-reviewer
    description: 代码审查专家,检查安全性和最佳实践
    tools: Read, Grep, Glob
    permissionMode: plan
    ---

    你是安全专家,专注于:
    1. 识别潜在安全漏洞
    2. 检查代码质量
    3. 建议改进方案

    **关键**: 你只能读取和分析,不能修改代码


**权限模式类型:**

* `default`: 默认交互模式
* `plan`: 计划模式,不执行修改
* `acceptEdits`: 自动接受编辑
* `bypassPermissions`: 绕过权限检查(谨慎使用)

新增加了tool_use_id 字段

在 `PreToolUseHookInput` 和 `PostToolUseHookInput` 中添加 `tool_use_id` 字段,实现工具调用的精确追踪。

**Skills 自动加载**

子代理可以在 frontmatter 中声明所需技能，实现自动加载。

这个功能也是为AI智能体编排准备的，可以灵活的调用之前编排好的子代理。

**实际案例:**

    <!-- .claude/agents/api-developer.md -->
    ---
    name: api-developer
    description: 专门开发 RESTful API 的专家
    tools: Read, Write, Edit, Bash
    skills: openapi-generator, api-testing, error-handling
    ---

    # API 开发专家

    当你创建 API 时:
    1. 自动加载 openapi-generator 技能生成规范
    2. 使用 api-testing 技能创建测试
    3. 应用 error-handling 技能处理边缘情况

    这些技能已通过 frontmatter 自动加载,无需手动触发。


**技能结构示例:**

    <!-- .claude/skills/openapi-generator/SKILL.md -->
    ---
    name: openapi-generator
    description: 从代码生成 OpenAPI 规范文档
    allowed-tools: Read, Bash
    ---

    # OpenAPI 规范生成器

    \## 使用流程

    1. 分析路由文件识别端点
    2. 提取请求/响应模式
    3. 生成完整 OpenAPI 3.0 规范

    \## 执行脚本

    使用 `scripts/generate-spec.sh` 自动生成规范。


技能使用渐进式披露设计，首先加载元数据(名称、描述)，如果相关则加载完整 SKILL.md,最后按需加载辅助文件和脚本。

**SubagentStart 钩子事件**

新增 `SubagentStart` 钩子,在子代理启动时触发。

**实际案例:**

    {
      "hooks": {
        "SubagentStart": [
          {
            "type": "command",
            "command": "uv run .claude/hooks/subagent_start.py"
          }
        ]
      }
    }


**完整生命周期监控:**

    # 完整的子代理生命周期钩子系统
    HOOKS_CONFIG = {
        "SubagentStart": ["初始化环境", "加载上下文", "记录开始时间"],
        "PreToolUse": ["验证权限", "记录工具调用"],
        "PostToolUse": ["验证结果", "更新状态"],
        "SubagentStop": ["清理资源", "计算指标", "生成报告"]
    }


**多代理文档生成流水线**

结合所有新功能，这里是一个构建完整的自动化文档系统:

    <!-- .claude/agents/doc-coordinator.md -->
    ---
    name: doc-coordinator
    description: 协调整个文档生成流程
    tools: Read, Bash, AgentTool
    permissionMode: default
    skills: project-analysis, markdown-formatting
    ---

    # 文档协调器

    你负责协调以下子代理:
    1. code-analyzer: 分析代码结构
    2. diagram-generator: 生成架构图
    3. api-documenter: 生成 API 文档
    4. markdown-compiler: 编译最终文档


    <!-- .claude/agents/code-analyzer.md -->
    ---
    name: code-analyzer
    description: 分析代码库结构和依赖关系
    tools: Read, Grep, Glob
    permissionMode: plan
    skills: ast-parsing, dependency-graph
    ---

    提取代码结构,识别关键模块和依赖关系。


**钩子配置:**

    {
      "hooks": {
        "SubagentStart": [{
          "type": "command",
          "command": "uv run .claude/hooks/log_start.py"
        }],
        "SubagentStop": [{
          "type": "command",
          "command": "uv run .claude/hooks/aggregate_results.py"
        }],
        "PostToolUse": [{
          "matcher": "Write|Edit",
          "hooks": [{
            "type": "command",
            "command": "uv run .claude/hooks/validate_docs.py"
          }]
        }],
        "Stop": [{
          "type": "prompt",
          "model": "claude-haiku-4-5-20250929",
          "prompt": "检查所有子代理是否完成,文档是否生成完整。如果缺少任何部分,返回 block。"
        }]
      }
    }


整个流程也是非常清晰的，使用 doc-coordinator 生成完整项目文档，SubagentStart 触发后记录 code-analyzer启动，中间会使用SubagentStop 触发保存分析结果，最后的Stop 钩子使用 LLM 验证完整。

[别学n8n了！用Claude Code Skills 复刻n8n工作流](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247507976&idx=1&sn=4b9d6b1658295e24b22c713ddb83f576&payreadticket=HAy-Vnvt2GzjXu4RkJ_k2Ey5t7Mo5X1aGiCh26lF2mgaWWZofKo7gtkdD_io4S4WHQsyp38&scene=21\#wechat_redirect)  

[MCP已废？Claude Code下的MCP正确打开方式！](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247508293&idx=1&sn=f5475ee41699a055b44ca5d72f146a66&scene=21\#wechat_redirect)  

[使用Claude Skills 快速学习一切](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247508365&idx=1&sn=e2a575e83a64074dc2192217a1a9d006&scene=21\#wechat_redirect)  


[Read in Cubox](https://cubox.pro/web/card/7395715492368878501)

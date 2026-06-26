---
id: "7395002192941286835"
cubox_url: https://cubox.pro/web/card/7395002192941286835
url: https://baoyu.io/translations/claude-skills-deep-dive
tags:
  - AI-Agent/context-engineering
  - AI-Agent/skill
---
# 从第一性原理深度拆解 Claude Agent Skill | 宝玉的分享

执行工作流 (The Lifecycle)
当 Claude 决定使用某个 Skill（例如 pdf 处理技能）时，系统会执行以下非传统的工具调用流程：
1. 调用阶段：Claude 发出工具调用请求 Skill(command="pdf")。
2. 拦截与注入 (The Injection - 核心步骤)：
系统不执行该命令并返回结果。
相反，系统读取 pdf 技能的 SKILL.md 文件。
上下文修改：系统将 Markdown 中的详细指令作为新的用户消息 (User Messages) 插入到对话历史中。
执行环境修改：系统更新当前会话的权限（例如临时授予读取文件和运行特定 Bash ...

[Read in Cubox](https://cubox.pro/web/card/7395002192941286835)  
[Read Original](https://baoyu.io/translations/claude-skills-deep-dive)  

---

## Annotations  

> 工具做了一件事，返回了一个结果，交互就结束了。技能的运作方式根本不同。技能不是执行离散动作并返回结果，而是注入全面的指令集，修改 Claude 对任务的推理和处理方式。这创造了一个普通工具从未面临的设计挑战：用户需要了解哪些技能正在运行以及它们在做什么的透明度，而 Claude 需要详细的、可能非常冗长的指令来正确执行技能。  

[Link️](https://cubox.pro/web/annotations/cards/7395002192941286835?highlight=7395008116699430955)  


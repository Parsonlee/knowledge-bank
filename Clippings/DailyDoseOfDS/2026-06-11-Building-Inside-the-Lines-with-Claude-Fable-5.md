title: "借助 Retool 与 Claude Fable 5 在安全边界内构建 Agent" source: "https://mail.google.com/mail/u/0/#inbox/19eb880a3ed57fd8" author:

"[[DailyDoseOfDS]]" published: "2026-06-11" created: "2026-07-28" description: "探讨长程自主 Agent 的安全边界，展示如何将 Claude 部署到 Retool 运行时中以接入 SSO、角色权限校验与完整审计日志。" tags:

clippings

# 借助 Retool 与 Claude Fable 5 在安全边界内构建 Agent

当 Agent（如 Claude Fable 5）能够自主运行数小时甚至数天时，核心问题不再是它能构建什么，而是它在运行过程中允许触碰什么资源。

在一个内部退款工具的测试中，Claude 编写了 SQL 并生成了退款按钮。虽然构建极为迅速，但控制哪些人能触发退款、记录审计日志等安全控制是模型本身无法单独处理的。

将该 Agent 部署到 Retool 运行时中，Agent 会自动继承企业的 SSO 认证、退款角色校验以及对所有 SQL 查询和操作的完整 Audit Log。Retool 将此称为“在安全边界内构建（Building inside the lines）”。

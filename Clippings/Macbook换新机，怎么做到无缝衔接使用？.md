---
title: Macbook换新机，怎么做到无缝切换？
source: https://www.superlinear.academy/c/notes/macbook
author:
  - superlinear.academy
published:
created: 2026-06-26
description: 新旧MacBook迁移
tags:
  - Life
---
## 【经验总结】Macbook换新机，怎么做到无缝衔接使用？

这几天拿新旧 MacBook 做了数据迁移。  
  
现在我的新 MacBook 完美继承了旧机的环境配置，使用起来没有任何断层的感觉。  
  
我所有的 Agent 配置，Skill，MCP 都无缝衔接到新机上了，不需要重新部署和安装，非常丝滑。  
  
分享几个可能"人尽皆知"的小 Tips。  
  
1。  
  
新旧机的用户名，一定要保持一致。  
  
因为 Skill 是用符号链接挂在系统里的，路径里带着 /Users/你的用户名，用户名一变，链接全断，Skill 直接读不到。  
  
连带跨会话的记忆、历史会话的路径，全按用户名编码，名字一改全失效。  
  
这个坑我是真踩过，新机一开始顺手设了个不一样的名字，结果一堆东西连环出问题，改回跟旧机一致才恢复正常。  
  
2。  
  
==第二个，数据迁移这一步，可以用 Mac 自带一个叫"迁移助理"的工具。  
  
新机一开机就会引导你用，你可以选择性传输旧机的文件、APP、账户、配置等等。  
  
然后它会让你选传输方式，非常建议准备一根雷电 4 或 5 的数据线，把两台 Mac 直接连起来，走霹雳网桥通道。==  
  
传输速度比 WIFI 快几十上百倍，几百 G 的东西一会就搬完。  
  
线价格也不贵，我在某团上买的，20多块钱。  
  
趁着换机备一根，后面需要传输大型文件的时候也用得着。  
  
3。  
  
==有时候“迁移助理”并不能完全确保100%可靠，可能传的时候会漏些东西。  
  
这里第三个技巧来了，先别急着把旧机处理掉，反过来让它给新机当“初始化大脑”。  
  
我的做法是：先在旧机上让 Agent 做一次全面的体检——装了哪些工具、各自什么版本、配置都放在哪，全摸一遍，最后整理出一份新机的部署和校验清单。  
  
等新机到了，把两台机器打通：在两台 Mac 的「系统设置 → 共享」里，都打开"远程登录"（也就是 SSH）和"文件共享"，这样旧机就能访问和处理新机的硬盘文件了。  
  
然后让Agent会比对两台机器的环境配置和文件，有问题或者缺失的就在新机上自己修复。==  
  
整个过程我基本没怎么手动盯，Agent自己就能处理好。  
  
做完这几步，新机的使用体验就和旧机一毛一样了。  
  
真正值钱的从来不是这台机器，是里面的 Skill、上下文、记忆和跑着的 Agent，这些才是我的电脑本体。  
  
恭喜陪伴我五年的Intel老登Pro退役了，他的下一站是：转转。

![](https://app.circle.so/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRkVUdXdvPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--795f90678c44d21455d7e049fecf8fb726ce8848/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJNEJEQTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--7535ef66ff04b52d1ea165e904a77a64f9cc7389/xhs-05.png)

Conversation summary

评论区主要围绕如何无缝衔接新旧MacBook的使用展开，大家对使用雷电数据线进行快速数据迁移和利用Agent进行环境体检的建议表示认可和赞赏。同时，部分用户分享了旧机的后续用途，整体氛围积极且实用。

旧机准备给儿子玩了

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCRlh5TlFnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--b3188cbb609f09767a8e9e7eeb3ffafb3d77aed0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lKYW5CbFp3WTZCa1ZVT2hSeVpYTnBlbVZmZEc5ZmJHbHRhWFJiQjJrQ0xBRnBBaXdCT2dwellYWmxjbnNHT2dwemRISnBjRlE9IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--ef295ed08e817a599d692fd6d8761673d3ed547f/IMG_2643.jpeg)](https://www.superlinear.academy/u/f7e34206)

准备一根雷电 4 或 5 的数据线，把两台 Mac 直接连起来，走霹雳网桥通道。  
  
学习了！  
  
还有最后用agent综合体检的思路也很有用！

Yan Wang 鸭哥 榨干旧机的最后一滴 哈哈

[![](https://www.superlinear.academy/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTVNBTXdnPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--4cdb078a6803ddf96a1c9fc02fe3d083d6ff8a62/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJc0FXa0NMQUU2Q25OaGRtVnlld1k2Q25OMGNtbHdWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--67365f61f655fbc86c65a51f2e9992ab818c41cd/%E5%A4%B4%E5%83%8F.jpg)](https://www.superlinear.academy/u/452cd000)

诶这个好实用

立正 谢谢～
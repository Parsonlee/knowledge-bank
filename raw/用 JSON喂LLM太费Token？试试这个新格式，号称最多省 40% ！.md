---
title: "用 JSON喂LLM太费Token？试试这个新格式，号称最多省 40% ！"
---

# 用 JSON喂LLM太费Token？试试这个新格式，号称最多省 40% ！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/YrjNB1yM8E4HB62PClRrag?mpshare=1&scene=1&srcid=1215BLO1s4iPQFiJlFKwGvzx&sharer_shareinfo=5ad9bde1dc967aed0a0ef33a6f68656c&sharer_shareinfo_first=5ad9bde1dc967aed0a0ef33a6f68656c&from=industrynews&color_scheme=light)架构资源栈 架构资源栈


大家好，这里是**架构资源栈** ！点击上方关注，添加"**星标** "，一起学习大厂前沿架构！

关注、发送C1即可获取JetBrains全家桶激活工具和码！


*** ** * ** ***

做 LLM 应用这两年，很多人都有同一个感受：**逻辑不复杂，账单倒是涨得飞快。**

大部分时候，钱都烧在「结构化数据 → 文本 → LLM」这一步上： 我们习惯用 JSON 把各种上下文、参数、结果打包给模型，结果：

*
  字段名一长，一堆双引号和逗号就先占了一半 token
*
  深层嵌套对象 + 大数组，越提示越贵

最近社区里冒出来一个新东西：**TOON（Token-Oriented Object Notation，面向令牌的对象表示法）** ，目标就很直接：
> ❝
>
> **做一个"长得像 JSON、读起来像 YAML、数组像 CSV 一样紧凑"的格式，专门给 LLM 用，尽量少占 token。**

官方号称：在不少场景里，TOON 相比 JSON 可以少用 25%～40% 的 token，甚至有例子能省到 55%。
![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FicWkcuBOpQLiarkekY99nDUOY68Vd8ZlqJjga25RzibQadbSLKXNadaYrrj9mgiaM2loHXbuNK346f1WelcL9KcObw%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0&valid=false) image

*** ** * ** ***

\## TOON 是啥？一句话：给 LLM 用的「节省版 JSON」

作者给 TOON 的定义是：
image ❝
>
> 一种\*\*模式感知（schema-aware）\*\*的、紧凑的人类可读编码，用来承载 JSON 数据模型，专门优化给 LLM 提示用。

先看同一份数据在 JSON 和 TOON 里的对比。

\#\## 传统 JSON 写法

    {
      "context": {
        "task": "Our favorite hikes together",
        "location": "Boulder",
        "season": "spring_2025"
      },
    "friends": ["ana", "luis", "sam"],
        "hikes": [
        {
          "id": 1,
          "name": "Blue Lake Trail",
          "distanceKm": 7.5,
          "elevationGain": 320,
          "companion": "ana",
          "wasSunny": true
        },
        {
          "id": 2,
          "name": "Ridge Overlook",
          "distanceKm": 9.2,
          "elevationGain": 540,
          "companion": "luis",
          "wasSunny": false
        },
        {
          "id": 3,
          "name": "Wildflower Loop",
          "distanceKm": 5.1,
          "elevationGain": 180,
          "companion": "sam",
          "wasSunny": true
        }
      ]
    }

\#\## 换成 TOON 写法

    context:
      task: Our favorite hikes together
      location: Boulder
      season: spring_2025

    friends[3]: ana,luis,sam

    hikes[3]{id,name,distanceKm,elevationGain,companion,wasSunny}:
      1,Blue Lake Trail,7.5,320,ana,true
      2,Ridge Overlook,9.2,540,luis,false
      3,Wildflower Loop,5.1,180,sam,true

可以看到几个关键点：

*
  **嵌套对象** ：长得有点像 YAML，用缩进表示层级，没有一堆花括号和双引号
*
  **定长数组** ：friends[3]: ...，声明长度 + 逗号分隔，结构非常紧凑
*
  **统一结构的数组** ：hikes[3]{id,...} 先声明字段列表，下面每一行就是一条记录，类似 CSV

这套写法对 LLM 来说很友好：

*
  人类读得懂
*
  字段名只写一次，后面全是「纯数据」
*
  结构清晰、冗余少，tokenizer 看着也舒服

*** ** * ** ***

\## 省了多少 token？

image

在上面这个例子里，结果大概是：

*
  相比**格式化 JSON** （带缩进、换行），TOON token 数量减少 **55%**
*
  相比**紧凑 JSON** （去掉所有空格缩进），减少 **25%**
*
  相比 **YAML** ，减少 **38%**

当然，这只是一个「中等复杂度 + 比较规整」的例子。TOON 自己也很诚实地说：

*
  **非统一结构的数据** ：JSON 可能反而更省
*
  **深度嵌套对象** ：YAML 有时更紧凑
*
  **纯扁平数据表** ：CSV 还是 token 王者

TOON 的定位是：
> ❝
>
> 在「有明确 schema、数组比较规整、但又不想扁成生硬 CSV」的场景里， 用少量额外结构（字段头 + 数组声明，约 5% 开销）换来更好的 token 利用率和 LLM 准确性。

*** ** * ** ***

\## 省 token 会不会影响准确率？

这是大家看到新格式第一反应的问题。

TOON 的作者在 X 上专门回应了一句（原话大意）：
> ❝
>
> "令牌效率会影响准确性吗？" 不会 :) 在 GPT-5 Nano 上，TOON 在减少 46% token 的前提下，依然能达到 **99.4% 的准确率** 。 测试覆盖了大约 160 个问题和 3 个不同的 LLM，用语义方式做的验证。 他个人的猜测是：**明确指定长度和字段列表，反而减少了错误。**

从 LLM 的角度想一下就挺合理：

*
  JSON 虽然结构严整，但对模型来说，噪音也不少：

  *
    成堆的 {}、[]、""、,、重复字段名
*
  TOON 一旦声明了 hikes[3]{id,name,...}：

  *
    模型已经拿到了「数组长度 + 字段顺序」，后面每一行变量都可以精确对齐
  *
    解析起来反而更像读表格，而不是在对象树里穿梭

只要你在提示里把「字段含义」讲清楚，模型用这套结构做信息抽取、工具调用，其实是更轻松的。

*** ** * ** ***

\## TOON 是怎么混搭 YAML / CSV 的？

从上面的例子基本可以看出它的设计取向：

1.
   **对象 = YAML 风格键值 + 缩进**

   *
     context:
   *
     task: ...
   *
     没有双引号、逗号和花括号，既压缩 token 又保留可读性
2.
   **定长数组 = 元信息 + 列表**

   *
     friends[3]: ana,luis,sam
   *
     [3] 给模型一个强约束：这里应该有 3 个元素
3.
   **统一结构数组 = CSV 风格表格 + 头部 schema**

   *
     hikes[3]{id,name,...}:
   *
     下一行开始就是一个 mini-CSV，每行一个记录

这种 schema-first 的拼接方式有几个直接好处：

*
  把「结构描述」集中在一处说明，后面全是密集数据
*
  模型在生成或解析时可以借助 [...] 和 {...} 做自检
*
  与 JSON 的字段重复相比，很自然就节省了不少 token

*** ** * ** ***

\## 什么时候不建议用 TOON？

TOON 本身的文档（不建议使用的情况)
image

*
  **结构高度不规则** ：每条记录字段都不一样，那你写 {id,name,...} 意义不大
*
  **递归 / 深度嵌套树** ：TOON 照样能写，但省 token 优势不明显，YAML/JSON 也能干
*
  **本来就适合 CSV 的纯表格** ：直接 CSV 就完事了，没有必要绕一圈

简单粗暴的判断标准可以是：
> ❝
>
> 你已经有一个比较清晰的 JSON Schema， 又希望既能节省 token，又保留相对好的可读性 → 可以尝试 TOON。

*** ** * ** ***

\## 想自己试试？生态和工具链已经准备好了

目前 TOON 的官方资源大致有这些：

*
  规格说明（英文）：https://github.com/toon-format/spec
*
  文档与 LLM 提示指南：https://toonformat.dev/guide/llm-prompts
*
  在线测试 \& Token 对比 playground：https://www.curiouslychase.com/playground/format-tokenization-exploration
*
  TypeScript/JavaScript 参考实现（MIT License）：https://github.com/toon-format/toon

参考实现里已经包含：

*
  编码器 / 解码器（TOON ↔ JSON）
*
  JSON→TOON 的 CLI 转换工具
*
  性能和准确性基准测试脚本

如果你在做的是：

*
  高频调用、多轮工具调用的 Agent 系统
*
  需要给模型塞很大一坨上下文的 RAG / 工作流引擎
*
  对延迟和成本都比较敏感的在线服务

可以挑几类典型 payload：

1.
   先用 JSON 提示跑一轮，记录：

   *
     token 消耗
   *
     首 token 时间（TTFT）
   *
     tokens/s
   *
     以及任务正确率
2.
   再把同样结构改成 TOON 跑一轮，重新量同一套指标

最终怎么选，就不一定只看「省了多少 token」，还要看：

*
  延迟有没有改善
*
  是否更容易让模型遵守结构
*
  工程上引入 TOON 的复杂度，值不值

*** ** * ** ***

\## 小结：JSON 继续当"接口格式"，TOON 可以专门当"提示格式"

站在工程落地的角度，不太可能在短时间里把所有 API 接口都改成 TOON。 但你完全可以做一个分层：

*
  **对外 / 服务间通信** ：照旧用 JSON（生态成熟、工具丰富）
*
  **对内 / 喂给 LLM 的 payload** ：在网关层转成 TOON，压一压 token 成本

TOON 目前还很新，肯定算不上"标准"，但它代表了一种值得关注的趋势：
> ❝
>
> **给 LLM 设计数据格式时，应该把"人类可读性 + token 效率 + 模型可解析性"一起考虑，而不是沿用老一套通用序列化格式。**

如果你正好在为 LLM 的账单皱眉，那不妨找一两个场景试试： 就算最后没选 TOON，这类 schema-aware 的提示格式设计思路，本身也会对整个系统架构有帮助。

*** ** * ** ***

**喜欢就奖励一个"👍"和"在看"呗\~**
image

\## 专属付费版全家桶

如果你只是激活JetBrains全家桶IDE，那这个应该是目前最经济、最实惠的方法了！

专属付费版全家桶除了支持IDE的正常激活外，还支持常用的付费插件和付费主题！
全家桶+付费插件授权

100%保障激活，100%稳定使用，100%售后兜底！

\#\## 为什么说专属付费版全家桶最经济、最实惠？

因为专属付费版全家桶支持常用付费插件和付费主题。而任意一款或两款付费插件或付费主题，其激活费用就远高于我提供的专属付费版全家桶。

比如，最方便的彩虹括号符Rainbow Brackets，124/年。
Rainbow Brackets

再如，MyBatis最佳辅助框架MyBatisCodeHelperPro的官方版本MyBatisCodeHelperPro (Marketplace Edition)，157/年。
MyBatisCodeHelperPro

还有最牛的Fast Request，集API调试工具 + API管理工具 + API搜索工具一体！157/年。
Fast Request

`专属付费版全家桶`包含上述这些付费插件，但不限于上述这些付费插件！

需要的小伙伴，可以扫码二维码，回复付费，了解优惠详情\~
付费获取方式

[Read in Cubox](https://cubox.pro/web/card/7400425151617041303)

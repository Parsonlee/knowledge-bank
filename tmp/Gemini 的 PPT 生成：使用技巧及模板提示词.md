# Gemini 的 PPT 生成：使用技巧及模板提示词

[mp.weixin.qq.com](https://mp.weixin.qq.com/s?__biz=MzU0MDk3NTUxMA==&mid=2247493410&idx=1&sn=218d4a6269cde93005745b9f3b85b454&poc_token=HPlOEWmj4U84MAXKSFecEpLOzxBKpIVllrIfbuzk)歸藏的 AI 工具箱 歸藏的AI工具箱


Gemini APP 前几天上线了 PPT 生成的能力，我昨天尝试了一下发现相当可以啊。

由于用的前端代码的方式实现，所以我们可以用提示词控制的非常细，包括 PPT 的各种风格细节，生成的质量比 Anthropic 那一坨强多了。

另外这东西可以跟 Gemini 本身和谷歌其他产品的各种功能打通。

比如你可以去 Google 幻灯片编辑 PPT 的细节，导出成 PPT 格式，也可以将深度研究的结果变成 PPT。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FfbRX0iaT8Egc24JRStBqTc2tF7Pz0ndnRha5ngD3kDECUjicBB2EGkPhXoaMxhdaibajhBC1KVe17u3olBABl5XVQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D0&valid=false)

这次的内容我会先介绍一下具体这个功能怎么使用，然后分享一些我探索出来的各种 Gemini PPT 生成提示词。

如果你不想要复杂的内容的话，让 Gemini 帮你生成 PPT 很简单。

在输入框开启 Canvas 模式，然后直接跟他说以"XXXX"为主题帮我生成 PPT 就可以了。

而且 Gemini 是自带搜索的，所以你甚至可以完全让他帮你填充内容，比如我这里就让他搜 Open AI 最近的算力投资信息然后生成 PPT。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FfbRX0iaT8Egc24JRStBqTc2tF7Pz0ndnRpRfGgmXLE0QI6IGsLAPqFlTjWIP5hmibnPiaiarrubjIDxYFqRSmbecsQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D1&valid=false)

然后你可能会注意到，生成的结果右上角有个选项可以下载，下载下来的结果是 PDF 格式的。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FfbRX0iaT8Egc24JRStBqTc2tF7Pz0ndnRtFmX5LPM8nJ0iaYtcETg9XXfFa8VH1N9iaiccunSbJrRPopxNdhzJbuSg%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D2&valid=false)

看到这里你可能就得说了 PDF 没有用啊，我需要 PPT 格式的。

别着急，我们这时候点一下右上角的"导出到谷歌幻灯片"，稍微等待一会之后就可以在谷歌幻灯片打开刚才做的 PPT 文件了，这个时候你想编辑什么就编辑什么，甚至支持 AI 生成图片插入。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2FfbRX0iaT8Egc24JRStBqTc2tF7Pz0ndnRrrzq2HRRsblanLh5XhyRdXiawrJZic7WaicOMpqNiaApFpEc4zB75pxbxw%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D3&valid=false)

如果你说你还是习惯在 Office 里面编辑，也可以在谷歌幻灯片的右上角文件位置选择导出成常见的 pptx 格式，是不是一下就感觉这个功能有用多了。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FfbRX0iaT8Egc24JRStBqTc2tF7Pz0ndnRaRaJkq0m8WKmVsQr3Ymc8j4tJOG4VrlMOzC4jve1TyULCicW83PtibmQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1%23imgIndex%3D4&valid=false)

另外也可以结合 Gemini 的深度研究能力去生成结果之后再变成 PPT。

但可惜的是这步得你自己复制一下结果操作，搜索结果那里的快捷生成只有网页没有 PPT，应该过段时间就会加上了。


我试了一下支持风格自定义之后用了一晚上帮大家探索了几个非常百搭的 PPT 风格提示词。

有些是从我之前的网页提示词演变来的有些是我新整理的，欢迎尝试以及在评论区返图。

Bento Grid 风格：

帮我基于文章内容生成 XXX 主题的 PPT，PPT 风格设计要求为：

苹果发布会PPT的Bento Grid风格的视觉设计；

背景为#F8F6F5、卡片背景为白色，文字颜色为#010101，高亮按钮和文字背景色为#F69AAC-DF95E3-7DBDE9 的渐变 ，卡片内的布局为主标题简短表述加大图标；注意配图的比例；

强调超大字体或数字突出核心要点，画面中有超大视觉元素强调重点，与小元素的比例形成反差；

中英文混用，中文大字体粗体，英文小字作为点缀 ；

运用高亮色自身透明度渐变制造科技感，但是不同高亮色不要互相渐变 ；数据可以引用在线的图表组件，样式需要跟主题一致；


极简主义中性色风格：

帮我基于文章内容生成 XXX 主题的 PPT，PPT 风格设计要求为：

用极简主义的布局和中性的色调作为"画布"，通过"高对比度的大号字体"和"专业高清的视觉内容"来讲述一个清晰、自信、且富有情感的故事。

采用极其简洁的布局。它们大量使用"留白"，在视觉上创造了呼吸感和空间感。

使得用户的注意力能立刻集中在核心信息（标题、关键图片）上，没有多余的边框、分割线或装饰元素，界面非常干净。

字体是设计的核心元素。所有页面都使用了强烈的字体层级对比：一个非常巨大、粗重的标题，配上小号、纤细的说明性文字。

将衬线字体（传统上用于印刷和书籍）与极简的科技感布局结合，旨在增加一种"人文主义"、"故事感"或"高级定制"的调性，使其在众多科技网站中脱颖而出。

基础色调非常克制，"黑色文字 + 浅色背景"（白色或米白色）。

通过一个巨大、流动的彩色渐变背景来增加页面的活力和"AI感"，但界面元素本身（文字、按钮）依旧是黑白的。

色彩主要来自于高质量的摄影或渲染图

文案（如 "For the builders, the tinkerers...", "The best AI audio models...", "Building a world where we do more of what we love..."）都非常直接、自信且富有感召力。设计通过极简的布局，放大了这些文案的力量。


荧光绿瑞士国际主义设计风格：

排版方式 ：

严格的栅格系统： 这是最核心的特点。每一页都严格遵守了网格布局，无论是两栏、三栏还是多行。这使得所有元素都能完美对齐，页面专业且不凌乱。

大量的留白： 设计中奢侈地使用了大面积的空白区域。这不仅让内容更容易阅读，也营造出一种从容、自信和高端的视觉感受。

清晰的视觉层次： 通过字体大小、粗细和颜色的对比，严格区分了标题、副标题、正文和数据。用户的视线会自然地被引导到最重要的信息上（例如大号的数字和加粗的标题）。

非对称平衡： 很多页面采用了非对称布局，但通过元素的精心放置，在视觉上依然保持了很好的平衡感，显得专业而不死板。

字体：

现代无衬线字体： 整个演示文稿都使用了一种或一组非常简洁、现代的无衬线字体。这种字体清晰易读，传达出一种高效、直接和具有科技感的特质。

强烈的字重对比： 设计师大胆地使用了极粗的字重来展示标题和关键数字，同时用极细（Light/Regular）的字重来展示正文。这种高对比度极具视觉冲击力。

字号差异化： 关键KPI数字被极度放大，成为页面上的视觉焦点元素，而辅助性文字（如导航栏）则非常小，主次分明。

配色：

主色调：黑 + 白 + 灰： 以白色为背景，黑色为主要文本颜色，不同深浅的灰色作为辅助（如正文、图表背景），构建了干净、专业的基础。

高饱和度的主强调色（荧光绿）： 选用了非常抢眼的荧光绿（Acid Green）作为核心品牌色。它被用在关键数据、图表、标题高亮和视觉素材上，瞬间抓住了观众的注意力，并传达出创新、活力和"未来感"。

辅助强调色（芥末黄）： 在"Sales Strategy"和"Roadmap"页面中，我们还看到了一个芥末黄/金色。它被用来标记序号（如01, 02）或时间节点，作为次要的强调色，既能区分信息，又不会与主色（绿色）冲突。

配色策略： 整体上是"中性色 + 单一强点缀色"的方案，非常克制且高效。

独特的元素：

"品牌色块"： 一个反复出现的视觉母题 (Motif) 是将黑色矩形色块作为背景，上面放置绿色的关键数字或文字。这个元素非常独特，强化了品牌形象。

极简导航栏： 页面右上角的导航栏，字体非常小且颜色很浅。它提供了功能性，但完全不会干扰主要内容的呈现。

CTA 按钮： 所有的行动号召（CTA）按钮都统一设计为简单的黑色矩形和白色文字，风格统一且十分醒目。


极简黑白风格：

帮我调研XXX分析后做成英文ppt，PPT 风格要求为：

配色 ：

基调： 严格的单色系（Monochromatic），主要由 黑、白、灰 构成。这奠定了专业、严肃且高级的视觉基础。

点缀色： 使用了单一的高饱和度亮绿色（或薄荷绿）作为点缀色。这个颜色用得非常克制，只出现在最需要强调的地方。

字体：

字体家族： 通篇只使用了一种无衬线字体（Sans-serif）。这种字体（类似于 Helvetica, Inter 或 Akkurat）线条简洁、易读性高，非常适合传达现代感和科技感。

视觉层级： 字体的层级完全通过 字重（Weight）、大小（Size） 和 大小写（Case） 来区分，而不是通过切换字体。

主标题： 通常是全大写（ALL CAPS）、粗体（Bold），并且有时刻意增加了字间距（Tracking），使其看起来更疏朗、更有设计感。

正文： 使用常规（Regular）或细体（Light）字重，字号较小，确保了与标题的强烈对比。

排版方式 ：

网格系统： 设计严格遵循一个不对称的网格系统（Asymmetrical Grid）。所有元素（文字、图片）都严格地沿着不可见的垂直和水平线对齐。

大量留白： 设计中使用了非常慷慨的留白（White Space）（在黑色背景的幻灯片上则称为"留黑"）。这使得每一页都不显得拥挤，让观众的视线可以聚焦在关键信息上。

强对齐： 绝大多数文本都采用了严格的左对齐。这创造了干净利落的纵向视觉流，阅读体验非常舒适。

结构： 频繁使用清晰的多栏布局（例如图文两栏、三栏对比），结构一目了然。

独特的元素：

黑白背景交替： 设计师巧妙地在全白背景（用于信息密集的页面，如目录、图表）和全黑背景（用于强调性的页面，如封面、标题页）之间切换。这种强烈的反差创造了一种视觉节奏感，让演示不单调。

纯文字排版： 像"目录页"（Table of Content）完全依赖字体的大小、粗细和空间排版来呈现，不添加任何多余的图标或装饰，显示了设计师对排版的高度自信。


好了今天的内容就是这些了。

目前来看整个 Gemini PPT 生成最大的问题就是对于 PPT 的页数非常克制，基本上可能固定在了 13 页。

希望后面可以通过提示词控制 PPT 的页数就好了。

另外目前还有个用法就是你别把他当做完整 PPT 生成的结果，当成 PPT 模板生成就好，生成结束后你下载下来再编辑和填写你自己的内容，可控性和美观度会好不少。

如果觉得内容对你有帮助的话可以帮我点个赞👍或者喜欢🩷，也可以转发给你被 PPT 困扰的朋友们。

[Read in Cubox](https://cubox.pro/web/card/7387387562941218975)

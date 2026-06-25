---
title: "OCR的有效数据增强"
source: https://mp.weixin.qq.com/s/y7wsvmodtm7R9bPuVpvuaA
created: 2026-06-25
tags:
  - clipping
  - cubox
---

# OCR的有效数据增强

> [!quote]
> OpenCV是一个众所周知的计算机视觉库。Albumentations是一个相对较新的Python库，用于进行简单但功能强大的图像增强。

> [!quote]
> 为了产生像是使用宽线宽度笔的效果，我们可以膨胀原始图像：

> [!quote]
> 第二种增强技术：引入噪声
> 我们可以从图像中删除黑色像素，也可以添加白色像素。有几种方法可以实现这一点。我尝试了许多方法，但这是我的简短清单：
> 黑色下降颜色的RandomRain非常有害。即使对我来说，仍然很难阅读文本。这就是为什么我选择将其发生的机会设置得很低的原因：

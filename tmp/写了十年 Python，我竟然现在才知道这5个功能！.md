# 写了十年 Python，我竟然现在才知道这5个功能！

[mp.weixin.qq.com](https://mp.weixin.qq.com/s/YdKuIzRgmXgrz7MDPqSfig)AI研究生 PyTorch研习社


> 听说过__missing__吗？

我猜你现在在想什么。

"又一篇'隐藏的Python功能'文章？我都看腻了！无非就是说用collections.defaultdict，试试enumerate而不是range(len())，哦，还有谁不知道f-strings啊？"

无聊的水文。

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_jpg%2F6Ex6Atic0gTyVPDUKWbKStRzWic2wgZEQt0uJlALLWlWOEMvOPCSXp9hUad0O1IckLBGAp04Gc1xDSo2TbsoA5Mw%2F640%3Fwx_fmt%3Dwebp%26from%3Dappmsg%26randomid%3Dc82ip1k3%26tp%3Dwebp%26wxfrom%3D5%26wx_lazy%3D1&valid=false)

先别急，这篇不一样。这些不是那种"显而易见"的功能------它们是真正的宝藏。除非你深入研究过源代码，或者在Python Enhancement Proposal (PEP)的兔子洞里迷路了三个小时，不然你很难发现它们。

我挑了5个Python功能，教程里很少提到，但能干净利落地解决实际问题，代码简洁，几乎不用写繁琐的模板代码。

开始吧！

### 1. contextlib.suppress：悄悄干掉异常（不用丑陋的try块）

**问题** ：你想忽略某个特定的异常，但为了这点小事写try/except块感觉太夸张了。

你可以这么写：

    try:
        os.remove('tempfile.txt')
    except FileNotFoundError:
        pass

或者，用更优雅、Pythonic、像Jedi一样的方式：

    from contextlib import suppress

    with suppress(FileNotFoundError):
        os.remove('tempfile.txt')

就这么简单。

没有try，没有except，没有pass。只有清晰的意图：  
"我要运行这个代码，如果遇到这个特定错误，默默继续。"

**什么时候用** ：

*
  • 删除文件或关闭socket
*
  • 清理可能不存在的临时文件
*
  • 关闭可能不存在的服务

**额外福利** ：还能同时忽略多个异常。

    with suppress(FileNotFoundError, PermissionError):
        os.remove('config.yaml')

**为什么重要** ：  
这种功能让你的代码干净10倍------它就藏在contextlib模块里，大多数人只在用@contextmanager时才会碰它。

### 2. sys.setrecursionlimit：搞定递归，免受其害

**问题** ：你在写递归算法，比如树遍历或DFS，突然Python抛出：

    RecursionError: maximum recursion depth exceeded

这是因为CPython默认的递归限制是1000。

教程里很少告诉你：你可以用一行代码提高这个限制。

    import sys
    sys.setrecursionlimit(10**6)

是的，100万。

再也不会因为递归代码完全没问题却遇到诡异的栈溢出。

**什么时候用** ：

*
  • 自定义解析器
*
  • 递归遍历数据结构
*
  • 回溯算法

**专业提示** ：  
除非你清楚程序的调用栈深度，别随意设太高的值。每次调用都会吃内存。但如果你知道自己在干嘛，这招绝对改变游戏规则。

**为什么被忽视** ：  
因为大多数人不敢碰sys设置。但你不一样，你不是普通人。

### 3. typing.Literal：字符串安全的秘密武器

**问题** ：你的函数接收字符串，但实际上只接受几个有效值。比如：

    def connect(mode: str):
        if mode not in ['read', 'write']:
            raise ValueError("无效的模式")

这没问题，但这是运行时验证。为什么不把验证交给类型检查器呢？

来认识Literal：

    from typing import Literal

    def connect(mode: Literal['read', 'write']):
        ...

现在，如果你传入'read'或'write'以外的值，IDE或静态类型检查器（比如mypy）会在代码运行前就发出警告。

**现实场景** ：

    def get_user(role: Literal['admin', 'moderator', 'user']):
        ...

这让你的API自带文档，安全又健壮------不用写if块或自定义验证器。

**为什么重要** ：  
这是在动态语言里实现干净的编译时验证。而且它跟pydantic、FastAPI和现代工具配合得天衣无缝。

**额外炫技** ：还能跟Union一起用：

    def get_data(format: Literal['json', 'xml'] | None = None):
        ...

### 4. **missing** ：dict子类里被低估的魔法方法

**问题** ：你在用字典，想自定义处理不存在的键，但defaultdict给你的控制不够。

是时候重写那个驱动一切的隐藏方法了：**missing** 。

    class AutoDict(dict):
        def __missing__(self, key):
            value = self[key] = f"[{key} 未找到]"
            return value

使用方式：

    d = AutoDict()
    print(d['python'])  # [python 未找到]
    print(d['java'])    # [java 未找到]

**发生了什么** ？  
当键不存在时，__missing__会被触发。你可以记录、转换、设置默认值，甚至自动插入值。

**进阶场景** ：  
跟踪未知的访问模式：

    class AccessTracker(dict):
        def __missing__(self, key):
            print(f"键 {key} 被访问但未找到。")
            raise KeyError(key)

**为什么重要** ：  
它让你对字典行为有手术刀般的控制。大多数开发者甚至不知道__missing__的存在------它在官方Python数据模型文档之外很少被提及。

### 5. **subclasshook** ：让你的API像鸭子一样灵活

**问题** ：你定义了一个抽象基类，但不想强迫别人继承它------你只希望他们实现正确的方法。

Python管这叫结构化类型------这就是为什么你会爱上__subclasshook__。

    from abc import ABC, abstractmethod

    classJsonSerializable(ABC):
        @abstractmethod
        defto_json(self):
            pass

        @classmethod
        def__subclasshook__(cls, C):
            ifany("to_json"in B.__dict__ for B in C.__mro__):
                returnTrue
            return NotImplemented

现在，只要一个类有to_json()方法------不管有没有继承关系------它都会被视为子类。

    class MyClass:
        def to_json(self):
            return '{"hello": "world"}'

    print(issubclass(MyClass, JsonSerializable))  # True

**为什么重要** ：  
你获得了接口式的行为，而不用强制继承。这在构建插件、API或框架时超级强大------灵活性胜过僵硬的继承关系。

你不是在检查类的血统------你在检查它的行为。

够Pythonic吧？非常。

够稀有吧？极其。

感谢阅读！


[Read in Cubox](https://cubox.pro/web/card/7350408999809844914)

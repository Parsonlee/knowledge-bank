## 线上部署

机器：172.29.24.6、 ~~172.29.24.15~~、172.29.24.47

1.  ~~**dify**部署在机器 **172.29.24.15:4410**
    ，域名地址：[dify.yiyaowang.com](https://dify.yiyaowang.com)~~

> （已废弃，使用
> [https://chatbi-dify.111.com.cn/](https://chatbi-dify.111.com.cn/apps)）

2.  **dify-tools**服务提供工具接口，部署在**两台机器的4411端口**

    a.  API
        URL：[dify-tools.yiyaowang.com](https://dify-tools.yiyaowang.com)

    b.  git-lab：<http://new-gitlab.yiyaowang.com/zhongtai_alg/dify_tools_server>

    c.  项目更新：需要本地push到gitlab，然后在easyops上走流水线发布

3.  crontab定时任务设置在**172.29.24.6**机器上，查看指令：**crontab -l**

4.  流程：3条每天执行的定时命令，

    a.  9点50调用 **53-dify** 的测试流程，

    b.  10点调用 **172.29.24.6：虎鲸dify** 上的生产流程，

    c.  11点45调用 **dify-tools** 中的 **/record_stats**
        接口记录当日访问量

![descript](media/image1.png){width="6.299305555555556in"
height="1.4733081802274717in"}

5.  访问量查看：**172.29.24.6 -
    /data/services/models/ai_news_staff/visit_stats.txt**

## 企业微信机器人的key

个人test-bot：ab798464-7911-438c-8504-4d08f498f0a7

内部测试bot：47ba8d6b-6ae0-4bd5-bee7-8897d663b544

*[线上]{.underline}：*

资讯：a1d0bc0e-197c-44f4-a477-d5aa461aaca7

知识分享：c0a0915c-67f8-4438-9886-47b03cb13b20

错误捕捉：3ddd2586-4962-4d0d-adad-197c8e40e588

## 新闻日报

<http://10.6.10.53/app/419851b3-0428-4cb8-8c2f-66e4738c92ea/workflow>

![descript](media/image2.png){width="6.299305555555556in"
height="1.2275426509186351in"}

### v1：

- crontab定时**每周**一上午10点执行auto_web_news.py脚本

  - 查看crontab job：crontab -l，

  - 每执行一次会在/data-new/houqing/dify_project_api/crontab.log留下一条记录

- dify流程中的**爬虫模块**：

  - /data-new/houqing/dify/project_api/db_flask.py（接口：/news，方法：post）

  - news_crawler.py：**基于Jina_Reader
    实现**，crawler类定义多个函数，每个函数首先获取来自Jina处理过的网站新闻，然后执行定制化后处理

### v2：

1.  crontab改为**每天**10点执行：

2.  爬取新闻接口\"53：4411/news\"**放弃使用jina_reader**，改用beautifulSoup进行**手动解析**后处理

<!-- -->

3.  流程启动设置两个参数：

    a.  duration：1代表爬取前一天的新闻

    b.  env：test/prod，分别执行"AI资讯播报"和"AI资讯播报-Backup"两个流程

4.  **posted_news_url.txt**
    文件用于存放前三天（每次调用设置duration=3）的新闻url，用作过滤。作用：1）避免按日期进行强过滤时产生遗漏；2）周一爬取时获取周末几天的新闻

5.  增加[XiaoHu.AI](https://xiaohu.ai)的新闻来源，使用三个新闻网站，**保证了整体新闻数量，让gpt4控制新闻输出在3-5条稳定输出**

### v3:

1.  **记录访问量**：新增了一个历史新闻的前端页面，以\"/\"默认路径作为访问入口，解析原新闻链接并自增访问量，新增接口**record_stats**将当天访问量进行记录，并重置全局变量visit_count

2.  **给GPT4整理和输出兜底：**由于gpt4在进行新闻整理输出模板时的**质量不可控**，在后面添加了一个gpt3.5节点，用于判断4的输出是否存在问题，gpt4输出有误则结束流程，向错误捕捉机器人发送消息

### v4:

1.  **将posted_news_url.txt、visit_stats.txt移动到堡垒机共享目录：**由于请求被无序分发到两台堡垒机，因此将所有需要进行写入的文件进行共享，并在记录访问量时分别调用两台机器的接口进行汇总

2.  **bug修复：**ai-bot网站对来源网站进行了重定向并隐藏了原始url，使得之前的url解析逻辑失效。修改了解析逻辑

## 知识分享

<http://10.6.10.53/app/2e6acfb0-ada0-446c-8325-77cfb7993de0/workflow>

- 流程设计：1）接口返回本次主题 2）RAG检索获取可能的参考链接
  3）GPT构建输出

  - 预定义一个学习路线主题词库栈，每次执行返回顶部主题词并从中删除

  - 知识库的信息定义为：（简述，URL）的形式

  - gpt输出模板为：1）主题词的简述 2）可供学习的参考链接

- demo：接口返回本次主题词 -\> google搜索相关参考链接 -\> GPT整理输出

![descript](media/image3.png){width="6.299305555555556in"
height="1.6700896762904638in"}

每个已收集的链接以"**URL + 类型 + 说明 +
描述**"四个字段进行组织，用来提高检索成功率

![descript](media/image4.png){width="4.503319116360455in"
height="3.4423982939632545in"}

输出样式

![descript](media/image5.png){width="3.8854166666666665in"
height="2.105138888888889in"}

最终样式

![descript](media/image6.png){width="3.8004385389326334in"
height="1.8514949693788276in"}

需要调整的点：

1.  输出样式需要调整

2.  要限制搜索到的链接来源，指定**白名单**（Wiki等）

3.  需要触发检索，与本次主题相关的**已收集的学习资料链接**加入到输出

4.  主题词的细腻度

5.  知识库的持续性扩充

### v1

1.  **添加投票和反馈系统：**

    a.  在每次分享的消息中加入投票入口，从备选主题中投出下次主题

    b.  让用户提交关于资讯和分享的反馈

    c.  将主题词放入mysql，以数据库方式进行CRUD操作

2.  **将检索和网络搜索结合：**提高知识库召回阈值，避免不相关的链接被加入到消息中

3.  以prompt的方式，**做简单的筛选**：

    a.  去除URL过长、图书详情页的链接

    b.  当搜索的结果含有wiki链接优先使用

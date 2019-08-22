Welcome to amazing-python!
==========================

**Code here all run in the latest python stable version python3.7**

[![image](https://codebeat.co/assets/svg/badges/A-398b39-669406e9e1b136187b91af587d4092b0160370f271f66a651f444b990c2730e9.svg)](https://codebeat.co/projects/github-com-pynickle-amazing-python-master)

[![image](https://badges.gitter.im/amazing-python/community.svg)](https://gitter.im/amazing-python/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

[![image](https://hits.b3log.org/b3log/amazing-python.svg)](https://github.com/pynickle/amazing-python)

[![image](https://img.shields.io/github/languages/code-size/pynickle/amazing-python.svg)](https://github.com/pynickle/amazing-python)

  --------------------- -----------------------------------------------------------------------------------------------------------------------
  **Travis CI**         .. image:: <https://travis-ci.org/pynickle/amazing-python.svg?branch=master>
                        :target: <https://travis-ci.org/pynickle/amazing-python>
  ===================   ==========
  **Azure Pipelines**   .. image:: <https://dev.azure.com/2330458484/2330458484/_apis/build/status/pynickle.amazing-python?branchName=master>
                        :target: <https://github.com/pynickle/amazing-python>
  --------------------- -----------------------------------------------------------------------------------------------------------------------

Contents
--------

[requirements.txt](),
[Pull\_Requests\_Template](https://github.com/pynickle/amazing-python/blob/master/.github/PULL_REQUESTS_TEMPLATE.md),
[Python\_Use](), [study\_program](), [interesting\_program]()

[what\_the\_fuck](), [pip\_update](), [scrapy\_images](),
[translate\_app](), [zip\_to\_see]()

[how\_many\_code](), [beautify\_code](), [pyinstaller\_all](),
[voice\_picture](), [test]()

[pyaudio](), [command\_to\_code](), [auto\_copyright](), [bilibili](),
[remove]()

[equation\_solver](), [pip\_install]()

Usage
-----

requirements.txt
----------------

这个项目需要用到的所有第三方库，用:

    pip install -r requirements.txt

安装所有第三方库，pyaudio库由于会安装失败，请自行到
[pyaudio-install](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
下载

------------------------------------------------------------------------

Pull\_Requests\_Template
------------------------

*用于pull requests的模板文档*

------------------------------------------------------------------------

Python\_Use
-----------

*Python的框架和它们的网站整理*

-   web-development
-   web-spider
-   data-analysis
-   artificial-intelligence
-   data-visualization
-   picture
-   game
-   internet
-   send-email
-   audio
-   GUI programming
-   environmental isolation
-   python2-3
-   python-shell
-   code-quality
-   python and c

------------------------------------------------------------------------

study\_program
--------------

*通过程序学习python及其高极用法*

这里面的book文件夹则是我对这些知识的解析。

**-- written by me**

------------------------------------------------------------------------

interesting\_program
--------------------

*可以用来练手或有用的的小型python程序*

------------------------------------------------------------------------

what\_the\_fuck
---------------

*为wtfpython所启发，收集各种令人难以理解的输出并给予好玩而微妙的注释*

------------------------------------------------------------------------

pip\_update
-----------

*使用pip库一键升级python第三方库*

no thread的文件代表不使用redis数据库，在速度方面会慢一些。

而with
thread使用redis数据库，在使用前请自行查询相关教程安装好redis！首先运行一遍主程序（注意，只运行一遍！）。然后在多个命令行里运行slave1.py，然后等待完成。

------------------------------------------------------------------------

scrapy\_images
--------------

*抓取任意网站图片并保存到指定路径*

你可以制定抓取网址，存储位置和存储格式。

------------------------------------------------------------------------

translate\_app
--------------

*多种方式翻译你的文本*

目前已发布到pypi上，可以使用如下命令下载:

    pip install quicktranslate

使用方式如下:

    trans -t example

------------------------------------------------------------------------

zip\_to\_see
------------

*快速解压zip文件*

选择zip文件并按下按钮，该文件会被解压到当前目录下

------------------------------------------------------------------------

how\_many\_code
---------------

*计算路径下你曾经写过多少python代码*

输入路径，程序会输出每个文件的注释行数，空行数和代码行数以及总的数据。

------------------------------------------------------------------------

beautify\_code
--------------

*使用gofmt（格式化go代码），autopep8或black格式化你的代码，目前支持自定义参数*

**自定义参数规则如下**:

    file_type ** parameters_run

file\_type代表文件类型，示例：.py .go

parameters\_run代表你要执行的命令，其中可以包括两个变量，他们用{{
}}包裹： - root ： 代表你输入的文件路径 - file ： 代表该路径下的所有文件

file\_type和parameters\_run用 \*\* 分割

一个示例自定义参数如下:

    .py ** autopep8 --in-place -a {{root}}/{{file}}

------------------------------------------------------------------------

pyinstaller\_all
----------------

*批量以-F开启时使用pyinstaller打包文件并自动删除冗余文件，也可删除路径下所有exe文件*

目前已发布到pypi上，可以使用如下方式下载:

    pip install quickpack

如下方式使用:

    pack -r -p path

-r代表在打包前去除所有exe文件。

**注意，带tkinter的已经停止维护，以命令行使用为最新版本**

------------------------------------------------------------------------

voice\_picture
--------------

*音频可视化每一帧，以图片形式更清晰*

------------------------------------------------------------------------

test
----

*用cProfile测试你的代码并将结果写入csv文件*

------------------------------------------------------------------------

pyaudio
-------

*录音并保存到文件，也可播放*

可以选择秒数，文件名，按下按钮开始。保存到当前目录，也可以使用下面的按钮直接回收。

------------------------------------------------------------------------

command\_to\_code
-----------------

*将python命令行转换为可运行的python代码*

目前已发布置我的GitHub pages，网址为:

    https://code-nick-python.github.io/ctc.html

左边的输入框用来输入命令行，右边会实时显现出转换后的代码

------------------------------------------------------------------------

auto\_copyright
---------------

*自动为你的作品加上版权说明*

目前已支持配置文件，json格式配置文件说明如下:

    {
        //必备参数，否则在程序中输入
        path: "遍历路径",
        title: "标题",
        license: "许可证",
        year: "年份",
        owner: "拥有者",
        //可选参数，也可以在程序中输入
        description: "描述",
        cversion: "版本号",
        update: "更新时间",
        file: "文件名"
    }

参数说明与上面一样，配置文件选择为:

    --config "config file path"

------------------------------------------------------------------------

bilibili
--------

*爬取bilibili弹幕并制作爱心词云*

av获取方式如下，如果bilibili视频网址为:

    https://www.bilibili.com/video/av57841919?from=search&seid=6703067031502678934

则av为57841919，输入即可

------------------------------------------------------------------------

remove
------

*移除目录下所有已某个后缀结尾的文件*

实例：

file\_path(-p, --path) : xxx file\_type(-t, --type) : class

------------------------------------------------------------------------

equation\_solver
----------------

*算出方程的所有根*

目前支持：

-   一元二次方程
-   一元一次方程

参数说明：

-   -q, --quadratic: **输入一元二次方程**
-   -d, --dimensional: **输入一元一次方程**
-   abc
    -   -aq, --quadratic: **输入一元二次方程三个参数**
    -   -ad, --dimensional: **输入一元一次方程二个参数**

------------------------------------------------------------------------

po\_operation
-------------

*po文件操作*

-   generate\_po.py: 用来根据rst文件生成po文件
-   get\_po.py: 解析po文件并将翻译写入文档

------------------------------------------------------------------------

pip\_install
------------

*使用镜像下载包*

帮助:

    usage: pipi.py [-h] [-p PACKAGE] [-a | -k | -d | -q | -j]

    使用镜像下载python第三方库

    optional arguments:
    -h, --help            show this help message and exit
    -p PACKAGE, --package PACKAGE
                            你想要下载的库
    -a, --aliyun          使用阿里云镜像
    -k, --keji            使用中国科技大学镜像
    -d, --douban          使用豆瓣镜像
    -q, --qinghua         使用清华大学镜像
    -j, --jishu           使用中国科学技术大学镜像

------------------------------------------------------------------------

english\_word
-------------

*背单词的网站*

网站地址：https://cishen.herokuapp.com

### How to contribute

1.  **Fork the repository to your own repository**
2.  **Commit your code in your fork repository**
3.  **Change the document accordingly**
4.  **Use the document**
    [Pull\_Requests\_Template](https://github.com/pynickle/amazing-python/blob/master/.github/PULL_REQUESTS_TEMPLATE.md)
    **to pull requests**

**PS : If you have any good idea, welcome talk and pull requests!**

------------------------------------------------------------------------

License
-------

author : **pynickle**

license :

*FOR STUDY PROGRAM(EXCEPT BOOK FOLDER), INTERESTING PROGRAM AND WHAT THE
FUCK:*

**WTFPL License**

*FOR BOOK FOLDER:*

**BSD-2-Clause License**

*FOR ELSE:*

**MIT License**

下载science文库中的一些书的图片然后生成pdf，导入了书签。

下载仅需要书的主页面
<img src="README.assets/image-20220318002845878.png" alt="image-20220318002845878" style="zoom: 25%;" />

>网络上东拼西凑 俺不会python
>
>当使用python运行时，请手动创建两层目录
>
>>  python文件位于第二层目录
>>
>> 以免下载的文件不好找（生成的exe有两层目录，就写了 放到第一层目录了）
>>
>> 

# 注意

如果程序闪退

​	解决方案有：

1. 确保输入书籍页面网址正确
2. 进入书籍的阅读页面后重试
3. 留言或私信（哔哩哔哩）



# 前言：



程序的使用优先级 userId_and_defid 

>exe启动很慢。。。。。。 无内容显示时可以键入任意键 但不要按回车
>
>第一次启动exe可能会报错 
>
>也有可能会报毒。报毒原因不清。
>
>~~导入的目录标题分级可能会有错误，但是页码绝对正确，（完全正确的有空在搞）~~目录已分级
>
>如果网络正常 输入网址正确  可能是bug 也可能不可以下载了

可能出现的问题：

1. 下载的书籍如果同名，请将已下载的前一册文件夹删除或重命名，生成的pdf移走或重命名。

2. 

   1. 如果浏览器的阅读界面出现下图

      ![image-20220411203812899](README.assets/image-20220411203812899.png)

      请刷新界面。（似乎当下载的页数与你浏览器中当前查看的页数相近时，下载的成功率会更高）

3. 重新下载不要慌，当全部文件正确下载，完成后就会退出。

4. 如果程序报错请留言（将测试 是否了可以解决，如无法解决，将告知）。

   



# 程序位置：

> 在相对应的文件夹下有exe文件可以运行, 最好为其新建快捷方式，放在易寻处。
>
> **userId_and_defid**
>
> ![image-20220318202806202](README.assets/image-20220318202806202.png)
>
> > 如果出现**userId_and_defid**无法下载并且访问书籍的阅读页面会出现下图情形。请使用**uuid_download**尝试
> >
> > ![image-20220325224307028](README.assets/image-20220325224307028.png)
>
> 
>
> 
>
> **usecookie**
>
> ![image-20220318202934110](README.assets/image-20220318202934110.png)
>
> 

# 下载书籍的位置

![image-20220319150950504](README.assets/image-20220319150950504.png)

<font color='red'>如果下载书籍图片一直失败（如图标红）可以等待程序继续运行，下载完成后会有失败的下载将会重下。</font>

![image-20220319151146481](README.assets/image-20220319151146481.png)

# 运行userId_and_bookdefid.exe准备环境

1. 科学文库书籍主页 （见最后的备注）
2. 需打开至阅读页面后运行程序



# 运行usecookie.exe需要准备环境

1. 安装火狐浏览器 并且安装位置为C:\Program Files\Mozilla Firefox

2. geckodriver.exe 位置放在火狐浏览器的安装位置（C:\Program Files\Mozilla Firefox\geckodriver.exe）网盘文件夹firefox下有geckodriver.exe压缩包

3. 调用火狐浏览器时，会运行火狐浏览器，访问下载书籍的阅读页面获取用户cookie切勿关闭！

4. 运行：1. 点击运行；2.在程序所在文件夹显示路径键入cmd回车，跳出cmd终端 。在终端，输入程序首字母，按table键。（回车运行）

   >![image-20220318103431804](README.assets/image-20220318103431804.png)
   >
   >![image-20220318103824438](README.assets/image-20220318103824438.png)
   >
   >



# py代码

## 准备环境

> cookie因该是cookie.js生成  但是不懂啊不懂，不会啊不会。不用浏览器类浏览器，可以用其他方式获取吗



>使用的库有
>
>import os
>
>import wget,os,random
>from time import sleep
>
>from time import time
>from selenium import webdriver
>import pickle
>
>import urllib.request
>from bs4 import BeautifulSoup
>import requests
>import jsonsearch
>import json
>import sys
>
>import re
>
>from PyPDF2 import PdfFileReader as pdf_read, PdfFileWriter as pdf_write



- python main.py





# 运行页面



![image-20220318003715725](README.assets/image-20220318003715725.png)

- 输入书籍主页 回车

<img src="README.assets/image-20220318003252643.png" alt="image-20220318003252643" style="zoom:50%;" />

- 开始响应

<img src="README.assets/image-20220318003434192.png" alt="image-20220318003434192" style="zoom:80%;" />



# 备注：

## 书籍的网址，书籍主页类似于下图

<img src="README.assets/image-20220318002845878.png" alt="image-20220318002845878" style="zoom: 25%;" />



## 操作步骤截图：

- ### 书籍的主页面点击阅读

![image-20220325225040241](README.assets/image-20220325225040241.png)









## 重新获取cookie：

需要安装火狐浏览器（因为代码使用了火狐浏览器）

安装位置为默认安装位置 有关代码在py目录下的default_userCookieVal.py第30行 ，geckodriver.exe 在firefox文件夹下

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 01:33:16 2022

@author: MeiYouDYC
"""
from py.book import *
from py.download import *
from py.default_userCookieVal import *
#from py.directory import *
from py.chulimulu import *
from py.creatPDF import *
import os
from time import sleep
from py.ml import *

if __name__=='__main__':
    print('请输入科学文库书籍的介绍页面')
    url=input('类似于这个链接的样子：https://book.sciencereading.cn/shop/book/Booksimple/show.do?id=BB4EB124D2A72B4DBE053020B0A0A860E000\n打开链接访问看看~\n')
    parent=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
    os.chdir(parent)
    
    pwd=os.getcwd();
    print(pwd)
    cookiesDir=pwd +'\\cookies\\'
    #获取book的id和用户cookie
    bookId_cookie=bookIdAndDefault_userCookieVal(cookiesDir, url)
    
    #发送book的id和cookie 返回下载地址的特殊book标识idNum 
    Book=book(bookId_cookie.id, bookId_cookie.cookie)
    
    bookDir=pwd+'\\'+Book.name+'\\'
    #使用idNum 去下载每一页的png文件 
    #此时的目录在以bookname命名的文件夹下
    download(Book.idNum, Book.name, Book.page)
    
    #将下载的图片合成一个pdf
    creatPdf(Book.name)
    
    #使用用户的cookie和book id 下载book的目录
    #dire=directory(bookId_cookie.get_cookie(),Book.id,Book.name)
     dire=ml.ml(Book.idNum, Book.name)
    
    
    #将下载的目录格式化 并且打入目录
    muluchuli(bookDir, Book.name,dire.ml)
    
    sleep(100)
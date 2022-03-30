# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:58:02 2022

@author: MeiYouDYC

uuid_downlaod.py
"""



from py.bookUuid import *
from py.download import *
#from py.directory import *
from py.chulimulu import *
from py.creatPDF import *
from time import sleep
from py.ml import *

if __name__ == '__main__':
    print('书籍主页类似于(打开链接查看一下)：https://book.sciencereading.cn/shop/book/Booksimple/show.do?id=BB4EB124D2A72B4DBE053020B0A0A860E000')
    print('!!!注意链接最后不要含有    #')
    url=input('请输入科学文库书籍主页:')
    bookId=url[63:]
    # bookdefid=(input('请输入defid'))
    book=book()
    book.id=bookId
    
    # bookdefid=(input('请输入defid'))
    uuid=input('uuid(uuid请查看README.PDF):')
   
    book.idNum=uuid
    book.page=book.bookPages()
    book.name=book.bookName()
    parent=path.abspath(path.join(path.dirname("__file__"),path.pardir))
    chdir(parent)
    
    pwd=getcwd();
    print(pwd)
    # page=(input('请输入页数'))
    # download.download(book.idNum, book.id, book.page)
    
    bookDir=pwd+'\\'+book.name+'\\'
    #使用idNum 去下载每一页的png文件 
    #此时的目录在以bookname命名的文件夹下
    download(book.idNum, book.name, book.page)
    
    #将下载的图片合成一个pdf
    creatPdf(book.name)
    
    
    #使用用户的cookie和book id 下载book的目录
    #dire=directory('',bookId,book.name)
    dire=ml(book.idNum, book.name)
    
    
    #将下载的目录格式化 并且打入目录
    muluchuli(bookDir, book.name,dire.ml)
    sleep(10)
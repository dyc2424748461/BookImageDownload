# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 23:36:18 2022

@author: MeiYouDYC
book.py
"""


import urllib.request
from bs4 import BeautifulSoup
import requests
import jsonsearch
import json
import sys
from time import sleep


class book:
    id=str()
    idNum=str()
    name=str()
    page=int()
    cookie=str()
    def __init__(self):
        self.id=''
        self.idNum=''
        self.name=''
        self.page=''
        
        
        
    
    
    # def __init__(self,id,cookie):

    #     self.id=id
    #     self.cookie=cookie
    #     # def 
    #     self.idNum=self.getIdNum()
        
    #     self.name=self.bookName()
        
    #     self.page=self.bookPages()
    #     self.createTxt()
        



    def getIdNum(self):
        #readurl = 'https://book.sciencereading.cn/shop/book/Booksimple/onlineRead.do?id=B001CCEA30DC346C2839439559EB8C6EB000&readMark=0'
        # try:
        #     indexStr = readUrl.index('=')
        #     idNum0=readUrl[indexStr+1:]
        # except Exception as e:
        #     print(e.args)
        #     print('输入的网址有误')
        #     sys.exit(1)
        # # print(type(idNum0))
        # print('bookId='+idNum0)
        
    
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accessToken': 'accessToken',
            'Origin': 'https://book.sciencereading.cn',
            'Connection': 'keep-alive',
            'Referer': 'https://book.sciencereading.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }
        tmpid=self.id
        userId=self.cookie
        # print(type(userId))
        print("userID:"+userId)
        data = {
          'params': '{"params":{"userName":"Guest","userId":"'+userId+'","file":"http://159.226.241.32:81/'+tmpid+'.pdf"}}',
          'type': 'http'
        }
        #print(data)
        try:
            response = requests.post('https://wkobwp.sciencereading.cn/api/file/add', headers=headers, data=data)
            defId=response.text[11:-2]
           
        except Exception as e:
            print('*'*20)
            print (e.args)
            print('*'*20)
            print('网络错误')
            sys.exit(0)
        print("书籍的特殊标识："+defId)
        return defId
    
    
    
        
    #获取书籍的页数
    def bookPages(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'accessToken': 'accessToken',
            'x-auth-doc': '',
            'Origin': 'https://book.sciencereading.cn',
            'Connection': 'keep-alive',
            'Referer': 'https://book.sciencereading.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }
        
        params = (
            ('language', 'zh-CN'),
        )
        getPagesUrl='https://wkobwp.sciencereading.cn/asserts/'+self.idNum+'/manifest'
        response = requests.get(getPagesUrl, headers=headers, params=params)
        # print(response)
        # print(type(response))
        # result=ast.literal_eval(response.text)
        # print(type(result))
        # print(result['docinfo'])
        args=json.loads(response.text)
        jsondata = jsonsearch.JsonSearch(object=args, mode='j')    
        keyValue=jsondata.search_first_value(key='docinfo') 
        # print(keyValue)
        sleep(3)
        txt = json.loads(str(keyValue))
        # print(txt)
        # print(type(txt))
        book_page=txt['PageCount']
        print("bookpage="+str(book_page))
        return book_page
    
    
    def bookName(self):
        url="https://book.sciencereading.cn/shop/book/Booksimple/show.do?id="+ self.id
        req=urllib.request.Request(url)
        resp=urllib.request.urlopen(req)
        data=resp.read().decode('utf-8')
        soup = BeautifulSoup(data,'html.parser')
        print("BookName："+soup.title.string)
        sleep(2)
        return soup.title.string
    
    def createTxt(self):
        f=open(self.name+'.html','w')
        url="https://book.sciencereading.cn/shop/book/Booksimple/show.do?id="+self.id
        html='<meta http-equiv="refresh" content="1;url="'+url+'">'
        f.write(html)
        f.close()
    

if __name__=='__main__':
    url=input('请输入科学文库书籍主页:')
    bookId=url[63:]
    book1=book()
    book1.id=bookId
    book1.idNum=input('uuid')
    print(book1.name)
    print(book1.page)


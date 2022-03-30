# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:13:22 2022

@author: MeiYouDYC
"""
"""

https://blog.csdn.net/qq_41248959/article/details/110081876
"""
#获取目录
import pickle
import requests
import re
import json
#下载目录
class directory:
    def __init__(self,cookies,bookid,bookName):
        self.cookies=cookies
        self.bookid=bookid
        self.bookName=bookName
        self.ml=self.bookName+'.ml'
        self.writeML(self.getDir())
        
        
    def getDir(self):
        # cookies = {
        #     'pgv_pvid': '9466411227',
        #     'default_user': '0a63229aa6494315950934262961e9aa',
        #     'JSESSIONID': '8B75ADF616FF6EAAB6CB09B38D14CAB9',
        #     '__qc_wId': '769',
        # }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://book.sciencereading.cn/shop/main/Login/shopFrame.do',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        }
        # https://book.sciencereading.cn/shop/book/Booksimple/show.do?id=B6A85EB385E694D64A4DA05116247FF63000
        params = (
            ('id', ''+self.bookid+''),
        )
        
        response = requests.get('https://book.sciencereading.cn/shop/book/Booksimple/show.do', headers=headers, params=params, cookies=self.cookies)
        # filename=self.bookName;
        dic=re.findall('var zNodes=(.*);\r\n',response.text)
        test=json.loads(str(dic[0]))#将获取的目录信息
        # print('test='+test)
        return test
    # for i in test:
        
        
    # f=open(filename,'wb')
    # pickle.dump(response.text, f)
    # f.close()
    #截取url中 书的页数
    def getPage(self,url):
        num=-1
        for i in range(5):
            if(url[num-1]=='='):
                return url[num:]
            else :
                num=num-1
            
    
    # with open(filename, 'rb+') as f:
    #     d = pickle.load(f)
    #     # print(d)
    #将list 目录 获取有用信息
    def directory(self,test):
        direList=list()
        for i in test:
            name=i['name']
            # print(self.getPage(i['url']))
            page=self.getPage(i['url'])
            direList.append(name+' '+str(page))
            
        return direList
    
    #将目录写入文件
    def writeML(self,test):
        m=self.directory(test)
        # m=test
        f=open(self.ml,'w')
        for i in m:
            f.write(i+'\n')
        f.close()
            
    
    
# if __name__=='__main__':
    
    
    # def 
#/html/body/script[14]
# zNodes
# dic=re.findall('var zNodes=(.*);\r\n',response.text)

# json.loads(re.findall('var cities = (.+);\n', response.body.decode('utf-8'))[0])
#
# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.get('https://book.sciencereading.cn/shop/book/Booksimple/show.do?id=B6239E7721BCA413DB3A13E07A3922AC5000', headers=headers, cookies=cookies)


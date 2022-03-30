# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:35:13 2022

@author: MeiYouDYC
dir
"""
from requests import get 
from json import loads

class ml:
    def __init__(self,bookIdNum,bookname):
        self.bookname=bookname
        self.ml=self.bookname+'.ml'
        self.bookIdNum=bookIdNum
        self.creatML()
    
    def creatML(self):
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
        
        params = {
            'formMode': 'true',
        }
        
        response = get('https://wkobwp.sciencereading.cn/asserts/'+self.bookIdNum+'/bookmarks', headers=headers, params=params)
        dirc = loads(loads(response.text)['BookmarkInfo'])['bmks']
        dirc = list(dirc)
        f=open(self.bookname+'.ml','w')
        #计算标题的级别
        tmp = dict()
        tmp.update({0:0})
        for i in dirc:
            cur=i['cur']#第多少个目录
            parent=i['parent']#父节点的cur
            m=tmp.get(parent)
            tmp.update({cur:m+1})#添加级别
            p=i['dest']['p']+1
            ttl=i['ttl']
            ts='\t'*m 
            title=ts + ttl +' $'+str(p)
            #写入文件
            
            
            f.write(title+'\n')
        f.close()
    #print(title)
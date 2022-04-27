# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 23:36:18 2022

@author: MeiYouDYC
"""



from urllib.request import Request
from urllib.request import urlopen
from requests import post,get

from bs4 import BeautifulSoup

from jsonsearch import JsonSearch
from json import loads
from sys import exit
from time import sleep
from re import sub


class book:
    id=str()
    idNum=str()
    name=str()
    page=int()
    cookie=str()
    def __init__(self,id,cookie):

        self.id=id
        self.cookie=cookie
        # def 
        self.idNum=self.getIdNum()
        self.page=self.bookPages()
        self.name=self.bookName()
        self.createTxt()


#获取takeid-》uuid
    def outsizeGetUuid(self):
        #获取takeid
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accessToken': 'accessToken',
            'Origin': 'https://book.sciencereading.cn',
            'Connection': 'keep-alive',
            'Referer': 'https://book.sciencereading.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }
        
        
        data = {
            'filetype': 'http',
            'zooms': '-1,100',
            'tileRender': 'false',
            'fileuri': '{"params":{"userName":"Guest","userId":"","file":"http://159.226.241.32:81/'+self.id+'.pdf"}}',
            'pdfcache': 'true',
            'callback': '',
        }
        
        response = post('https://wkobwp.sciencereading.cn/spi/v2/doc/pretreat', headers=headers, data=data)
        ##使用list去读取json
        dirc = loads(response.text)

        taskid=dirc['resultBody']['taskid']
        geUuidUrl='https://wkobwp.sciencereading.cn/api/v2/task/'+taskid+'/query'
        
        

        ##获取uuid

         ###预处理一下连接 提高成功率
         
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://book.sciencereading.cn/shop/book/Booksimple/show.do?id='+self.id+'',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        }
        
        params = (
            ('id', self.id),
            ('readMark', '0'),
        )
        
        response = get('https://book.sciencereading.cn/shop/book/Booksimple/onlineRead.do', headers=headers, params=params)


        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'accessToken': 'accessToken',
            'Origin': 'https://book.sciencereading.cn',
            'Connection': 'keep-alive',
            'Referer': 'https://book.sciencereading.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }
        

        url='https://wkobwp.sciencereading.cn/api/v2/task/'+taskid+'/query'


        response = get(url, headers)
        dirc1 = loads(response.text)
        tmp=list(dirc1['resultBody'])
        while(tmp[0]!='docid'):
            sleep(3)
            response = get(url, headers)
            dirc1 = loads(response.text)
            tmp=list(dirc1['resultBody'])
        
        uuid=dirc1['resultBody']['uuid']
        
           
            #response = get(url, headers)
        print("uuid",uuid)
        return uuid 
        
                
        
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
            response = post('https://wkobwp.sciencereading.cn/api/file/add', headers=headers, data=data)
            
            dirc = loads(response.text)

            uuid=dirc['result']
            defId=uuid
            if(defId=='OutOfFileSizeLimit'):
                return self.outsizeGetUuid()
            #defId=response.text[11:-2]
           
        except Exception as e:
            print('*'*20)
            print (e.with_traceback())
            print('*'*20)
            print('网络错误')
            exit(0)
        print("书籍的特殊标识（uuid）："+defId)
        return defId
    
    
    
        
    #获取书籍的页数
    def bookPages(self):
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'accessToken': 'accessToken',
            'Origin': 'https://book.sciencereading.cn',
            'Connection': 'keep-alive',
            'Referer': 'https://book.sciencereading.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
        }
        
        params1 = (
            ('fileId', self.idNum),
        )
        
        response1 = get('https://wkobwp.sciencereading.cn/api/file/info', headers=headers, params=params1)
                
        
        params = (
            ('language', 'zh-CN'),
        )
        getPagesUrl='https://wkobwp.sciencereading.cn/asserts/'+self.idNum+'/manifest'
        response = get(getPagesUrl, headers=headers, params=params)
        # print(response)
        # print(type(response))
        # result=ast.literal_eval(response.text)
        # print(type(result))
        # print(result['docinfo'])
        args=loads(response.text)
        while(args['error']!=0):
            response1 = get('https://wkobwp.sciencereading.cn/api/file/info', headers=headers, params=params1)
            sleep(3)
            response = get(getPagesUrl, headers=headers, params=params)
            args=loads(response.text)
            # print(response.text)
        
        jsondata = JsonSearch(object=args, mode='j')    
        
        
        
        
        keyValue=jsondata.search_first_value(key='docinfo') 
        # print(keyValue)
        txt = loads(str(keyValue))
        # print(txt)
        # print(type(txt))
        book_page=txt['PageCount']
        print("bookpage="+str(book_page))
        return book_page
    
    
    def bookName(self):
        url="https://book.sciencereading.cn/shop/book/Booksimple/show.do?id="+ self.id
        req=Request(url)
        resp=urlopen(req)
        data=resp.read().decode('utf-8')
        soup = BeautifulSoup(data,'html.parser')
        print("BookName："+soup.title.string)
         #将bookname中含有特殊字符替换成“-”，以便建文件夹
        EPunctuation='\\\\/:*?"<>|'
        name=sub('[{}]'.format(EPunctuation),'-',soup.title.string)
        # print('name:'+str(type(name)))
        return name
    
    def createTxt(self):
        f=open(self.name+'.html','w')
        url="https://book.sciencereading.cn/shop/book/Booksimple/show.do?id="+self.id
        html='<meta http-equiv="refresh" content="1;url="'+url+'">'
        f.write(html)
        f.close()
    

if __name__=='__main__':
    #https://book.sciencereading.cn/shop/book/Booksimple/show.do?id=B6094AD96CD3A907CE053010B0A0A87DE000
    inputUrl='https://book.sciencereading.cn/shop/book/Booksimple/show.do?id=B58A6236D81858334E053020B0A0A3528000'
    # bookId='B58A6236D81858334E053020B0A0A3528000'
    bookId='B6094AD96CD3A907CE053010B0A0A87DE000'
    test=book(bookId, '')
    print(test.idNum)
    #print(test.page)
    

    



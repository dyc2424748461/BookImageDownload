# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 23:36:18 2022

@author: MeiYouDYC
"""


import urllib.request
from bs4 import BeautifulSoup
import requests
import jsonsearch
import json
import sys



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
        return soup.title.string
    
    def createTxt(self):
        f=open(self.name+'.html','w')
        url="https://book.sciencereading.cn/shop/book/Booksimple/show.do?id="+self.id
        html='<meta http-equiv="refresh" content="1;url="'+url+'">'
        f.write(html)
        f.close()
    


    

    
    
# class default_userCookieVal:
#     id=str()
#     cookie=str()
#     def __init__(self,id):
#         self.id=id
#         self.cookie=self.get_cookie_Default_user()
        
        
#         #从文件中获取 cookie
#     def get_cookie_from_cache():
    
#         cookie_dict = {}
        
    
#         for parent, dirnames, filenames in os.walk('./'):
        
#             for filename in filenames:
            
#                 if filename.endswith('.cookies'):
                    
                
#                     print('cookie\'s filename:\t'+filename)
        
#                     with open(filename, 'rb+') as f:
        
#                         d = pickle.load(f)
        
#                         if d.__contains__('name') and d.__contains__('value') and d.__contains__('expiry'):
        
#                             expiry_date = int(d['expiry'])
        
#                             if expiry_date > (int)(time()):
        
#                                 cookie_dict[d['name']] = d['value']
        
#                             else:
        
#                                 return {}
#             # if(check!=True):
#             #     return get_cookie_from_network();
                    
        
#         return cookie_dict
    
    
#     #若缓存cookie过期，则再次从网络获取cookie
    
#     def get_cookie():
    
#         cookie_dict = default_userCookieVal.get_cookie_from_cache()
        
#         if not cookie_dict: 
        
#             cookie_dict = default_userCookieVal.get_cookie_from_network()
        
#         return cookie_dict
    
    
#     def get_cookie_Default_user():
#         cooke=default_userCookieVal.get_cookie()
#         print('default_user value:')
#         print('defalut_user:'+cooke.get('default_user'))
#         m=cooke.get('default_user')
#         return m

#     # cookie=get_cookie_Default_user()
        
        
        
        
        
        
# class download:
    
#     def __init__(self,idNum=book.idNum,page=book.page):
#         self.page=page
#         self.idNum=idNum
       
        
#     falseList=list()
        
        
        
        
#     def init():

#         # named a exchange name 
#         # mkdir a folder 
#         try:
#             folder= book.name
#             isExists=os.path.exists(folder)
#             #print(isExists)
#             if not isExists:
#                 os.mkdir(folder)
#         except:
#                print("network or fileOs occured error")
#                sys.exit (0)
            
#         #chang dir to ./png
#         pwd=os.getcwd()+'\\'+ folder
#         print(pwd)
#         os.chdir(pwd)
#         return pwd

#        #create a url
# #this url need you to change
#     def url(num):
#         url = ('https://wkobwp.sciencereading.cn/asserts/'
#                +download.idNum
#                +'/image/'
#                +str(num)
#                +'/100?accessToken=accessToken&formMode=true')
#         print('正在下载第\t'+str(num+1)+'\t页')
#         return url
 


#     def downloadPng(page):
#         #download by wget
#         for i in range(page):
#             filename = str(i)+'.png'
#             #print(os.path.exists(filename))
#             #os.path.exists(pwd)
#             '''
            
#             '''
#             if os.path.exists(filename):
#                 print(str(i+1)+'\t页已存在')
#                 continue
#             else:
#                 download.downloadOne(i, filename)
            
# #单个下载
#     def downloadOne(pageNum,AFilename):
#         try:
#             wget.detect_filename(AFilename)
#             wget.download(download.url(pageNum),out=AFilename)
#             sleep(random.randint(3, 5))
#         except:
#             print("when downloaded the page" +str(pageNum+1)+"\t error occured")
#             sleep(3)
#             download.falseList.append(pageNum)
            
#     def check():
#         tmpCheck = False
#         #print(os.listdir())
#         for checkfile in os.listdir():
#             orderNum = checkfile.split('.')[0]
#             if(os.path.getsize(checkfile)<=2048):
#                 print(checkfile+'\twill be removed')
#                 download.falseList.append(int(orderNum))
#                 print(orderNum)
#                 os.remove(checkfile)
#                 tmpCheck=True
#         return tmpCheck
        
#     def download():
#         n=5
#         init()
#         while(n>0):
#             n=5
#             try:
#                 #page=bookPages()
#                 page = bookPages()
#                 downloadPng(page)
#                 if(check()):
#                     while(len(falseList)!=0):
#                         for j in falseList:
#                             falseName=str(j)+'.png'
#                             downloadOne(j, falseName)
#                             if(os.path.getsize(falseName)>2048):
#                                 falseList.remove(j)
#                                 print("第"+str(j+1)+"页已重下")
#                             else:
#                                 print(str(j+1)+"\t下载失败，将稍后重试")
#                 print(bookNameString)
#                 print('Number of pages of the book:'+ str(page))
#                 print("下载完成啦~~~尽情享用")
#                 n=0
#             # except Exception as e:
#             #     print(e.args)
#             #     print("some error occured,will try again!\t"+str(n)+'')
#             #     n=n-1
#             #     sleep(5)
#         # print(type(123))
#             #downloadPng(page)
    
    
    
    
    
    
    
    
    
    
    
# if __name__ == '__main__':


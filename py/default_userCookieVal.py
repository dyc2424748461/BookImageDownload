# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 01:06:20 2022

@author: MeiYouDYC
"""
import os
from time import time
from selenium import webdriver
import pickle

class bookIdAndDefault_userCookieVal:
    id=str()
    cookie=str()
    cookiesdir=str()
    def __init__(self,pwdcookie,url):

        self.cookiesdir = pwdcookie
        if not os.path.exists(self.cookiesdir):
            os.mkdir(self.cookiesdir)
        self.url=url
        indexStr = url.index('=')
        self.id=url[indexStr+1:]
        self.cookie=self.get_cookie_Default_user()
        
        
        
    def get_cookie_from_network(self):
    
        path="C:\Program Files\Mozilla Firefox\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=path)
        # indexStr = url.index('=')
        # bookIdtmp= url[indexStr+1:]
        url="https://book.sciencereading.cn/shop/book/Booksimple/onlineRead.do?id="+self.id+"&readMark=0"
        
        driver.get(url)
        #get cookie
        cookie_list=driver.get_cookies();
        cookie_dict = {}

        #print(isExists)
        for cookie in cookie_list:
    
        #写入文件
        
            f = open(self.cookiesdir+cookie['name']+'.cookies','wb')
            
            pickle.dump(cookie, f)
            
            f.close()
            
            if cookie.__contains__('name') and cookie.__contains__('value'):
                cookie_dict[cookie['name']] = cookie['value']   
    ##return cookie_dict
        # print('cookie:')
        # print('*'*20)
        # print(cookie_list)
        # print('*'*20)
        
        return cookie_dict
        

        
        
        
        #从文件中获取 cookie
    def get_cookie_from_cache(self):
    
        cookie_dict = {}
        print(os.getcwd())
    
        for parent, dirnames, filenames in os.walk(self.cookiesdir):
        
            for filename in filenames:
            
                if filename.endswith('.cookies'):
                    
                
                    print('cookie\'s filename:\t'+filename)
        
                    with open(self.cookiesdir+filename, 'rb+') as f:
        
                        d = pickle.load(f)
        
                        if d.__contains__('name') and d.__contains__('value') and d.__contains__('expiry'):
        
                            expiry_date = int(d['expiry'])
        
                            if expiry_date > (int)(time()):
        
                                cookie_dict[d['name']] = d['value']
        
                            else:
        
                                return {}
            # if(check!=True):
            #     return get_cookie_from_network();
                    
        
        return cookie_dict
    
    
    #若缓存cookie过期，则再次从网络获取cookie
    
    def get_cookie(self):
    
        cookie_dict = self.get_cookie_from_cache()
        
        if not cookie_dict: 
        
            cookie_dict = self.get_cookie_from_network()
        
        return cookie_dict
    
    
    def get_cookie_Default_user(self):
        cooke=self.get_cookie()
        # print('default_user value:')
        print('defalut_user:'+cooke.get('default_user'))
        m=cooke.get('default_user')
        return m

    # cookie=get_cookie_Default_user()
    
    
if __name__ == "__main__":
    url="https://book.sciencereading.cn/shop/book/Booksimple/show.do?id=B6A85EB385E694D64A4DA05116247FF63000"
    test=bookIdAndDefault_userCookieVal(url)
    print(test.id+" "+test.cookie)
    
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 01:07:15 2022

@author: MeiYouDYC
"""


from wget import download,detect_filename

from os import path,mkdir,chdir,listdir,remove
from random import randint
from time import sleep
from os import getcwd

#下载 一次性任务
class Download:
    print('下载')
    falseList=list()
    
    def __init__(self,idNum,name,page):
        self.page=page
        self.idNum=idNum
        self.name=name
        self.downloadF()
       
        

        
        
        
        
    def init(self):

        # named a exchange name 
        # mkdir a folder 
        try:
            folder= self.name
            isExists=path.exists(folder)
            #print(isExists)
            if not isExists:
                mkdir(folder)
        except:
               print("network or fileOs occured error")
               exit(0)
            
        #chang dir to ./png
        pwd=getcwd()+'\\'+ folder
        print(pwd)
        chdir(pwd)
        return pwd

       #create a url
#this url need you to change
    def url(self,num):
        urladd = ('https://wkobwp.sciencereading.cn/asserts/'
               +self.idNum
               +'/image/'
               +str(num)
               +'/200?accessToken=accessToken&formMode=true')
        print('正在下载第\t'+str(num+1)+'/'+str(self.page+1)+'页')
        return urladd
 


    def downloadPng(self,page):
        #download by wget
        for i in range(self.page):
            filename = str(i)+'.png'
            #print(os.path.exists(filename))
            #os.path.exists(pwd)
            '''
            
            '''
            if path.exists(filename):
                print(str(i+1)+'\t页已存在')
                continue
            else:
                self.downloadOne(i, filename)
            
#单个下载
    def downloadOne(self,pageNum,AFilename):
        # try:
            detect_filename(AFilename)
            download(self.url(pageNum),out=AFilename)
            sleep(randint(3, 5))
            print()
        # except:
        #     print("when downloaded the page" +str(pageNum+1)+"\t error occured")
        #     sleep(3)
        #     self.falseList.append(pageNum)
            
    def check(self):
        tmpCheck = False
        #print(os.listdir())
        for checkfile in listdir():
            orderNum = checkfile.split('.')[0]
            if(path.getsize(checkfile)<=50 and checkfile.endswith(".png")):
                print(checkfile+'\twill be removed')
                self.falseList.append(int(orderNum))
                print(orderNum)
                remove(checkfile)
                tmpCheck=True
        return tmpCheck
        
    def downloadF(self):
        n=5
        self.init()
        while(n>0):
            # n=5
            try:
                self.downloadPng(self.page)
                if(self.check()):
                    while(len(self.falseList)!=0):
                        for j in self.falseList:
                            falseName=str(j)+'.png'
                            self.downloadOne(j, falseName)
                            if(path.getsize(falseName)>2048):
                                self.falseList.remove(j)
                                print("第"+str(j+1)+"页已重下")
                            else:
                                remove(falseName);
                                print(str(j+1)+"\t下载失败，将稍后重试")
                n=5
                print(self.name)
                print('Number of pages of the book:'+ str(self.page))
                print("下载完成啦~~~尽情享用")
                n=0
            except Exception as e:
                print(e.args)
                print("some error occured,will try again!\t"+str(n)+'')
                n=n-1
                sleep(5)
        # print(type(123))
            #downloadPng(page)
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:48:58 2022

@author: MeiYouDYC

https://zhuanlan.zhihu.com/p/107894786
原文链接：https://blog.csdn.net/qq_41248959/article/details/110081876
"""
#导入书签 一次性任务 可直接修改目录
from os import getcwd,chdir,path
from re import search

class muluchuli:
    def __init__(self,bookdir,bookName,mlName):
        if(bookdir!=getcwd()):
            chdir(bookdir)
        self.bookdir=bookdir
        self.txt=mlName
        self.pdfName=bookName+'.pdf'
        self.bookName=bookName
        self.ml=mlName
        # fin = open(self.ml, "r", encoding='GBK')
        # fout = open('New_'+self.ml, "w")
        # self.init(fin,fout)
        self.inputDirectory()
        
    # def init(self,fin,fout):
    #     for each_line in fin:
    #         list = each_line.split()
    #         for i in range(len(list) - 1): #倒数第一个元素是数字，先不放
    #             index=list[i].split('.')
    #             if(len(index)>1):
    #                  # 第二级目录
    #                 fout.write('\t')
    #                 if(len(index)>2):
    #                  # 第三级目录
    #                     fout.write('\t')
    #                     # 假如还有下级目录，可以继续追加...
    #             #  输出序号
    #             fout.write(list[i])
    #             # 输出空格
    #             fout.write(' ')
    #         # 为书页号置tap位
    #         # fout.write('\t')
    #         fout.write('$')
    #         num = int(list[-1]) + 0 #单独处理倒数第一个数字
    #         fout.write(str(num))#书页号
    #         # 下一行
    #         fout.write("\n")
        
    #     fin.close()
    #     fout.close()
    #     return 0
        
    

    
    def inputDirectory(self):
        from PyPDF2 import PdfFileReader as pdf_read, PdfFileWriter as pdf_write
        pdf_write = pdf_write()
        with open(self.pdfName, 'rb') as f:
            pdf = pdf_read(self.pdfName)
            pages = pdf.getNumPages()
            #将测试用.pdf里面的内容拷贝到pdf_write这个pdf对象中
            for i in range(pages):
                page_1 = pdf.getPage(i)
                pdf_write.addPage(page_1)
        
        directory_list = []
        #读取txt文本中的目录信息(每行作为一个字符串存放到directory_list中)
        with open(self.txt, 'r', encoding='gbk') as f:
            directory_list = f.readlines()
        
        
        #最多支持40级目录层数
        bookmark_list = [None]*40
        #为PDF对象添加书签
        for i,line in enumerate(directory_list):
            if search(r'\S', line):
                #提取书签名称(去掉前面的制表符,去掉$包括后边的页数)
                mark = search(r'\S.*(?=\$)', line).group()
                # print("mark="+mark)
                #提取出书签指向的页数(使用$分隔目录和页数, 你也可以使用其它符号,此时代码应作相应修改)
                page_num_str = search(r'(?<=\$)\d*', line).group()
                page_num_str = page_num_str.rstrip()
                # print(int(page_num_str))
                if(int(page_num_str)):
                    #此处为书签指向的页数增加偏移量(具体的数字取决与pdf文件)
                    page_num = int(page_num_str) + 0 - 1
                    print('正在导入第\t'+str(page_num)+'\t的标题')
                else:
                    page_num = 0
                #计算该目录的级数(四个空格符表示一级)
                num = line.count('\t')
                # print(num)
                #将不同级数的目录名存放在列表中, 添加书签
                if num == 0:
                    bookmark_list[num] =  pdf_write.addBookmark(mark, page_num)
                else:
                    bookmark_list[num] =  pdf_write.addBookmark(mark, page_num, bookmark_list[num-1])
        
        #将添加好书签的pdf对象写入到new.pdf文件中
        with open('..\\New_'+self.pdfName, 'wb') as f:
            pdf_write.write(f)
            
        f.close()
        print('New_'+self.pdfName+'已经导入目录')
        print('pdf文件在：'+path.abspath(path.join(path.dirname("__file__"),path.pardir))+'\\New_'+self.pdfName)



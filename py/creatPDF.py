# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:49:28 2022

@author: MeiYouDYC
"""

#https://blog.csdn.net/weixin_42081389/article/details/100734926

import glob
import os
import fitz  # pip install PyMuPDF
class creatPdf:
    print('合成pdf')
    def __init__(self,bookName):
        print('pdf合成：')
        self.bookName=bookName
        self.pic2pdf('.')
        
    def pic2pdf(self,img_dir):
        doc = fitz.open()
        # for img in sorted(glob.glob("{}/*".format(img_dir))):  # 读取图片，确保按文件名排序
        for img in sorted(glob.glob(os.path.join(img_dir, '*.png')),key=len):
            print(img+'正在添加到pdf中')
            imgdoc = fitz.open(img)  # 打开图片
            pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
            imgpdf = fitz.open("pdf", pdfbytes)
            doc.insertPDF(imgpdf)  # 将当前页插入文档
        if os.path.exists(self.bookName+".pdf"):
            os.remove(self.bookName+".pdf")
        doc.save(self.bookName+".pdf")  # 保存pdf文件
        doc.close()


# if __name__ == '__main__':
#     img_dir = "C:\\Users\\MeiYouDYC\\Desktop\\2021\\Courses\\Python\\作业\\1、2、3！三步搞定物理波动学"
#     pic2pdf(img_dir)

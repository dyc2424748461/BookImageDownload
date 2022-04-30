# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:49:28 2022

@author: MeiYouDYC
"""

#https://blog.csdn.net/weixin_42081389/article/details/100734926
# https://buildmedia.readthedocs.org/media/pdf/pymupdf/latest/pymupdf.pdf

from glob import glob
from os import path,remove
import fitz  # pip install PyMuPDF
class creatPdf:
    print('合成pdf')
    def __init__(self,bookName):
        print('pdf合成：')
        self.bookName=bookName
        img_dir='C:\\Users\\MeiYouDYC\\Desktop\\2022\\stealBookOne-stop(book.sciencereading.cn)\\stealBookOne-stop(book.sciencereading.cn)\\dist\\全球生物安全发展报告（2019年度）'
        self.pic2pdf(img_dir)
        
    def pic2pdf(self,img_dir):
        doc = fitz.open()
        # for img in sorted(glob.glob("{}/*".format(img_dir))):  # 读取图片，确保按文件名排序
        for img in sorted(glob(path.join(img_dir, '*.png')),key=len):
            print(img+'正在添加到pdf中')
            # img=fitz.Pixmap(img).set_dpi(300, 300)
            imgdoc = fitz.open(img) # 打开图片
            #imgdoc = fitz.Pixmap(imgdoc).set_dpi(300, 300)
            pdfbytes = imgdoc.convertToPDF()   # 使用图片创建单页的 PDF
            pdfbytes = imgdoc.tobytes()
            # imgpdf = fitz.open("pdf", pdfbytes)
            imgpdf = fitz.open("pdf", pdfbytes)
            doc.insertPDF(imgpdf)  # 将当前页插入文档
        if path.exists(self.bookName+".pdf"):
            remove(self.bookName+".pdf")
        doc.save(self.bookName+".pdf")  # 保存pdf文件
        doc.close()


if __name__ == '__main__':
    # img_dir = "C:\\Users\\MeiYouDYC\\Desktop\\2021\\Courses\\Python\\作业\\1、2、3！三步搞定物理波动学"
    # img_dir='C:\\Users\\MeiYouDYC\\Desktop\\2022\\stealBookOne-stop(book.sciencereading.cn)\\stealBookOne-stop(book.sciencereading.cn)\\dist\\全球生物安全发展报告（2019年度）'
    creatPdf('test')

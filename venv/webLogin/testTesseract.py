#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: testTesseract.py
@time: 2019/12/31 13:38
@desc:
'''
import os
from PIL import Image
from PIL import ImageEnhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def code_ocr(image):
    """
    灰度化
    :param image:
    :return:
    """
    image = image.convert('L')
    image_con = ImageEnhance.Contrast(image)
    image_en = image_con.enhance(3)
    return image_en

def image_thresholding(image):
    """
    图片二值化处理
    :param image:转灰度处理后的图片文件
    :return: 二值化处理后的图片文件
    """
    # 阈值，控制二值化程度，自行调整（不能超过256）
    pixdata = image.load()
    width, height = image.size
    threshold = sum(image.getdata()) / (width * height)
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return image

image = Image.open(r'D:\Pictures\testknn\1 (2).png')
image = code_ocr(image)
image = image_thresholding(image)
image.show()
print(pytesseract.image_to_string(image))
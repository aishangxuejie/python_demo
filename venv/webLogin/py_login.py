#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: py_login.py
@time: 2019/12/30 14:28
@desc: 自动登陆 -- 垃圾
'''
from selenium import webdriver
from PIL import Image
from PIL import ImageEnhance
from io import BytesIO
from time import sleep
import re
import requests
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
url=r'http://www.sunreal.cn:8023/hbhis'
driver = webdriver.Chrome(executable_path=r'E:\ChromeDrive\chromedriver.exe')
driver.get(url)
sleep(1)
driver.set_window_size(1400,900)
driver.find_element_by_id('userName').clear()
driver.find_element_by_id('userName').send_keys('superman')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('123456')
certCodeUrl = driver.find_element_by_id('certCodeUrl').get_attribute('src')
response = requests.get(certCodeUrl)
# print(certCodeUrl)
image = Image.open(BytesIO(response.content))
image = image.convert('L')
image_con=ImageEnhance.Contrast(image)
image_en=image_con.enhance(4)
image_en.show()
# print(pytesseract.image_to_string(image_en))
certCode = ''
for certCodes in re.findall(r'[0-9a-zA-Z]',pytesseract.image_to_string(image_en)):
    certCode = certCode+certCodes
print(certCode)
driver.find_element_by_id('certCode').send_keys(certCode)
username = driver.find_element_by_id('userName').get_attribute('value')
password = driver.find_element_by_id('password').get_attribute('value')

# print('username:%s;password:%s'%(username,password))
driver.find_element_by_id('dl').click()


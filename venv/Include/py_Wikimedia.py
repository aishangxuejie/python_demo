#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: py_Wikimedia.py
@time: 2020/3/19 15:56
@desc:
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://baike.baidu.com/item/%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91/106382?fr=aladdin")
bsObj = BeautifulSoup(html,features="html.parser")
for link in bsObj.findAll("a"):
    if "href" in link.attrs:
        print(link.attrs['href'])


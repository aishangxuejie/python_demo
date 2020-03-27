#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: py_pachong.py
@time: 2020/3/19 15:29
@desc:
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),features="html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return  None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("not found")
else:
    print(title)

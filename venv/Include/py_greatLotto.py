#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: py_greatLotto.py
@time: 2020/3/19 16:41
@desc:
'''
# http://datachart.500.com/dlt/history/newinc/history.php?start=19001&end=20012
import urllib.request
from urllib.error import HTTPError
from io import BytesIO
import gzip
from bs4 import BeautifulSoup
import json
def gethtml(url):
    try:
        response=urllib.request.urlopen(url).read()
        buff = BytesIO(response)
        files = gzip.GzipFile(fileobj=buff)
        htmls = files.read().decode('utf-8')
        jsonResponse = json.loads(htmls)
    except HTTPError as e:
        return None
    return html
def getbsObj(html):
    try:
        bsObj = BeautifulSoup(html, features="html.parser")
    except AttributeError as e:
        return None
    return bsObj
def showhtml(html):
    print(html)
htmls = gethtml("http://datachart.500.com/dlt/history/newinc/history.php")
gethtml(htmls)

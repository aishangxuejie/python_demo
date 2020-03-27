#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: __init__.py.py
@time: 2020/3/27 13:30
@desc:
'''
import os
os.chdir("E:/apache-tomcat-9.0.8 - 副本/webapps/lwjs/sql/")
path="E:/apache-tomcat-9.0.8 - 副本/webapps/lwjs/sql/"
# 列出当前目录下所有的文件
files = os.listdir()  # 如果path为None，则使用path = '.'
for filename in files:
    portion = os.path.splitext(filename)  # 分离文件名与扩展名
    # 如果后缀是jpg
    if portion[1] == '.sql':
        # 重新组合文件名和后缀名
        newname = portion[0] + '.txt'
        os.rename(os.path.join(path,filename), os.path.join(path,newname))

#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: py_send.py
@time: 2020/3/25 14:51
@desc:
'''
import pyautogui as pygui
pygui.PAUSE = 2.5
pygui.FAILSAFE = True
pygui.num_seconds =2.0
def initQQsize():
    exetitle=pygui.getAllTitles()
    next=0
    for t in exetitle:
        if t=='QQ':
            next=1
    if next==1:
        print(exetitle)
        print(pygui.getWindowsWithTitle('QQ'))
        win = pygui.getWindowsWithTitle('QQ')[0]
        win.moveTo(0, 0)



initQQsize()

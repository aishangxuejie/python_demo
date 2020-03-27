#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: py_test1.py
@time: 2020/3/24 17:30
@desc: https://pyautogui.readthedocs.io/en/latest/quickstart.html
'''
import pyautogui
pos = pyautogui.position()
print(pos)
# size = pyautogui.size();
# print(size)
# x=400
# y=400
# tf = pyautogui.onScreen(x,y)
# print(tf)
# pyautogui.PAUSE = 2.5
# pyautogui.FAILSAFE = True
# num_seconds =10
# pyautogui.moveTo(x, y, duration=num_seconds)
# xOffset=500
# yOffset=500
# pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)
# pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY；如果duration为0或未指定，则立即移动
#
# moveToX=915
# moveToY=1062
# num_of_clicks=1
# secs_between_clicks=1
# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
# pyautogui.click(x=645,y=812,clicks=num_of_clicks,interval=2,button='left')
# pyautogui.typewrite('hello cui！')
# pyautogui.click(x=1278,y=851,clicks=num_of_clicks,interval=2,button='left')

print(pyautogui.getAllWindows())
print(pyautogui.getAllTitles())
print(pyautogui.getWindowsWithTitle('微信'))#329074
print(pyautogui.getActiveWindow())
# win=pyautogui.getWindowsWithTitle('QQ')[0]
# win.moveTo(0,0)
# win.resize(20,50)

# button7location=pyautogui.locateOnScreen('calc7key.png')#需要安装OpenCV才能使confidence关键字起作用
# print(button7location)
# button7point = pyautogui.center(button7location)
# print(button7point)
# # pyautogui.moveTo(x=button7point.x,y=button7point.y,duration=1)
# # pyautogui.click(x=button7point.x,y=button7point.y,duration=1)
# pyautogui.click('calc7key.png')

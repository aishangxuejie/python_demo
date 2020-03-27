#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: __init__.py.py
@time: 2020/3/26 10:34
@desc:
'''
import pyautogui
# 指定微信窗口位置（将微信图窗调整到最小）
x=0
y=0
WeChat=pyautogui.getWindowsWithTitle('微信')[0]
WeChat.moveTo(x, y)
# region=（左，顶部，宽度，高度的4整数元组）
# 仅搜索指定屏幕区域而不是全屏
pyautogui.screenshot(region=(30,0, 60, 500))
pyautogui.PAUSE = 1.0
pyautogui.FAILSAFE = True
num_seconds =1.0
butChat=pyautogui.locateOnScreen('sous.png',grayscale=True)
butPointX,butPointY = pyautogui.center(butChat)
i=0
while i <5:
    print('Please, be patient...')
    # print(butPointX,butPointY)
    pyautogui.moveTo(x=butPointX,y=butPointY*2)
    pyautogui.rightClick()
    butDelChat = pyautogui\
        .locateOnScreen('deletechat.png',grayscale=True)
    butDelChatX, butDelChatY = pyautogui.center(butDelChat)
    pyautogui.moveTo(x=butDelChatX,y=butDelChatY,duration=0.1)
    pyautogui.leftClick(x=butDelChatX,y=butDelChatY)
    i+=1
    print('- -> delete wechat chat record +',i)
print("plan over!")
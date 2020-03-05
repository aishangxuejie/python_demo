#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: py_xlwt.py
@time: 2020/1/7 8:57
@desc:
'''
import pandas as pd
import xlwt
import xlrd

data=xlrd.open_workbook('medicine.xlsx')
mysheets=data.sheets() #获取工作表list
#通过索引获取第一个sheet
# mysheet=mysheets[0]
#通过名称获取
mysheet=data.sheet_by_name(u'medicine')
nrows=mysheet.nrows
ncols=mysheet.ncols
code=''
workbook=xlwt.Workbook('medicine.xlsx')
worksheet = workbook.add_sheet('medicine01')
for j in range(nrows):
    medCode=mysheet.cell(j,0)
    medCodeValue = medCode.value

    # print(myCellValue)
    if medCodeValue=='':
        print(code)
        worksheet.write(j, 0, label=code)
    else:
        print(medCodeValue)
        code = medCodeValue
        worksheet.write(j, 0, label=code)
    workbook.save('Excel_test.xls')

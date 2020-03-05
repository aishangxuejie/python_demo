#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@author: cuiguiming
@project: python_demo
@file: py_excel.py
@time: 2020/1/6 12:33
@desc:
'''
import numpy as np
import pandas as pd
import xlwt

df = pd.DataFrame(pd.read_excel('medicine.xlsx',sheet_name='medicine'))
# print(df.shape[0])
# print("输出列标题",df.columns.values)
data = df.head(5)
code = ''
# print("line {0}".format(data))
for row in data.itertuples(name="RowData"):
    # print(row.Index)
    nex_code = data['medCode'][row.Index]
    # print(data['medCode'][row.Index])
    # print(data['medNum02'][row.Index])
    if pd.isnull(nex_code):
        # print(code)
        data['medCode'][row.Index] = code
    else:
        code = nex_code  # type01 有值记录下来
# 创建workbook和sheet对象 注意Workbook的开头W要大写
workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
sheet1.wr
workbook.save('Workbook2.xls')
print("line {0}".format(data))







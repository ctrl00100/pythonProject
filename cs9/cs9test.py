# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/16 0016 14:28
# @Author : Administrator
# @File : cs9test.py
# @Software: PyCharm
import unittest
from unittestreport import ddt,list_data
import openpyxl

from cs8测试1 import login_check

workbook=openpyxl.load_workbook(r'F:\pythonwenjiain\pythonProject\cs9\cs9.xlsx')
sh=workbook['Sheet1']
res=list(sh.rows)

title=[i.value for i in res[0]]

cases=[]
for item in res[1:]:
    data=[i.value for i in item]
    dic=dict(zip(title,data))
    cases.append(dic)
# print(eval(cases['expected']))
# print(cases['data'])
# print(cases,66)
# print(cases)
# print("---------------------")

@ddt
class TestLgin(unittest.TestCase):
    # @list_data(cases)
    # def test_login(self,item):
    #     print(item)
    #     print(item['username'])
    #     expected=item['username']
    #     params=item['password']
    #     res=login_check(username=expected,password=params)
    #     self.assertEqual(expected,res)
    @list_data(cases)
    def test_login(self,item):


        # print(res)
        print(item,"item")
        print(item['expected'],"item['expected']")
        print(item['data'],"password")
        expected=eval(item['expected'])

        params = eval(item['data'])
        res = login_check(username='python35',password='a123')
        # res = login_check(**params)
        print(res,'+-------------------------',expected)
        self.assertEqual(res,res)
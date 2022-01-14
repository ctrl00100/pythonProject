# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/14 0014 10:59
# @Author : Administrator
# @File : cs6文件操作.py
# @Software: PyCharm

# f=open(file='abc.txt',mode='r',encoding='utf-8')
#
# # print(f.read())
# # print(f.readline())
# print(f.readlines())

# f=open(file='abc.txt',mode='a',encoding='utf-8')
#
#
# f.write("\n"+'aann')
# f.close()

# f=open(file='abc.txt',mode='w',encoding='utf-8')
#
#
# f.write("\n"+'aann')
# f.close()
import random
def work01():
    with open('abc.txt',encoding='utf-8')as f:
        datas=f.readlines()
    res ={}
    for i,v in enumerate(datas):
        key='data{}'.format(datas)
        value=v.replace("\n", "")
        res[key]=value
    return res

print( work01())














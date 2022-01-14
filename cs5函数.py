# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/13 0013 17:32
# @Author : Administrator
# @File : cs5函数.py
# @Software: PyCharm
def print_func():
    for i in range(9):
        for j in range(i+1):
            print('^',end='')
        print()

print_func()
print('100后')
print_func()
print('200后')
print_func()

# 第二题
def work2(data):
    # # 创建一个新列表
    # new_data=[]
    # # 遍历
    # for i in data:
    #     res=eval(i)
    #     new_data.append(res)
    # return [new_data]
    return [eval(i) for i in data]
data =["{'a':11,'b':12}","[10,11,14,12]"]
print(work2(data))

# 第三题
def work3(cases):
    new_list=[]
    title =cases[0]
    for i in cases[1:]:
        dic=dict(zip(title,i))
        new_list.append(dic)
    return new_list
cases=[
    ['case_di','case_title','url','data','excepted'],
    [1,'测试1','url112233','001','ok'],
    [2,'测试2','url112233','001','ok'],
    [3,'测试3','url112233','001','ok'],
    [4,'测试4','url112233','001','ok'],
    [5,'测试5','url112233','001','ok'],
]
print(work3(cases))
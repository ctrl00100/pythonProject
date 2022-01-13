# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/9 0009 15:55
# @Author : Administrator
# @File : cs1_4_print.py
# @Software: PyCharm
# print("hello world")

# a=1
# b=0.22
# c='stt'
# d=True
# print('a的类型' ,type(a))
# print('b的类型' ,type(b))
# print('c的类型' ,type(c))
# print('d的类型' ,type(d))
# name=input('请输入姓名：')
name=2
money=222333
# money=input('请输入金额：')
# print('收到'+name,'金额'+money)
# format
# desc="今收到{}，金额{}"
# desc1="今收到%s，金额%s"
desc="今收到{}，金额{}".format(name,money)
desc1="今收到%s，金额%s"%(name,money)
'''
%s字符
%d整数
%f浮点数 bool int  float
'''
print(desc)
print(desc1)
desc2="今收到%f，金额%f"%(True,2.22)

print(desc2)

desc4=f'收到{name}，学费{money}'
print(desc4)


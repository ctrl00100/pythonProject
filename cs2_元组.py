# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/11 0011 7:48
# @Author : Administrator
# @File : cs2_元组.py
# @Software: PyCharm
# 列表
li=['mes',18,'nan']
# 元组
a=0
a+=1
print("(元组使用)   " + str(a)+"号 ")
tu=('mes',18,'nan',)
print(tu[0])
print(tu[1:])
print(tu.index(18))
print(tu.count('mes'))

a+=1
print("(数据转换)   " + str(a)+"号 ")

n1=99
n2=88.88
print(type(n1),type(n2))

n3=int(n1)
n4=str(n2)
print(type(n3),type(n4))
# 列表 元组转换
a+=1
print("(列表 元组转换)   " + str(a)+"号 ")
tu=['mes',18,'man']
li=list(tu)
print(li,type(li))

li2=['mes2',18,'man']
tu2=tuple(li2)
print(tu2,type(tu2))
# 列表转字符串
a+=1
print("(列表转字符串)   " + str(a)+"号 ")
s0=[11,22,22]
print(str(s0),type(str(s0)))
# 字符串转列表
a+=1
print("(字符串转列表)   " + str(a)+"号 ")
s='[11,22,22]'
li6=list(s)
print(li6,'   错误')
print(eval(s),'   正确')
# 列表测试
a+=1
print("(列表测试)   " + str(a)+"号 ")
print('----第一题----')
li2=[1,2,3,4,5]
li2[3]=66
li2.insert(0,0)
li2.extend([11,22,33])
print(li2)
print(li2.sort())
li3=li2.copy()
li3.sort(reverse=True)
print(li3)
print('---第二题---')
# user=[]
# name=input('请输入姓名:')
# age=input('请输入年龄:')
# height=input(('请输入升高:'))
# print('用户姓名为:{},年龄为:{},身高为:{}'.format(name,age,height))
# user.extend([name,age,height])
# print(user)
print('---第三题---')
str1='hello xiao mi'
data=str1.split(' ')
data.reverse()
print(data)
res=' '.join(data)
print(res)
print('---第四题---')
li=[1,2,3,4,5,6,7,8,9]
print(li[2::3])
tu=('java','c++','python','c','php','c#',)
print(tu[::4])
print('---第五题---')
datas=["1","2","3","4","5","6","7"]
# -1
num=int(input("输入1-7:"))-1
dasc='今天是周{}'.format(datas[num])
print(dasc)




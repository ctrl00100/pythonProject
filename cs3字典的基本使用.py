# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/12 0012 20:51
# @Author : Administrator
# @File : cs3字典的基本使用.py
# @Software: PyCharm
import random

li=['11',18,'男']

# 增删改查
dic={}
dic['skill']='python'
print(dic)
#
dic.update({'name':'mus','age':18})
print(dic)
#
dic['skill']='java'
print(dic)
print(dic['name'])
#指定删除
res=dic.pop('age')
print(dic,'    ',res)
#删除后加入的
print(dic.popitem())
#
dic.update({'name':'mus','age':18})
print(dic.clear())
#
dic.update({1:'1',2:18})
print(dic[1])
# 获取字典中所有的键
res=list(dic.keys())
print(res,'获取字典中所有的键')
# 获取字典中所有的值6
re2=dic.values()
print(re2,'获取字典中所有的值6')
print(dic.items(),'    获取字典中键值对')
# 空字典
set2={}
print(type(set2))
#空集合
set3=set()
print(type(set3))

# 集合去重
li=['101','101','101','101','102','103']
res3=set(li)
print(list(res3),'集合去重')
print(res3,'集合去重')

#
res=random.randint(1,5)
print(res)
res=random.random()
print(res)


str1='pythonjavaC++'
if 'python' in str1:
    print('在的')

# for 循环
i=1
while i<100:
    print('第几次循环  {}'.format(i))
    i+=1
print('end')


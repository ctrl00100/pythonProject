# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/10 0010 11:12
# @Author : Administrator
# @File : cs2_列表的基本使用.py
# @Software: PyCharm
age=15
info=[15,'牧神','男','python']
res = info[1:3]
''' 切割'''
res2 = info[1]

print(res)
print(res2)

# ---------------列表存放任意数据
# ---------------列表crud
li=[11,22,11,33]
li.append(99)
print(li)

li.insert(-1,'0101')
print(li)

li.extend([88,99,66])
print(li)

li.remove(11)
print(li)

li_1=li.pop(1)
print(li)
print(li_1)

li.clear()
print(li)
print(li_1)

li2=[11,22,11,33]
li2[1]=66
print(li2)

res=li2.index(33)
print(res)

res1=li2.count(11)
print(res1)

# 列表复制 排序
a=0
a+=1
print("   (列表复制 排序)顺序是" + str(a)+"号 ")

lo=[11,22,33]
lo2=lo.copy()
lo3=lo
print('lo的id',lo)
print('lo2的id',lo2)
print('lo3的id',lo3)

print('lo的id',id(lo))
print('lo2的id',id(lo2))
print('lo3的id',id(lo3))

a+=1
print("(列表排序 )顺序是" + str(a)+"号 ")
lo6=[11,22,55,5,8,99,95,22,00]
lo6.sort()
# 升序  降序
print(lo6)
res=lo6.sort(reverse=True)

print(lo6)

a+=1
print("(列表倒序 )顺序是" + str(a)+"号 ")

lo7=[11,'tt',55,5,8,99,95,22,00]
lo7.reverse()
print(lo7)











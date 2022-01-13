# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/9 0009 17:24
# @Author : Administrator
# @File : cs1format0.py
# @Software: PyCharm
name=2
money=222333
# 1
a=1
desc4="今收到{1}，学费{0}".format(name,money)
print(desc4+ "   顺序是" + str(a)+"号 ")
# 2
a+=1
desc5="今收到{1}，学费{0:.2f}".format(name,money)
print(desc5+ "   顺序是" + str(a)+"号 ")
# 3
a+=1
desc6="通过率为:{:.3%}".format(400/500)
print(desc6+ "   顺序是" + str(a)+"号 ")

# 3
a+=1
desc7="通过率为:{:^20},66667878".format('400/500')
desc8="通过率为:{:<20},66667878".format('400/500555')
desc81="通过率为:{:+<20},66667878".format('400/500555')
desc82="通过率为:{:0<20},66667878".format('400/500555')
desc9="通过率为:{:>20},66667878".format('400/500555555')
print(desc7+'\n'+desc81 +desc82)
print(desc8)
print(desc9+ "   顺序是" + str(a)+"号 ")
# 字符串的索引
a+=1
s1='abcdefg'
res=s1[4]
res1=s1[-4]
print(res + "   (字符串的索引 正向)顺序是" + str(a)+"号 ")
print(res1 + "   (字符串的索引 反向)顺序是" + str(a)+"号 ")
# 切片
a+=1
s2='Java python php'

res3=s2[5:11]
print(res3 + "   (字符串的索引 切片 左开右闭)顺序是" + str(a)+"号 ")

s3='123456789'
# 123 456 7
res4=s3[0:7:3]
print(res4)
# 234 567 8
res5=s3[1:8:3]
print(res5)
# 字符串常用
q='java123python456123'
q.format()
print(q)
a+=1
q1=q.replace('123','444')
print(q1)
q2=q.replace('123','444',1)
print(q2+ "   (字符串替换)顺序是" + str(a)+"号 ")
q22='java123python456123'
res=q22.find('o',10)
a+=1
print(str(res)+"   (字符串find)顺序是" + str(a)+"号 ")

a+=1
s1='python'
s2='java'
s3='c++'
res=''.join((s1,s2,s3))
print(res+ "   (字符串拼接)顺序是" + str(a)+"号 ")

a+=1
s1='python'
s2='java'
s3='c++'
res=' _ '.join((s1,s2,s3))
print(res+ "   (字符串拼接2)顺序是" + str(a)+"号 ")

a+=1
s1='python123213131231'
s2='java'
s3='c++'
res=s1.split('123')
# print(res+ "   (字符串分割)顺序是" + str(a)+"号 ")
print("   (字符串分割)顺序是" + str(a)+"号 ")
print(res)

a+=1
s1='            python12321313123  1  '
s2='java'
s3='c++'
res=s1.strip()
# print(res+ "   (字符串分割)顺序是" + str(a)+"号 ")
print("   (字符串去前后空白)顺序是" + str(a)+"号 ")
print(s1)
print(res)
s6='---python12321313123  1  '
res=s6.strip('-')
# s2.lstrip()  去前
# s2.rsplit()  去后
print("   (字符串去前后特殊字符)顺序是" + str(a)+"号 ")
print(res)

a+=1
print(" (字符串去强制大小写)顺序是" + str(a)+"号 ")
s1='python'
print(s1.lower())
print(s1.upper())

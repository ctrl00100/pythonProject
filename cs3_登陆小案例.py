# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/13 0013 11:18
# @Author : Administrator
# @File : cs3_登陆小案例.py
# @Software: PyCharm


u='123'
p='212'


q=0

status=0
while status==0:
 user = input('请输入账号')
 pwd = input('请输入密码')
 if user==u and pwd==p:
    status += 1


    print('ok')

 elif user==u:
    q += 1
    print('')
    if q>2:
        print('密码错误太多')
        break
 else:
    q += 1
    if q>2:
        print('全错太多')
        break

    print('全错')
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/14 0014 15:39
# @Author : Administrator
# @File : cs7异常捕获.py
# @Software: PyCharm
def work1():
    while True:
        try:
            n=int(input('请输入数字:'))
        except:
            print('请输入正确的数字')
            continue
        else:
            if n<=1:
                print('请输入大于1的数字')
                continue
            nums=[]
            for i in range(1,n+1):
                if i%2==0:
                    nums.append(i)
            print('所有偶数为:',nums)
            print('偶数个数为:',len(nums))
            num_avg=sum(nums)/len(nums)
            print('偶数平均值:',num_avg)
            break
work1()

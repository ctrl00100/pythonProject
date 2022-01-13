# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/13 0013 14:27
# @Author : Administrator
# @File : cs4for循环.py
# @Software: PyCharm
'''
money=float(input('请输入金额:'))
if 0<=money<=49:
    print('总金额为{}元,不打折'.format(money))

elif 50<=money<=100:
    print('总金额为{}元,打9折'.format(money),0.9*money)
elif 100 < money :
    print('总金额为{}元,打8折'.format(money),0.8*money)
    '''
import random

'''
money2=float(input('请输入一个整数:'))
if money2 % 3==0 and money2 % 5==0:
    print("是3和5的公倍数,有优惠")
else:
    print('miss优惠')
'''
# 石头剪刀布
'''
i=0
while i<4:
    a=random.randint(1,3)
    money3 = float(input('请输入一个数(1-3):'))
    if money3-a==0:
        print('平局',a)
    elif (money3==1and a==2 ) or (money3==2and a==3 ) or (money3==3and a==1 ) :
        print('win',a)
    else:
        print('loser',a)

    i += 1
'''
# 打印星星
# for i in range(4):
#     for a in range(4-i):
#         print('*',end=' ')
#     print()

# 乘法口诀
# for i in range(10):
#     for a in range(i):
#         print(a+1,'*',i,'=',(a+1)*i,end=' ')
#     print()

# 列表推导式
li=[]
for i in range(21):
    d='page{}'.format(i)
    li.append(d)
print(li)

li2=['page{}'.format(i) for i in range(10)]
print(li2)

tu =(11,22,55,5,3,7,3)
li3=[i+1 for i in  tu]
print(li3)
li3=[i*10 for i in  tu]
print(li3)


li4=[1,2,3,4]
count=0
for a in  li4:
    for b in li4 :
      for c in li4 :
         if a!=b and a!=c and c!=b:
             count+=1

print(count,'6')

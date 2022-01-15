# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/15 0015 13:23
# @Author : Administrator
# @File : cs8测试1.py
# @Software: PyCharm
def login_check(username=None,password=None):
    '''
    登陆校验函数
    :param username:
    :param password:
    :return:
    '''
    if username!=None and password!=None:
        if username=='python35' and password =='a123':
            return {'code':0,'msg':'登陆成功'}
        else:
            return {'code':1,'msg':'账号或密码不正确'}
    else:
        return {'code':1,'msg':'账号和密码不能为空'}


if __name__=='__main__':

    res=login_check('python35','123')
    expected ={'code':0,'msg':'登陆ok'}
    if res==expected:
        print("可以通过")
    res=login_check('python35','1234')
    expected ={'code':1,'msg':'登陆000ok'}
    if res!=expected:
        print("可以不通过")




























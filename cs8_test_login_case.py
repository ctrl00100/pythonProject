# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/15 0015 14:38
# @Author : Administrator
# @File : cs8_test_login_case.py
# @Software: PyCharm
import unittest

from cs8测试1 import login_check
# 第一 创建测试套件,加载测试用例到套件
# 1.创建套件
# 2.创建一个用例加载器
# 3.加载测试用例到套件



class TestLogin(unittest.TestCase):
    def test_login_pass(self):
        res=login_check('python35','a123')
        expeted ={'code':0,'msg':'登陆成功'}
        # 断言
        assert res==expeted

    def test_login_pass2(self):
        params={'username':'python35','password': 'a123'}
        # res = login_check('python35', 'a123')
        expeted = {'code': 0, 'msg': '登陆成功'}
        result=login_check(username=params['username'],password=params['password'])
        assert result == expeted

    def test_login_pass_pwserrot(self):
        params = {'username': 'python35', 'password': 'a1232'}
        # res = login_check('python35', 'a123')
        expeted = {'code': 0, 'msg': '登陆成功'}
        result = login_check(username=params['username'], password=params['password'])
        assert result == expeted

    def test_login_pass_user_error(self):
        params = {'username': 'pyth2on35', 'password': 'a123'}
        # res = login_check('python35', 'a123')
        expeted = {'code': 0, 'msg': '登陆成功'}
        result = login_check(username=params['username'], password=params['password'])
        assert result == expeted

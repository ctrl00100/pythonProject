# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/15 0015 15:25
# @Author : Administrator
# @File : cs8test1.py
# @Software: PyCharm

import unittest



class TestMusen(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('setUpClass---------')

    @classmethod
    def tearDownClass(self) -> None:
        print('tearDown')
    def setUp(self)->None:
        print('tearDownClass----------------')

    def tearDown(self) -> None:
        print('tearDown')

    def test_01(self):
        print('这是第一条测试用例')

    def test_02(self):
        print('这是第2条测试用例')

    def test_03(self):
        print('这是第3条测试用例')

    def test_04(self):
        print('这是第4条测试用例')

if __name__=="__main__":
    unittest.main()
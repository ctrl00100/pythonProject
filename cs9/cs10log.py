# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/1/16 0016 17:06
# @Author : Administrator
# @File : cs10log.py
# @Software: PyCharm

import logging
log=logging.getLogger()

log.setLevel("INFO")
log.debug("这是一条debug级别日志")
log.info("这是一条info级别日志")
log.warning("这是一条warning级别日志")
log.error("这是一条error级别日志")
log.critical("这是一条critical级别日志 ")
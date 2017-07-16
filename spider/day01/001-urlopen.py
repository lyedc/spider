#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/16 0:42
# @Author  : zhl
# @Site    : 
# @File    : 001-urlopen.py
# @Software: PyCharm
import urllib2


def spider():
    try:
        # 发送请求
        response = urllib2.urlopen('http://www.itheima.com/', timeout=3)
        # 返回抓取到的内容
        html = response.read()
        print html
    except Exception as err:
        print err


if __name__ == "__main__":
    spider()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/16 8:23
# @Author  : zhl
# @Site    : 
# @File    : 002-url_request.py
# @Software: PyCharm
import urllib2


def spider():
    url = 'http://www.itheima.com'
    # 构造请求
    request = urllib2.Request(url)
    # 返回响应
    response = urllib2.urlopen(url)
    # 返回请求的状态码
    print(response.getcode())
    # 返回实际的url地址
    print(response.geturl())
    # 返回读取到的内容
    print(response.read())


def main():
    spider()


if __name__ == "__main__":
    main()

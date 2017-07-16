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
    header = {"User-Agent" : "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",}
    # 构造请求
    request = urllib2.Request(url, headers=header)
    # 返回响应
    response = urllib2.urlopen(url)
    request.add_header("Connection", "keep-alive")
    print(request.get_header('Connection'))
    print(request.get_header('User-agent'))
    print(response.getcode())
    print(response.geturl())
    print(response.read(300))


def main():
    spider()


if __name__ == "__main__":
    main()

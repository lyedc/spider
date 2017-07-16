#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/16 8:54
# @Author  : zhl
# @Site    : 
# @File    : 004_add_header.py
# @Software: PyCharm
import urllib
import urllib2
import random


def spider():
    url = 'https://www.baidu.com/s'
    keyword = {'wd':'传值播客'}
    keyword = urllib.urlencode(keyword)
    print(keyword)
    print(urllib.unquote(keyword))
    new_url = url +"?" + keyword
    print(new_url)
    print(url)
    header = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"
    ]
    # 动态的去获取头信息
    user_header = random.choice(header)
    request = urllib2.Request(new_url)
    # 往请求中添加头信息
    request.add_header('User-Agent', user_header)
    response = urllib2.urlopen(request)
    print(request.get_header('User-agent'))
    print(response.getcode())
    print(response.geturl())
    print(response.read())


def main():
    spider()


if __name__ == "__main__":
    main()

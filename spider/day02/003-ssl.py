# coding=utf-8

import urllib
import urllib2
import ssl


def demo():
    # 忽略证书的验证请求 这样就可以跳过ssl证书验证 没有第三方认证的证书的使用
    context = ssl._create_unverified_context()
    url = "https://www.12306.cn/mormhweb/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, context=context)
    # response = urllib2.urlopen(request)
    print response.read()


def main():

    demo()


if __name__ == '__main__':
    main()

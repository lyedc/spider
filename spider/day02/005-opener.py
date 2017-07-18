# coding=utf-8


import urllib
import urllib2


def create_handler():
    """创建自定义的handler对象"""
    url = 'http://www.baidu.com'
    # 创建一个httphandler处理器对象 支持处理http的请求
    http_handler = urllib2.HTTPHandler(debuglevel=1)
    # 创建支持处理http请求的opener对象
    opener = urllib2.build_opener(http_handler)
    # 构建请求
    request = urllib2.Request(url)
    # 调用自定义的opener对象来发送请求
    response = opener.open(request)
    print response.getcode()


def main():
    create_handler()


if __name__ == '__main__':
    main()

# coding=utf-8

import urllib2
"""
代理设置的流程p：
    1 先构建代理处理器  proxyhandler({代理的ip地址和端口号})
    2 构建opener（）对象 使用 urllib2.build_opener(http_proxy_handler)
    3 构建请求 urllib2.Request(url, data, headers)
    4 发送请求  opener.open(request)

"""


def proxy_handler(url):
    # 私密代理的设置模式
    proxy = {"http": "mr_mao_hacker:sffqry9r@122.114.214.159:16816"}
    # 设置代理
    http_proxy_handler = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(http_proxy_handler)
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)"}
    request = urllib2.Request(url, headers=headers)
    response = opener.open(request)
    print response.getcode()


def spider():
    url = 'http:.//www.baidu.com'
    proxy_handler(url)


def main():
    spider()


if __name__ == "__main__":
    main()

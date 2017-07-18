# coding=utf-8


import urllib2


def proxy_handler():
    """代理的设置"""''
    ip = '61.54.206.0:6675'
    url = 'http://www.biadu.com'
    # 构建代理地址  是一个字典的形式的
    proxy = {'http': ip}
    # 使用代理服务器 参数是一个字典
    http_proxy_handler = urllib2.ProxyHandler(proxy)
    # 构建空的代理服务起
    null_http_proxy_handler = urllib2.ProxyHandler({})

    # 定义一个代理的开关
    proxy_switch = True

    # 构建opener（） 方法来使用构建的代理
    if proxy_switch:
        opener = urllib2.build_opener(http_proxy_handler)
    else:
        opener = urllib2.build_opener(null_http_proxy_handler)
    # 构建请求对象
    request = urllib2.Request(url)
    # 发送请求
    response = opener.open(request, timeout=2)
    print response.getcode()
    print response.read()


def spider():
    proxy_handler()


def main():
    spider()


if __name__ == '__main__':
    main()

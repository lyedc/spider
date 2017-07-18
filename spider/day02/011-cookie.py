# coding=utf-8

import urllib2
import cookielib

def get_cookie(url):
    # 创建cookie对象的实例来保存获取到的cookie的值
    cookie_jar = cookielib.CookieJar()
    # 使用httpcookieprocessor（）来创建cookie处理器对象 参数为cookiejar对象
    cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
    # 创建自定义的opener对象
    opener = urllib2.build_opener(cookie_handler)
    # 构建请求
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    request = urllib2.Request(url, headers=headers)
    opener.open(request)
    cookie_str = ''
    # 拼接cookie成为正常的cookie的值
    for item in cookie_jar:
        cookie_str = cookie_str + item.name + "=" + item.value + ";"
    print cookie_str[:-1]
def main():
    url = 'http://www.baidu.com'
    get_cookie(url)


if __name__ == "__main__":
    main()
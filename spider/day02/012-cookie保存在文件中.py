# coding=utf-8
import urllib2
import cookielib

"""
把cookie存储在本地的文件中

"""

filename = "cookie.txt"
url = 'http://www.baidu.com'
# 使用mozi把cookie保存在本地
cookie_jar = cookielib.MozillaCookieJar(filename=filename)
# 创建cookiehandler对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
# 构建operer 对象
opener = urllib2.build_opener(cookie_handler)
request = urllib2.Request(url)
opener.open(request)
cookie_jar.save()
print cookie_jar

"""
把本地的文件中的cookie的信息读取出来进行使用

"""
# 创建对象
cookie_jar3 = cookielib.MozillaCookieJar()
# 读取文件中的cookie信息
cookie_jar3.load('cookie.txt')
print  cookie_jar3
# 创建coolie处理器
cookie_handler3 = urllib2.HTTPCookieProcessor(cookie_jar3)
# 创建自定义的opener对象
opener3 = urllib2.build_opener(cookie_handler3)
request = urllib2.Request(url)
# 发送请求

response = opener3.open(request)
print response.getcode()
print response.read()

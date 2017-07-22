# coding=utf-8
import requests

"""
使用requests 实现代理:
    在使用的是代理的时候 传入的参数是一个字典 
使用requests 实现web端的登录:
    传入的是自己账号和密码 传入的参数 是一个元组的形式

"""

# 构建免费代理  构建的参数是一个字典
proxies = {'http': 'http://12.34.56.79:9527'}
# 私密代理的设定方式  还可以把私密道代理设定在 环境变量中 这样就不会在自己的代码中

# 暴露自己的代理地址和账户
proxies3 = {"http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816"}

switch = True

if switch:
    # 发送请求 采用代理
    response = requests.get('http://www.baidu.com', proxiesp=proxies)
else:
    # 构建私密的代理 带上自己的用户名和密码
    response = requests.get('http://www.baidu.com', proxiesp=proxies3)
# 打印返回的内容
print response.content

# 构建web端验证的请求   传入的参数 是一个元组
auth = ('test', '123456')

response = requests.get('http://192.168.199.107', auth=auth)

print response.content

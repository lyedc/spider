# coding=utf-8
import urllib2
import urllib
"""
web 客户端验证流程：
    先指定自己的账号 密码 站点
    1 先创建密码管理器对象：urllib2.HTTPPasswordMGRWITHDEFAULTEADLM（）
    2 使用创建出来的管理器对象添加用户的信息和站点信息
    3 构建认证的代理 使用 urllib2.HTTPBasicAuthHandler(None,uri=server,user=  passwd=)
    4 构建opener对象  使用 urllib2.build_opener(认证代理对象)
    4 构建请求对象  urllib2.request（url headers）
    5 发送请求：opener.open(request)
"""

def load_page():
    # 用户信息
    username = 'zhuhaoliang'
    password = 'zhuhaoliang'
    server = 'http://127.0.0.1:8000'
    # 创建密码管理器对象
    passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # 添加用户名和密码等信息
    passwdmgr.add_password(None, uri=server, user=username, passwd=password)
    # 创建一个http认证的处理器的对象
    http_auth_handler = urllib2.HTTPBasicAuthHandler(passwdmgr)
    # 构建自定义的opener（）
    opener = urllib2.build_opener(http_auth_handler)
    # 构建请求
    request = urllib2.Request('http://127.0.0.1:8000/admin/shop_order/ordermain/')
    # 发送请求
    response = opener.open(request)
    print response.getcode()
    print response.read()


def main():
    load_page()


if __name__ == "__main__":
    main()

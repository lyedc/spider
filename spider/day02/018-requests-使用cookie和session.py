# coding=utf-8
import requests


def get_cookie():
    """获取到访问地址中的cookie信息"""
    # 发送请求:
    response = requests.get('https://www.baidu.com/')
    # 保存返回的cookie信息
    cookie_jar = response.cookies
    # 把cookie转换为字典
    cookie_dict = requests.utils.dict_from_cookiejar(cookie_jar)

    print cookie_jar
    print cookie_dict
    # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
    # {'BDORZ': '27315'}


def use_session():
    """使用session来实现人人的登录"""
    """
    使用session简介:
        在 requests 里，session对象是一个非常常用的对象，
        这个对象代表一次用户会话：从客户端浏览器连接服务器开始，
        到客户端浏览器与服务器断开。
        会话能让我们在跨请求时候保持某些参数，比如在同一个 Session 实例发出的所有请求之间保持 
        cookie 。
        session.cookies  需要的cookie保存在了 session 中 通过session中的属性 这样来获
        保存的cookie的信息
    """
    # 1 创建session对象可以用来保存cookie的值
    session = requests.session()
    # 2 处理headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # 3 构建需要的登录密码和账户
    data = {'email': '****@qq.com', 'password': '*****'}
    # 4 发送带有用户和密码的请求, 病获取登录后的cookie信息
    # 登录自己的主页
    response = session.post('http://www.renren.com/PLogin.do', data=data)
    print response.status_code
    # print response.content
    # 5 session 中包含了登录后的cookie的信息 可以直接访问那些登录或才能访问的页面
    # 通过获取到的 cookie的信息 去访问自己的好友
    response = session.get('http://www.renren.com/221190670/profile')
    print response.status_code
    # print response.content
    print session.cookies


if __name__ == '__main__':
    get_cookie()
    use_session()

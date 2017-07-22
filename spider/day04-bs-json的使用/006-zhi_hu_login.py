# coding=utf-8
import time
import requests
from bs4 import BeautifulSoup


def captcha(data):
    """获取验证码"""
    with open('captcha.png', 'wb') as fp:
        fp.write(data)
    return raw_input('请输入验证码:>>>')


def login(url):
    """登录页面解析"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    session = requests.session()
    zhi_hu_url = 'https://www.zhihu.com/'  # 通过get请求 获取图片的验证码
    html = session.get(zhi_hu_url, headers=headers).content  # 这一步主要是用来获取csrf-token 的 跨站防御攻击验证码的
    soup = BeautifulSoup(html, "lxml")
    _xsrf = soup.find('input', attrs={'name': '_xsrf'}).get("value")
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
    # 发送请求获取图片内容 病保存在本地
    captcha_data = session.get(captcha_url, headers=headers).content
    # 需要提交的信息
    form_data = {
        'account': '18500250699',
        'password': 'zhu3850835',
        'captcha': captcha(captcha_data),
        '_xsrf': _xsrf
    }
    # 向这个地址提交的自己的登录信息 注意后面的 account 的会 登录的地址也是accout 如果是email的话 后面的就是email
    login_url = 'https://www.zhihu.com/login/account'
    text = session.post(login_url, data=form_data, headers=headers).content
    # 登录成功然后带着cookie 去登录自己的个人主页/
    html = session.get("https://www.zhihu.com/people/wove-13/activities", headers=headers).content
    # 数据写入文件中
    with open('./数据/zhi_hu.html', 'w') as fp:
        fp.write(html)


def zhi_hu_spider():
    url = ''
    login(url)


if __name__ == '__main__':
    zhi_hu_spider()

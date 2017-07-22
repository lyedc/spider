# coding=utf-8
import urllib2
import cookielib
import urllib


def login(url, data):
    """爬虫登录主函数"""
    # 创建cookiejar 来保存cookie的信息
    cookie_jar = cookielib.CookieJar()
    # 处理cookie的handler
    cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)
    # 自定义的额opener
    opener = urllib2.build_opener(cookie_handler)
    # 构建请求
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    request = urllib2.Request(url, data, headers=headers)
    # 发送请求
    response = opener.open(request)
    print response.getcode()
    print response.read()
    print cookie_jar


def main():
    """爬虫登录入口函数"""
    url = "http://www.renren.com/PLogin.do"
    # url = "http://www.renren.com/"
    # url = 'http: // www.renren.com / ajaxLogin / login'
    data = {
        'email': '****@qq.com',
        'origURL': 'http://www.renren.com/home',
        'password': '*****',
        "domain": "renren.com",
        "key_id": "1",
        "captcha_type": "web_login",
        "rkey": "488c7e70ed9a9ff58385877142a5f294",
        "f": "http % 3A % 2F % 2Fwww.renren.com % 2F342445972"
    }
    data = urllib.urlencode(data)
    login(url, data)


if __name__ == '__main__':
    main()

"""
    <dl class="bottom">
    <input type="hidden" name="origURL" value="http://www.renren.com/home">
    <input type="hidden" name="domain" value="renren.com">
    <input type="hidden" name="key_id" value="1">
    <input type="hidden" name="captcha_type" id="captcha_type" value="web_login">
    <input type="submit" id="login" class="input-submit login-btn" stats="loginPage_login_button" value="登录" tabindex="5">
    rkey 488c7e70ed9a9ff58385877142a5f294
    f http%3A%2F%2Fwww.renren.com%2F342445972
    http://www.renren.com/home
    """

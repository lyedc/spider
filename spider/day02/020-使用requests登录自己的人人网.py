# coding=utf-8
import requests


def session_login(session_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    data = {
        'email': '906300817@qq.com',
        'password': 'zhu3850835'
    }
    session = requests.session()
    response = session.post(session_url,data=data, headers=headers)
    print response.status_code
    print response.content
    print type(session.cookies)
    print requests.utils.dict_from_cookiejar(session.cookies)

def login(url):
    """登录程序"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Cookie": "anonymid=j58g0ct9-bq2xtg; depovince=GW; _r01_=1; JSESSIONID=abcFJPulLguyKcNtY0t1v; wp_fold=0; jebecookies=8a3532dd-bc0e-4e13-b3c4-53a834068df4|||||; ick_login=995d28ba-81f1-40e2-877c-46892a8a1fe3; _de=2D9F19A0E2D84167C5BC13FF67F7809D696BF75400CE19CC; p=8e9f54b7c419bd77d7371799c53bc5492; first_login_flag=1; ln_uact=906300817@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20120427/2220/h_main_9i34_5f4c00069bf82f75.jpg; t=189b9c57de896c3e0915c86b518eb0d02; societyguester=189b9c57de896c3e0915c86b518eb0d02; id=342445972; xnsid=ac107f18; loginfrom=syshome"
    }
    response = requests.get(url, headers=headers)
    print response.status_code
    print response.content


def spider():
    """爬虫主程序"""
    url = 'http://www.renren.com/342445972'
    session_url = "http://www.renren.com/PLogin.do"
    # login(url)
    session_login(session_url)


if __name__ == '__main__':
    spider()

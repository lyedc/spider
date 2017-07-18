# coding=utf-8

import urllib2
import urllib


def login(url):
    """爬虫模拟登录程序"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Cookie": "anonymid=j58ablxmn0rqx0; _de=2D9F19A0E2D84167C5BC13FF67F7809D696BF75400CE19CC; p=108630a9bb9b7f7677bce309aa5d55112; first_login_flag=1; ln_uact=906300817@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20120427/2220/h_main_9i34_5f4c00069bf82f75.jpg; t=967cfb07138956486af55f38b78a37fd2; societyguester=967cfb07138956486af55f38b78a37fd2; id=342445972; xnsid=aee82741; loginfrom=syshome"
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request, timeout=3)
    print response.getcode()
    html = response.read()
    try:
        with open('renren_login.html', 'w') as fp:
            fp.write(html)
    except Exception as err:
        print err


def main():
    url = 'http://www.renren.com/342445972'
    login(url)


if __name__ == "__main__":
    main()

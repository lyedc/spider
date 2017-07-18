# coding=utf-8

# 分析url：

# Request URL:http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link
# Request Method:POST  这里是post提交  那么就需要post提交的数据
# Status Code:200 OK
# Remote Address:220.181.76.76:80
# Referrer Policy:no-referrer-when-downgrade
# post 提交的数据
# i:你好
# from:AUTO
# to:AUTO
# smartresult:dict
# client:fanyideskweb
# salt:1500280514215
# sign:d648cfebc5193abbbe2df85b0b7557ca
# doctype:json
# version:2.1
# keyfrom:fanyi.web
# action:FY_BY_CL1CKBUTTON
# typoResult:true

#  新版 url = http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link
# 旧版 url = http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=https://www.baidu.com/link

import urllib
import urllib2
import os


def load_page(url, data):
    """发送请求加载页面"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    request = urllib2.Request(url, data=data, headers=headers)
    # 发送请求
    try:
        response = urllib2.urlopen(request)
        if response.getcode() == 200:
            json_data = response.read()
            print response.getcode()
            print json_data
            # 保存数据
            if not os.path.exists('./数据'):
                os.mkdir('./数据')
            file_path = os.path.join('./数据', 'youdao.json')
            try:
                # 写入文件
                with open(file_path, 'w+') as fp:
                    fp.write(json_data)
            except Exception as err:
                print err
        else:
            print response.getcode()
    except Exception as err:
        print err


def spider():
    """爬虫主程序"""
    # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null'
    # url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {
        "i": "你好",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        # "salt": "1500280514215",
        # "sign": "d648cfebc5193abbbe2df85b0b7557ca",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CL1CKBUTTON",
        "typoResult": "true"
    }
    data = urllib.urlencode(data)
    load_page(url, data)


def main():
    spider()


if __name__ == '__main__':
    main()

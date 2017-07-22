# coding=utf-8
import requests
import json


def request_post(url, data):
    """使用requests来发送post请求"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.post(url, data=data, headers=headers)
    print response.content
    result = eval(response.content)
    result3 = json.loads(response.content)
    print result['translateResult'][0][0]['src']

def main():
    """程序主函数"""

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {
        "i": "你好",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1500280514215",
        "sign": "d648cfebc5193abbbe2df85b0b7557ca",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CL1CKBUTTON",
        "typoResult": "true"
    }
    request_post(url, data)


if __name__ == '__main__':
    main()

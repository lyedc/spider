# coding=utf-8
import requests


def request_get(url, keywords):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    response = requests.get(url, params=keywords, headers=headers)
    # 查看相应的状态
    print response.status_code
    # 返回的字节流 文本内容制定的是什么样式就返回什么格式的数据
    print response.content
    # 返回的是unicode 格式的数据
    print response.text
    # 返回实际的url的地址
    print response.url
    # 返回响应头的编码格式
    print response.encoding


def main():
    url = 'https://www.baidu.com/s?'
    keywords = {'wd': '北京'}
    request_get(url, keywords)


if __name__ == '__main__':
    main()

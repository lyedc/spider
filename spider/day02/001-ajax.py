# coding=utf-8

# https://movie.douban.com/j/new_search_subjects?
# sort=T&range=0,10&tags=%E5%89%A7%E6%83%85&start=0
# 分析：
# 请求需要带去的参数
# sort:T   排序
# range:0,10  评分范围
# tags:电影,剧情   标签（电影类型）
# start:0 数据的起始位置 从0 开始  每页20条数据

import urllib
import urllib2
import os


def load_page(url):
    """发送请求加载页面"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    # 构造请求
    request = urllib2.Request(url, headers=headers)
    try:
        # 发送请求
        response = urllib2.urlopen(request)
        if response.getcode() == 200:
            json_data = response.read()
            if not os.path.exists('./数据'):
                os.mkdir('./数据')
            file_path = os.path.join('./数据', 'douban.json')
            with open(file_path, 'w') as fp:
                fp.write(json_data)
        else:
            print '请求出错'
    except Exception as err:
        print err


def spider():
    """爬虫程序"""
    base_url = 'https://movie.douban.com/j/new_search_subjects?'
    # 构造关键字  请求需要带上的参数
    key_words = {
        "sort": "T",
        "range": "0,10",
        "tags": "电影,剧情,美国",
        "playable": "1",
        "start": "0"
    }
    # 编码
    key_words = urllib.urlencode(key_words)
    url = base_url + key_words
    # 调用函数
    load_page(url)


def main():
    """程序主函数"""
    spider()


if __name__ == "__main__":
    main()

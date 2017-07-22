# coding=utf-8
from lxml import etree
import requests
import random
import json
import time


def load_page(url, key_words, base_xpath, page):
    """页面加载"""
    headers = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"
    ]
    user_agent = {"User-Agent": random.choice(headers)}
    base_xpath = '//tr[@class="even"]|//tr[@class="odd"]'
    try:
        response = requests.get(url, params=key_words, headers=user_agent)
        if response.status_code == 200:
            html_tree = etree.HTML(response.content)
            url_list = html_tree.xpath(base_xpath)
            print '开始解析第{}页数据==============='.format(page)

            num = 0
            for item in url_list:
                time.sleep(0.3)
                num += 1
                print '开始解析第{}条信息'.format(num)
                position_dic = {}
                position_dic['url'] = 'http://hr.tencent.com/' + item.xpath('./td[1]/a/@href')[0]
                position_dic['desc'] = item.xpath('./td[1]/a/text()')[0]
                position_dic['lei_bei'] = item.xpath('./td[2]/text()')[0]
                position_dic['num'] = item.xpath('./td[3]/text()')[0]
                position_dic['address'] = item.xpath('./td[4]/text()')[0]
                position_dic['time'] = item.xpath('./td[5]/text()')[0]
                position_list.append(position_dic)
                print '第{}条信息解析完毕'.format(num)
            print '第{}页数据已经保存=================='.format(page)
        else:
            print  '请求出错'
    except Exception as err:
        print err


def tent_cent_spider():
    """调度器"""
    url = 'http://hr.tencent.com/position.php?'
    base_xpath = '//tr[@class="even"]|//tr[@class="odd"]'
    for page in range(0, 3):
        key_words = {
            "keywords": "python",
            "tid": "87",
            "lid": "2156",
            'start': str(page)
        }
        load_page(url, key_words, base_xpath, page)


if __name__ == '__main__':
    position_list = []
    tent_cent_spider()
    json_file = json.dumps(position_list)
    # 写入文件 json 后的内容
    with open('json.json', 'a') as fp:
        fp.write(json_file)

"""
http://hr.tencent.com/position.php?keywords=python&tid=87&lid=2156&start=0

页面和url分析:
    get请求
    http://hr.tencent.com/position.php?
    http://hr.tencent.com/position.php?  基础url
    keywords=python&tid=87&lid=2156&start=0 关键字
    请求参数
    keywords:python
    tid:87 职位
    lid:2156 城市
    start:0 起始页  每页10个
"""

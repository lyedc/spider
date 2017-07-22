# coding=utf-8
import requests
from urllib import parse
import random
from lxml import etree
import time
"""
遗留问题:
    一次解析的是一个页面  一个页面一条招聘信息 解析出来的detail_list 就是一条完整的招聘广告
    列表中的每项都是一条信息 每行 
    2 需要把里面的字符给替换点  先转换成string类型 然后及进行替换
['技术总监 （大数据、数据挖掘/java/python）', '北京', '2.5-5万/月', '\r\n\t\t\t\t\t\t', '职位描述：', '\r\n\t\t\t\t\t\t1.负责灵云人工智能大数据系统设计、功能模块设计

"""


def load_page(url, url_xpath):
    """加载页面"""
    headers = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"
    ]
    user_agent = {"User-Agent": random.choice(headers)}
    response = requests.get(url, headers=user_agent)
    if response.status_code == 200:
        html = response.content
        html_format = etree.HTML(html)
        url_list = html_format.xpath(url_xpath)
        return url_list
    else:
        print('load_page请求出错..errcode={}'.format(response.status_code))
        return None


def load_detail_html(url_list):
    """解析每个招聘信息的详情页面"""
    # detail_xpath = '//div[@class="cn"]//h1/text()|//div[@class="cn"]//span/text()|//div[@class="cn"]/strong/text()|//div[@class="bmsg job_msg inbox"]/span/text()|//div[@class="bmsg job_msg inbox"]/div/span/text()'
    detail_xpath = '//div[@class="cn"]//h1/text()|//div[@class="cn"]//span/text()|//div[@class="cn"]/strong/text()|//div[@class="bmsg job_msg inbox"]/span/text()|//div[@class="bmsg job_msg inbox"]/text()|//div[@class="bmsg job_msg inbox"]/div/span/text()'
    for url in url_list:
        detail_list = load_page(url, detail_xpath)
        if detail_list is None:
            print('详情页面请求错误...')
            break
        save_txt(detail_list, 'detail.text')


def save_txt(url_list, file_name):
    """保存具体的招聘信息"""
    with open(file_name, 'a+') as fp:
        for item in url_list:
            fp.write(item)
            fp.write('\n')


def spider():
    """爬虫主程序"""
    """
    http://search.51job.com/list/010000,000000,0000,00,9,99,python,2,2.html
    
    http://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html
    
    就到5 就可以了
    """
    for page in range(1,6):
        url = ' http://search.51job.com/list/010000,000000,0000,00,9,99,python,2,' + str(page) + '.html'
        url_xpath = '//div[@class="el"]/p/span/a/@href'
        url_list = load_page(url, url_xpath)
        if url_list == None:
            print('请求出错')
            return
        save_txt(url_list, 'url_list.txt')
        load_detail_html(url_list)
        print(url)
        time.sleep(0.03)

if __name__ == '__main__':
    spider()

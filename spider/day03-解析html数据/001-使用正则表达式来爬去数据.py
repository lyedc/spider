# coding=utf-8
import urllib2
import re
import os


# base_url = 'http://www.neihan8.com/article/list_5_1.html'

def load_page(url, pattern):
    """发送请求"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    request = urllib2.Request(url, headers=headers)
    try:
        response = urllib2.urlopen(request)
        if response.getcode() == 200:
            # 对读取到的html进行编码的处理
            html = response.read().decode('gbk').encode('utf-8')
            # 采用正则处理数据
            content_html = pattern.findall(html)
            save_content(content_html)
    except Exception as err:
        print err


def save_content(content):
    """保存数据"""
    # pattern1 = re.compile(r'"\s*?"|"<.*?>|"&(.*?);"', re.S)
    pattern1 = re.compile(r"&(.*?);|<(.*?)>|\s|　")
    try:
        with open("dunzi.txt", 'a') as fp:
            for item in content:
                data = pattern1.sub("", item)
                fp.write(data)
                fp.write('\n\n')
    except Exception as err:
        print err


def duan_zi_spider():
    """爬虫调度"""
    pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
    base_url = 'http://www.neihan8.com/article/list_5_'
    page = 1
    while True:
        command = raw_input("按回车键继续,按q结束爬取数据:")
        if command == 'q':
            break
        url = base_url + str(page) + '.html'
        load_page(url, pattern)
        print url
        page += 1

def main():
    """程序入口"""
    duan_zi_spider()


if __name__ == '__main__':
    main()

"""
      <div class="f18 mb20">
                            <p>
	　　今天去女朋友家见家长，特么的发现她姐居然是我初中时候的初恋女友，而她爸是我们公司的单位领导，<br />
	最特么扯蛋的就是她妈居然是是高中时期棒打鸳鸯的班主任，我特么的和你们一家子有仇是吧？</p>

                            
                        </div>

"""

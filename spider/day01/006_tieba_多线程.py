#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import os
from threading import Thread
import threading
import time


def get_request(url):
    """发起请求"""
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
    request = urllib2.Request(url, headers=header)
    try:
        response = urllib2.urlopen(request, timeout=5)
        if response.getcode() == 200:
            html = response.read()
            return html
        else:
            print('请求失败....')
    except Exception as err:
        print(err)


def write_html(html, page):
    """爬取出来的内容写入到文件中"""
    file_path = os.path.join('./贴吧', '贴吧的第' + str(page) + '内容.html')
    try:
        with open(file_path, 'w') as fp:
            fp.write(html)
        print('保存成功')
    except Exception as err:
        print(err)


def thread_task(url, page):
    """多线程执行任务的函数"""
    html = get_request(url)
    write_html(html, page)
    print(threading.current_thread().name, url)


def spider(name, start_page, end_page):
    """爬虫主程序"""
    base_url = 'https://tieba.baidu.com/f?'
    keyword = {"kw": "美女"}

    # 编码
    keyword = urllib.urlencode(keyword)
    t_list = []  # 存放建立的线程
    start_time = time.time()
    for page in range(start_page, end_page + 1):
        pn = urllib.urlencode({'pn': page * 50})
        url = base_url + keyword + "&" + pn
        t = Thread(target=thread_task, args=(url, page))
        t_list.append(t)
        t.start()
    for t in t_list:  # 遍历线程加入等待
        t.join()
    print ("结束时间", time.time() - start_time)


def main():
    """程序的入口"""
    # name = raw_input("请输入你要爬取的贴吧的名称:>>>")
    name = "美女"
    start_page = int(raw_input('请输入开始的页码:>>>'))
    end_page = int(raw_input('请输入结束的页码:>>>'))
    spider(name, start_page, end_page)


if __name__ == "__main__":
    lock = threading.Lock()
    if not os.path.exists('./贴吧'):
        os.mkdir('./贴吧')
    main()

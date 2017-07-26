# coding=utf-8
"""
需求: 爬去豆瓣电影top 250
    url https://movie.douban.com/top250
    页面结构分析: div class="info"  每个完整电影的div
                xpath: //div[@class="info"] 获取的是每个电影的内容  不包含图片
                        ./div/a/span[1][@class="title"]/text()  获取25部电影的名字
                        ./div[2]/div/span[2]/text() 评分
                        ./div[2]/div/span[4]/text() 评价人数
                        ./div[2]/p[2]/span/text()  简述

实现流程: 
    1 先获取到电影的每个节点:
    2 再获取到的节点的基础上再去获取每个信息  通过筛选出来的数据
    3 
"""
import requests
from lxml import etree
import Queue
import time
import sys
import threading

reload(sys)
sys.setdefaultencoding('utf-8')


class DuBanTop250Spider():
    """豆瓣电影top250榜单"""

    def __init__(self):
        self.base_url = 'https://movie.douban.com/top250'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
        }
        self.dataQueue = Queue.Queue()
        self.num = 1

    def load_page(self, url):
        """发送url请求,返回响应的内容"""
        time.sleep(1)
        return requests.get(url, headers=self.headers).content

    def parse_page(self, url):
        """获取响应, 解析数据"""
        content = self.load_page(url)
        html = etree.HTML(content)
        node_list = html.xpath('//div[@class="info"]')  # 返回每个电影的节点
        for node in node_list:
            title = node.xpath('./div/a/span[1][@class="title"]/text()')[0]
            score = node.xpath('./div[2]/div/span[2]/text()')[0]
            num = node.xpath('./div[2]/div/span[4]/text()')[0]
            decs = node.xpath('./div[2]/p[2]/span/text()')
            if len(decs) == 0:
                decs = "没有简介".decode('utf-8')
            else:
                decs = decs[0]
            self.dataQueue.put(score + "\t\t" + title + "\t\t" + num + "\t\t" + decs)
            print threading.current_thread().name + '\t'+ url + '数据保存成功'
            # self.num += 1
        if url == self.base_url:
            # 返回所有的页码的链接
            return [self.base_url + link for link in html.xpath("//div[@class='paginator']/a/@href")]

    def main(self):
        link_list = self.parse_page(self.base_url)  # 返回最后的页码数据
        t_list = []
        # 开启多线程下载
        for link in link_list:
            t = threading.Thread(target=self.parse_page, args=(link,))
            t.start()
            t_list.append(t)
        # 加入等待
        for t in t_list:
            t.join()
        # 数据写入磁盘
        with open('./数据/豆瓣电影top250.text', 'w') as fp:
            while not self.dataQueue.empty():
                # print self.dataQueue.get()
                fp.write(str(self.num) + ".\t" + self.dataQueue.get())
                fp.write('.\n')
                self.num += 1


if __name__ == '__main__':
    spider = DuBanTop250Spider()
    start = time.time()
    spider.main()
    print '总的时间是:{}'.format(time.time() - start)

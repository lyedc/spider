# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TencentPipeline(object):
    """保存数据"""

    def __init__(self):
        """初始化管道"""
        self.fp = open('tencent.json', 'w')

    def process_item(self, item, spider):
        """保存文件"""
        json_obj = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.fp.write(json_obj)
        return item

    def close_spider(self, spider):
        """关闭文件"""
        self.fp.close()


class TencentCsv(object):
    """保存数据为csv格式的"""

    def open_spider(self, spider):
        """爬虫开始的时候"""
        print '我被执行了open_spider'
        self.fp = open('tencent.txt', 'w')

    def process_item(self, item, spider):
        """接受引擎给的数据"""
        print '我被调用了 process_item'
        json_csv = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.fp.write(json_csv)
        return item

    def close_spider(self, spider):
        """爬虫结束的时候调用这个函数"""
        print '我被调用了close_spider'
        self.fp.close()

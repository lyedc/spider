# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class JsonPipeline(object):
    """管道文件 来存储解析后返回的数据"""

    def __init__(self):
        """爬虫开始时候会初始这个类 调用一次"""
        self.fp = open('teacher006.json', 'w')

    def process_item(self, item, spider):
        """解析的过程中 会执行这个文件每次返回一个item 就会执行一次这个方法"""
        json_item = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.fp.write(json_item)
        return item

    def close_spider(self, spider):
        """在爬虫结束后会执行这个方法"""
        self.fp.close()


class CsvPinLine(object):
    """保存为csv文件格式"""

    def __init__(self):
        self.fp = open('teacher005.txt', 'w')

    def process_item(self, item, spider):
        json_csv = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.fp.write(json_csv)
        return item

    def close_spider(self, spider):
        self.fp.close()

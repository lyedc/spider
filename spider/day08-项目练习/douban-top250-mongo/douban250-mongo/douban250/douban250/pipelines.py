# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class Douban250Pipeline(object):
    def __init__(self):
        self.host = settings['MONGODB_HOST']  # 获取配置的主机名称 就是 ip地址
        self.port = settings['MONGODB_PORT']  # 端口号
        self.dbname = settings['MONGODB_DBNAME']  # 数据库名称
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.mdb = self.client[self.dbname]  # 选择数据库
        self.post = self.mdb[settings['MONGODB_DOCNAME']]  # 选择表明

    def process_item(self, item, spider):
        data = dict(item)
        # 向制定额表中的添加数据
        self.post.insert(data)
        return item

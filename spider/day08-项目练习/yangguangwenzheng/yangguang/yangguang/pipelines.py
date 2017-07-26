# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from .items import TouSuContent, DongguanItem

class ToSuItemPipeline(object):
    def __init__(self):
        self.fp = open('list.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, DongguanItem):
            print "管道中" ,"*" * 40
            json_data = json.dumps(dict(item), ensure_ascii=False)
            self.fp.write(json_data)
        return item

    def close_spider(self, spider):
        self.fp.close()


class ToSuContentPipeline(object):
    def __init__(self):
        self.fp = open('content.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TouSuContent):
            json_data = json.dumps(dict(item), ensure_ascii=False)
            self.fp.write(json_data)
        return item

    def close_spider(self, spider):
        self.fp.close()

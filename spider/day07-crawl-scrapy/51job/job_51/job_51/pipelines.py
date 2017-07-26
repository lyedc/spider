# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from .items import Job51Item
from .items import Detail51Content

class Job51Pipeline(object):
    def __init__(self):
        self.fp = open('tencent_list.txt', 'w')

    def process_item(self, item, spider):
        if isinstance(item, Job51Item):
            item_json = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.fp.write(item_json)
        return item

    def close_spider(self, spider):
        self.fp.close()


class Job51DetailPipeline(object):
    def __init__(self):
        self.fp = open('tencent_content.txt', 'w')

    def process_item(self, item, spider):
        if isinstance(item, Detail51Content):
            item_json = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.fp.write(item_json)
        return item

    def close_spider(self, spider):
        self.fp.close()

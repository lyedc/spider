# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import TencentItem
from .items import TencentContent

import json


class TencentItemPipeline(object):
    def __init__(self):
        self.fp = open('tencent_list.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            item_json = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.fp.write(item_json)
        return item

    def close_spider(self, spider):
        self.fp.close()


class TencentContentPipeline(object):
    def __init__(self):
        self.fp = open('tencent_content.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, TencentContent):
            item_json = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.fp.write(item_json)
        return item

    def close_spider(self, spider):
        self.fp.close()

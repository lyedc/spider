# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TencentMeatPipeline(object):
    def __init__(self):
        self.fp = open('tencent_detail.json', 'w')

    def process_item(self, item, spider):
        data_json = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.fp.write(data_json)
        return item

    def close_spider(self, spider):
        self.fp.close()

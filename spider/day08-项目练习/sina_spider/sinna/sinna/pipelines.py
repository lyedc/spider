# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import redis
from xpinyin import Pinyin


class DouyuImagesPipeline(ImagesPipeline):
    """完成图片的下载功能"""
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_url = item['vertical_src']
        yield scrapy.Request(image_url)


class SinnaPipeline(object):
    def process_item(self, item, spider):
        print item['subFilename']
        fp = open(item['subFilename'], 'w')
        content_json = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        fp.write(content_json)
        fp.close()
        return item


class RedisItem(object):
    """把数据保存在redis数据库中"""
    def __init__(self):
        self.conn = redis.Redis(host='127.0.0.1', port=6379)
        self.p = Pinyin()

    def process_item(self, item, spider):
        content_json = json.dumps(dict(item), ensure_ascii=False)
        key = self.p.get_pinyin(item['parentTitle'], "") + "/" + self.p.get_pinyin(item['subTitle'], "")
        self.conn.lpush(key, content_json)
        return item

# p = Pinyin()
# a=p.get_pinyin('上海'.decode('utf-8'),"")

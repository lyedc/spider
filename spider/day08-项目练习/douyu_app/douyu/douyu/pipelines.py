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


class DouyuImagesPipeline(ImagesPipeline):
    """完成图片的下载功能"""
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_url = item['vertical_src']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        """完成图片重新命名的功能"""
        # 从results 中取出来 图片的保存的相对的路径  然后对图片的路径进行重新的命名的操作 得到的是一个列表
        image_path = [x['path'] for ok, x in results if ok]
        item['image_path'] = self.IMAGES_STORE + item['nick_name'] + '.jpg'
        try:
            os.rename(self.IMAGES_STORE + image_path[0], item['image_path'])
        except:
            pass
        return item




"""

 def item_completed(self, results, item, info):
        if isinstance(item, dict) or self.images_result_field in item.fields:
            item[self.images_result_field] = [x for ok, x in results if ok]
        return item

[(True, {'url': 'https://rpic.douyucdn.cn/appCovers/2017/07/26/825860_20170726123202_big.jpg', 'path': 'full/e0415e2ba056c472fc1151ba4a2b3ad96d953941.jpg', 'checksum': 'e21ef03ee5845bc908f678b88925c077'})]


"""

class DouyuPipeline(object):
    """把斗鱼的信息保存在json文件中"""

    def __init__(self):
        self.fp = open('douyu.json', 'w')

    def process_item(self, item, spider):
        json_data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.fp.write(json_data)
        return item

    def close_spider(self, spider):
        self.fp.close()

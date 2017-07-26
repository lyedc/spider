# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # 每个帖子的编号
    number = scrapy.Field()
    # 每个帖子的标题
    title = scrapy.Field()
    # 每个帖子的状态
    statue = scrapy.Field()
    # 发帖人
    who = scrapy.Field()
    # 链接
    content_url = scrapy.Field()
    # 发帖时间
    date = scrapy.Field()


class TouSuContent(scrapy.Item):
    # 每个帖子的标题
    title = scrapy.Field()
    # 每个帖子的内容
    content = scrapy.Field()

    image_url = scrapy.Field()

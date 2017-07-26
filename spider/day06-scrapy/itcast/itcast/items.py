# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    """定义需要保存的字段名称"""
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()
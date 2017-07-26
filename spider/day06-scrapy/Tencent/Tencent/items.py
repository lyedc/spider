# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_name = scrapy.Field()
    position_category = scrapy.Field()
    position_num = scrapy.Field()
    position_city = scrapy.Field()
    position_date = scrapy.Field()
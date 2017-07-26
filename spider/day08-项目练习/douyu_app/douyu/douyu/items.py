# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    room = scrapy.Field()
    vertical_src = scrapy.Field()
    room_name = scrapy.Field()
    nick_name = scrapy.Field()
    online = scrapy.Field()
    game_name = scrapy.Field()
    anchor_city = scrapy.Field()
    image_path = scrapy.Field()

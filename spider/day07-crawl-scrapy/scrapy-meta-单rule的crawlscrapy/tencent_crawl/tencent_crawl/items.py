# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    """招聘信息的列表页面"""
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_catefory = scrapy.Field()
    position_num = scrapy.Field()
    position_city = scrapy.Field()
    position_date = scrapy.Field()



class TencentContent(scrapy.Item):
    """招聘信息的详情页面"""
    position_content = scrapy.Field()
    position_require = scrapy.Field()





# class List51Item(scrapy.Item):
#     """招聘信息的列表页面"""
#     position_name = scrapy.Field()
#     position_link = scrapy.Field()
#     position_company = scrapy.Field()
#     position_city = scrapy.Field()
#     position_salary = scrapy.Field()
#     position_date = scrapy.Field()
#
#
#
# class Detail51Content(scrapy.Item):
#     """招聘信息的详情页面"""
#     position_content = scrapy.Field()
#     position_require = scrapy.Field()

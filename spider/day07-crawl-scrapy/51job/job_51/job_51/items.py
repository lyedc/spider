# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_company = scrapy.Field()
    position_city = scrapy.Field()
    position_salary = scrapy.Field()
    position_date = scrapy.Field()



class Detail51Content(scrapy.Item):
    """招聘信息的详情页面"""
    position_name = scrapy.Field()
    position_city = scrapy.Field()
    position_salary = scrapy.Field()
    position_company = scrapy.Field()
    position_company_desc = scrapy.Field()
    position_work_year = scrapy.Field()
    position_info = scrapy.Field()

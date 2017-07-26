#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from Tencent.items import TencentItem
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TenCentSpider(scrapy.Spider):
    """腾讯职位"""
    name = "tencent"
    allowed_aomains = ['hr.tencent.com']
    base_url = 'http://hr.tencent.com/position.php?keywords=python&lid=2156&tid=0&start='
    off_set = 0
    start_urls = [base_url + str(off_set)]
    base_xpath = '//tr[@class="even"]|//tr[@class="odd"]'

    def parse(self, response):
        node_list = response.xpath(self.base_xpath)
        for node in node_list:
            item = TencentItem()
            item['position_name'] = node.xpath('./td/a/text()').extract_first()
            item['position_category'] = node.xpath('./td[2]/text()').extract_first()
            item['position_num'] = node.xpath('./td[3]/text()').extract_first()
            item['position_city'] = node.xpath('./td[4]/text()').extract_first()
            item['position_date'] = node.xpath('./td[5]/text()').extract_first()
            yield item

            self.off_set += 10
            if self.off_set <= 70:
                url = self.base_url + str(self.off_set)
                request = scrapy.Request(url, callback=self.go_parse)
                yield request

    def go_parse(self, response):
        print '调用的是自定义的parse'
        node_list = response.xpath(self.base_xpath)
        for node in node_list:
            item = TencentItem()
            item['position_name'] = node.xpath('./td/a/text()').extract_first()
            item['position_category'] = node.xpath('./td[2]/text()').extract_first()
            item['position_num'] = node.xpath('./td[3]/text()').extract_first()
            item['position_city'] = node.xpath('./td[4]/text()').extract_first()
            item['position_date'] = node.xpath('./td[5]/text()').extract_first()
            yield item

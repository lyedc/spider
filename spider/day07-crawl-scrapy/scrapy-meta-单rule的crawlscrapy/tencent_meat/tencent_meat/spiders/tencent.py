# -*- coding: utf-8 -*-
import scrapy
from tencent_meat.items import TencentMeatItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
需求: 给予上次的开发 完善自动获取下一页的的方案

"""


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    page_url = 'http://hr.tencent.com/'
    'position.php?&start=10#a'

    off_set = 0
    start_urls = ['http://hr.tencent.com/position.php?&start=0']
    base_xpath = '//tr[@class="even"]|//tr[@class="odd"]'
    page_xpath = '//a[@class="noactive" and @id="next"]'

    def parse(self, response):  # extract()
        node_list = response.xpath(self.base_xpath)
        for node in node_list:
            item = TencentMeatItem()
            item['position_name'] = node.xpath('./td/a/text()').extract_first()
            item['position_link'] = node.xpath('./td/a/@href').extract_first()
            item['position_category'] = node.xpath('./td[2]/text()').extract_first()
            item['position_num'] = node.xpath('./td[3]/text()').extract_first()
            item['position_city'] = node.xpath('./td[4]/text()').extract_first()
            item['position_date'] = node.xpath('./td[5]/text()').extract_first()
            yield item
        if not len(response.xpath(self.page_xpath)):
            url = self.page_url + response.xpath('//a[@id="next"]/@href').extract_first()
            request = scrapy.Request(url, callback=self.parse)
            yield request

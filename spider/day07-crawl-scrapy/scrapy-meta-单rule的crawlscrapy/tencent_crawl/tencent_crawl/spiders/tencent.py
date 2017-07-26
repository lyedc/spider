# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent_crawl.items import TencentItem
from tencent_crawl.items import TencentContent
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
"""
需求:  使用 crawlspider 来进行深度的爬取数据  使用第一层过滤 每个页面的地址
    使用第二层地址来过滤每个职位的详情页面的url地址
    rules 当过滤到地址后 就会自动的去发送请求 返回响应会去指定的回调函数来进行页面内容的解析
    当页面中的链接需要在进一步的去进行过滤的时候 就 把继续跟踪设置为false 

"""


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    base_url = 'http://hr.tencent.com/'
    start_urls = ['http://hr.tencent.com/position.php?&start=0']
    base_xpath = '//tr[@class="even"]|//tr[@class="odd"]'

    rules = (
        # 获取下一页的地址
        Rule(LinkExtractor(allow=r'position.php?&start=\d+'), callback='parse_item', follow=True),
        # 获取页面上内容详细页面的地址
        # Rule(LinkExtractor(allow=r'position_detail.php?id=\d+'), callback='parse_content', follow=False),
    )

    def parse_item(self, response):
        node_list = response.xpath(self.base_xpath)
        for node in node_list:
            item = TencentItem()
            item['position_name'] = node.xpath('./td/a/text()').extract_first()
            item['position_link'] = self.base_url + node.xpath('./td/a/@href').extract_first()
            item['position_category'] = node.xpath('./td[2]/text()').extract_first()
            item['position_num'] = node.xpath('./td[3]/text()').extract_first()
            item['position_city'] = node.xpath('./td[4]/text()').extract_first()
            item['position_date'] = node.xpath('./td[5]/text()').extract_first()
            yield item

    def parse_content(self, response):
        item = TencentContent()
        content_list = response.xpath('//tbody/tr[3]/td/ul//li/text()').extract()
        require_list = response.xpath('//tbody/tr[4]/td/ul//li/text()').extract()
        # 获取出来的数据是一个列表  需要组和起来全部存储
        item['position_content'] = " ".join(content_list)
        item['position_require'] = ' '.join(require_list)
        yield item

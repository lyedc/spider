# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yangguang.items import DongguanItem
from yangguang.items import TouSuContent
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class TousuSpider(CrawlSpider):
    name = 'tousu'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']
    base_xpath = '//div[@class="greyframe"]/table[2]/tbody/tr//tr'  # 获取到所有的tr
    rules = (
        Rule(LinkExtractor(allow=r'/questionType\?type=4&page=\d+'), callback='parse_item',
             follow=True),
        Rule(LinkExtractor(allow=r'question/\d+?/\d+?\.shtml'), callback='parse_content',
             follow=False),
        # process_links='get_link',
    )

    def get_link(self, links):
        if links:
            for link in links:
                print "*" * 40
                print '获取到的链接是:', link
                print "*" * 40

    def parse_item(self, response):
        node_list = response.xpath(self.base_xpath)
        for node in node_list:
            item = DongguanItem()
            item['number'] = node.xpath('./td[1]/text()').extract_first()
            item['title'] = node.xpath('./td[2]/a[2]/text()').extract_first()
            item['statue'] = node.xpath('./td[3]/span/text()').extract_first()
            item['who'] = node.xpath('./td[4]/text()').extract_first()
            item['content_url'] = node.xpath('./td[2]/a[2]/@href').extract_first()
            item['date'] = node.xpath('./td[5]/text()').extract_first()
            print "*" * 40
            yield item

    def parse_content(self, response):
        # 需要处理 带有图片和没有图片的额

        node_list = response.xpath('//div[@class="pagecenter p3"]/div[1]')
        for node in node_list:
            item = TouSuContent()
            item['title'] = node.xpath('./div[1]/div[1]/strong/text()').extract_first()
            # 根据有没有图片来分段处理
            if node.xpath('.//div[@class="textpic"]/img/@src'):
                item['image_url'] = node.xpath('.//div[@class="textpic"]/img/@src').extract_first()
                item['content'] = node.xpath('./div[2]/div[1]/div[2]/text()').extract_first()
            else:  # 没有图片
                item['image_url'] = "null"
                item['content'] = node.xpath('./div[2]/div[1]/text()').extract_first()
            yield item


"""
    '//div[@class="pagecenter p3"]/div[1]/div[1]/div[1]/strong/text()'
    # '//div[@class="pagecenter p3"]/div[1]/div[2]/div[1]/text()'
    # 有图片的内容的匹配
    '//div[@class="textpic"]/img/@src'
    # 标题还是原来的标题
    '//div[@class="pagecenter p3"]/div[1]/div[2]/div[1]/div[2]/text()'
    # 没有图片的图片的时候

"""

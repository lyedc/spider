# -*- coding: utf-8 -*-
import scrapy
from sinna.items import SinnaItem
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')


class Sina001Spider(scrapy.Spider):
    name = 'sina001'
    allowed_domains = ['sina.com.cn']
    start_urls = ["http://news.sina.com.cn/guide/"]
    base_xpath = '//div[@id="tab01"]//h3[@class="tit02"]/a/text()'  # 获取到所有的大标题  但是需要去掉最后一个 地方站的

    def parse(self, response):
        """处理大的分类"""

        # chuqu最后一个地方站的
        parent_node_list = response.xpath('//div[@id="tab01"]//h3[@class="tit02"]')
        parent_node_list.pop()

        # sub_node_list.pop()
        for parent_node in parent_node_list:
            parent_dir_name = parent_node.xpath('./a/text()').extract_first()
            parent_dir = os.path.join('./' + parent_dir_name)
            if not os.path.exists(parent_dir):
                os.mkdir(parent_dir)
            sub_node_list = parent_node.xpath('../ul/li')
            for sub_node in sub_node_list:
                item = SinnaItem()
                item['parentTitle'] = parent_node.xpath('./a/text()').extract_first()
                item['parentUrl'] = parent_node.xpath('./a/@href').extract_first()
                item['subTitle'] = sub_node.xpath('./a/text()').extract()[0]
                item['subUrl'] = sub_node.xpath('./a/@href').extract()[0]
                sub_dir = os.path.join(parent_dir + "/" + item['subTitle'])
                if not os.path.exists(sub_dir):
                    if not os.path.exists(parent_dir):
                        os.mkdir(parent_dir)
                        os.mkdir(sub_dir)
                    else:
                        os.mkdir(sub_dir)
                item['subFilename'] = sub_dir
                url = item["subUrl"]
                yield scrapy.Request(url, meta={'item': item}, callback=self.parse_sub)

    def parse_sub(self, response):
        meta_1 = response.meta['item']
        sub_link_list = response.xpath('//a/@href').extract()
        for link in sub_link_list:
            if link.startswith(meta_1['parentUrl']) and link.endswith('.shtml'):
                item = SinnaItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrl'] = meta_1['parentUrl']
                item['subTitle'] = meta_1['subTitle']
                item['subUrl'] = meta_1['subUrl']
                item['sonUrl'] = link
                item['subFilename'] = meta_1['subFilename'] + "/" + link[7:-6].replace('/', '_') + '.txt'
                yield scrapy.Request(item['sonUrl'], meta={'item': item}, callback=self.parse_content)

    def parse_content(self, response):
        """解析内容"""
        item = response.meta['item']
        item['head'] = response.xpath('//h1/text()').extract_first().strip()
        item['content'] = "".join(response.xpath('//div[@id="artibody"]//p//text()').extract()).strip()
        yield item

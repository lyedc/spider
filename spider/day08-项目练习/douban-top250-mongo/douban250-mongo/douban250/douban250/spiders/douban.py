# -*- coding: utf-8 -*-
import scrapy
from douban250.items import Douban250Item

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    base_url = 'https://movie.douban.com/top250'
    start_urls = [base_url]

    def parse(self, response):
        node_list = response.xpath('//div[@class="info"]')  # 返回每个电影的节点
        for node in node_list:
            item = Douban250Item()
            item['title'] = node.xpath('./div/a/span[1][@class="title"]/text()')[0]
            item['score']= node.xpath('./div[2]/div/span[2]/text()')[0]
            decs = node.xpath('./div[2]/p[2]/span/text()')
            if len(decs) == 0:
                item['decs'] = "没有简介".decode('utf-8')
            else:
                item['decs'] = decs[0]
            yield item

        node_page = response.xpath("//span[@class='next']/a/@href")
        if node_page:
            url = self.base_url + node_page.extract_first()
            yield scrapy.Request(url, callback=self.parse)



"""



"""
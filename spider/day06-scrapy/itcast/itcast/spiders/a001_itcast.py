# -*- coding: utf-8 -*-
import scrapy
from itcast.items import ItcastItem
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class A001ItcastSpider(scrapy.Spider):
    name = '001-itcast'  # 项目的文件名称
    allowed_domains = ['itcast.cn']  # 允许爬去的域名 没有这个就什么都允许 只能爬制定的
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#aandroid']  # 其实的url地址
    base_xpath = '//div[@class="tea_con"]/div[1]/ul/li/div[@class="li_txt"]'

    def parse(self, response):
        """解析返回的响应"""

        html_node = response.xpath(self.base_xpath)
        # teacher_list = []
        for node in html_node:
            item = ItcastItem()
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['level'] = node.xpath('./h4/text()').extract_first()
            item['info'] = node.xpath('./p/text()').extract_first()
            # teacher_list.append(item)
            yield item






        # html = response.body
        # with open('itcast.html', 'w') as fp:
        #     fp.write(html)

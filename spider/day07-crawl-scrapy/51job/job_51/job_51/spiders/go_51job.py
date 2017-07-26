# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from job_51.items import Job51Item
from job_51.items import Detail51Content
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Go51jobSpider(CrawlSpider):
    name = 'go_51job'
    allowed_domains = ['search.51job.com']
    start_urls = ['http://search.51job.com/list/010000%252C00,000000,0000,00,9,99,python,2,1.html?']
    base_xpath = '//div[@id="resultList"]/div[@class="el"]'
    rules = (
        # 每个列表页面的解析
        # 详情页面的  dizhi
        Rule(LinkExtractor(allow=r'python,2,\d+\.html\?'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/beijing-hdq/\d+\.html\?'), callback='parse_content', follow=False),

    )

    # 'http://jobs.51job.com/beijing-hdq/85458414.html?s=01&t=0'
    def parse_item(self, response):
        node_list = response.xpath(self.base_xpath)
        for node in node_list:
            item = Job51Item()
            item["position_name"] = node.xpath('./p/span/a/text()').extract_first()
            item["position_link"] = node.xpath('./p/span/a/@href').extract_first()
            item["position_company"] = node.xpath('./span[1]/a/text()').extract_first()
            item["position_city"] = node.xpath('./span[2]/text()').extract_first()
            item["position_salary"] = node.xpath('./span[3]/text()').extract_first()
            item["position_date"] = node.xpath('./span[4]/text()').extract_first()
            yield item

    def parse_content(self, response):
        print("+" * 40)
        print "shdfjslkdfjlsjdfl;s" + response.url
        item = Detail51Content()
        item["position_name"] = response.xpath('//div[@class="cn"]/h1/text()').extract_first()
        item["position_city"] = response.xpath('//div[@class="cn"]/span/text()').extract_first()
        item["position_salary"] = response.xpath('//div[@class="cn"]/strong/text()').extract_first()
        item["position_company"] = response.xpath('//div[@class="cn"]/p/a/text()').extract_first()
        item["position_company_desc"] = response.xpath('//div[@class="cn"]/p[2]/text()').extract_first()
        item["position_work_year"] = ' '.join(response.xpath('//div[@class="jtag inbox"]/div/span/text()').extract())
        item["position_info"] = response.xpath('//div[@class="bmsg job_msg inbox"]/text()').extract_first()
        yield item


"""
需求分析:
    拿到每个数据的地址: 的   //div[@id="resultList"]/div[@class="el"]  共50个
        具体的链接地址:  ./p/span/a/@href   http://jobs.51job.com/beijing-hdq/85458414.html?s=01&t=0
        职位名:  ./p/span/a/text()
        公司名称: ./span[1]/a/text()
        公司介绍链接: ./span[1]/a/@href    http://jobs.51job.com/all/co3836310.html
        地点:   ./span[2]/text()
        薪资:   ./span[3]/text()
        日期:    ./span[4]/text()
        下一页:  http://search.51job.com/list/010000,000000,0000,00,9,99,python,2,3.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=


        详情页面职位介绍://div[@class="cn"]/h1/text()
        详情页面工作地点介绍://div[@class="cn"]/span/text()
        详情页面薪资介绍://div[@class="cn"]/strong/text()
        详情页面公司名称://div[@class="cn"]/p/a/text()
        详情页面公司简介://div[@class="cn"]/p[2]/text()
        经验和福利:  //div[@class="jtag inbox"]/div/span/text()   shi  yige li biao  xu yao zu he 
        职位信息: //div[@class="bmsg job_msg inbox"]/text()
"""

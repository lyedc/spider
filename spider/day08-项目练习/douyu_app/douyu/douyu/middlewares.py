# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from settings import USER_AGENT_LIST
import random
import base64


class UserAgentMiddlewares(object):
    def process_request(self, request, spider):
        # 从指定的列表中获取一个user-agent
        user_agent = random.choice(USER_AGENT_LIST)
        # 给制定的请求报头设定一个默认的值
        request.headers['User-Agent'] = user_agent


"""
class ProxyMiddlewares(object):
    def process_request(self, request, spider):
        # 使用免费代理的配置
        proxy = '122.114.214.159:16816'
        request.meta['proxy'] = 'http://' + proxy
        # 使用独享代理的设置  需要代理的验证
        auth = 'mr_mao_hacker:sffqry9r'
        # 讲代理账户账户密码经过base64 转码
        base64_auth = base64.b64encode(auth)
        # 给制定的请求报头设定一个默认的代理值
        request.headers['Proxy-Authorization'] = 'Basic ' + base64_auth
"""



# 下面的是框架提供的代理的设定

# class DouyuSpiderMiddleware(object):

# # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)

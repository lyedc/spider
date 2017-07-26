# -*- coding: utf-8 -*-
import scrapy
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from douyu.items import DouyuItem

"""
需求: 抓取斗鱼app平台的直播信息
使用下载中间件 来完成随机user-agent 和 代理的切换

"""


class DouyuAppSpider(scrapy.Spider):
    name = 'douyu_app'
    allowed_domains = ['capi.douyucdn.cn']
    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=5&offset="
    off_set = 0
    start_urls = [base_url + str(off_set)]

    def parse(self, response):
        douyu_data = json.loads(response.body)['data']
        if not douyu_data:
            return
        for content in douyu_data:
            item = DouyuItem()
            item['room'] = "http://capi.douyucdn.cn/" + content['room_id']
            item['vertical_src'] = content['vertical_src']
            item['room_name'] = content['room_name']
            item['nick_name'] = content['nickname']
            item['online'] = content['online']
            item['game_name'] = content['game_name']
            item['anchor_city'] = content['anchor_city']
            yield item
        self.off_set += 20
        url = self.base_url + str(self.off_set)
        yield scrapy.Request(url, callback=self.parse)

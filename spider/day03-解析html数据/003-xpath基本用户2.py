# coding=utf-8
from lxml import etree



def xpath():
    """xpath的测试使用"""
    # 从本地文件中加载html文档
    html_parse = etree.parse('./html.html')
    # 转换为字符串
    # html_format = etree.tostring(html_parse)
    # 转化为标准的dom对象
    # html_dom = etree.HTML(html_format)
    li_a = html_parse.xpath('//li[@class="item-0"]/a/@href')
    li_text = html_parse.xpath('//li[@class="item-0"]/a/text()')
    li_a_text = html_parse.xpath('//li[@class="item-0"]/a[@href="link1.html"]/text()')
    li_span = html_parse.xpath('//li//span')
    print li_a
    # print li_a[0].tag
    print li_span
    # print li_a[1]
    # print li_text[0]
    # print type(li_text)

if __name__ == '__main__':
    xpath()

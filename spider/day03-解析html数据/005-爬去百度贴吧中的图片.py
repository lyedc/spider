# coding=utf-8
import urllib2
import urllib
from lxml import etree


def load_page(url, xpath_url):
    """加载页面"""
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()  # 返回获取到的html
    html_dom = etree.HTML(html)
    print "开始解析{}".format(url)
    url_list = html_dom.xpath(xpath_url)
    return url_list, html_dom


# 美女

def load_detail_page(url_list):
    """解析每个帖子的页面"""
    base_detail_url = 'https://tieba.baidu.com'
    page_xpath = '//ul[@class="l_posts_num"]/li/a/text()'
    image_xpath = '//img[@class="BDE_Image"]/@src'
    for url in url_list:
        detail_url = base_detail_url + url
        # 解析每个帖子  返回的是每个帖子中的图片地址
        image_url_list, html_dom = load_page(detail_url, image_xpath)
        page_list = html_dom.xpath(page_xpath)
        print "帖子{}解析完成".format(detail_url)
        save_image(image_url_list)


def save_image(image_url_list):
    """保存图片"""
    try:
        for img_url in image_url_list:
            urllib.urlretrieve(img_url, "./数据/" + img_url[-10:])
            print "帖子的图片{}解析完成".format(img_url[-10:])
    except Exception as err:
        print err


def main():
    name = raw_input('请输入贴吧的名称:>>>')
    start_page = int(raw_input('请输入开始的页面>>>'))
    end_page = int(raw_input('请输入结束的页面>>>'))
    base_url = 'https://tieba.baidu.com/f?'
    xpath_url = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
    for item in range(start_page, end_page + 1):
        page = (item - 1) * 50
        key_words = {
            "kw": name,
            "page": page
        }
        key_words = urllib.urlencode(key_words)
        url = base_url + key_words
        url_list, html_dom = load_page(url, xpath_url)
        load_detail_page(url_list)


if __name__ == '__main__':
    main()

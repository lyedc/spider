# coding=utf-8
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# print soup.prettify()  # 格式化输出
# print soup.title  #获取title的名称
#
# print soup.a  # 获取一个a标签
# print soup.a.name  # 获取一个a标签名名称 a
# print soup.a.attrs  # 所有的属性 返回的是一个字典的形式 class  是一个列表 意味着乐一个class 可以有多个类名
# print type(soup.a)  # 标签对象
# print soup.p['class']
# print soup.p.get('class')  # 雷鸣
# print soup.p.string  # 获取的是内容
#
# print soup.body.contents  # 返回的是list  所有的子节点
# print soup.body.children  # <listiterator object at 0x7f7ed1475b90>
# for item in soup.body.children:  #  可以进行迭代
#     print item
#
# print soup.find_all('b')  # 找所有的a标签
# print soup.find_all('a')
# for item in soup.find_all('a'):
#     print item
print  soup.find_all(id='link2')  # 按照id来进行查询
print soup.find_all(text='Tillie')  # 文档中字符串中的内容 返回的是一个列表
print soup.select('title')  # 返回的是列表
print soup.select('.sister')  # 返回的是列表 但会的是但钱的对象
print type(soup.select('.sister')[0])  # 返回的是一个tag对象
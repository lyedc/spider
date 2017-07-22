# coding=utf-8

from lxml import etree

text = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意次序缺少一个li标签</li>
     </ul>
 </div>
"""
# 把html格式的字符串转化为html形式的dom文档 并补充完成的html的dom类型
html = etree.HTML(text)
# 把html的dom对象 转换为html的字符串的形式
html = etree.tostring(html)
print html.encode('utf-8')


# 从文件中读取到html文档
html_tree = etree.parse('./html.html')
print html_tree  # <lxml.etree._ElementTree object at 0x7f5bf3b5c3b0>
print type(html_tree) #<type 'lxml.etree._ElementTree'>
html_format = etree.HTML(etree.tostring(html_tree))
print html_format # <Element html at 0x7f5bf3b5ca70>
print type(html_format) # <type 'lxml.etree._Element'>
html = etree.tostring(html_format)
print html  # 格式后的是一个标准的html格式的字符串形式
print type(html)  # <type 'str'>

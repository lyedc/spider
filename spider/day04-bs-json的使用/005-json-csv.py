# coding=utf-8
import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 创建json文件对象  从文件中 读取json数据
json_file = file('./数据/北京python.json', 'r')
# 读物本地磁盘json文件, 返回原来的数据类型:列表
content_list = json.load(json_file)

# 创建csv文件对象
csv_file = file('./数据/北京python.csv', 'w')
# 创建csv的读写对象 来操作csv
csv_write = csv.writer(csv_file)
# 获取表头部分
sheet =content_list[0].keys()
print sheet  # <built-in method keys of dict object at 0x7fd602a56e88>
# 将所有的数据放到一个大的列表里面  列表推倒式
data = [content.values() for content in content_list]
# 写入的是一行的数据 参数是一个列表
csv_write.writerow(sheet)
# 写入多行的数据 参数是一个列表
csv_write.writerows(data)
csv_file.close()
json_file.close()
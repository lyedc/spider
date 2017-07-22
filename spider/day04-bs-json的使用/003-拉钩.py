# coding=utf-8
import requests
import json
import jsonpath
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class LaGouSpider():
    def __init__(self):
        """初始化数据"""
        self.city_name = raw_input('请输入城市名称>>>')
        self.position_name = raw_input('请输入职位名称>>>')
        self.end_page = int(raw_input('请输入多少页>>>'))
        self.base_url = 'https://www.lagou.com/jobs/positionAjax.json?'
        self.page = 1
        self.key_words = {
            'city': self.city_name,
            'needAddtionalResult': 'false'
        }
        self.post_data = {
            "first": "true",
            "pn": self.page,
            "kd": self.position_name
        }
        self.headers = {
            "Cookie": "user_trace_token=20170719200729-d65ed04f-6c7a-11e7-a813-525400f775ce; LGUID=20170719200729-d65ed5db-6c7a-11e7-a813-525400f775ce; JSESSIONID=ABAAABAACDBABJB87F82A93D2286475B9328D5B23A57A84; _gat=1; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Di6kEVPc3RMuANaU4t_RKSbw50aSXlGkaGn9Wls1VKz3%26wd%3D%26eqid%3Da130402400005ae30000000359708999; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _putrc=F9E1E9830D38F5EC; login=true; unick=%E6%9C%B1%E8%B1%AA%E4%BA%AE; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500477953,1500478364,1500547617,1500547630; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500547843; _gid=GA1.2.477516447.1500466046; _ga=GA1.2.818797701.1500466046; LGSID=20170720184710-c86b0884-6d38-11e7-aca7-5254005c3644; LGRID=20170720185044-47ceb8c5-6d39-11e7-aca7-5254005c3644; TG-TRACK-CODE=index_search; SEARCH_ID=9d98588abf4f48e5a1a315b2cc33fd3f; index_location_city=%E5%8C%97%E4%BA%AC",
            "Host": "www.lagou.com",
            "Origin": "https://www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": "None",
            "X-Requested-With": "XMLHttpRequest"
        }
        self.work_list = []

    def load_page(self):
        """加载页面"""
        response = requests.post(self.base_url, params=self.key_words, data=self.post_data, headers=self.headers)
        json_obj = response.json()  # 返回的是一个字典 然后转换成json  存入文件中
        json_path = jsonpath.jsonpath(json_obj, '$..result')
        for item in json_path[0]:
            work_info = {}
            work_info['positionUrl'] = 'https://www.lagou.com/jobs/' + str(item['positionId']) + '.html'
            work_info['companyFullName'] = item['companyFullName']
            work_info['city'] = item['city']
            work_info['address'] = item['district']
            work_info['positionName'] = item['positionName']
            work_info['salary'] = item['salary']
            work_info['workYear'] = item['workYear']
            work_info['secondType'] = item['secondType']
            work_info['industryField'] = item['industryField']
            work_info['createTime'] = item['createTime']
            self.work_list.append(work_info)

    def la_gou_spider(self):
        """爬去调度"""
        while self.page <= self.end_page:
            self.load_page()
            self.page += 1
        print len(self.work_list)
        file_json = json.dumps(self.work_list, ensure_ascii=False)
        with open(self.city_name + self.position_name + '.json', 'w') as fp:
            fp.write(file_json)

    def start_spider(self):
        """启动工作"""
        self.la_gou_spider()


if __name__ == '__main__':
    la_gou_spider = LaGouSpider()
    la_gou_spider.start_spider()

"""
转换成json 存文件中
json_obj = json.dumps(response.json(), ensure_ascii=False)  # 返回的是一个字典 然后转换成json  存入文件中
with open('logou.json', 'w') as fp:
     fp.write(json_obj)
"""

"""
0
appShow
:
0
approve
:
1
businessZones
:
null
city
:
"北京"
companyFullName
:
"北京掌控世代科技有限公司"
companyId
:
49870
companyLabelList
:
["股票期权", "带薪年假", "定期体检", "年度旅游"]
companyLogo
:
"image1/M00/42/B4/Cgo8PFXMdCeATrFtAAA4a7G5khU136.png"
companyShortName
:
"掌控"
companySize
:
"15-50人"
createTime
:
"2017-07-20 09:03:56"
deliver
:
0
district
:
"海淀区"
education
:
"本科"
explain
:
null
financeStage
:
"成长型(A轮)"
firstType
:
"技术"
formatCreateTime
:
"09:03发布"
gradeDescription
:
null
imState
:
"today"
industryField
:
"移动互联网,电子商务"
industryLables
:
[]
jobNature
:
"全职"
lastLogin
:
1500531963000
pcShow
:
0
plus
:
null
positionAdvantage
:
"大用户,高速发展,技术导向,行业第一"
positionId
:
2405039
https://www.lagou.com/jobs/2405039.html
positionLables
:
["技术导向", "大用户", "纯移动端", "快速增长"]
positionName
:
"Python"
promotionScoreExplain
:
null
publisherId
:
649103
salary
:
"10k-20k"
score
:
0
secondType
:
"后端开发"
workYear
:
"1-3年"

"""

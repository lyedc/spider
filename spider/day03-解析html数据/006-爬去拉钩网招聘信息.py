# coding=utf-8
import requests
from urllib import parse


"""
标题:
//div[@class="cn"]//h1/text()|//div[@class="cn"]//span/text()|//div[@class="cn"]/strong/text()
//div[@class="cn"]//h1/text()|//div[@class="cn"]//span/text()|//div[@class="cn"]/strong/text()|//div[@class="bmsg job_msg inbox"]/span/text()|//div[@class="bmsg job_msg inbox"]/div/span/text()


"""


def load_page(url, post_data):
    """加载页面"""
    headers = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Cookie": "user_trace_token=20170719200729-d65ed04f-6c7a-11e7-a813-525400f775ce; LGUID=20170719200729-d65ed5db-6c7a-11e7-a813-525400f775ce; SEARCH_ID=740f28f4dad54d9dae18c3ddf98e3829; _gat=1; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fATEwT0J_Kg0FNkUsjqXyqu00000rhhYH300000F48l3L.THL0oUhY1x66dIjA80K85yF9pywdpAqVuNqsusK15HbsryfknH9-nj0snWnLmhR0IHYdnWF7wDndPbn4wRndwbcvn1nLrRNKn1DLPWRLnDckP0K95gTqFhdWpyfqnWbLrH03nj0znBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYE5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAn0mLFW5HfvrHRY%26tpl%3Dtpl_10085_15673_1%26l%3D1053927145%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%25259A%2525E6%25259C%2525BA%2526xp%253Did%28%252522m260704b2%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D128%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%2520%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26f%3D3%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26inputT%3D2030%26prefixsug%3Dlago%26rsp%3D1; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_user; JSESSIONID=ABAAABAABEEAAJA4E2E9930A6D5FB08D1A371BDFB7F933D; X_HTTP_TOKEN=d7064daf97de5e11b70aa7b20d843ad5; _ga=GA1.2.818797701.1500466046; _gid=GA1.2.477516447.1500466046; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500466050,1500477953; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500477980; LGSID=20170719232552-8d4aa212-6c96-11e7-ab99-5254005c3644; LGRID=20170719232620-9d995ff2-6c96-11e7-ab99-5254005c3644; _putrc=F9E1E9830D38F5EC; login=true; unick=%E6%9C%B1%E8%B1%AA%E4%BA%AE; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0"
    }
    response = requests.get(url, data=post_data, headers=headers)
    if response.status_code == 200:
        print(response.status_code)
        # html = response.content.decode('utf-8')
        json = response.content
        print(json)
        # with open('html.json', 'w') as fp:
        #     fp.write(json)
    else:
        print('请求出错')


def spider():
    """爬虫主程序"""
    # url = 'https://www.lagou.com/jobs/list_python?'
    base_url = 'https://www.lagou.com/jobs/positionAjax.json?'
    key_words = {
        'city': '北京',
        'needAddtionalResult': 'false'
    }
    post_data = {
        "first": "true",
        "pn": "1",
        "kd": "python"
    }
    key_words = parse.urlencode(key_words)
    url = base_url + key_words
    print(url)
    load_page(url, post_data)


if __name__ == '__main__':
    spider()

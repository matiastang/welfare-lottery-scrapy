'''
Author: matiastang
Date: 2022-08-09 17:50:16
LastEditors: matiastang
LastEditTime: 2022-08-17 18:05:39
FilePath: /welfare-lottery-scrapy/welfareLottery/welfareLottery/spiders/welfare_last_spider.py
Description: 爬取到目前为止最新的数据
'''
import scrapy
import json
from welfareLottery.items import WelfarelotteryItem

class WelfareLastSpider(scrapy.Spider):

    name = "welfare_last"
    # allowed_domains = ['cwl.gov.cn']

    # 地址相关
    urls = ['http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=10']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(self.name + 'parse')
        bodyStr = str(response.body, encoding='utf-8')
        # json字符串转换为dict
        body = json.loads(bodyStr)
        if body:
            result = body['result']
            for item in result:
                yield WelfarelotteryItem(code=item['code'], date=item['date'], red=item['red'], blue=item['blue'])
    
    # def closed(reason):
    #     print('welfare_last_spider closed')
'''
Author: matiastang
Date: 2022-08-09 17:50:16
LastEditors: matiastang
LastEditTime: 2023-03-06 19:48:44
FilePath: /welfare-lottery-scrapy/welfare-lottery-scrapy/welfareLottery/spiders/welfare_last_spider.py
Description: 爬取到目前为止最新的数据
'''
import scrapy
import json
from welfareLottery.items import WelfarelotteryItem
# import logging

# logging.getLogger("filelock").setLevel(logging.INFO)

class WelfareLastSpider(scrapy.Spider):

    name = "welfare_last"
    # allowed_domains = ['www.cwl.gov.cn']

    def __init__(self, count=None, *args, **kwargs):
        super(WelfareLastSpider, self).__init__(*args, **kwargs)
        self.start_urls = f'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount={count}'

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse, dont_filter=True)   

    def parse(self, response):
        bodyStr = str(response.body, encoding='utf-8')
        body = json.loads(bodyStr)
        if body:
            result = body['result']
            for item in result:
                yield WelfarelotteryItem(code=item['code'], date=item['date'], week=item['week'], red=item['red'], blue=item['blue'], content=item['content'], prizegrades=item['prizegrades'], sales=item['sales'], poolmoney=item['poolmoney'], videoLink=item['videoLink'], detailsLink=item['detailsLink'])
    
    def closed(self, reason):
        print('====== welfare_last_spider closed ======')
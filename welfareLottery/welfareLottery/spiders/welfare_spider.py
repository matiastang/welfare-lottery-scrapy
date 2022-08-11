'''
Author: matiastang
Date: 2022-08-09 17:50:16
LastEditors: matiastang
LastEditTime: 2022-08-11 12:16:00
FilePath: /welfare-lottery-scrapy/welfareLottery/welfareLottery/spiders/welfare_spider.py
Description: 
'''
import scrapy
import json
from welfareLottery.items import WelfarelotteryItem

class WelfareSpider(scrapy.Spider):

    name = "welfare"

    def start_requests(self):
        urls = [
            'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=300&issueStart=&issueEnd=&dayStart=&dayEnd=',
        ]
        for url in urls:
            HMF_CI_Cookie = 'a60ab06db4b776d3110d0b4e993449f018834c2094daa81e2df06925d2c07539ead7b1c3420b3495a6a635940aeddf9d5b8855cc2f172714e5d48cb58c104db10e; 21_vq=4'
            yield scrapy.Request(url=url, callback=self.parse, cookies={'HMF_CI': HMF_CI_Cookie})

    def parse(self, response):
        bodyStr = str(response.body, encoding='utf-8')
        # json字符串转换为dict
        body = json.loads(bodyStr)
        if body:
            result = body['result']
            # if result:
            #     def getItemValue(item):
            #         return {
            #             'code': item['code'],
            #             'date': item['date'],
            #             'red': item['red'],
            #             'blue' : item['blue'],
            #         }
            #     # 使用 list() 转换为列表，Python 3.x 返回迭代器。
            #     values = list(map(getItemValue, result))
            #     self.log('--------------response.body.result--------------')
            #     print(values)
            #     print(len(values))
            '''
            Selector有四个基本的方法，最常用的还是xpath:
            xpath(): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表
            extract(): 序列化该节点为字符串并返回list
            css(): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表，语法同 BeautifulSoup4
            re(): 根据传入的正则表达式对数据进行提取，返回字符串list列表
            '''
            for item in result:
                yield WelfarelotteryItem(code=item['code'], date=item['date'], red=item['red'], blue=item['blue'])
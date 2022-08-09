'''
Author: matiastang
Date: 2022-08-09 17:50:16
LastEditors: matiastang
LastEditTime: 2022-08-09 18:02:16
FilePath: /welfare-lottery-scrapy/welfareLottery/welfareLottery/spiders/welfare_spider.py
Description: 
'''
import scrapy

class WelfareSpider(scrapy.Spider):

    name = "welfare"

    def start_requests(self):
        urls = [
            'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=30&issueStart=&issueEnd=&dayStart=&dayEnd=',
        ]
        for url in urls:
            HMF_CI_Cookie = 'a60ab06db4b776d3110d0b4e993449f018834c2094daa81e2df06925d2c07539ead7b1c3420b3495a6a635940aeddf9d5b8855cc2f172714e5d48cb58c104db10e; 21_vq=4'
            yield scrapy.Request(url=url, callback=self.parse, cookies={'HMF_CI': HMF_CI_Cookie})

    def parse(self, response):
        self.log('--------------response.body--------------')
        self.log(response.body)
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
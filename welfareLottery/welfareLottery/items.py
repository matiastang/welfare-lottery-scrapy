'''
Author: matiastang
Date: 2022-08-09 17:07:12
LastEditors: matiastang
LastEditTime: 2022-08-11 11:02:18
FilePath: /welfare-lottery-scrapy/welfareLottery/welfareLottery/items.py
Description: items
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WelfarelotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 期号2021150
    code = scrapy.Field()
    # 时间2021-12-30(四)
    date = scrapy.Field()
    # 红球09,14,20,21,24,26
    red = scrapy.Field()
    # 篮球04
    blue = scrapy.Field()

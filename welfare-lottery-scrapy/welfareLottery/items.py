'''
Author: matiastang
Date: 2022-08-09 17:07:12
LastEditors: matiastang
LastEditTime: 2023-03-02 19:29:13
FilePath: /welfare-lottery-scrapy/welfare-lottery-scrapy/welfareLottery/items.py
Description: items
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WelfarelotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # 期号2021150
    code = scrapy.Field()
    # 时间2021-12-30(四)
    date = scrapy.Field()
    # week
    week = scrapy.Field()
    # 红球09,14,20,21,24,26
    red = scrapy.Field()
    # 篮球04
    blue = scrapy.Field()
    # content
    content = scrapy.Field()
    # prizegrades {type: 1, typenum: "1", typemoney: "10000000"}[]
    prizegrades = scrapy.Field()
    # sales
    sales = scrapy.Field()
    # poolmoney
    poolmoney = scrapy.Field()
    # videoLink
    videoLink = scrapy.Field()
    # detailsLink
    detailsLink = scrapy.Field()



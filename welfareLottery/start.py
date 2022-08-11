'''
Author: matiastang
Date: 2022-08-11 11:13:01
LastEditors: matiastang
LastEditTime: 2022-08-11 11:14:18
FilePath: /welfare-lottery-scrapy/welfareLottery/start.py
Description: 启动
'''
from scrapy import cmdline
cmdline.execute('scrapy crawl welfare'.split())
'''
Author: matiastang
Date: 2022-08-11 11:13:01
LastEditors: matiastang
LastEditTime: 2022-08-18 11:01:18
FilePath: /welfare-lottery-scrapy/welfareLottery/start.py
Description: 启动
'''
#!/usr/bin/python3
#coding=utf-8
import sys
from scrapy import cmdline

# process = CrawlerProcess()
# process.crawl(MySpider, category="electronics")

if __name__ == '__main__':

    argv = sys.argv
    argvLen = len(argv)
    if argvLen < 2:
        print('请添加welfare_last获取条数')
    else:
        # 运行welfare_last
        cmdline.execute(f'scrapy crawl welfare_last -a count={argv[argvLen - 1]}'.split())

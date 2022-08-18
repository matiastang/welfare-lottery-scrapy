'''
Author: matiastang
Date: 2022-08-11 11:13:01
LastEditors: matiastang
LastEditTime: 2022-08-18 11:17:30
FilePath: /welfare-lottery-scrapy/welfareLottery/start.py
Description: 启动
'''
#!/usr/bin/python3
#coding=utf-8
from ast import Try
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
        try:
            count = int(argv[argvLen - 1])
            # 运行welfare_last
            print('welfare_last获取条数需要在1~100') if count <= 0 or count > 100 else cmdline.execute(f'scrapy crawl welfare_last -a count={count}'.split())
        except ValueError as e:
            print('参数转换int错误', argv)
        

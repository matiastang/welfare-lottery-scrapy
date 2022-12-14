'''
Author: matiastang
Date: 2022-08-19 10:12:34
LastEditors: matiastang
LastEditTime: 2022-08-19 14:45:38
FilePath: /welfare-lottery-scrapy/welfareLottery/wl_apscheduler.py
Description: 定时任务
'''
#!/usr/bin/python3
#coding=utf-8

import subprocess
import time
from apscheduler.schedulers.blocking import BlockingScheduler
 
def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # cmdline.execute(f'scrapy crawl welfare_last -a count=1'.split())
    # 使用cmdline.execute报错：signal only works in main thread of the main interpreter
    # subprocess.Popen('scrapy crawl welfare_last -a count=1', shell=True)
    # 或者用run方法也行,Popen有安全隐患
    subprocess.run('scrapy crawl welfare_last -a count=1'.split())

if __name__ == '__main__':
    sched = BlockingScheduler()
    sched.add_job(
        id="0001", name="scrapy_welfare_last",
        func=my_job, trigger="cron",
        # day_of_week="1, 3, 6", hour="21", minute="30"
        day_of_week="4", hour="14", minute="44"
    )
    sched.start()
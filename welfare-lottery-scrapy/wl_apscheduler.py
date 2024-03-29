'''
Author: matiastang
Date: 2022-08-19 10:12:34
LastEditors: matiastang
LastEditTime: 2023-03-17 15:18:51
FilePath: /welfare-lottery-scrapy/welfare-lottery-scrapy/wl_apscheduler.py
Description: 定时任务
'''
#!/usr/bin/python3
#coding=utf-8

import subprocess
import time
from apscheduler.schedulers.blocking import BlockingScheduler
 
def run_scrapy_welfare_last():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # cmdline.execute(f'scrapy crawl welfare_last -a count=1'.split())
    # 使用cmdline.execute报错：signal only works in main thread of the main interpreter
    # subprocess.Popen('scrapy crawl welfare_last -a count=1', shell=True)
    # 或者用run方法也行,Popen有安全隐患
    subprocess.run('scrapy crawl welfare_last -a count=1'.split())

if __name__ == '__main__':
    sched = BlockingScheduler()
    # 定时获取
    sched.add_job(
        func=run_scrapy_welfare_last, trigger="cron",
        day_of_week="1, 3, 6", hour="22", minute="00"
    )
    # 定时更新
    sched.add_job(
        func=run_scrapy_welfare_last, trigger="cron",
        day_of_week="0, 2, 4", hour="1", minute="00"
    )
    sched.start()
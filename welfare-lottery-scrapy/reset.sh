#!/bin/bash  
###
 # @Author: matiastang
 # @Date: 2023-03-09 19:48:07
 # @LastEditors: matiastang
 # @LastEditTime: 2023-03-17 15:26:17
 # @FilePath: /welfare-lottery-scrapy/welfare-lottery-scrapy/reset.sh
 # @Description: 重置定时任务
### 
source /etc/profile
ps -ef | grep wl_apscheduler.py | grep -v grep | awk '{print $2}' | xargs kill -9
cd /var/mt-project/mt-scrapy/welfare-lottery-scrapy/
nohup python3 ./wl_apscheduler.py >>output.out 2>&1 &
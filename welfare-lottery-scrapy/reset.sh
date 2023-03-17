#!/bin/bash  
###
 # @Author: matiastang
 # @Date: 2023-03-09 19:48:07
 # @LastEditors: matiastang
 # @LastEditTime: 2023-03-17 15:48:15
 # @FilePath: /welfare-lottery-scrapy/welfare-lottery-scrapy/reset.sh
 # @Description: 重置定时任务
### 
source /etc/profile
# ps -ef | grep wl_apscheduler.py | grep -v grep | awk '{print $2}' | xargs kill -9
PID=`ps -ef | grep wl_apscheduler.py | grep -v grep | awk '{print $2}'`
if [ "$PID" = "" ] 
then 
    echo "切换路径：/var/mt-project/mt-scrapy/welfare-lottery-scrapy/"
    cd /var/mt-project/mt-scrapy/welfare-lottery-scrapy/
    echo "启动：wl_apscheduler.py"
    nohup python3 ./wl_apscheduler.py >>output.out 2>&1 &
    echo "启动完成"
else
    echo "关闭任务：$PID"
    kill -9 $PID
    echo "切换路径：/var/mt-project/mt-scrapy/welfare-lottery-scrapy/"
    cd /var/mt-project/mt-scrapy/welfare-lottery-scrapy/
    echo "重启：wl_apscheduler.py"
    nohup python3 ./wl_apscheduler.py >>output.out 2>&1 &
    echo "重启完成"
fi
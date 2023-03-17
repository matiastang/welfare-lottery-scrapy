#!/bin/bash  
###
 # @Author: matiastang
 # @Date: 2023-03-09 19:48:07
 # @LastEditors: matiastang
 # @LastEditTime: 2023-03-09 19:48:14
 # @FilePath: /welfare-lottery-scrapy/welfare-lottery-scrapy/stop.sh
 # @Description: 更具文件名称结束任务
### 
source /etc/profile
nohup echo "hello world"
ps -ef|grep "文件名称" | grep -v grep| awk '{print "kill -9 " $2}' 
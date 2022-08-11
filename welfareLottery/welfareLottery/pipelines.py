'''
Author: matiastang
Date: 2022-08-09 17:07:12
LastEditors: matiastang
LastEditTime: 2022-08-11 12:40:01
FilePath: /welfare-lottery-scrapy/welfareLottery/welfareLottery/pipelines.py
Description: pipelines
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class WelfarelotteryPipeline:

    def __init__(self) -> None:
        self.connect = pymysql.connect(
            host='127.0.0.1',
            db="mt_scrapy",
            user="root",
            passwd="MySQL_18380449615",
            charset='utf8',
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def open_spider(self, spider):
        print('open_spider')

    def process_item(self, item, spider):
        print('---process_item---')
        print(item)
        # sql = """
        #     insert into welfare_lottery_ssq(%s) value(%s)
        # """ % (','.join([k for k, v in item()]), ','.join(["%s" for k, v in item()]))
        # self.cursor.execute(sql, [v for k, v in item()])
        sql = """
            insert into welfare_lottery_ssq(code, date, red, blue) value(%s, %s, %s, %s)
        """
    
        try:
            self.cursor.execute(sql, [item['code'], item['date'], item['red'], item['blue']])
            print(item['code'] + '保存成功----')
            self.connect.commit()
            # post_id = self.cursor.lastrowid

        except:
            print(item['code'] + '保存失败----')
            self.connect.rollback()

        return item

    def close_spider(self, spider):
        print('close_spider')
        self.connect.close()
        self.cursor.close()
'''
Author: matiastang
Date: 2022-08-09 17:07:12
LastEditors: matiastang
LastEditTime: 2023-11-10 10:51:16
FilePath: /welfare-lottery-scrapy/welfare-lottery-scrapy/welfareLottery/pipelines.py
Description: pipelines
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import json

class WelfarelotteryPipeline:

    def __init__(self) -> None:
        self.connect = pymysql.connect(
            host='127.0.0.1',
            db="mt_scrapy",
            user="matias",
            passwd="matias_18380449615",
            charset='utf8',
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        # self.connect = pymysql.connect(
        #     # host="${{secrets.TDY_HOST}}",
        #     # db="${{secrets.TDY_MYSQL_SCRAPY_DB}}",
        #     # user="${{secrets.TDY_MYSQL_USER}}",
        #     # passwd="${{secrets.TDY_MYSQL_PASSWD}}",
        #     host='110.41.145.30',
        #     db="mt_scrapy",
        #     user="matiastang",
        #     # user="root",
        #     passwd="MySQL_18380449615",
        #     charset='utf8',
        #     use_unicode=True,
        #     cursorclass=pymysql.cursors.DictCursor
        # )
        print('====== mysql链接成功 ======')
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        # 查询最新一条数据
        sql = """
            SELECT * FROM welfare_lottery_double ORDER BY code DESC LIMIT 1
        """
        self.cursor.execute(sql)
        # 这是获取表中最后的数据
        result = self.cursor.fetchone()
        if result:
            self.lastCode = result['code'] if result['code'] else None
        else:
            self.lastCode = None
        print('====== lastCode: ', self.lastCode)

    def open_spider(self, spider):
        print('====== open_spider ======')

    def process_item(self, item, spider):
        print('====== process_item ======')
        insertSql = """
            insert into welfare_lottery_double(code, date, week, red, blue, content, prize_grades, sales, poolmoney, video_link, details_link) value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        updateSql = """
            UPDATE welfare_lottery_double SET
            date=%s,
            week=%s,
            red=%s,
            blue=%s,
            content=%s,
            prize_grades=%s,
            sales=%s,
            poolmoney=%s,
            video_link=%s,
            details_link=%s
            WHERE code=%s
        """
        prizegrades = json.dumps(list(map(lambda info: { 'type': str(info['type']), 'num': info['typenum'], 'money': info['typemoney'] }, item['prizegrades'])))
        # name区分爬虫
        if spider.name == 'welfare_last':
            if self.lastCode == None or int(item['code']) > int(self.lastCode):
                try:
                    self.cursor.execute(insertSql, [item['code'], item['date'], item['week'], item['red'], item['blue'], item['content'], prizegrades, item['sales'], item['poolmoney'], item['videoLink'], item['detailsLink']])
                    print(item['code'] + '====== 新增成功 ======')
                    self.connect.commit()

                except:
                    print(item['code'] + '====== 新增失败 ======')
                    self.connect.rollback()
            else:
                # if int(item['code']) > int(self.lastCode):
                #     try:
                #         self.cursor.execute(insertSql, [item['code'], item['date'], item['week'], item['red'], item['blue'], item['content'], prizegrades, item['sales'], item['poolmoney'], item['videoLink'], item['detailsLink']])
                #         print(item['code'] + '====== add保存成功 ======')
                #         self.connect.commit()

                #     except:
                #         print(item['code'] + '====== add保存失败 ======')
                #         self.connect.rollback()
                print(updateSql, [item['date'], item['week'], item['red'], item['blue'], item['content'], prizegrades, item['sales'], item['poolmoney'], item['videoLink'], item['detailsLink'], item['code']])
                try:
                    self.cursor.execute(updateSql, [item['date'], item['week'], item['red'], item['blue'], item['content'], prizegrades, item['sales'], item['poolmoney'], item['videoLink'], item['detailsLink'], item['code']])
                    print(item['code'] + '====== 更新成功 ======')
                    self.connect.commit()

                except:
                    print(item['code'] + '====== 更新失败 ======')
                    self.connect.rollback()
            
            return item
    
        try:
            self.cursor.execute(insertSql, [item['code'], item['date'], item['week'], item['red'], item['blue'], item['content'], prizegrades, item['sales'], item['poolmoney'], item['videoLink'], item['detailsLink']])
            print(item['code'] + '====== 保存成功 ======')
            self.connect.commit()

        except:
            print(item['code'] + '====== 保存失败 ======')
            self.connect.rollback()

        return item

    def close_spider(self, spider):
        print('====== close_spider ======')
        self.connect.close()
        self.cursor.close()
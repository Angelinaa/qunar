# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
"""
class QunarspiderPipeline(object):

    cityInsert = '''insert into city(city_id,city_name,province,area) values \
    ('{city_id}','{city_name}','{province}','{area}')'''

    def process_item(self, item, spider):
        sqlinsert = self.cityInsert.format(
            city_id=item['city_id'],
            city_name=item.get('city_name'),
            province=item.get('province'),
            area=item.get('area')
        )
        self.cursor.execute(sqlinsert)
        return item

    def open_spider(self, spider):
        self.connect = pymysql.connect('localhost', 'root', '123456', 'test', charset='utf8', use_unicode=True)
        self.cursor = self.connect.cursor()
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
"""
class QunarspiderPipeline(object):
    cityInsert = '''insert into city(city_id,city_name,province,area) values \
        ('{city_id}','{city_name}','{province}','{area}')'''

    def process_item(self, item, spider):

        sqlinsert = self.cityInsert.format(
            city_id=item['city_id'],
            city_name=item.get('city_name'),
            province=item.get('province'),
            area=item.get('area')
        )
        self.cursor.execute(sqlinsert)
        print("已存入数据库！！！")
        return item

    def open_spider(self, spider):
        self.connect = pymysql.connect('localhost', 'root', '123456', 'test', charset='utf8', use_unicode=True)
        self.cursor = self.connect.cursor()
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


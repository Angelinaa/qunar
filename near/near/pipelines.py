# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class NearPipeline(object):
    scenicInsert1 = '''INSERT INTO nearby_shop VALUES ('{shop_id}','{shop_name}','{distance}','{score}')'''
    def process_item(self, item, spider):
        sqlinsert = self.scenicInsert1.format(
            shop_id=item.get('shop_id'),
            shop_name=item.get('shop_name'),
            distance=item.get('distance'),
            score=item.get('score')
        )
        self.cursor.execute(sqlinsert)
        #self.cursor.execute(testinsert)
        print("已存入数据库！！！")
        return item

    def open_spider(self, spider):
        self.connect = pymysql.connect('localhost', 'root', '123456', 'test', charset='utf8', use_unicode=True)
        self.cursor = self.connect.cursor()
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


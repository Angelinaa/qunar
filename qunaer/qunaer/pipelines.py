
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class QunaerPipeline(object):
    scenicInsert1 = '''INSERT INTO sight VALUES ('{scenic_id}','{scenic_name}','{city_id}','{rank}','{introduction}','{playtime}','{score}','{address}','{phone_number}','{open_time}','{ticket}','{season}','{transport}','{comment_num}','{num_5}','{num_4}','{num_3}','{num_2}','{num_1}','{good_comment_num}','{middle_comment_num}','{bad_comment_num}')'''
    def process_item(self, item, spider):
        sqlinsert = self.scenicInsert1.format(
            scenic_id=item.get('scenic_id'),
            scenic_name=pymysql.escape_string(item.get('scenic_name')),
            city_id=pymysql.escape_string(item.get('city_id')),

            rank=item.get('rank'),
            introduction=item.get('introduction'),
            playtime=item.get('playtime'),
            score=item.get('score'),
            address=item.get('address'),
            phone_number=item.get('phone_number'),
            open_time=item.get('open_time'),
            ticket=item.get('ticket'),
            season=item.get('season'),
            transport=item.get('transport'),
            comment_num=item.get('comment_num'),
            num_5=item.get('num_5'),
            num_4=item.get('num_4'),
            num_3=item.get('num_3'),
            num_2=item.get('num_2'),
            num_1=item.get('num_1'),
            good_comment_num = item.get('good_comment_num'),
            middle_comment_num = item.get('middle_comment_num'),
            bad_comment_num =item.get('bad_comment_num')
        )
        print("介绍！！！",item.get('introduction'))
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


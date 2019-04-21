# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class ScenicItem(scrapy.Item):
    pass

class sceItem(scrapy.Item):
    scenic_id = scrapy.Field()
    scenic_name = scrapy.Field()
    city_id = scrapy.Field()
    rank = scrapy.Field()
    introduction = scrapy.Field()
    playtime = scrapy.Field()
    score = scrapy.Field()
    address = scrapy.Field()
    phone_number = scrapy.Field()
    open_time = scrapy.Field()
    ticket = scrapy.Field()
    season = scrapy.Field()
    transport = scrapy.Field()
    comment_num = scrapy.Field()
    num_5 = scrapy.Field()
    num_4 = scrapy.Field()
    num_3 = scrapy.Field()
    num_2 = scrapy.Field()
    num_1 = scrapy.Field()
    good_comment_num = scrapy.Field()
    middle_comment_num = scrapy.Field()
    bad_comment_num = scrapy.Field()





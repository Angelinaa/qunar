# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NearItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class near_scenic_Item(scrapy.Item):
    shop_id=scrapy.Field()
    shop_name = scrapy.Field()
    distance = scrapy.Field()
    score = scrapy.Field()
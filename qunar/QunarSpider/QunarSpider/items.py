# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunarspiderItem(scrapy.Item):
    pass


class CityItem(scrapy.Item):
    # define the fields for your item here like:
    city_id = scrapy.Field()
    city_name = scrapy.Field()
    province = scrapy.Field()
    area = scrapy.Field()



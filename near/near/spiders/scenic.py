# -*- coding: utf-8 -*-
import scrapy
from near.items import near_scenic_Item

import pymysql
from scrapy import Request
import re
import time,random

class ScenicSpider(scrapy.Spider):
    name = "scenic"
    allowed_domains = ["travel.qunar.com"]
    def start_requests(self):
        self.connect = pymysql.connect('localhost', 'root', '123456', 'test', charset='utf8', use_unicode=True)
        self.cursor = self.connect.cursor()
        self.connect.autocommit(True)
        sql1 = """select url from jingdian"""
        self.cursor.execute(sql1)
        results1 = self.cursor.fetchall()
        start_urls =list(results1)
        random.shuffle(start_urls)
        for each_url in start_urls:
            #print("目前url", each_url)
            print("目前url[0]",each_url[0])
            request=Request(each_url[0],callback=self.parse_sight,dont_filter=True)
            time.sleep(random.random() * 5)
            yield request


    def parse_sight(self, response):
        near_scenic=response.xpath('//div[@class="listbox clrfix"]/div[@class="contbox box_padd"]/ul[@class="list_item "]')[2].xpath('./li[@class="item"]')
        for each_scenic in near_scenic:
            item = near_scenic_Item()
            url=each_scenic.xpath('./div[@class="t clrfix"]/a[@class="tit"]/@href').extract()[0]
            item['shop_id']=re.findall(r'\d+', url)[0]
            item['shop_name']=each_scenic.xpath('./div[@class="t clrfix"]/a[@class="tit"]/@title').extract()[0]
            item['distance']=each_scenic.xpath('./div[@class="t"]/span[@class="distance"]/text()').extract()[0]
            item['score']=each_scenic.xpath('./div[@class="t"]/span[@class="total_star"]/span[@class="cur_star"]/@style').extract()[0][6:]
            print(item)
            yield item
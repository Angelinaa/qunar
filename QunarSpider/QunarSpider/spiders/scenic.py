# -*- coding: utf-8 -*-
import scrapy
from QunarSpider.items import CityItem

class ScenicSpider(scrapy.Spider):
    name = "scenic"
    allowed_domains = ["travel.qunar.com"]
    start_urls = ['http://travel.qunar.com/place/?from=header']

    def parse(self, response):
        #直辖市
        city_name = response.xpath('//ul[@class="list_item  clrfix"]/li/a/text()').extract()
        for each_city_name in city_name:
            item = CityItem()
            item['city_id']=response.xpath('//ul[@class="list_item  clrfix"]/li/a/@href').extract()[0][28:34]
            item['city_name'] = each_city_name
            item['province']="直辖市"
            item['area'] = "直辖市"
            #print(item)
            yield item
        #国内除直辖市外其他城市
        city_name2=response.xpath('//ul[@class="list_item patch_pl clrfix"]/li[@class="item "or "item last"]')
        for each_city_name2 in city_name2:
            item2 = CityItem()
            item2['city_id']=each_city_name2.xpath('./a/@href').extract()[0][28:34]
            item2['city_name'] = each_city_name2.xpath('./a/text()').extract()[0]
            item2['province']=each_city_name2.xpath('./../../div[@class="titbox"]/span/text()').extract()[0][:-1]
            item2['area'] = each_city_name2.xpath('./../../../../dt/text()').extract()[0]
            #print(item2)
            yield item2
# -*- coding: utf-8 -*-
import scrapy
from sight.items import SightItem
from scrapy import Request
import time,random


class ScenicSpider(scrapy.Spider):
    name = "scenic"
    allowed_domains = ["travel.qunar.com"]
    start_urls = ['http://travel.qunar.com/p-cs300020-chenzhou-jingdian-1-'+ str(i+1) for i in range(30)]
    custom_settings = {
        "ITEM_PIPELINES": {
            'sight.pipelines.SightPipeline': 100
        },
        "DEFAULT_REQUEST_HEADERS": {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'zh-CN,zh;q=0.9',
            'referer': 'http://travel.qunar.com/p-cs1003249-taihu-jingdian-1-1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        },
        "ROBOTSTXT_OBEY": False  # 需要忽略ROBOTS.TXT文件
    }

    """def start_requests(self):
        scenic_url = '''http://travel.qunar.com/p-cs299914-beijing-jingdian-1-{page}'''
        requests = []
        print("1进来了")
        #循环点击下一页按钮
        for i in range(200):
            print("2进来了")
            url=scenic_url.format(page=i+1)
            request = Request(url, callback=self.parse_sight,dont_filter=True)
            print("url=",url)
            requests.append(request)
            time.sleep(random.random() * 3)
            print("3进来了")
        return requests"""


    def parse(self, response):
        ScenicItems = []
        sight_name= response.xpath('//ul[@class="list_item clrfix"]/li[@class="item"]')
        #print("sightname=",sight_name)
        for each_sight_name in sight_name:
            line=each_sight_name.xpath('./div[@class="ct"]/div[@class="titbox clrfix"]/a[@class="titlink"]/span[@class="cn_tit"]/text()').extract()
            item=SightItem()
            if line!=None:
                item['sight_name'] = line[0]
            #print(item['sight_name'])
            if each_sight_name.xpath('./div[@class="ct"]/div[@class="titbox clrfix"]/a[@class="titlink"]/@href').extract() != None:
                item['url'] = each_sight_name.xpath('./div[@class="ct"]/div[@class="titbox clrfix"]/a[@class="titlink"]/@href').extract()[0]
            ScenicItems.append(item)
            yield item
            print(item)
        #time.sleep(random.random() * 1)
        #return ScenicItems

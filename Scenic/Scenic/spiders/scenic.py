# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
import json
from Scenic.items import sceItem

class ScenicSpider(scrapy.Spider):
    name = 'scenic'
    allowed_domains = ["piao.qunar.com"]


    custom_settings = {
        "ITEM_PIPELINES": {
            'Scenic.pipelines.ScenicPipeline': 300
        },
        "DEFAULT_REQUEST_HEADERS": {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'zh-CN,zh;q=0.9',
            'referer': 'http://piao.qunar.com/ticket/list.htm?keyword=%E5%8C%97%E4%BA%AC&region=%E5%8C%97%E4%BA%AC&from=mpl_search_suggest&page=1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        },
        "ROBOTSTXT_OBEY": False  # 需要忽略ROBOTS.TXT文件
    }
    def start_requests(self):
        city="北京"
        scenic_url = '''http://piao.qunar.com/ticket/list.json?keyword={city}&region={city}&from=mpl_search_suggest&page={page}'''
        requests = []
        #循环点击下一页按钮
        for i in range(5):
            request = Request(scenic_url.format(city=city,page=i+1), callback=self.parse_scenic)
            requests.append(request)
        return requests

    def parse_scenic(self, response):
        #print(response.body.decode())
        jsonBody = json.loads(response.body.decode())
        subjects = jsonBody['data']['sightList']
        ScenicItems = []
        city = "北京"
        for subject in subjects:
            item = sceItem()
            item['scenic_id'] = int(subject['sightId'])
            item['scenic_name'] = subject['sightName']
            item['city_id'] = city
            item['rank'] = ""  #
            item['introduction'] = subject['intro']
            item['playtime'] = "" #
            item['score'] = subject['score']
            item['address'] = subject['address']
            item['phone_number'] = "" #
            item['open_time'] = "" #
            item['ticket'] = subject['qunarPrice']
            item['season'] = "" #
            item['transport'] = "" #

            comment_url='''http://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId={sightId}&index=1&page=1&pageSize=100&tagType=0'''
            Request(url=comment_url.format(sightId=item['scenic_id']), meta={'item': item}, callback=self.comment_Info)
            ScenicItems.append(item)
            #print(item)

        return ScenicItems

    def comment_Info(self, response):
        item = response.meta['item']
        jsonBody = json.loads(response.body.decode())
        subjects = jsonBody['data']['tagList']
        for subject in subjects:
            if subject['tagName']=="全部":
                item['comment_num'] = subject['tagNum']  #
            item['num_5'] = 0  #
            item['num_4'] = 0  #
            item['num_3'] = 0  #
            item['num_2'] = 0 #
            item['num_1'] = 0  #
            if subject['tagName'] == "好评":
                item['good_comment_num'] = subject['tagNum']
            if subject['tagName'] == "中评":
                item['middle_comment_num'] = subject['tagNum']
            if subject['tagName'] == "差评":
                item['bad_comment_num'] = subject['tagNum']
        #print(item)
        yield item




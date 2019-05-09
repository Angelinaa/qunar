# -*- coding: utf-8 -*-
import scrapy
from qunaer.items import QunaerItem
#from qunaer.items import near_scenic_Item
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
        #print("数据类型！",type(results1))
        start_urls =list(results1)
        random.shuffle(start_urls)
        #print("打乱后的列表",start_urls)
        for each_url in start_urls:
            #print("目前url", each_url)
            print("目前url[0]",each_url[0])
            request=Request(each_url[0],callback=self.parse_sight,meta={'url':each_url[0]},dont_filter=True)
            time.sleep(random.random() * 5)
            yield request


    def parse_sight(self, response):
        url=response.request.meta['url']

        item = QunaerItem()
        item['scenic_id'] = re.findall(r'\d+', url)[0]
        print("scenic_id=", item['scenic_id'])
        item['scenic_name'] = response.xpath('//div[@class="b_title clrfix"]/h1[@class="tit"]/text()').extract()[0]
        print("item['scenic_name']=", item['scenic_name'])
        cityname=response.xpath('//div[@class="e_crumbs"]/ul[@class="clrfix"]/li[@class="item pull"]/a/@title').extract()[1]
        print("cityname=",cityname)
        item['city_id'] =cityname

        item['rank'] = response.xpath('//div[@class="txtbox"]/div[@class="ranking"]/span[@class="sum"]/text()').extract()[0]
        if response.xpath('//div[@class="b_detail_section b_detail_summary"]/div[@class="e_db_content_box"]/p[@class="inset-p"]/text()').extract() != []:
            item['introduction'] = response.xpath('//div[@class="b_detail_section b_detail_summary"]/div[@class="e_db_content_box"]/p[@class="inset-p"]/text()').extract()[0]
        else: item['introduction']="null"
        if response.xpath('//div[@class="txtbox"]/div[@class="time"]/text()').extract()!=[]:
            item['playtime'] = response.xpath('//div[@class="txtbox"]/div[@class="time"]/text()').extract()[0][7:]
        else:item['playtime'] = "null"
        if response.xpath('//div[@class="scorebox clrfix"]/span[@class="cur_score"]/text()').extract()!=[]:
            item['score'] = response.xpath('//div[@class="scorebox clrfix"]/span[@class="cur_score"]/text()').extract()[0]
        else:
            item['score'] = "null"
        if response.xpath('//td[@class="td_l"]/dl/dd/span/text()').extract()!=[]:
            item['address'] = response.xpath('//td[@class="td_l"]/dl/dd/span/text()').extract()[0]
            item['phone_number'] = response.xpath('//td[@class="td_l"]/dl')[1].xpath('./dd/span/text()').extract()[0]
            item['open_time'] = \
            response.xpath('//td[@class="td_r"]/dl[@class="m_desc_right_col"]/dd/span/p/text()').extract()[0]
        else:
            item['address'] = "null"
            item['phone_number'] = "null"
            item['open_time'] = "null"
        if response.xpath('//div[@class="b_detail_section b_detail_ticket"]/div[@class="e_db_content_box e_db_content_dont_indent"]/p/text()').extract()!=[]:
            item['ticket'] = response.xpath('//div[@class="b_detail_section b_detail_ticket"]/div[@class="e_db_content_box e_db_content_dont_indent"]/p/text()').extract()[0]
            item['season'] = response.xpath('//div[@class="b_detail_section b_detail_travelseason"]/div[@class="e_db_content_box e_db_content_dont_indent"]/p/text()').extract()[0]
            item['transport'] = response.xpath('//div[@class="b_detail_section b_detail_traffic"]/div[@class="e_db_content_box e_db_content_dont_indent"]/p/text()').extract()[0]
        else:
            item['ticket'] = "null"
            item['ticket'] = "null"
            item['ticket'] = "null"
        if response.xpath('//div[@class="b_detail_section b_detail_comment"]/div[@class="e_title_box"]/h3/span[@class="num"]/text()').extract()!=[]:
            item['comment_num'] = response.xpath('//div[@class="b_detail_section b_detail_comment"]/div[@class="e_title_box"]/h3/span[@class="num"]/text()').extract()[0][1:-1]
            item['num_5'] = response.xpath('//div[@class="b_detail_section b_detail_comment"]/div[@class="star-filter"]/div[@class="star-top"]/ul[@class="top-mid"]/li/div[@class="total"]/div[@class="rate"]/@style').extract()[0][7:]
            item['num_4'] = response.xpath('//div[@class="b_detail_section b_detail_comment"]/div[@class="star-filter"]/div[@class="star-top"]/ul[@class="top-mid"]/li/div[@class="total"]/div[@class="rate"]/@style').extract()[1][7:]
            item['num_3'] = response.xpath('//div[@class="b_detail_section b_detail_comment"]/div[@class="star-filter"]/div[@class="star-top"]/ul[@class="top-mid"]/li/div[@class="total"]/div[@class="rate"]/@style').extract()[2][7:]
            item['num_2'] = response.xpath('//div[@class="b_detail_section b_detail_comment"]/div[@class="star-filter"]/div[@class="star-top"]/ul[@class="top-mid"]/li/div[@class="total"]/div[@class="rate"]/@style').extract()[3][7:]
            item['num_1'] = response.xpath('//div[@class="b_detail_section b_detail_comment"]/div[@class="star-filter"]/div[@class="star-top"]/ul[@class="top-mid"]/li/div[@class="total"]/div[@class="rate"]/@style').extract()[4][7:]
            item['good_comment_num'] = item['num_5']
            item['middle_comment_num'] = item['num_3']
            item['bad_comment_num'] = item['num_1']
        else:
            item['comment_num'] = "null"
            item['num_5'] = "null"
            item['num_4'] = "null"
            item['num_3'] = "null"
            item['num_2'] = "null"
            item['num_1'] = "null"
            item['good_comment_num'] = "null"
            item['middle_comment_num'] = "null"
            item['bad_comment_num'] = "null"

        print(item)
        yield item
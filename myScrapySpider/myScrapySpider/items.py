# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 我们自己要抓取的数据
    # 职位名称
    positionName = scrapy.Field()
    # 职位详情链接
   # positionLinke = scrapy.Field()
    # 职位类别
   # positionType = scrapy.Field()
    # 招聘人数
   # positionNum = scrapy.Field()
    #　地点
   # address = scrapy.Field()
    # 发布时间
   # publishTime = scrapy.Field()
    
    
    

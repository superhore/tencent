# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyscrapyspiderPipeline(object):
    
    def __init__(self):
        self.fileName = open("tecent.json", "wb")
        
    def process_item(self, item, spider):
        """
        保存json的本地文件
        """
        text = json.dumps(dict(item), 
                          ensure_ascii=False)+'\n'
        self.fileName.write(text.encode('utf-8'))
        return item
    
    def close_spider(self, spider):
        # 关闭爬虫时同时关闭json文件
        self.fileName.close()
    

#class MyscrapyspiderPipeline2(object):
#    def process_item(self, item, spider):
#        """
#        保存到mysql
#        """
#        return item
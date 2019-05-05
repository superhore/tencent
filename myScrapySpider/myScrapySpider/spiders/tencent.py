# -*- coding: utf-8 -*-
import scrapy
from myScrapySpider.items import MyscrapyspiderItem
from bs4 import BeautifulSoup


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    url = "https://hr.tencent.com/position.php?keywords=python&lid=2156&tid=87&start="
    offset = 0
    start_urls = [url+str(offset)+"#a"]
    
#    for i in range(0,111,10):
#        url = "https://hr.tencent.com/position.php?keywords=python&lid=2156&tid=87&start="+str(i)+"#a"
#        start_urls.append(url)

    def parse(self, response):
        """
          接受Download传回的response信息，
          我们需要提取出我们真正需要的信息
        """
#//*[@id="position"]/div[1]/table/tbody/tr[2]
#//*[@id="position"]/div[1]/table/tbody/tr[2]
#//*[@id="position"]/div[1]/table/tbody/tr[2]/td[1]/a
#//*[@id="position"]/div[1]/table/tbody/tr[2]/td[2]
#//*[@id="position"]/div[1]/table/tbody/tr[2]/td[3]
        
        #for each in response.xpath('//*[@id="position"]/div[1]/table/tbody/tr[2]'):
        #    print(each.xpath('./td[1]/a/text()'))

        #print(response.xpath('//*[@id="position"]/div[1]/table/tbody/tr[2]/td[1]/a'))
        #print('--------------------------')
        """
        for i in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            print(i.xpath('./td[1]/a/text()').extract()[0])


        //*[@id="position"]/div[1]/table/tbody/tr[4]/td[1]/a

	In [1]: title = response.xpath('//*[@id="post-112614"]/div[1]/h1/text()') 
        In [2]: print(title) [<Selector xpath='//*[@id="post-112614"]/div[1]/h1/text()' data='为什么 SQL 正在击败 NoSQL，数据的未来是什么。'>] 
        In [3]: print(title.extract()) ['为什么 SQL 正在击败 NoSQL，数据的未来是什么。']  """

        #print(response.text)

        item = MyscrapyspiderItem()
        soup = BeautifulSoup(response.text)
        for i in soup.select('a[target="_blank"]'):
            if '-' in i.string:
                item['positionName'] = i.string
                yield item
                
            #if "-" in i.string:
        #print(soup.select('a[target="_blank"]'))
        print("----------------------------------------")

        

#        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
 #           item = MyscrapyspiderItem()
            # 职位名称
  #          item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            # 职位详情链接
   #         item['positionLinke'] = "https://hr.tencent.com/"+each.xpath('./td[1]/a/@href').extract()[0]
            # 职位类别
    #        item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            # 招聘人数
     #       item['positionNum'] = each.xpath('./td[3]/text()').extract()[0]
            #　地点
      #      item['address'] = each.xpath('./td[4]/text()').extract()[0]
            # 发布时间
       #     item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]
            
            # 将item数据给管道文件
        #    yield item
        
        # 翻页的另一种实现
        # 注意：这里最好的做法是把这里的nextPageUrl通过正则匹配出来
        if self.offset < 111:
            self.offset += 10
            nextPageUrl = self.url+str(self.offset)+"#a"
        else:
            return
        # 对下一页发起请求
        yield scrapy.Request(nextPageUrl, callback=self.parse)
            

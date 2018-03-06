# -*- coding: utf-8 -*-
import scrapy
import random


visited=['https://en.wikipedia.org/wiki/%C3%86thelfl%C3%A6d']
unvisited = []
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = []
    start_urls = ['https://en.wikipedia.org/wiki/%C3%86thelfl%C3%A6d']



    def parse(self, response):
        pass
        #self.settings.DUPEFILTER_DEBUG = True




        #print("Existing settings: %s" % self.settings.attributes.keys())
       # p_tag = response.xpath("//*[@class='span6'] ")
       # for quote in p_tag:
        #    wiki = response.xpath('//*[@class="mw-parser-output"]/p/text()').extract()
         #   print()

        wiki = response.xpath('//*[@class="mw-parser-output"]/p/text()').extract()
       # print (wiki)


        urls = response.xpath('//*/p/a/@href').extract()
        urls1=[]
        for x in urls:
            if "/wiki/" in x:
                if "/file:" not in x:
                  urls1.append(x)



        p= len(urls1)

        rand = random.randint(0,p-1)

        next_page_url = urls1[rand]


        for x in urls1:
            if x not in visited:
                unvisited.append(x)

        absolute_next_page_url = response.urljoin(next_page_url)
        try:
            yield scrapy.Request(absolute_next_page_url,callback=self.parse, dont_filter=True)
            visited.append(urls1[rand])
        except  :
            p = len(unvisited)
            rand = random.randint(0, p - 1)
            next_page_url = unvisited[rand]
            absolute_next_page_url = response.urljoin(next_page_url)

            yield scrapy.Request(absolute_next_page_url, callback=self.parse, dont_filter=True)


        #scrapy crawl -s "DUPEFILTER_DEBUG"=True -s "dont_filter"=True quotes
        #scrapy crawl -s "dont_filter"=True quotes





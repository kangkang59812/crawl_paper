# -*- coding: utf-8 -*-
import scrapy
from ..items import EccvItem
import pdb


class EccvSpider(scrapy.Spider):
    name = 'eccv'
    allowed_domains = ['eccv.com']
    start_urls = ['http://eccv.com/']
    User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    url = 'http://openaccess.thecvf.com/ECCV2018.py'

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.parse, headers={'User-Agent': self.User_Agent})

    def parse(self, response):
        title = []
        au = []
        id = []
        for paper in response.xpath("//dl/dt/a/text()"):
            title.append(paper.extract())
        for i,authors in enumerate(response.xpath("//dl/dd")):
            if i%2==0:
                aa=[]
                for one in authors.xpath('./form/a/text()').extract():
                    aa.append(one)
                    #pdb.set_trace()
                print('i=====%d',i)
                au.append(aa)
        #pdb.set_trace()
        for i in range(len(title)):
            item = EccvItem()
            item['PaperID'] = str(i+1)
            item['Type'] = 'Poster'
            item['Title'] = title[i]
            item['Authors'] = au[i]
            print('save %d', i)
            yield item


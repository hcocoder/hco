# -*- coding: utf-8 -*-
import scrapy
import os

from kkp.items import KkpItem


class WallhavenSpider(scrapy.Spider):
    name = 'wallhaven'
    allowed_domains = ['alpha.wallhaven.cc']
    start_urls = ['https://alpha.wallhaven.cc/'
                  'search?q=&categories=010&purity=100&resolutions=1920x1080&sorting='
                  's&order=asc']

    def parse(self, response):

        img_url=response.xpath('//li//a[@class="preview"]/@href').extract()
        next_page=response.xpath('//span[@class="thumb-listing-page-num"]/text()').extract_first()
        n=int(next_page)
        for img in  img_url:
            item = KkpItem()
            yield scrapy.Request(url=img,meta={'item':item} ,callback=self.img_parse)
            n=n+1
            next_url='https://alpha.wallhaven.cc/' \
                 'search?q=&categories=010&purity=100&resolutions=1920x1080&sorting=views&order=asc&page='+str(n)
            yield  scrapy.Request(url=next_url,callback=self.parse)

    def img_parse(self,response):
        item= response.meta["item"]
        item['img_url']='https:'+response.xpath('//img[@id="wallpaper"]/@src').extract_first()

        return item






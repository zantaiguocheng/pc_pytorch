# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pytorch.items import PytorchItem


class WendangSpider(CrawlSpider):
    name = 'wendang'
    allowed_domains = ['pytorch.apachecn.org']
    start_urls = ['http://pytorch.apachecn.org/cn/docs/0.3.0/index.html']

    rules = (
        Rule(LinkExtractor(allow=r'[a-z]+\.html',),
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = PytorchItem()
        item['file_urls'] = [response.url]
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item

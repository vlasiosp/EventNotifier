# -*- coding: utf-8 -*-
import scrapy


class FbCrawlSpider(scrapy.Spider):
    name = 'fb_crawl'
    allowed_domains = ['https://mobile.facebook.com/search/photos/?q=%CF%87%CE%B1%CE%BD%CE%B9%CE%B1']
    start_urls = ['http://https://mobile.facebook.com/search/photos/?q=%CF%87%CE%B1%CE%BD%CE%B9%CE%B1/']

    def parse(self, response):
        pass

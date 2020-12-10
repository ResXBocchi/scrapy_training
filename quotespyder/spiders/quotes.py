# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        title = response.css('title::text').extract_first()
        tags = response.css('.tag-item a::text').extract()

        yield{
            'Title':title,
            'Tags':tags
        }
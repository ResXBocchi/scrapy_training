# -*- coding: utf-8 -*-
import scrapy
from quotespyder.items import QuotespyderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        quotes = response.xpath('//*[@class="quote"]')

        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@class="tag"]/text()').extract()

            item = QuotespyderItem()

            item['text'] = text
            item['author'] = author
            item['tags'] = tags

            yield item

        next_page_url = response.xpath('.//*[@class="next"]/a/@href').extract_first()
        next_page = response.urljoin(next_page_url)

        yield scrapy.Request(next_page)
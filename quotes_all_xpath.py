# -*- coding: utf-8 -*-
import scrapy

# focus on multiple quotes on the first page
class QuotesAllSpider(scrapy.Spider):
    name = 'quotes_all_xpath'
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log('My Spider just visited: ' + response.url)

        # using XPATH selectors
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//span[@class="text"]/text()').extract_first()
            author = quote.xpath('.//small[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//meta[@class="keywords"]/@content').extract_first()

            print ('\n')
            print (text)
            print (author)
            print (tags)
            print ('\n')

            yield {

            'quote': text,
            'author': author,
            'tags': tags,
            }
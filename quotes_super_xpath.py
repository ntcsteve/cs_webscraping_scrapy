# -*- coding: utf-8 -*-
import scrapy

# focus on multiple quotes on the first page
class QuotesAllSpider(scrapy.Spider):
    name = 'quotes_super_xpath'
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log('My Spider just visited: ' + response.url)
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//span[@class="text"]/text()').extract_first()
            author = quote.xpath('.//small[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//meta[@class="keywords"]/@content').extract_first()

            yield {

            'quote': text,
            'author': author,
            'tags': tags,
            }

        # follow the pagination link
        next_page_href = response.xpath('//li[@class="next"]/a/@href').extract_first()
        
        # stop crawling when the spider reached to the last page
        if next_page_href:
            next_page_url = response.urljoin(next_page_href)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
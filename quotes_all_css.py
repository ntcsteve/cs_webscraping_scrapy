# -*- coding: utf-8 -*-
import scrapy

# focus on multiple quotes on the first page
class QuotesAllSpider(scrapy.Spider):
    name = 'quotes_all_css'
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log('My Spider just visited: ' + response.url)

        # using CSS selectors
        quotes = response.css('div.quote')
        for quote in quotes:
            item = {
                'text' : quote.css('span.text::text').extract_first(),
                'author' : quote.css('small.author::text').extract_first(),
                'tags' : quote.css('a.tag::text').extract(),
            }

            yield item
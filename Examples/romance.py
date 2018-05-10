# -*- coding: utf-8 -*-
import scrapy

class RomanceSpider(scrapy.Spider):
    name = 'romance'
    allowed_domains = ["booktopia.com.au"]
    start_urls = ['https://www.booktopia.com.au/romance-fiction-bestsellers/promo299.html']

    # spider - crawl - find out each href on the current page
    def parse(self, response):
    	urls = response.xpath('//div[@class="cover-container"]/a/@href').extract()
    	for url in urls:
    		url = response.urljoin(url)
    		yield scrapy.Request(url=url, callback=self.parse_details)

    # spider - scrape - a simple example to extract the title and the price
    def parse_details(self, response):
    	yield {
    	'Title': response.xpath('.//div[@id="product-title"]/h1/text()').extract_first(),
        'Price': response.xpath('.//div[@id="price"]//div[@class="sale-price"]/text()').extract_first(),
        }
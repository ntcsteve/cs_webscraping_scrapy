# -*- coding: utf-8 -*-
import scrapy

class BooksAllSpider(scrapy.Spider):
    name = 'books_all'
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['http://books.toscrape.com/index.html']

    # spider - crawl
    def parse(self, response):

        # a loop to crawl through every designated URL on the current page
    	urls = response.xpath('//article[@class="product_pod"]/h3/a/@href').extract()
    	for url in urls:
    		url = response.urljoin(url)

            # once the spider reached the designated URL, call parse_details to extract data
    		yield scrapy.Request(url=url, callback=self.parse_details)

    # spider - scrape 
    def parse_details(self, response):

        # creating a dictionary to store extracted data from the current page
    	yield {

    	'Title': response.xpath('.//div[@class="col-sm-6 product_main"]/h1/text()').extract_first(),
        'Price': response.xpath('.//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').extract_first(),
        'Description': response.xpath('.//div[@id="content_inner"]/article/p/text()').extract_first(),
    	
        }
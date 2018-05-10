# -*- coding: utf-8 -*-
import scrapy

class BooksAllSpider(scrapy.Spider):
    name = 'books_super_all'
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['http://books.toscrape.com/index.html']

    # spider - crawl
    def parse(self, response):
    	urls = response.xpath('//article[@class="product_pod"]/h3/a/@href').extract()
    	for url in urls:
    		url = response.urljoin(url)
    		yield scrapy.Request(url=url, callback=self.parse_details)

        # follow the pagniation link
    	next_page_href = response.xpath('//li[@class="next"]/a/@href').extract_first()

        # stop crawling when the spider reached to the last page
    	if next_page_href:
    		next_page_url = response.urljoin(next_page_href)
    		yield scrapy.Request(url=next_page_url, callback=self.parse)

    # spider - scrape 
    def parse_details(self, response):
    	yield {

    	'Title': response.xpath('.//div[@class="col-sm-6 product_main"]/h1/text()').extract_first(),
        'Price': response.xpath('.//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').extract_first(),
        'Description': response.xpath('.//div[@id="content_inner"]/article/p/text()').extract_first(),
    	
        }
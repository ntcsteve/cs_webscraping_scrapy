# -*- coding: utf-8 -*-
import scrapy

class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    allowed_domains = ["pokemondb.net"]
    start_urls = ['http://pokemondb.net/pokedex/all']

    # spider - crawl - find out each href on the current page
    def parse(self, response):
    	urls = response.xpath('//a[@class="ent-name"]/@href').extract()
    	for url in urls:
    		url = response.urljoin(url)
    		yield scrapy.Request(url=url, callback=self.parse_details)

    # spider - scrape - a simple example to extract the name and the location for each pokemon
    def parse_details(self, response):
    	yield {
    	'Pokemon': response.xpath('.//article/h1/text()').extract_first(),
        'Location': response.xpath('.//div[@class="col desk-span-7 lap-span-12"]/table[@class="vitals-table"]/tbody/tr/td/a/@href').extract(),    	
        }
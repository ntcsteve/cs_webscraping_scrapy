# -*- coding: utf-8 -*-
import scrapy

# base url to work with
base_url = "https://www.goodfood.com.au/recipes/recipe-collections/glutenfree-20160601-gp9061"

class RecipesSpider(scrapy.Spider):
    name = 'recipes'
    allowed_domains = ["goodfood.com.au"]
    start_urls = ['https://www.goodfood.com.au/recipes/recipe-collections/glutenfree-20160601-gp9061']
    
    # spider - crawl - find out each href on the current page
    def parse(self, response):
        self.log('My Spider just visited: ' + response.url)
        urls = response.xpath('//article[@class="story story--stacked"]/figure/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        # example - construct the next pagination link manually 
        for page in range(2, 4):
            new_url = base_url + "?p=" + str(page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    # spider - scrape - a simple example to extract the title, the description and the ingredients
    def parse_details(self, response):
        yield {
            'Title': response.xpath('.//header[@class="article__header"]/h1/text()').extract_first(),
            'Description': response.xpath('.//p[@class="recipe__summary"]/text()').extract_first(),
            'Ingredients': response.xpath('.//div[@class="recipe__instructions--ingredients"]/p/text()').extract(),
        }
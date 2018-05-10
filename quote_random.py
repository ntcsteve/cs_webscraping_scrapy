# -*- coding: utf-8 -*-
import scrapy

# focus on one random quote per page
class QuotesRandomSpider(scrapy.Spider):

    # name must be unique for each project
    name = 'quotes_random'

    # this setting is useful for broad crawls, if the domain of the URL is not in this setting, then the URL would be ignored.
    allowed_domains = ["quotes.toscrape.com"]

    # starting URL for our spider to crawl
    start_urls = ['http://quotes.toscrape.com/random']

    # a method that will be called to handle the response downloaded for each of the requests made.
    def parse(self, response):

    	# a simple notification that my spider visited the requested URL
        self.log('My Spider just visited: ' + response.url)

        # using CSS selectors
        # extract_first() will extract the first element as a string
        # extract() will extract data as a list
        text = response.css('span.text::text').extract_first()
        author = response.css('small.author::text').extract_first()
        tags = response.css('a.tag::text').extract()

        print ("\n")
        print (text)
        print (author)
        print (tags)
        print ("\n")

        # creating a dictionary with the extracted value
        yield {
 
            'quote': text,
        	'author': author,
        	'tags': tags,
        }
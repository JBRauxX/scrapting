# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BukkrawlSpider(CrawlSpider):
    name = 'bukkrawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-1.html']

    le_book_details = LinkExtractor(restrict_css='h3 > a')

    rule_book_details = Rule(le_book_details, callback='parse_item', follow=False)
    
    rules = (
        rule_book_details,
    )

    def parse_item(self, response):
        yield {
            'Title': response.css('h1 ::text').get(),
            'Category': response.xpath('//ul[@class="breadcrumb"]/li[last()-1]/a/text()').get(),
            'Link': response.url
        }

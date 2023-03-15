import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UserkrawlPSpider(CrawlSpider):
    name = 'userkrawl_p'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html']
    le_book_details = LinkExtractor(restrict_css='h3 > a')
    le_next = LinkExtractor(restrict_css='.next > a')
    rule_book_details = Rule(le_book_details, callback='parse_item', follow=False)
    rule_next = Rule(le_next, follow=True)
    rules = (
        rule_book_details,
        rule_next
    )

    def parse_item(self, response):
        yield {
            'Title': response.css('h1 ::text').get(),
            'Category': response.xpath('//ul[@class="breadcrumb"]/li[last()-1]/a/text()').get(),
            'Link': response.url
        }

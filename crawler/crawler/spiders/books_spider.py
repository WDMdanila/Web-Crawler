import scrapy
from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response, **kwargs):
        item = BookItem()

        for prod in response.css('.product_pod'):
            item['title'] = prod.css('h3 a::attr(title)').get()
            item['price'] = prod.css('div .price_color::text').get()
            item['in_stock'] = True if prod.css('.icon-ok').get() else None
            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            item['title'] = 'FINISHED PROCESSING'
            item['price'] = '%123321%'
            yield item

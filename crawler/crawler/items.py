import scrapy


class SteamItem(scrapy.Item):
    name = scrapy.Field()
    normal_price = scrapy.Field()
    sale_price = scrapy.Field()
    quantity = scrapy.Field()

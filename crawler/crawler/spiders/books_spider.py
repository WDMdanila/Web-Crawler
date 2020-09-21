import scrapy
from ..items import SteamItem


class SteamSpider(scrapy.Spider):
    name = 'agents'
    start_urls = ["https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_Type_CustomPlayer&appid=730"]
    page_num = 1

    def parse(self, response, **kwargs):
        item = SteamItem()

        for prod in response.css('div .market_listing_row'):
            item['name'] = prod.css('.market_listing_item_name::text').get()
            item['normal_price'] = prod.css('.normal_price .normal_price::text').get()
            item['sale_price'] = prod.css('.sale_price::text').get()
            item['quantity'] = prod.css('.market_listing_num_listings_qty ::attr(data-qty)').get()
            yield item

        if not response.css('#searchResults_btn_next.pagebtn.disabled').get():
            self.page_num += 1
            page = response.url + f'#p{self.page_num}_popular_desc'
            yield scrapy.Request(page, callback=self.parse)
        else:
            item['name'] = 'FINISHED PROCESSING'
            item['normal_price'] = '%123321%'
            item['sale_price'] = '%123321%'
            yield item

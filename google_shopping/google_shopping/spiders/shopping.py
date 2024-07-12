from typing import Any
import scrapy
import csv
from google_shopping.items import GoogleShoppingItem


class ShoppingSpider(scrapy.Spider):
    name = "shopping"
    allowed_domains = ["www.google.com"]
    with open('lista_compra.csv', 'r') as f:
        shop_list = list(csv.reader(f, delimiter=';'))
        print(shop_list)
    start_urls = [f"https://www.google.com/search?q={shop_list[0][0].replace(' ', '+')}&tbm=shop"]
    custom_settings = {
		'DOWNLOAD_DELAY': 10, # seconds of delay
        'RANDOMIZE_DOWNLOAD_DELAY': True
		}

    def parse(self, response):
        print(response)
        products = response.css('div.sh-dgr__content')
                
        product_item = GoogleShoppingItem()

        for product in products:
            product_item['description'] = product.css('h3.tAxDx::text').get()
            product_item['vendor'] = product.css('div.aULzUe.IuHnof::text').get()
            product_item['link'] = product.css('a.shntl::attr(href)').get()
            product_item['price'] = product.css('span.a8Pemb.OFFNJ::text').get()
            product_item['image'] = product.css('div.ArOc1c img::attr(src)').get()

            yield product_item

        for item_list in self.shop_list[1:]:
            next_page = f"https://www.google.com/search?q={item_list[0].replace(' ', '+')}&tbm=shop"
            yield response.follow(next_page, callback=self.parse)


# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GoogleShoppingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    vendor = scrapy.Field()
    link = scrapy.Field()
    image = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BotLazadaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Tensanpham = scrapy.Field()
    Giasanpham = scrapy.Field()
    Danhgia = scrapy.Field()
    pass

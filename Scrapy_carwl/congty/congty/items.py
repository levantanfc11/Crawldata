# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CongtyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Tencongty = scrapy.Field()
    Linhvuc = scrapy.Field()
    Quocgia = scrapy.Field()
    pass

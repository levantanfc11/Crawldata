# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HosodoanhnghiepItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Tendoanhnghiep = scrapy.Field()
    Diachi = scrapy.Field()
    Dienthoai = scrapy.Field()
    #Email = scrapy.Field()
    #website = scrapy.Field()
    #mst = scrapy.Field()
    

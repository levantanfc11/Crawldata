import scrapy


class HosoSpider(scrapy.Spider):
    name = 'hoso'
    allowed_domains = ['dulieu.mbs.com.vn']
    start_urls = ['http://dulieu.mbs.com.vn/']

    def parse(self, response):
        pass

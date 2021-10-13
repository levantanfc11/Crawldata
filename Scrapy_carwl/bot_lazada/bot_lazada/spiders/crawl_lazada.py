import scrapy
from scrapy.item import Item
from ..items import BotLazadaItem

class CrawlLazadaSpider(scrapy.Spider):
    name = 'crawl_lazada'
    allowed_domains = ['lazada.vn']
    start_urls = ['https://www.lazada.vn/products/tra-gop-0-super-sale-2109-laptop-gaming-asus-tuf-fa506iu-al127t-amd-r7-4800hgtx1660ti-6g8gb-ram512g-ssd15-inch-fhdwin-10-i614970100-s1419554728.html?spm=a2o4n.searchlistcategory.list.1.6c487d0ecyjzSp&search=1']

    def parse(self, response):
        #<h1 class="pdp-mod-product-badge-title" data-spm-anchor-id="a2o4n.pdp_revamp.0.i0.4376408fbnFdHp">
        Tensanpham = response.xpath('//h1[@class="pdp-mod-product-badge-title"]/text()').get()
        #<span class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl" data-spm-anchor-id="a2o4n.pdp_revamp.0.i2.4376408fbnFdHp">26.642.050 ₫</span>
        Giasanpham = response.xpath('//span[@class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]/text()').get()
        #<span class="score-average" data-spm-anchor-id="a2o4n.pdp_revamp.ratings_reviews.i1.4376408fbnFdHp">3.5</span>
        Danhgia = response.xpath('//span[@class="score-average"]/text()').get()

        item = BotLazadaItem()
        item["Tensanpham"] = Tensanpham
        item["Giasanpham"] = Giasanpham
        item["Danhgia"] = Danhgia
        yield item
        

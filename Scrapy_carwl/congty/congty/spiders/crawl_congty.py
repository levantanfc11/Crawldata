import scrapy
from scrapy import item
from ..items import CongtyItem

class CrawlCongtySpider(scrapy.Spider):
    name = 'crawl_congty'
    allowed_domains = ['forbes.com']
    start_urls = ['https://www.forbes.com/companies/icbc/?list=global2000/&sh=2a793a4f1679',
                'https://www.forbes.com/companies/ping-an-insurance/?list=global2000/&sh=2dfd5c325c7b',
                'https://www.forbes.com/companies/agricultural-bank-of-china/?list=global2000/&sh=68bd5e8c18d0',
                'https://www.forbes.com/companies/china-construction-bank/?list=global2000/&sh=171b7ca27374',
                'https://www.forbes.com/companies/toyota-motor/?list=global2000/&sh=50dd835752bd',
                'https://www.forbes.com/companies/samsung-electronics/?list=global2000/&sh=6d2077ed2450',
                'https://www.forbes.com/companies/china-mobile/?list=global2000/&sh=29719f02129e',
                'https://www.forbes.com/companies/taiwan-semiconductor/?list=global2000/&sh=31e247074575',
                'https://www.forbes.com/companies/ptt/?list=global2000/&sh=29130b144e9a',
                'https://www.forbes.com/companies/qatar-national-bank/?list=global2000/&sh=7f532fce41eb'
    ]

    def parse(self, response):
        
        #//div[@class="profile-heading--desktop"]/h1[1]
        Tencongty = response.xpath('//div[@class="profile-heading--desktop"]/h1[1]/text()').get()

        #<span class="profile-row--value">Banking</span>
        #//div[@class="profile-row"][2]/span[2]
        Linhvuc = response.xpath('//div[@class="profile-row"][2]/span[2]/text()').get()

        #//div[@class="profile-row"][4]/span[2]
        Quocgia = response.xpath('//div[@class="profile-row"][4]/span[2]/text()').get()

        item = CongtyItem()
        item["Tencongty"] = Tencongty
        item["Linhvuc"] = Linhvuc
        item["Quocgia"] = Quocgia
        yield item


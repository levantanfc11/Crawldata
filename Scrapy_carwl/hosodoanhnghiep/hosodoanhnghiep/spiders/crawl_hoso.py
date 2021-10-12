import scrapy
from ..items import HosodoanhnghiepItem


class CrawlHosoSpider(scrapy.Spider):
    name = 'crawl_hoso'
    allowed_domains = ['dulieu.mbs.com.vn']
    start_urls = ['https://dulieu.mbs.com.vn/vi/Enterprise/EnterpriseProfile?StockCode=VGI']

    def parse(self, response):
        #<p class="tin-name" id="StockCodeLabel">Tổng Công ty cổ phần Đầu tư Quốc tế Viettel</p>
        Tendoanhnghiep = response.xpath('//p[@id="StockCodeLabel"]/text()').get()
        #<span id="epBox10Address">Tầng 39-40 Tòa nhà Keangnam Landmark, lô E6, khu đô thị mới Cầu Giấy - P - Mễ Trì - Nam Từ Liêm - Hà Nội</span>
        Diachi = response.xpath('//span[@id="epBox10Address"]/text()').get()
        #<span id="epBox10Phone">(84.24) 6262 6868  </span>
        Dienthoai = response.xpath('//span[@id="epBox10Phone"]/text()').get()

        item = HosodoanhnghiepItem()
        item["Tendoanhnghiep"] = Tendoanhnghiep
        item["Diachi"] = Diachi
        item["Dienthoai"] = Dienthoai
        yield item
        pass
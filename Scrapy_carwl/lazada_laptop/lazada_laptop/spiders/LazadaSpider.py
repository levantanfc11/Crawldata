import scrapy
from ..items import LazadaLaptopItem
from selenium import webdriver
from scrapy.utils.project import get_project_settings
class LazadaspiderSpider(scrapy.Spider):
    name = 'LazadaSpider'
    def start_requests(self):
        settings= get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options= webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get('https://www.lazada.vn/laptop/')
        link_elements = driver.find_elements_by_xpath(
            '//*[@data-qa-locator="product-item"]//a[text()]'
        )
        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)
        driver.quit()


    def parse(self, response):
        name= response.xpath('//h1[@class="pdp-mod-product-badge-title"]//text()').get()
        price = response.xpath('//span[@class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]/text()').get()
        soluongdanhgia = response.xpath('//div/div[@class="content"]//div//div/div[@class="count"]//text()').get()
        #danhgia5sao = response.xpath('//div//div//span[@class="percent"]//text()').get()
        item= LazadaLaptopItem()
        item['name']=name
        item['price']=price
        item['soluongdanhgia']=soluongdanhgia
        #item['danhgia5sao']=danhgia5sao
        yield item
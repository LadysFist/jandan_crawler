import scrapy
from jandan.items import jandanItem
from scrapy.crawler import CrawlerProcess
class meizispider(scrapy.Spider):
    name = 'jandanmeizi'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx']

    def parse(self, response):
        item = jandanItem()
        item['image_urls'] = response.xpath('//img/@src').extract()
        yield item

        new_url = response.xpath('//*[@id="comments"]/div[2]/div/a[4]//@href').extract()
        if new_url:
            yield  scrapy.Request(new_url, callback=self.parse)


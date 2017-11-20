import scrapy


class mySpider(scrapy.Spider):
    name = 'google'
    allowed_domains = []
    start_urls = []
    custom_settings = []

    # def start_request ,if start_urls - no
    def parse(self, response):
        pass
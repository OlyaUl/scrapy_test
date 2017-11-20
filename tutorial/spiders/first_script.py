import scrapy


class mySpider(scrapy.Spider):
    name = 'google'
    allowed_domains = []
    start_urls = ['https://www.google.com.ua']
    custom_settings = []

    # def start_request ,if start_urls - no

    def parse(self, response):
        search_url = "https://www.google.com.ua/search?q={}".format('test')
        yield scrapy.Request(url=search_url, callback=self.result_parse)

    def result_parse(self, response):
        # print(response.body)
        # res = response.xpath("//div[contains(@class,'srg')]/div[contains(@class,'g')]/div/"
                             # "div[contains(@class,'rc')]/h3[contains(@class,'r')]/a/@href")
        # res = response.xpath("//ol/div/h3/a//text()").extract()
        res = response.xpath("//ol/div[contains(@class,'g')]/h3[contains(@class,'r')]/a//text()").extract()

        print(res)







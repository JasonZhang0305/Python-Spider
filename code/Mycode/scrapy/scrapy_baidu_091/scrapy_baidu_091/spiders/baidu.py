import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字，用于运行爬虫的时候使用的值
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始url地址
    start_urls = ["http://www.baidu.com/"]

    def parse(self, response):
        pass

import scrapy
from scrapy import Request
from ..items import VnexpressItem


class VNEpress(scrapy.Spider):
    name = "education"
    start_urls = [
        "https://vnexpress.net/giao-duc"
    ]
    count = 0
    MAX_COUNT = 5000
    def parse(self, response):
        if self.count == 0:
            urls = response.xpath('//*[@id="automation_TV1"]/div/article/h3/a/@href').getall() + response.xpath('//*[@id="automation_TV0"]/div/article/h3/a/@href').getall()[:-1]
        else:
            urls = response.xpath('//*[@id="automation_TV0"]/div[2]/article/h3/a/@href').getall()
        next_page = response.xpath('//*[@id="pagination"]/div/a[5]/@href').get()
        for url in urls:
            if self.count < self.MAX_COUNT:
                self.count += 1
                connect_to_url = response.urljoin(url)
                yield Request(connect_to_url, callback=self.parse_content)
            else:
                break
        if next_page is not None and self.count < self.MAX_COUNT:
            next_url = response.urljoin(next_page)
            yield Request(next_url, callback=self.parse)

    def parse_content(self, response):
        title = response.xpath('/html/body/section[4]/div/div[2]/h1/text()').get()
        description = response.xpath('/html/body/section[4]/div/div[2]/p/text()').get()
        contents = response.xpath('/html/body/section[4]/div/div[2]/article/p/text()').getall()
        body = ". ".join(content for content in contents if content.strip() != "" and content != [])
        news = ""
        if title is not None:
            news += str(title) + ". "
        if description is not None:
            news += str(description) + ". " + str(body)
        else:
            news += str(body)
        with open("education.txt", "a+") as f:
            f.write(news)
            f.write("\n")
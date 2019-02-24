import scrapy
import urllib
from imagescraper.items import Image


class QuotesSpider(scrapy.Spider):
    name = "images"

    def start_requests(self):
        urls = [
            'https://www.pexels.com/search/bird/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file = open("../testfile.txt", "w") 

        for image in response.css('a.js-photo-link'):
            file.write(image.css('img::attr(srcset)').get().split()[0] + "\n")
            yield {
                'file_url': image.css('img::attr(srcset)').get().split()[0]
            }


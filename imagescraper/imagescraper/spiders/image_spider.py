import scrapy
import urllib
from imagescraper.items import Image


class QuotesSpider(scrapy.Spider):
    name = "images"
 

    def __init__(self, *args, **kwargs): 
        super(QuotesSpider, self).__init__(*args, **kwargs) 

        imagesPerPage = 30

        base_url = 'https://www.pexels.com/search/'
        endpoints = kwargs.get('catigories').split(',')
        self.nImages = kwargs.get('nImages')
        open('image_urls.txt', 'w').close()

        nPages = self.nImages/imagesPerPage + 1

        self.counter = 0
        self.urls = []
        for page in range(1, nPages+1):
            for catigory in endpoints:
                self.urls.append(base_url+catigory+'/?page='+str(page))

        # self.urls = [base_url + catigory for catigory in endpoints]
        for url in self.urls:
            print url +'\n\n\n\n'

    def start_requests(self):
        # urls = [
        #     'https://www.pexels.com/search/disc/'
        # ]
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

        # base_url = 'https://www.pexels.com/search/'
        # for catigory in self.catigories:
        #     print "CATIGORY", catigory, '\n\n'
        #     yield scrapy.Request(base_url + catigory, callback=self.parse)

        for url in self.urls:
            yield scrapy.Request(url, callback=self.parse)

        # print "NIMAGES: ", self.nImages, '\n\n'
        # print "Counter: ", self.counter, '\n\n'

    def parse(self, response):
        file = open("image_urls.txt", "a+") 

        for image in response.css('a.js-photo-link'):

            print "Counter: ", self.counter, '\n\n'

            full_url = image.css('img::attr(srcset)').get().split()[0]
            # shorten_url = full_url.split("?auto=compress")[0]
            # file.write(shorten_url + "\n")
            file.write(full_url + '\n')

            # file.write(image.css('img::attr(srcset)').get().split()[0] + "\n")
            yield {
                'file_url': image.css('img::attr(srcset)').get().split()[0]
            }


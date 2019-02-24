from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from download_urls import *


def combineKeywords(keywords):
	ret = ''
	for i, word in enumerate(keywords):
		ret += word
		if i != len(keywords)-1:
			ret+=','
	return ret

def process_images(keywords):
	combined_keywords = combineKeywords(keywords)

	process = CrawlerProcess(get_project_settings())

	process.crawl('images', catigories = combined_keywords, nImages = 40)
	process.start()

	# downloadImages("image_urls.txt", 'images/')


# print combineKeywords(['ball', 'swim'])
process_images(['ball', 'swim'])
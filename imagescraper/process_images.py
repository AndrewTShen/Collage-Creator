from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from download_urls import *
import sys

def combineKeywords(keywords):
	ret = ''
	for i, word in enumerate(keywords):
		ret += word
		if i != len(keywords)-1:
			ret+=','
	return ret

def process_images(keywords):
	# combined_keywords = combineKeywords(keywords)
	combined_keywords = keywords

	process = CrawlerProcess(get_project_settings())

	process.crawl('images', catigories = combined_keywords, nImages = 40)
	process.start()

	downloadImages("image_urls.txt", 'images/')


# print combineKeywords(['ball', 'swim'])

print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)

print sys.argv
# process_images("swim,ball")
process_images(sys.argv[1])
import os
import glob
import requests

def download(url, dl_loc):
	f = open(dl_loc,'wb')
	f.write(requests.get(url).content)
	f.close()

def downloadImages(readFile, writeDir):

	# clear the write directory

	files = glob.glob(writeDir+'*')
	for f in files:
	    os.remove(f)


	with open(readFile) as f:
	    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content] 

	for fileNum, url in enumerate(content):
		print 'downloading: file ' + str(fileNum) 
		download(url, writeDir + 'file' + str(fileNum) + '.jpeg')

# downloadImages("image_urls.txt", 'images/')
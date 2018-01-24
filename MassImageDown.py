DownloadURL = None    #Remove None and type the url in quotes

import re
import os
import urllib2
import datetime


def ExtractURL(textContent):
	RetrievedData = re.findall(r'(https?://[^\s"]+jpg)', textContent)
	print "Image Found : ",len(RetrievedData);

	#Print all URLs
	if RetrievedData is not None:
		for i in range(0, len(RetrievedData)):
			print RetrievedData[i]

	return RetrievedData

def DownloadFiles(urlList, destPath):

	fbHeaders = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
						'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
						'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
						'Accept-Encoding': 'none',
						'Accept-Language': 'en-US,en;q=0.8',
						'Connection': 'keep-alive'}
						
	outputData=0
	outputBinaryData = None
	confirmString = '\n>> Proceed to download '+ str(len(urlList)) +' files?(Y/N)';
	confirmDownload = raw_input(confirmString)

	if confirmDownload == "y":
		print "\nDownloading now..."

		#Downloading files
		for i in range(0, len(urlList)):
			print str(i)+' : '+urlList[i]
			req = urllib2.Request(urlList[i],  headers=fbHeaders)
			try:
				outputBinaryData = urllib2.urlopen(req).read()
			except urllib2.HTTPError, e:
				print 'Unable to download the image : ',urlList[i], e.fp.read()			
			file = open(destPath+"/"+urlList[i].split('/')[-1] , "wb")
			if outputBinaryData is not None:
				file.write(outputBinaryData)
			file.close()
			outputBinaryData = None
	else:
		print "\nExiting the application"

	print "\n** DONE **"

def main():
	print "\n ** MaX ** \n";
	print "Downloading from the URL : ", DownloadURL

	if DownloadURL is None:
		print "\n\n******  ERROR : DownloadURL var is empty"
		raw_input("Press Enter to close this window")
	else:
		req = urllib2.Request(DownloadURL)

		#vars
		URLLink = urllib2.urlopen(req)
		urlResponse = URLLink.read()
		URLLists = ExtractURL(urlResponse)

		OutputFolderPath = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M")

		os.makedirs(OutputFolderPath)

		if(len(URLLists) > 0):
			DownloadFiles(URLLists, OutputFolderPath)

if __name__ == '__main__':
	main()

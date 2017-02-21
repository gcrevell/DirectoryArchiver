#!/usr/bin/env python

import sys
import ssl

import urllib2
from DownloadFile import downloadFile
from bs4 import BeautifulSoup

def main():
	if len(sys.argv) < 2:
		# Too few arguments, need a url!
		print 'Proper use: ' + sys.argv[0] + ' [URL]'
		return
	
	url = sys.argv[1]
	
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE

	urlpath = urllib2.urlopen(url, context=ctx)

	html = urlpath.read().decode('utf-8')
	
	soup = BeautifulSoup(html, 'html.parser')

	print soup

if __name__ == '__main__':
	main()

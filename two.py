#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import requests

cui = "http://www.cuindependent.com"
cam = "http://www.dailycamera.com"
post = "http://www.denverpost.com"

def make_soup(url):
	get = requests.get(url)
	print get.status_code
	content = get.content
	soup = BeautifulSoup(content)
	print soup.prettify()

make_soup(cui)
make_soup(cam)
make_soup(post)
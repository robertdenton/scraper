#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import dataset
import time

db = dataset.connect('sqlite:///headlines.db')

cui = "http://www.cuindependent.com"
cam = "http://www.dailycamera.com"
post = "http://www.denverpost.com"

def make_soup(url):
	get = requests.get(url)
	#print get.status_code
	content = get.content
	soup = BeautifulSoup(content)
	#print soup.prettify()
	if url == cui:
		cuiDiv=soup.find("div", "post_header")
		text=cuiDiv.find('a').text
		link=cuiDiv.find('a').get('href')
		#print text
		#print link
	else:
		dfmDiv=soup.find('a', 'listingItemTitle')
		text=dfmDiv.text
		link=dfmDiv.get('href')
		#print text
		#print link
	#print text + " " + link
	table=db['heads']
	table.insert(dict(day=time.strftime("%m/%d/%Y"),site=url,head=text,link=link))

make_soup(cui)
make_soup(cam)
make_soup(post)
	


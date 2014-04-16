#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import dataset
import time

db = dataset.connect('sqlite://Users/Rob/Documents/code/scraper/headlines.db')

one = "http://www.cuindependent.com"
two = "http://www.dailycamera.com"
three = "http://www.denverpost.com"

oneName = "CU Independent"
twoName = "Boulder Daily Camera"
threeName = "The Denver Post"

def make_soup(url):
	get = requests.get(url)
	#print get.status_code
	content = get.content
	soup = BeautifulSoup(content)
	#print soup.prettify()
	if url == one:
		div=soup.find("div", "post_header")
		text=div.find('a').text
		link=div.find('a').get('href')
		name=oneName
		#print text
		#print link
	elif url == two:
		div=soup.find('a', 'listingItemTitle')
		text=div.text
		link=div.get('href')
		name=twoName
		#print text
		#print link
	elif url == three:
		div=soup.find('a', 'listingItemTitle')
		text=div.text
		link=div.get('href')
		name=threeName
		#print text
		#print link
	#print text + " " + link
	table=db['headsReal']
	table.insert(dict(day=time.strftime("%m/%d/%Y"),name=name,site=url,head=text,link=link))
	print "success!"
make_soup(one)
make_soup(two)
make_soup(three)
	


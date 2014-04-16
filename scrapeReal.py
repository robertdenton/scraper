#!/usr/bin/env python

"""\
@file scrapeReal
@author Rob Denton
@date 4/16/2014
@brief runs a scraper of media sites and writes headline info to a sqlite db
 
$LicenseInfo:firstyear=2014&license=viewerlgpl$
Rob Denton
Copyright (C) 2014
 
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation;
version 2.1 of the License only.
 
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.
 
You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 
$/LicenseInfo$
"""

from bs4 import BeautifulSoup #for parsing HTML
import requests #for connecting to url
import dataset #for connecting to and writing to db
import time #for putting the current date into the db

print "thanks for using, depending on your Internet connection, this may take a moment"

#connect db
db = dataset.connect('sqlite:////Users/Rob/Documents/code/scraper/headlines.db') #change this to your local directory

#print "got database" #for testing purposes

#set sites to correct urls, needed as global
one = "http://www.cuindependent.com" #change these to the sites you want to scrape
two = "http://www.dailycamera.com"
three = "http://www.denverpost.com"

#set site names as global, not needed as global
oneName = "CU Independent" #change to yours
twoName = "Boulder Daily Camera"
threeName = "The Denver Post"

#make a function to get and write data to db
def make_soup(url):
	#print "in function" #for testing purposes
	get = requests.get(url)
	#print get.status_code #for testing purposes
	content = get.content
	soup = BeautifulSoup(content)
	#print soup.prettify() #for testing purposes
	# scrape different things for different sites
	#site one
	if url == one: #change these to what sites you want to scrape and what content you want from each 
		div=soup.find("div", "post_header")
		text=div.find('a').text
		link=div.find('a').get('href')
		name=oneName
		#print text #for testing
		#print link
	#site two
	elif url == two: #here two and three are similar becuase they are both DFM properties
		div=soup.find('a', 'listingItemTitle')
		text=div.text
		link=div.get('href')
		name=twoName
		#print text #for testing
		#print link
	#site three
	elif url == three:
		div=soup.find('a', 'listingItemTitle')
		text=div.text
		link=div.get('href')
		name=threeName
		#print text #for testing
		#print link
	
	#write to db
	table=db['headsReal'] #access the table, it will create on if not there
	#insert a cell for today's date, for the name, for the base url, for the headline text, for the headline link
	table.insert(dict(day=time.strftime("%m/%d/%Y"),name=name,site=url,head=text,link=link)) #new db entry for each site you scrape
	print "success!" #when done with each function, need three
#exit function

#call functions for each site
make_soup(one)
make_soup(two)
make_soup(three)
#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2

cui=urllib2.urlopen("http://www.cuindependent.com")

cuiContent=cui.read()

cuiSoup=BeautifulSoup(cuiContent)

cuiHed=cuiSoup.find("div", "post_header")

print(cuiHed)
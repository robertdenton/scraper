#!/usr/bin/python

"""

To-do list

>Make repetitive tasks functions
>Get it to write to db (postgres)
>Get it to schedule (cronjob)
>

"""



"""
cui
<div class="post_header single_post">
	<h3>
		<a href="http://cuindependent.com/2014/04/14/beginning-end-pre-finals-playlist/53390" title="Playlist Project: Preparing for finals">
			Playlist Project: Preparing for finals
		</a>
	</h3>
</div>
---
Camera
<a href="http://www.dailycamera.com/news/ci_25560489/jewish-food-movement-ethical-living-gives-passover-new" class="listingItemTitle">
	Jewish food movement for ethical living gives Passover new meaning<br>
</a>
---
Post is similar to Camera
"""

from bs4 import BeautifulSoup
import urllib2
import psycopg2

cui=urllib2.urlopen("http://www.cuindependent.com")
#
cam=urllib2.urlopen("http://www.dailycamera.com")
#
post=urllib2.urlopen("http://www.denverpost.com")

###

cuiContent=cui.read()
#
camContent=cam.read()
#
postContent=post.read()

###

cuiSoup=BeautifulSoup(cuiContent)
#
camSoup=BeautifulSoup(camContent)
#
postSoup=BeautifulSoup(postContent)

###

cuiDiv=cuiSoup.find("div", "post_header")#gets whole div, see above
cuiA=cuiDiv.find('a')#gets whole a tag
cuiText=cuiA.text#gets just the text in whithin the a tags
cuiLink=cuiA.get('href')#gets the link
#
camA=camSoup.find("a", "listingItemTitle")#gets the a tag we want with id=listingItemTitle
camText=camA.text#gets the text
camLink=camA.get('href')#gets the link
#
postA=postSoup.find("a", "listingItemTitle")#gets the a tag we want with id=listingItemTitle
postText=postA.text#gets the text
postLink=postA.get('href')#gets the link


#print(cuiDiv) 
#print(cuiA)
print(cuiText)
print(cuiLink)
#
print(camText)
print(camLink)
#
print(postText)
print(postLink)
#!/usr/bin/python
# AJ Cave and Garrett Garcia

import scraperwiki
import lxml.html
import re

ldata = []
for page in xrange(1,101):
	html = scraperwiki.scrape('http://programmers.stackexchange.com/users?page=%d&tab=reputation&filter=all' % page)
	root = lxml.html.fromstring(html)
	
	for li in root.cssselect('div.user-info'):
		link = li.cssselect("div.user-details a")[0]
		location = li.cssselect("span.user-location")[0]
		
		data = {"name":link.text.strip(), "link":link.attrib.get('href'), "location":(location.text or '')}
		tags = []
		for tag in li.cssselect("div.user-tags")[0].cssselect("a"):
			tags.append(tag.text.strip())
		data["tags"] = tags
		# to do: separate the name into country code and state properly
		ldata.append(data)

scraperwiki.sqlite.save(['name'], ldata, "newtable")
#print ldata[0]
print 'Programmers scraped:%d' % len(ldata)

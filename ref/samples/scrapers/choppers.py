#!/usr/bin/python
#
# Copied from Nicola Hughes file at  
# https://classic.scraperwiki.com/scrapers/python_meetup_groups_usa/
#
# This served as the initial example of how to scrape
# 
# Note:  this saves to a scraperwiki sqlite database!
#

import scraperwiki
import lxml.html
import re
import pprint

html = scraperwiki.scrape("http://www.meetup.com/West-Code-Choppers/members/")
root = lxml.html.fromstring(html)
ldata = [ ]
for link in root.cssselect('ul#memberList div.member-details a.memName'):
    data = {"name":link.text.strip(), "link":link.attrib.get('href')}
    ldata.append(data)

#scraperwiki.sqlite.save(['name'], ldata, "newtable")
pprint.pprint(ldata)

'''
Form implementation and extraction of data from nse website 
Uses Mechanize and Urllib of python 
'''
from BeautifulSoup import BeautifulSoup

import urllib, urllib2, cookielib, webbrowser
import mechanize
from distutils.filelist import findall
import json
 
'''
Browser initialization starts here
It is important to prevent identification from bot activity   	
'''

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

'''
Browser Initialized, now we can go ahead and scrape the data
''' 

'''
Significance of User-Agents, It is important to identify which browser you are using even though you are a bot
'''
br.addheaders = [('User-agent', 'Firefox'), ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]



final_data={}
count =0;
json2 = br.open('http://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftybankStockWatch.json')
#A url which I identified from which all the data was coming

ht = json2.read()

data = json.loads(ht)

for element in data["data"]:
    code = element["symbol"]
    print element["symbol"]
    open = element["open"]
    print "open "+element["open"]
    high = element["high"]
    print "high "+element["high"]
    low = element["low"]
    print "low " +element["low"]
    current = element["ltP"]
    print "current "+element["ltP"]
    wkhi = element["wkhi"]
    print "week-high "+element["wkhi"]
    wklo = element["wklo"]
    print "week-low "+element["wklo"]
    print "\n"
    if code not in final_data:
        final_data[code]= [open, high, low, current, wkhi, wklo]
        count +=1

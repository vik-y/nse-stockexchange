'''
Form implementation and extraction of data from nse website 
Uses Mechanize and Urllib of python 
'''
from BeautifulSoup import BeautifulSoup

import urllib, urllib2, cookielib, webbrowser
import mechanize
from distutils.filelist import findall
import json
#Browser 

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)


#Follow refresh 0 but not hangs on refresh > 0 

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

#User Agent, understanding user agents is very important thing 



#Browser 


#Follow refresh 0 but not hangs on refresh > 0 

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

#Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

#User Agent, understanding user agents is very important thing 

br.addheaders = [('User-agent', 'Firefox'), ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]


#Open a google search result 
r = br.open("http://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm")
html = r.read()
#print htmlp
soup = BeautifulSoup(html)
#print soup.findAll('a','download-data-link1')
#print [f.controls for f in br.forms()]

#a = soup.find('a', 'download-data-link1')
#print a.attrs
#br.select_forms(name="dataform")


final_data={}
count =0;
json2 = br.open('http://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftybankStockWatch.json')
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
        
print count
#print forms[1].controls[0].get_items()
'''br.select_form(nr=1)loa
br.form['live-comm']=['MCX']
br.submit()'''

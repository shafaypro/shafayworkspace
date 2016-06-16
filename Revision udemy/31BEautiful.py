from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    print("The Program has been started")
    url ="https://finance.yahoo.com/q/bs?s=YHOO"
    hdr = {
          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'none',
          'Accept-Language': 'en-US,en;q=0.8',
          'Connection': 'keep-alive'}
    data = requests.get(url, hdr) # this gets the url link been requested in the page.
    source = data.text # this is to get the text of the html page
    #print(source) # this prints out the source code.
    soup = BeautifulSoup(source,"html5lib")
    #print (soup.prettify()) # This prettifies the page
    for i in soup.find_all('td',{'class':'yfnc_tabledata1'}):
         print(i.nextSibling.nextSibling.nextSibling.string)
         print(i.contents) # this returns the one step further

         # .childrens return all the sub tags (the child with in a tag(DIRECT TAGS)
	    # .decendents will return the stuff indivisual tag and the text all will be given in the body down.(EVERY THING)
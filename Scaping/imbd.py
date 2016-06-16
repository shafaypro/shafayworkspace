import urllib2
from bs4 import BeautifulSoup
def get_name(scraplist,scrap_list):

	for item in scraplist.find_all("span", {"itemprop": "name"}):
		scrap_list.append(item.a.string)
		print (item.a.string)
	return scrap_list


def get_times(scraplist):
	scrap_list = list()

def scrap_weblink(url):
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page, "lxml")
	scrap_movie = soup.find_all(class_="info")
	return scrap_movie

def main():
	url = 'http://www.imdb.com/showtimes/?ref_=nv_tp_sh_3'
	scrap_movie = scrap_weblink(url)
	soup = BeautifulSoup(str(scrap_movie), "lxml")
	name_list = get_name(soup, [])
	print (name_list)
	#print (soup.h4.span.a.string)
	#print (soup.p.string)
	#print (soup.p.span.nextsibling.span.stron.string)
if __name__ == '__main__':
    main()

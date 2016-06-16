import urllib
import requests
from bs4 import BeautifulSoup


def AnotherCheckLink(hrefrence):
	sourcecode = requests.get(hrefrence)
	plaintext = sourcecode.text
	soup = BeautifulSoup(plaintext)

if __name__ == '__main__':
	url1="https://docs.python.org/3.4/library/urllib.request.html"
	sourcecode=requests.get(url1)
	plaintext=sourcecode.text
	soup=BeautifulSoup(plaintext)

	for link in soup.findAll('a', {'class': 'reference internal'}):
		href = link.get('href')
		title = link.string
		print (href)
		print (title)
		AnotherCheckLink(href)

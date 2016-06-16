from bs4 import BeautifulSoup
import requests
import urllib

def File_download():
	print('This is the file download section')


def Web_scrap(link_input):
	title_list =list()
	price_list = list()
	old_price_list =list()
	link_input = link_input
	sourcecode = requests.get(link_input)
	plain_text = sourcecode.text
	beautified_text = BeautifulSoup(plain_text, "html.parser")
	count = 0
	#print (beautified_text.prettify())
	'''
	for link in beautified_text.find_all('h3', {'class': 'product-name nameoftheproduct'}):
		href = link.get('href')
		text = link.string
		print (text)
		print (href)
	'''
	for link in beautified_text.find_all('h3', {'class': 'product-name nameoftheproduct'}):
		if link.string not in title_list:
			title_list.append(link.string)
		else:
			continue
	for link in beautified_text.find_all('span', {'class': ('price')}):
		price_list.append(link.string)
	price_list.remove(price_list[0])

	for item in range(len(title_list)):
		print ('Item Name: ' + str(title_list[item]))
		print ('old price: ' + str(price_list[count]))
		print ('new price:' + str(price_list[count + 1]))
		count += 2

if __name__ == '__main__':
    Web_scrap("https://www.dscbalances.com")
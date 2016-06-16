import BeautifulSoup
import requests
import urllib
class ImageScrapperShafay():
	link=""
	counter = 0
	def __init__(self, link):
		self.link = link  # This intializes the link so that the images can be scrapped

	def get_Images(self):
			sourcecode = requests.get(self.link)
			plain_text = sourcecode.text
			soup = BeautifulSoup.BeautifulSoup(plain_text)
			list_of_images = list()
			for image in soup.findAll('img'):
				list_of_images.append(image['src'])
			return list_of_images
	def Download_List_Images(self, List_of_images):
		for list_element in Lists_of_images:
			if str(list_element).__contains__('.jpg'):
				name = str(self.counter) + '.jpg'
				urllib.urlretrieve(list_element, name)
				self.counter += 1



if __name__ == '__main__':
	link = 'http://www.stylebistro.com/Barefaced+Beauties+-+Celebrities+Without+Makeup/'
	IMSCRAP = ImageScrapperShafay(link) # Creates the object of the class
	Lists_of_images = IMSCRAP.get_Images() # this gets all the link of the images
	IMSCRAP.Download_List_Images(Lists_of_images)

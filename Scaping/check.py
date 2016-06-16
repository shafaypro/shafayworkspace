from bs4 import BeautifulSoup
import requests
import urllib
import urllib2
import re
#All Right Reserved To Shafay Pro.
class ImageScrapperShafay():
	link=""
	counter = 1
	def __init__(self, link):
		self.link = link  # This intializes the link so that the images can be scrapped

	def get_Images(self):
			sourcecode = requests.get(self.link)
			plain_text = sourcecode.text
			soup = BeautifulSoup.BeautifulSoup(plain_text)
			list_of_images = list()
			print ('###################Image Links################## ')
			for image in soup.findAll('img'):
				try:
					list_of_images.append(image['src'])
				except:
					list_of_images.append(image['srcset'][0])
					print (list_of_images.append(image['srcset']))
			print (list_of_images)
			return list_of_images
	def Download_List_Images(self, List_of_images):
		print ('###########names of the images##############')
		for list_element in Lists_of_images:
			if str(list_element).__contains__('.jpg'):
				try:
					name = 'image' + str(self.counter) + '.jpg'
					if str(list_element).startswith('http:'):
						print(name+' checked')
					else:
						list_element ='http:'+str(list_element)
					image_on_webR = urllib2.urlopen(list_element).read()
					download_image = file(name, 'wb')
					download_image.write(image_on_webR)
					download_image.close()
					self.counter += 1
				except:
					print ('url not identified')
			elif str(list_element).__contains__('.png'):
				try:
					name = 'image' + str(self.counter) + '.png'
					if str(list_element).startswith('http:'):
						print(name +' checked')
					else:
						list_element ='http:'+str(list_element)
					image_on_webR = urllib2.urlopen(list_element).read()
					download_image = file(name, 'wb')
					download_image.write(image_on_webR)
					download_image.close()
					self.counter += 1
				except:
					print ('url not identified')
			elif str(list_element).__contains__('.jpeg'):
				try:
					name = 'image' + str(self.counter) + '.jpeg'
					if str(list_element).startswith('http:'):
						print(name +' checked')
					else:
						list_element ='http:'+str(list_element)
					image_on_webR = urllib2.urlopen(list_element).read()
					download_image = file(name, 'wb')
					download_image.write(image_on_webR)
					download_image.close()
					self.counter += 1
				except:
					print ('url not identified')
			elif str(list_element).__contains__('.GIF') or str(list_element).__contains__('.gif'):
				try:
					name = 'image' + str(self.counter) + '.gif'
					if str(list_element).startswith('http:'):
						print(name + ' checked')
					else:
						list_element ='http:'+str(list_element)
					image_on_webR = urllib2.urlopen(list_element).read()
					download_image = file(name, 'wb')
					download_image.write(image_on_webR)
					download_image.close()
					self.counter += 1
				except:
					print ('url not identified')
			elif str(list_element).__contains__('.BMP'):
				try:
					name = 'image' + str(self.counter) + '.BMP'
					if str(list_element).startswith('http:'):
						print(name + ' checked')
					else:
						list_element ='http:'+str(list_element)
					image_on_webR = urllib2.urlopen(list_element).read()
					download_image = file(name, 'wb')
					download_image.write(image_on_webR)
					download_image.close()
					self.counter += 1
				except:
					print ('url not identified')
			elif str(list_element).__contains__('.WEBP'):
				try:
					name = 'image' + str(self.counter) + '.WEBP'
					if str(list_element).startswith('http:'):
						print(name + ' checked')
					else:
						list_element ='http:'+str(list_element)
					image_on_webR = urllib2.urlopen(list_element).read()
					download_image = file(name, 'wb')
					download_image.write(image_on_webR)
					download_image.close()
					self.counter += 1
				except:
					print ('url not identified')
			elif str(list_element).__contains__('.BPG'):
				try:
					name = 'image' + str(self.counter) + '.BPG'
					if str(list_element).startswith('http:'):
						print(name + ' checked')
					else:
						list_element = 'http:' + str(list_element)
					image_on_webR = urllib2.urlopen(list_element).read()
					download_image = file(name, 'wb')
					download_image.write(image_on_webR)
					download_image.close()
					self.counter += 1
				except:
					print ('url not identified')
			elif str(list_element).__contains__('.SVG'):
				try:
					name = 'image' + str(self.counter) + '.SVG'
					if str(list_element).startswith('http:'):
						print(name + ' checked')
					else:
						list_element = 'http:' + str(list_element)
					image_on_webR = urllib2.urlopen(list_element).read()
					download_image = file(name, 'wb')
					download_image.write(image_on_webR)
					download_image.close()
					self.counter += 1
				except:
					print ('url not identified')
if __name__ == '__main__':
	print ('This Script is all right reserved to Shafaypro , Only scrap websites if those websites allow !,')
	link = raw_input('Enter the link you want to scrap:')
	link = link.strip()
	IMSCRAP = ImageScrapperShafay(link) # Creates the object of the class
	Lists_of_images = IMSCRAP.get_Images() # this gets all the link of the images
	IMSCRAP.Download_List_Images(Lists_of_images)












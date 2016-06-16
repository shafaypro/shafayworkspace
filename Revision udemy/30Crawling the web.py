import re
import urllib.request
url = "http://www.dictionary.com/browse"
word = input("Enter the word you want to browser")
url = url + word+ "?s=t"  # updating the specific url

data = urllib.request.urlopen(url).read()  # this downloads the webpage
data1 = data.decode("UTF-8")  # this decodes the file
print(data1)

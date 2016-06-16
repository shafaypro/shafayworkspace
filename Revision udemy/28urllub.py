import urllib.request
import re
stock = input("Enter the stock name: ")
url = "http://www.google.com/finance?q="
url = url + stock  # this concatinate the strings
data = urllib.request.urlopen(url) # this opens up hte module in the website
plain_data = data.read() # this reads the html page
plain_data = plain_data.decode("utf-8")  # this decodes the page in the utf8 format
#print(plain_data)
messege = re.search('meta itemprop="price"', plain_data)
start = messege.start()
end = messege.start() + 50
body_message = plain_data[start:end]
print(body_message)
message_information = re.search("content=", body_message)  # this is the message information
end = message_information.end()
print(end)
print(body_message[end+1:end+7])
import re
import urllib.request
#  http://www.weather-forecast.com/locations/Paris/forecasts/latest
city = input("Enter your city: ")
url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")  # decoding the webpage with utf8 encoding
m = re.search('span class="phrase">', data1)  # using the regular expression to search
start = m.end()  # picking up the end index of the string
end = start + 300  # ending continued till the 300th + index
newString = data1[start:end]  # the new string is then genereted
print(newString)  # this print out the result which need to be displayed value of the new string
m = re.search("</span>", newString)  # finding the span element in the new searched regular expression string.
end = m.start() - 2
final = newString[0:end]
print (final) # this will print out the result

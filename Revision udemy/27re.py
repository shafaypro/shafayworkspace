import re
my_string = "The night was cold and dark"
message_place = re.search("night", my_string)  # this will held by searching the second parameter screen
print(message_place)  # this prints out the object with the source and the specific attribute

start = message_place.start()  # this knows the startin position in the span attribute
print(start)
end = message_place.end()  # this prints out the ending place of the message
print(end) #this prints the ending index of the message
print (my_string[start:end])
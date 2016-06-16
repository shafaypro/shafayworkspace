# Reading a file in python

file_reader = open("18text.txt", 'r')
data = file_reader.read()
print (data)
print (file_reader.tell()) #tells where the curson of the line is like where is the position of the file

file_reader.seek(0,0) # starting and which place
# these too are quirte helpful when you are working on the projects like Construction of the Compilers.
print (file_reader.read(20)) # provide till where you want to read to- :)
file_writer = open("18text.txt", 'w')
file_writer.write("\n This is the Writin a nes thing to a file ")
file_writer.close() # closing the file writee


file_appender = open("18text.txt",'a')  # this adds to the next of the filled lines.
file_appender.write("What was that it is an appending funcitoon")
file_appender.close()

file_reader_appender = open("18text.txt", "a+")  # to read and to append the file.
file_reader_appender.read()  #
file_reader_appender.write("Hola")
file_reader_appender.close() # so this closses ht
# for writinf and read --> it is wb+ <-- this is an access method

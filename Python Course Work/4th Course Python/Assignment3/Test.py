import xml.etree.ElementTree as ET
#********************XML READER *********************#
class Lookup:
	def __int__(self):
		print('An object of Lookup has been created')
	def Lookupcheck(self,dictonary,keyspecific):  # This function is for checking the inner data
		found = False
		for child in dictonary:
			if found:
				return child.text
			if child.tag== 'key' and child.text == keyspecific:
				found = True
		return None


class XML_READER:
	def __int__(self):
		print ('An object of the xml has been created')
	def xmlreading_Action(self,file_name):
		stuff = ET.parse(str(file_name)) # Parsing the file into the ET format XML
		all = stuff.findall('dict/dict/dict')
		print ('The length of the parsed xml is ' +str(len(all)))
		outerall=stuff.find('dict/dict')
		print ('The length of the outer all is '+str(len(outerall)))
		s=stuff.find('dict/dict/dict/').text

class File_method:

	file_name = ""
	def __init__(self):
		print ('An object has been created')  #just to cshow that the object has been created !
	def filename(self):
		file_name = raw_input('Enter the File name here:')   # taking the filename fro the user
		return file_name
	def File_reader(self,file_name):
		try:
			file_open = open(str(file_name), 'r')   #reading the file as per user except
			XML_READING = XML_READER()
			XML_READING.xmlreading_Action(file_name)   # Reading the complete file from the inout !
			#Lines=file_open.readlines()   # File has been Completely readed
			#for line in Lines:
				#print(line)
		except:
			print("Invalid File Input , Not found in the current directory!")
			exit(0)
# *******************************MAIN *******************************#
def main():
	F_CHECK=File_method()
	Filetoberead=F_CHECK.filename()
	print(Filetoberead+str(' It is Running upto here!'))
	F_CHECK.File_reader(Filetoberead)   # This is the main call where it calls all the methods
if __name__ == '__main__':
    main()

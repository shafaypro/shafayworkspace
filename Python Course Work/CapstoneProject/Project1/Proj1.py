import sqlite3
import matplotlib.pyplot as mplt
import time
import urllib
import numpy as np


# First Simplest Approach!
def file_read():
	print ('Reading the file.....')
	location_file = raw_input('Enter the location file')  # this is the location of the file, which is going to be read
	if location_file is "":
		print ('No File input, Taking Default File')  # a message to prompt the users that there was no file.
		'''
		location_file = "https://vincentarelbundock.github.io/Rdatasets/csv/datasets/AirPassengers.csv"  # WebFile def
		response = urllib.request.urlopen(location_file)  # request for the particular csv file and then store it
		data_in_csv = str(response.read())   # converts the file in to string format
		lines = data_in_csv.split("\\n")   # split the file at the each end before the next line
		file_open = open('AirPassengers.csv', 'w')  # Writes to the file
		for line in lines:
			file_open.write(line + '\n')
		file_open.close()
		'''
		file_open = open('AirPassengers.csv', 'r')
		data_in_file = file_open.readlines()
		return data_in_file
	else:
		file_open = open(location_file, 'r')  # file_opening command used to open the specific file
		time.sleep(2)  # just to wait (show the user the file read is in progress (otherwise it is quite fast)
		data_in_file = file_open.readlines()  # this is to read the data in the file and store in the variable
		file_open.close()  # file_open (file variable is closed since the data have been read , now there is no need
		return data_in_file  # final data is returned to the function m where the call of the Function was made
def database_writer(data):
	data = data.split(',')
	print (data[0] + data[1])  # This is just for debugging process (for logical error check's)
	connection = sqlite3.connect(
		'AirPassenger.sqlite')  # The connection is established from the python file to the data
	cursor_connector = connection.cursor()  # this activates the cursor used to run queries
	cursor_connector.execute(
		'''CREATE TABLE IF NOT EXISTS AirPassenger (id INTEGER UNIQUE, TimePeriod REAL ,Passenger INTEGER)''')
	cursor_connector.execute('''INSERT INTO AirPassenger(id,TimePeriod,Passenger) values (?,?,?)''',
							 (data[0], data[1], data[2]))
	connection.commit()  # Runs all the database queries which has been written above.
	connection.close()  # this ends the connection statment as the database is written.
def PassengersTimePeriod():
		connection = sqlite3.connect(
		'AirPassenger.sqlite')  # The connection is established from the python file to the data
		cursor_connector = connection.cursor()  # this activates the cursor used to run queries
		cursor_connector.execute('''Select TimePeriod from AirPassenger''')
		PTP_return = cursor_connector.fetchall()
		connection.commit()  # Runs all the database queries which has been written above.
		connection.close()  # this ends the connection statment as the database is written.
		return PTP_return
def Passengers():
		connection = sqlite3.connect(
		'AirPassenger.sqlite')  # The connection is established from the python file to the data
		cursor_connector = connection.cursor()  # this activates the cursor used to run queries
		cursor_connector.execute('''Select Passenger from AirPassenger''')
		Passengers_return = cursor_connector.fetchall()
		connection.commit()  # Runs all the database queries which has been written above.
		connection.close()  # this ends the connection statment as the database is written.
		return Passengers_return
def passengercheck_between(From, To):
	print ('This is the function that will check the maximum number of the passenger in the year')
	connection = sqlite3.connect(
		'AirPassenger.sqlite')  # The connection is established from the python file to the data
	cursor_connector = connection.cursor()  # this activates the cursor used to run queries
	cursor_connector.execute('''Select * from AirPassenger where TimePeriod  Between ? and ?''', (From, To))
	data = cursor_connector.fetchall()  # this fetchs all the data written in the cursor.
	connection.commit()  # Runs all the database queries which has been written above.
	connection.close()  # ends the connection as the database is done.
	return data
def scatterplot_creator(xaxisdata,yaxisdata,xlabel,ylabel,title):
	mplt.xlabel(xlabel)  # Sets the xlabel of the file
	mplt.ylabel(ylabel)  # set the ylabel of the file
	mplt.title(title)  # Sets the Title of the plotting graph
	np_xaxisdata = np.array(xaxisdata)  # set a numpy array (refinning the previous array)
	np_yaxisdata = np.array(yaxisdata)  # set a numpy array y axis
	mplt.scatter(np_xaxisdata, np_yaxisdata)
	mplt.show()
def plot_creator(xaxisdata,yaxisdata,xlabel,ylabel,title):
	mplt.xlabel(xlabel)  # Sets the xlabel of the file
	mplt.ylabel(ylabel)  # set the ylabel of the file
	mplt.title(title)  # Sets the Title of the plotting graph
	np_xaxisdata = np.array(xaxisdata)  # set a numpy array (refinning the previous array)
	np_yaxisdata = np.array(yaxisdata)  # set a numpy array y axis
	mplt.plot(np_xaxisdata, np_yaxisdata)
	mplt.show()
def main():
	print ('<----Program has been started.--->')
	#data = file_read()  # this is the variable data to read the file
	#inc_temp_var = 0  # An Incremental variable to show the Viewers the simplicity to skip the first line
	#for line in data:  # this is a loop to parse all the lines
	#	line = line.strip()  # Extra spaces are wiped off
	#	if inc_temp_var == 0:
	#		inc_temp_var += 1  # As the First line consist of the Title so , we just Skipped that line
	#		continue
		#database_writer(line)  # calls the function database writer, file is written in well organized format
	xaxisdata = PassengersTimePeriod()  # recieves the year of the passnegers
	yaxiddata = Passengers()  # recieves the passengers numbers
	scatterplot_creator(xaxisdata,yaxiddata,'Time Period','Passengers', 'AIR PASSENGERS STATS')
	plot_creator(xaxisdata,yaxiddata,'Time Period','Passengers', 'AIR PASSENGERS STATS')
if __name__ == '__main__':
	main()  # this is the call to the main function

import time
print(time.time())


def numbers(max):
	time1 = time.time()
	for i in range(0, max):
		print (i)  # this will loop and print the time
	time2 = time.time()  # this is hte time 2
	print (str(time2-time1))

#numbers(1000000)
print (time.asctime())
tup = (2015,4,)  # year , month , day, hour, min ,second
print (time.asctime())
print (time.localtime())
print (help(time.time()))
time =time.localtime()
year = time[0]
month = time[1]
day = time[2]
print (year,month,day)
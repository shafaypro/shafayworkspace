for i in range(2, 30):
	j = 2
	counter = 0
	while j < i:
		if i % j == 0:
			counter = 1
			j = j + 1
		else:
			j = j + 1
	if counter == 0:
		print (i, " is a prime number ")
	else:
		counter = 0


		# Break statment breaks the loop
		# pass statments passes the loop for the next argument. let it be , a filer statment
		# continue you dont want to run the specific line then the loop satatment is continues while leaving the specific statment

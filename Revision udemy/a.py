def Cal_fact(number):
	if number == 1 or number == 0:
		return 1
	else:
		return int(number) * Cal_fact(number - 1)

print(Cal_fact(100))


def unique(input):
	output = list()
	for x in input:
		if x not in input:
			output.append()
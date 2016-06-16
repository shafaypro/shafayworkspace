def Subject_gpa():
	gpa=0
	a = raw_input('enter the lecture marks')
	b = raw_input('enter the mid term marks')
	c= raw_input('Enter the annual s marks')
	total=a+b+c
	if total<50:
			return '0.0'
	elif total<60 and total >= 50:
			return '2.0'


math = Subject_gpa()
chem = Subject_gpa()
Total=float(math)+float(chem)
TotalSubjects=2

print ('Cgpa is '+float(Total/TotalSubjects))



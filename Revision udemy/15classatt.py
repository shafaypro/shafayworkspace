class Students:
	def __init__(self, name, age):
		self.name = name
		self.age = age


student1 = Students("Fred", 12)
student2 = Students("Mike", 12)
print (hasattr(student1,
			"age"))  # this funciton cals the atttibute if the class has the attibute then it will return a boolean condition

# adding the attribute to the clas
setattr(student1, 'grade', "8th")  # settingan attibute in the class such that it has another attribute.
hasattr(student1, 'grade')  # checking the attribute if it is added in the class
print (student1.grade)
delattr(student1, "grade")

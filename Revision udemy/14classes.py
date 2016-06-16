class MyFirstClass:
	pass

instance = MyFirstClass()  # this is and instance for the class which has been created
class Students:
	def __init__(self, name, age, grade): # the paramerters are provided when the intilization is taken place
		self.name = name
		self.age = age
		self.grade = grade

	def displaystudent(self):
		return "STUDENT NAME IS " + self.name + " and age is " + str(self.age)


instance_student = Students("Shafay",12,'A')  # as the constructor is

print (instance_student.age)
print (instance_student.name)
print (instance_student.grade)
instance_student.displaystudent()

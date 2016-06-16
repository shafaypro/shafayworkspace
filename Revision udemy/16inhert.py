class Parent:
	counter = 10
	def __init__(self):
		print ("This is the COnstructor of the class")
	def parentFunc(self):
		print ("This is the Parent Function being called")
	def setCOunter(self,num):
		Parent.counter = num # intializaing the counter with the number .
	def showcounter(self):
		print (str(Parent.counter))

class child(Parent):
	def __init__(self):
		print ("This is the child method.")
	def childFunc(self):
		print ("child function is being called.")

# as you can see we can now access the parent class from the child.
c = child()
c.childFunc()
c.parentFunc()
c.setCOunter(20)
c.showcounter()

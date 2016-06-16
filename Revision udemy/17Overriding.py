class Parent:
	def func(self):
		print ("This is the parent function")

class Child:
	def func(self):
		print("This is a child function")

c = Child()
c.func() # as the child class function overrrides the parent called function so it is not accessable.
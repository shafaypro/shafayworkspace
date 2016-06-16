sen = "Hello %s , you're invidted to the birthday"
print (sen%("Shafay"))  # this is the place holder so that any item can be added in the barackers within values.
arr = ["BOB","Jake","Michelle"]
for i in arr:
	print (sen%(i))  # every name is looped and the place holder places the different values.
print (sen%("BRACK  ObAMA"))
sen = "hi %s , your age is %d"
print (sen%('Shafay',20))
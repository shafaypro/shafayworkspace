students = {"Muhammad Shafay Amjad" : 20 ,"Zunair Cheema" : 21, "rafay amjad":22 , "aqsa amjad":23} # key-Value Pairs Brov.
# students.clear() Removes every single item from the dictionary
print (students)
print (len(students))
print (type(students))  # this prints out the type of the student variable.
print (students["Muhammad Shafay Amjad"])
del students["aqsa amjad"]
print (students)
# del students deletes the variable.
# Dictionaries functions about how to use the dictionaries.
print (students.keys())  # this prints out the keys of the dictionaries
print (students.values())  # this prints out the values of the dictinaries keys.
# if you want to add another dictionary to the current dictionary
other_students = {"AYESA" : 22, "Hom" : 12, "DON":18}
students.update(other_students)  # this adds the previos dictionary to the current dictiinary.
print (students) # prints out the dictionary.


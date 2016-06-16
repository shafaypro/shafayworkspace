
# --> a string --> combination of letters
# len()--> length of a stuff
# ------------> general structure --> Variablename[ index ]   :--> index is of integer form--> starts from 0--> to the ending value(size-1)
# 0 , size - 1
anyvariable = "Hi my name is Shafay"
'''
print(len(anyvariable))  # what is the size of that
print(anyvariable[0])  # --> for accessing any character in a string --> you use the address the index
# variablename[index]  --> index is the address in the object
print(anyvariable[1])
print(anyvariable[2])
print(anyvariable[0] + anyvariable[1])
print(anyvariable[14] + anyvariable[15] + anyvariable[16] + anyvariable[17] + anyvariable[18] + anyvariable[19])



print(anyvariable[0:2])  # anyvariable[startingvalue index: endinyvalue index]
print(len(anyvariable))  # checking the length of the variable
print(anyvariable[14:20])  #  variable [ starting value : ending value ] <-- starting valus is inclusive, while the ending value is exclusive
print(anyvariable[6:10])  # Keep in mind the computer
print(anyvariable[:])  # this prints out all the value (combination of characters in a string)
anyvariable2 = anyvariable[:]  # copies all the string value to the variable 2
print(anyvariable2)  # prints out the variable value
print(anyvariable[3:])  # ending value not specified --> Till the end !
print(anyvariable[:5])  # starting is taken 0 if not specified till the exclusive ending value
'''
# Replacment Value of Indications
name = "Shafay"  # A variable named "Name" --> holds --> Shafay as a value.
# print("Hi ", name)
age = 20
print("Hi %s" % name)   # %s --> string  in Quotations <---Present  The Value or the replacement value -->" the % variable Value
print("number %d" % age)   # %d--> digit  # --> "Within string replacment opertaor" % Value
print("%s" % name)
name2 = "Andre"
age2 = 41
name3 = "Micky"
age3 = 41
# print("HI you name is %s and age is %d \nHI your name is %s and age is %d \nHi your name is %s and age is %d" % (name, age, name2, age2, name3, age3))  # multiple
# --> exceptional Characters --> Some meaning !!!  \n --> go to next line \t--> TAB
print("\n\tHI you name is %s and age is %d \n\tHI your name is %s and age is %d \n\tHi your name is %s and age is %d" % (name, age, name2, age2, name3, age3))

print("ANDRE --- \t \t \t $10 \n  ticket \t \t \t USA")


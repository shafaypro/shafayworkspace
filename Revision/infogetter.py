'''
name = input("What is your name ")  # Every input value is in the form of the string
age = input("What is your age ") # --> "41"
money = input("How much you earn")
power = input("How much your your power")
print("Hi %s \t your age is %d \n You got %d \t so you are %s" % (name, int(age), int(money), power))  # --> 41
print(age, money)
print(type(age))
# --- TYPE CASTING : A string --> an integer int(variablename)
# integer --> string   str(variable)
'''

name = input("What is your name ")  # Every input value is in the form of the string
age = int(input("What is your age ")) # --> "41" 41--> stores 41 in the variable
money = int(input("How much you earn"))  # this is type casted to integer from the string value
power = input("How much your your power")
print("Hi %s \t your age is %d \n You got %d \t so you are %s" % (name, age, money, power))  # --> 41
print(type(age), type(money))  # to check the type of the age and the money

# --- TYPE CASTING : A string --> an integer int(variablename)
# integer --> string   str(variable)
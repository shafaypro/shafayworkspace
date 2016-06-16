shopping_list = ["eggs", "Banana", "pineapple","shafy"]
print (shopping_list)
for item in shopping_list:
	print (item)  # just looping through the list.
print (shopping_list[2])
shopping_list[1] = "what are those"
print(shopping_list)
del shopping_list[2]
print (shopping_list)
arr1 = [1, 2, 3]
arr2 = [32, 45, 1]
arr4 = arr1 + arr2
print(arr4)
print (len(arr4))
print (max(arr4))
print (min(arr4))
arr4.append(43)
print (arr4)
print (arr4.count(1))  # print the count of the array
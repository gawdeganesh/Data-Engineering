# initializing list
test_list = [4, 7, 8, 3, 2, 1, 9]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing delim
delim = "$"
a= '*'.join(str(element) for element in test_list)
print (f'the delimeted string is {a}')
# Python3 code to demonstrate
# Reverse All Strings in String List
# using map()
 
# initializing list
test_list = ["geeks", "for", "geeks", "is", "best"]
 
# printing original list
print ("The original list is : " + str(test_list))
 
# Reverse All Strings in String List
# using map()
reverse= lambda x: x[::-1]
reversed_list = list(map(reverse,test_list))

# printing result
print ("The reversed string list is : " + str(reversed_list))


# # using join() and reversed()
# res = [''.join(reversed(i)) for i in test_list]
   
# # printing result
# print ("The reversed string list is : " + str(res))
                      
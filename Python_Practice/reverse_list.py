# initializing list
test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
 
# printing original list
print("The original list is : " + str(test_list))

reverse_list = [sorted(ele,reverse=True) for ele in test_list]

# printing original list
print("The reversed list is : " + str(reverse_list))
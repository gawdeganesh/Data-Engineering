# initializing list
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
 
# printing original list
print("The original list : " + str(test_list))

test_dict = {ele : [ele]*test_list.count(ele) for ele in test_list}

print("The original dictionary  : " + str(test_dict))
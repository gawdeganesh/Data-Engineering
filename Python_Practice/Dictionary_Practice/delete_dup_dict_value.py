# initializing dictionary
test_dict = {'Manjeet': [1, 4, 5, 6],
             'Akash': [1, 8, 9],
             'Nikhil': [10, 22, 4],
             'Akshat': [5, 11, 22]}
 
# printing original dictionary
print("The original dictionary : " + str(test_dict))

complete_list = [ ele for value in test_dict.values() for ele in value ]
print("The original dictionary : " + str(complete_list))

unique_list = [ ele for ele in complete_list if complete_list.count(ele)==1] 

print("The original dictionary : " + str(unique_list))

final_dict = { key : [val for val in value if val in unique_list] for key,value in test_dict.items() }
print("The original dictionary : " + str(final_dict))
# initializing dictionary
test_dict = {"Gfg": [5, 7, 5, 4, 5],
             "is": [6, 7, 3, 3],
             "Best": [9, 9, 6, 5, 5]}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))

test_dict_unique = {key : len(set(value)) for key, value in test_dict.items()}

print("The unique key dictionary is : " + str(test_dict_unique))

max_value = max(test_dict_unique.values())

max_key = [ key for key in test_dict_unique.keys() if test_dict_unique[key]== max_value]


print("The unique key list is : " + ','.join(max_key))
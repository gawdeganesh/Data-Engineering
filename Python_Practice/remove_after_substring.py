test_str = 'geeksforgeeks is best for geeks'
 
# printing original string
print("The original string is : " + str(test_str))
 
# initializing sub string
sub_str = "best"

empty_list= []
for ele in test_str.split():
    if ele == sub_str:
        break
    else:
        empty_list.append(ele)

new_string = ' '.join(empty_list) 
print("The original string is : " + str(new_string))     
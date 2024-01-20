# initializing string
test_str = 'geeksforgeeks is best'
 
# printing original String
print("The original string is : " + str(test_str))
 
# initializing mapping dictionary
map_dict = {'e': '1', 'b': '6', 'i': '4'}

for char in test_str:
    if char in map_dict:
        test_str= test_str.replace(char,map_dict[char])

print("The transformed string is : " + str(test_str))       


new_str = ''.join([ map_dict.get(char, char) for char in test_str])
print("The transformed string is : " + str(new_str))     
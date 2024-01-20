
def least_frequent_char(str):
    dict = {}
    for char in str:
        if char in dict.keys(): #if char in dict :
            dict[char] +=1
        else:
            dict[char] =1
#  above code can be written as 
#     for char in str:
#       dict[char] = dict.get(char, 0) + 1
              
# need to find the min value
    min_value = min(dict.values())
    least_frequent_char = ''

    for key,value in dict.items():
        if value == min_value:
            least_frequent_char= key
            break

#  above code can be written as 
#  least_frequent_char = min(dict, key = dict.get)

    return least_frequent_char

# Driver Code
input_str = "geeksforgeeks"
 
print(least_frequent_char(input_str))
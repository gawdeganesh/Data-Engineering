# Initializing list
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]

# Printing original list
print("The original list is : ", test_list)

K = 20

# Creating a dictionary with words as keys and their lengths as values
list_dict = {key: len(key) for key in test_list}
print(list_dict)

cumulative_length = 0
for key, value in list_dict.items():
    cumulative_length += value
    if cumulative_length >= K:
        print("The word is:", key)
        break

# The corrected part to find the exact character where the limit is reached, if needed
index = cumulative_length - K
print("The additional characters beyond K in the word:", index)

# optimal solution 

# Initializing list
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]

# Printing original list
print("The original list is : ", test_list)

K = 20

# Initialize the cumulative length variable
cumulative_length = 0

# Iterate through the list
for word in test_list:
    cumulative_length += len(word)
    if cumulative_length >= K:
        print('The word is:', word)
        break


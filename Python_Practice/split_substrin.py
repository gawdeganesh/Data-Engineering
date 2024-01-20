
# initializing string
test_string = "GeeksforGeeks is best for geeks"
 
# initializing split word
spl_word = 'best'
 
# printing original string
print("The original string : " + str(test_string))
 
# printing split string
print("The split string : " + str(spl_word))

split_string = test_string.split(spl_word)[0]

print(split_string)

res = []
 
# Looping over the characters of the string
for words in test_string.split():
    # Checking if the current character is the first character of the substring
    if words == spl_word:
        break
    res.append(words)


# Printing the result
print("String before the substring occurrence: " + ' '.join(res))
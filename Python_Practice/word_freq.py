# Initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
 
# Printing original string
print("The original string is : " + str(test_str))

unique_words = set(test_str.split())
# print(unique_words)

dict = { words : test_str.count(words) for words in unique_words}

print (dict)



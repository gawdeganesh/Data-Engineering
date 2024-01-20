# initializing list
test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing K
K = "g"

final_list = []
for ele in test_list:
    temp= ele.split(' ')
    for words in temp:
        if words[0].lower() == K.lower():
            final_list.append(words)

# printing final list
print("The original list is : " + str(final_list))


new_list = [words for ele in test_list for words in ele.split(' ') if words[0].lower() == K.lower() ]

# printing final list
print("The final list is : " + str(new_list))
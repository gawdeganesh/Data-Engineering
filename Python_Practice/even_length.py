# Python code
# To print even length words in string
 
#input string
n="This is a python language"

temp = n.split(' ')
even_list = []
for words in temp:
    if len(words) % 2 == 0:
        even_list.append(words)

print(' '.join(even_list))
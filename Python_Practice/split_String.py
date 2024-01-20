
test_list = ['Gfg is best', 'for Geeks', 'Preparing']
K = ' '
 
# Split String of list on K character using List Comprehension
result = [word for phrase in test_list for word in phrase.split(K)]

result1 = ' '.join(test_list).split(K)
 
print("The extended list after split strings:", result) 
print("The extended list after split strings:", result1)
sentence = "hello geeks for geeks is computer science portal"
length = 4
list1 = [words for words in sentence.split() if len(words)> length]
list2= ' '.join(list1)
print(list2)

s= sentence.split(' ')
list3 = list(filter(lambda x: len(x)>length, s))
print(list3)
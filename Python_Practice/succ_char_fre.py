# initializing string
test_str = 'geeksforgeeks is best for geeks. A geek should take interest.'
 
# initializing word
que_word = 'geek'

count= {}

for i in range(len(test_str)-1):
    if test_str[i:len(que_word)+i] == que_word:
        char = test_str[len(que_word)+i]
        count[char] = count.get(char, 0) + 1
        # if char in count:
        #     count[char]+=1
        # else :
        #     count[char]=1

print(count)
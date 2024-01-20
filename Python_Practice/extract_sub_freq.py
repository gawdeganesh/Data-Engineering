test_str = "abababa"
print("The original string is : " + str(test_str))

# using sliding window with a dictionary to count substring frequencies
freq_dict = {}
n = len(test_str)
for i in range(n):
	window_size = i + 1
	for j in range(n - window_size + 1):
		substring = test_str[j:j+window_size]
		freq_dict[substring] = freq_dict.get(substring, 0) + 1

# printing result
print("Extracted frequency dictionary : " + str(freq_dict))

##### solution 2 

# initializing string
test_str = "abababa"
 
# printing original string
print("The original string is : " + str(test_str))
 
# list comprehension to extract substrings
temp = [test_str[idx: j] for idx in range(len(test_str))
        for j in range(idx + 1, len(test_str) + 1)]
 
# loop to extract final result of frequencies
res = {}
for idx in temp:
	res[idx] = res.get(idx, 0) + 1

 
# printing result
print("Extracted frequency dictionary : " + str(res))
print("The original string is : " + str(temp))
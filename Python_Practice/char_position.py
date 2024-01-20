# initializing list
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing K
K = 20

# len_list = list(map(lambda x: len(x), test_list))
list_dict ={ key : len(key) for key in test_list}
print(list_dict)

sum= 0
for key,value in list_dict.items():
    if sum>K:
        print('the word is:' + key)
        break
    else : 
        sum+=value
        

index= sum-K+1
print(index)



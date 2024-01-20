# initializing string
test_str = 'abcaaaacbbaa'
 
# printing original String
print("The original string is : " + str(test_str))
 
# initializing K
K = 'a'
cnt = 1
cnt_lst=[]

for i in range(len(test_str)):
    if i<len(test_str)-1 and test_str[i]==test_str[i+1] and test_str[i]==K :
        cnt+=1
    elif test_str[i]==K :
        cnt_lst.append(cnt)
        cnt=1
    else:
        cnt_lst.append(0)
        cnt=1
max_occur = max(cnt_lst)
print(max_occur)

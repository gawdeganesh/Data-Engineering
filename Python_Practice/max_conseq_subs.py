
# initializing string
test_str = 'geeksgeeks are geeks for all geeksgeeksgeeks'
# initializing subs
sub_str = 'geeks'
# printing original string
print("The original string is : " + str(test_str))

cnt= {}
for ele in list(set(test_str.split())):
    if ele.__contains__(sub_str):
        count = ele.count(sub_str)
        cnt[ele] = count
    else:
         cnt[ele] = 0   

max_value = max(cnt.values())
max_key = max(cnt, key=cnt.get)

print (max_key)


# initializing string
test_str2 = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
test_list = ['gfg', 'is', 'best']
 
# printing original string and list
print("The original string is : " + test_str2)
print("The original list is : " + str(test_list))

new_dict= {}
for ele in test_list: 
    new_dict[ele] = test_str2.count(ele)

max_value = max(new_dict.values())
max_key = max(new_dict, key=new_dict.get)

print (max_key)     

def split_On_Vowel(test_string):
    vowel_string = 'aeiouAEIOU'
    temp_list = []
    temp_string= ""

    for char in test_string:
        if char not in vowel_string:
            temp_string+=char
        else:
            if temp_string != "":
                temp_list.append(temp_string)
                temp_string=""

    if  temp_string != "":
        temp_list.append(temp_string)
   
    return temp_list  


test_str = 'GFGaBstuforigeeks'
print(split_On_Vowel(test_str))


# 2nd approach 

# splitting on vowels
vow="aeiouAEIOU"
for i in test_str:
    if i in vow:
        test_str=test_str.replace(i,"*")
res=test_str.split("*")
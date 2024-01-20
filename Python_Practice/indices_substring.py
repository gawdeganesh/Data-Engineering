# initializing list
test_list = ["Gfg is good", "for Geeks", "I love Gfg", "Its useful"]
 
# initializing K
K = "Gfg"
 
# printing original list
print("The original list : " + str(test_list))

main_index_list = []
sub_index_list = []
for index,str in enumerate(test_list):
    for char in str.split():
        if char.__contains__(K):
            main_index_list.append(index)
            sub_index_list.append(str.index(K))


print (main_index_list)
print (sub_index_list)

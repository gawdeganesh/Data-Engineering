# initializing list
test_list = ["Gfg", "is", "Best"]
 
# printing original list
print("The original list : " + str(test_list))
 
# initializing subs. Dictionary
subs_dict = {
    "Gfg" : [5, 6, 7],
    "is" : [7, 4, 2],
}

# initializing K
K = 2

new_list = [subs_dict[ele][K] if ele in subs_dict.keys() else ele
                     for ele in test_list ]
print(new_list)

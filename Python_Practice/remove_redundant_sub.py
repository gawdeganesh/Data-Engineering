# initializing list
test_list = ["Gfg", "Gfg is best", "Geeks", "Gfg is for Geeks"]
 
# printing original list
print("The original list : " + str(test_list))

# using loop to iterate for each string
test_list.sort(key = len)
res = []
for idx, val in enumerate(test_list):
     
    # concatenating all next values and checking for existence
    if val not in ', '.join(test_list[idx + 1:]):
        res.append(val)
 
#alternate  
res1 = [val for idx, val in enumerate(test_list) if val not in ', '.join(test_list[idx + 1:])]
  
# printing result
print("The filtered list : " + str(res))            


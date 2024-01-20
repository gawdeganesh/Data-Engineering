# Python3 code to demonstrate working of
# Mirror Image of String
# Using Mirror Image of String
 
# initializing strings
test_str = 'efdw'
 
# printing original string
print("The original string is : " + str(test_str))
 
# initializing mirror dictionary
mir_dict = {'b':'d', 'd':'b', 'i':'i', 'o':'o', 'v':'v', 'w':'w', 'x':'x'}
res = ''
 
# accessing letters from dictionary
for ele in test_str:
    if ele in mir_dict:
        res += mir_dict[ele]
     
    # if any character not present, flagging to be invalid
    else:
        res = "Not Possible"
        break
 
# printing result
print("The mirror string : " + str(res))
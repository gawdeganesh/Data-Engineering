test_str = "gekseforgeeks"
 
# printing original string
print("The original string is : " + str(test_str))
 
# initializing arg string
arg_str = "geeks"

list_1 = []
list_2 = []
for char in set(arg_str):
    cnt1 = test_str.count(char)
    list_1.append(cnt1)
    cnt2 = arg_str.count(char)
    list_2.append(cnt2)

res = min(test_str.count(char) // arg_str.count(char) for char in set(arg_str))    

# result = min(list_1//list_2)
# print(result)


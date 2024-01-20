test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing substring
K = 'seef'
ns = ""
for i in test_str:
	if i in K:
		ns += i
res = False
if ns.__contains__(K):
	res = True
# printing result
print("Is substring in order : " + str(res))
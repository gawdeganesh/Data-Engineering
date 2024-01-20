# A Simple Iterative Python program to 
# reverse a string

# Function to reverse a string
def reverseStr(str):
	
    for i in range(len(str)//2):
          str[i],str[len(str)-1-i] =str[len(str)-1-i],str[i]



# Driver code
if __name__ == "__main__":
	str = "geeksforgeeks"

	# converting string to list
	# because strings do not support
	# item assignment
	str = list(str)
	reverseStr(str)

	# converting list to string
	str = ''.join(str)

	print(str)


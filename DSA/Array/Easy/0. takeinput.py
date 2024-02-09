list1 = [item for item in input("Enter the value: \n").split()]
list2 = [int(item) for item in input("Enter the value: \n").split()]

print(list1)
print(list2)

# Get the input from the user
user_input = input("Enter a list of numbers: ")

# Split the input into a list of strings
numbers_as_strings = user_input.split()

# Convert the strings to numbers
numbers = [int(number) for number in numbers_as_strings]

# Create a list comprehension to create a list of the square of each number
squared_numbers = [number**2 for number in numbers]

# Print the list of squared numbers
print(squared_numbers)

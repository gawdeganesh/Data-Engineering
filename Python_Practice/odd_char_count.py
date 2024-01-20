def odd_freq_chars(test_str):
    # Create an empty dictionary to hold character counts
    char_counts = {}
 
    # Loop through each character in the input string
    for char in test_str:
        # Increment the count for this character in the dictionary
        # using the get() method to safely handle uninitialized keys
        char_counts[char] = char_counts.get(char, 0) + 1
 
    # Create a list of characters whose counts are odd
    return [char for char, count in char_counts.items() if count % 2 != 0]
 
 
# Test the function with sample input
test_str = 'geekforgeeks is best for geeks'
print("The original string is : " + str(test_str))
res = odd_freq_chars(test_str)
print("The Odd Frequency Characters are :" + str(res))
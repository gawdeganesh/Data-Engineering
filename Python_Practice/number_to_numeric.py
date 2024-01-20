def string_To_Numbers(str):
    word_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    list_1 = [word_to_digit[words] for words in str.split()]
    
    return ''.join(list_1)

# Define the input string
test_str = 'zero four zero one'

# Print the original string and the result
print('The original string is:', test_str)
print('The string after performing replace:', string_To_Numbers(test_str))



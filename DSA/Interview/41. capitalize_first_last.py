"""
Write a Python program to capitalize the first and last 
letters of each word in a given string.
"""


def capitalize_first_last_letters(input_string: str):

    new_string = input_string.title()
    trans_string = ""

    for words in new_string.split():
        trans_string += str(words[:-1]) + str(words[-1]).upper() + " "

    return trans_string[:-1]


print(capitalize_first_last_letters("python is a great language"))
print(capitalize_first_last_letters("delhi is best city with 0 AQI"))

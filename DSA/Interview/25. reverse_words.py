import re


def reverse_words(input_string: str) -> str:

    # Split the string on spaces and/or commas
    temp_list = re.split(r"[ ,]+", input_string)

    # temp_list = input_string.split()

    # reversal code
    # temp_list = temp_list[::-1] # option 1

    left, right = 0, len(temp_list) - 1

    while left < right:
        temp_list[left], temp_list[right] = temp_list[right], temp_list[left]
        left += 1
        right -= 1

    return " ".join(temp_list)


print(reverse_words("this is the simple string"))
print(reverse_words("this, is not a simple string"))
print(reverse_words("this,"))
print(reverse_words(" "))

def compressed_string(text: str) :
    """Compresses a string by counting the occurrences of each character."""

    if not text.isalpha():
        return 'String contains non-alphabetic characters'  # More accurate error message

    compressed_list = []
    previous_char = text[0]
    count_char = 1

    for i in range(1, len(text)):  # Start the loop from the second character
        if text[i] == previous_char:
            count_char += 1
        else:
            compressed_list.append(previous_char + str(count_char))  # Append previous char and count
            previous_char = text[i]
            count_char = 1

    # Append the last character and its count
    compressed_list.append(previous_char + str(count_char))

    return ''.join(compressed_list)


print(compressed_string("aaasddeeeew"))  # Output: a3s1d2e4w1

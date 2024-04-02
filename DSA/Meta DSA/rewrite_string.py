def rewrite_string(s):
    # Convert string to lowercase to ignore case sensitivity
    s = s.lower()
    # Count occurrences of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Rewrite the string in the specified format
    result = "".join(f"{char}{count}" for char, count in char_count.items())

    return result


# Example usage
input_string = "I am back."
result_string = rewrite_string(input_string)
print(result_string)

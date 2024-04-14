def compressed_string(text: str):
    """Compresses a string by counting the occurrences of each character."""

    if not text.isalpha():
        return (
            "String contains non-alphabetic characters"  # More accurate error message
        )

    compressed_list = []
    previous_char = text[0]
    count_char = 1

    for i in range(1, len(text)):  # Start the loop from the second character
        if text[i] == previous_char:
            count_char += 1
        else:
            compressed_list.append(
                previous_char + str(count_char)
            )  # Append previous char and count
            previous_char = text[i]
            count_char = 1

    # Append the last character and its count
    compressed_list.append(previous_char + str(count_char))

    return "".join(compressed_list)


print(compressed_string("aaasddeeeew"))  # Output: a3s1d2e4w1


def compress(chars: list[str]) -> int:
    # Pointer for the position in the original list to modify
    write_pos = 0
    count = 1  # Initialize character count

    for i in range(len(chars)):
        # Check if we're at the end or at a new character
        if i == len(chars) - 1 or chars[i] != chars[i + 1]:
            # Write the current character to the write position
            chars[write_pos] = chars[i]
            write_pos += 1

            # If the count is greater than 1, write it as well
            if count > 1:
                for digit in str(count):
                    chars[write_pos] = digit
                    write_pos += 1
            count = 1  # Reset count for the next character
        else:
            count += 1  # Increment count if the current and next chars are the same

    return write_pos

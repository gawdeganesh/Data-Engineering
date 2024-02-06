def valid_palindrome(input_string: str) -> bool:
    if not input_string:
        return False

    left, right = 0, len(input_string) - 1

    while left < right:
        # left < right is added because if the string contains only special characters then it will keep on adding left pointer
        # and go beyond the index
        while left < right and not input_string[left].isalpha():
            left += 1
        while left < right and not input_string[right].isalpha():
            right -= 1

        # compare characters
        if input_string[left].lower() != input_string[right].lower():
            return False

        left += 1
        right -= 1

    return True


print(valid_palindrome("abcba"))
print(valid_palindrome("abcBA"))
print(valid_palindrome("78abcba23@23#"))
print(valid_palindrome("78aba23@23#"))
print(valid_palindrome("783#"))

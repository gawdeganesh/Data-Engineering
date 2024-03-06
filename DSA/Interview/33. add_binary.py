"""
1.Start from the end of both strings: Since binary addition works from right to left, iterate over both strings from the end towards the beginning.
2.Bitwise addition with carry: Add the corresponding bits from each string. If the sum exceeds 1, set a carry for the next bit addition.
3.Handle carry: If there's a carry from the last addition, include it in the next step.
4.Concatenate the result: Keep appending the result of each bit addition (considering the carry) to the left of the result string.
5.Handle different lengths: If the strings are of different lengths, continue adding the remaining bits of the longer string with the carry.

"""


def add_binary(a, b):
    result = ""  # The result of binary addition
    carry = 0  # The carry bit

    # Start from the last characters of both strings
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:
        sum = carry
        if i >= 0:
            sum += int(a[i])
            i -= 1
        if j >= 0:
            sum += int(b[j])
            j -= 1

        carry = sum // 2  # Update carry
        result = str(sum % 2) + result  # Prepend the remainder to the result

    return result


# Example usage
a = "1010"
b = "1011"
print(add_binary(a, b))  # Output: "10101"

"""
1.Convert both binary strings to integers using the int() function with base 2.
2.Add the two integers.
3.Convert the sum back to a binary string using the bin() function and remove the '0b' prefix that Python uses to indicate a binary number.
"""


def add_binary(a, b):
    # Step 1: Convert binary strings to integers
    sum_decimal = int(a, 2) + int(b, 2)

    # Step 2 & 3: Convert the sum back to binary and remove the '0b' prefix
    sum_binary = bin(sum_decimal)[2:]  # 0b10101

    return sum_binary


# Example usage
a = "1010"
b = "1011"
print(add_binary(a, b))  # Output: "10101"

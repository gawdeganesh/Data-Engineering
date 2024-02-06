def longest_common_substring(str1, str2):
    # Generate all possible substrings of str1
    substrings_str1 = {
        str1[i:j] for i in range(len(str1)) for j in range(i + 1, len(str1) + 1)
    }

    print(substrings_str1)

    # Initialize the longest common substring and its length
    longest = ""

    # Iterate through all substrings of str1 and check if they are in str2
    for substring in substrings_str1:
        if substring in str2 and len(substring) > len(longest):
            longest = substring

    return longest  # O(n^3)


# Example usage
str1 = "ABABC"
str2 = "BABCA"
print(longest_common_substring(str1, str2))

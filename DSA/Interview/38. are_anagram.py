"""
Write a function that takes two strings as input and returns True if they are anagrams 
(contain the same characters with the same frequency), and False otherwise.
"""


def are_anagrams(str1, str2):
    # Check if the lengths of both strings are the same
    # If not, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Count the frequency of each character in both strings
    freq_str1 = {}
    freq_str2 = {}

    for char in str1:
        freq_str1[char] = freq_str1.get(char, 0) + 1

    for char in str2:
        freq_str2[char] = freq_str2.get(char, 0) + 1

    # Compare the frequency dictionaries
    return freq_str1 == freq_str2


# Example usage
print(are_anagrams("listen", "silent"))  # Should return True
print(are_anagrams("hello", "world"))  # Should return False

"""
Time Complexity: The time complexity of this function primarily depends on the lengths of the input strings. Let's denote n as the length of the first string and m as the length of the second string. The first if statement checks if the lengths are equal, which is an O(1) operation. Then, constructing the frequency dictionaries for both strings involves iterating over each character of both strings, which takes O(n) for the first string and O(m) for the second string. Finally, comparing two dictionaries has a complexity of O(n) because, in the worst case, every character in the first string is different, and we need to compare each entry in the dictionaries. Therefore, the overall time complexity is O(n + m + n) = O(2n) or simply O(n) if we assume n ≈ m.

Space Complexity: The space complexity is O(n + m) for the frequency dictionaries, where n and m are the lengths of the two input strings. However, if we consider that the character set is limited (e.g., ASCII characters, which are 128 or 256 in total), the space complexity can be considered as O(1) because the size of the dictionaries is bounded by the size of the character set, not the length of the string. For a more general case with Unicode characters where the character set is effectively unbounded, the space complexity remains O(n + m).

"""


def are_anagrams(str1, str2):
    # Sort both strings
    sorted_str1 = "".join(sorted(str1))
    sorted_str2 = "".join(sorted(str2))

    # Compare the sorted strings
    return sorted_str1 == sorted_str2


# Example usage
print(are_anagrams("listen", "silent"))  # Should return True
print(are_anagrams("hello", "world"))  # Should return False

"""
Time Complexity: O( nlog n)
Space Complexity: O(n)
"""

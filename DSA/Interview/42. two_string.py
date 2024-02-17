"""
Write a Python program to generate two strings from a given string. For
the first string, use the characters that occur only once, and for the
second, use the characters that occur multiple times in the said string.
"""


def two_string(input_str: str) -> list:
    dict = {}

    for ch in input_str:
        dict[ch] = dict.get(ch, 0) + 1

    string_1 = ""
    string_2 = ""

    for key, count in dict.items():
        if count == 1:
            string_1 += key
        else:
            string_2 += key

    return string_1, string_2


string_1, string_2 = two_string("aabbcceffgh")

print(f"{string_1} {string_2}")

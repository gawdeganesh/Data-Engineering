def are_anagrams(str1: str, str2: str) -> str:

    if (not str1 and not str2) or (str1.strip() == "" and str2.strip() == ""):
        return print("strings are empty")

    anagram_check = {}

    for char in str1:
        if char not in anagram_check:
            anagram_check[char] = 1
        else:
            anagram_check[char] += 1

    for char in str2:
        if char in anagram_check:
            anagram_check[char] -= 1

    for value in anagram_check.values():
        if value != 0:
            return print("strings are not anagram")

    print("strings are anagram")


are_anagrams("abbc", "bbac")
are_anagrams("abbxxsac", " ")
are_anagrams(" ", " ")

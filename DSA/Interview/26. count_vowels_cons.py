def count_vowels_consonants(input_string: str) -> dict:

    count_dict = {"cnt_vowels": 0, "cnt_consonant": 0}

    vowel_string = "aeiouAEIOU"

    for char in input_string:
        if char.isalpha():
            if char in vowel_string:
                count_dict["cnt_vowels"] += 1
            else:
                count_dict["cnt_consonant"] += 1

    return count_dict


print(count_vowels_consonants("this is the simple string"))
print(count_vowels_consonants("this, is not a simple string"))
print(count_vowels_consonants("this,"))
print(count_vowels_consonants(" "))

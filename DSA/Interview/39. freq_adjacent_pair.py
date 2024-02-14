"""
Given a string, create a dictionary where keys are pairs of adjacent characters, and values are the frequencies of each pair.
"""

# adjacent is not previous and next


def freq_char_pair(input_string: str) -> dict:
    list = []
    first_pair = input_string[:2]

    list.append(first_pair)

    for i in range(1, len(input_string)):

        if i <= len(input_string) - 2:
            next_pair = input_string[i - 1 : i + 2]
            list.append(next_pair)
        else:
            next_pair = input_string[i - 1 : i + 1]
            list.append(next_pair)

    dict_freq = {ele: list.count(ele) for ele in list}

    return dict_freq


# print(freq_char_pair("abcabcabcab"))


def pair_frequencies(s):
    freq_dict = {}
    # Iterate over the string until the second-to-last character
    for i in range(len(s) - 1):
        # Create a pair of adjacent characters
        pair = s[i : i + 2]
        # Update the frequency of the pair in the dictionary
        freq_dict[pair] = freq_dict.get(pair, 0) + 1


    return freq_dict


# Example usage
example_string = "abcabcabcab"
print(pair_frequencies(example_string))

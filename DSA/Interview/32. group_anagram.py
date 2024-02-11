def group_anagrams(strs):
    anagrams = {}  # Initialize a dictionary to hold lists of anagrams
    for s in strs:
        # Sort the string and use it as a key

        # key = tuple(sorted(s))
        key = "".join(sorted(s))  # key must be immutable hence tuple or string
        if key not in anagrams:
            anagrams[key] = [s]  # as a list hence [s] and not s
        else:
            anagrams[key].append(s)  # values are list  {'aet': ['eat', 'tea'], 'ant': ['tan']}

    return list(anagrams.values())


# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat", "abc", "123"]
print(group_anagrams(strs))

"""
# group with 2 or more values 
    anagrams_group = []
    
    for value in anagrams.values():
        if len(value)>1:
            anagrams_group.append(value)
    
    print(anagrams_group)
    
"""

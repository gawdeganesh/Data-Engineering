def longest_common_prefix(string_list: list[str]):
    if not string_list:
        return "List is blank"

    prefix = string_list[0]

    for str in range(1, len(string_list)):  # for str in string_list[1:]:

        # Update the length of the prefix as long as there's a match
        while not string_list[str].startswith(prefix):
            prefix = prefix[:-1]

            # If the prefix becomes empty, it means there's no common prefix
            if not prefix:
                return "No Match Found"

    return prefix  # time O(S) : worst case when all the strings are same, sum of all the characters


# Example usage

print(longest_common_prefix(["flower", "flow", "floght"]))
print(longest_common_prefix(["flower", "abc", "banana"]))
print(longest_common_prefix(["", "flow", "flight"]))
